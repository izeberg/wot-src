import logging, typing
from CurrentVehicle import g_currentPreviewVehicle
from account_helpers.AccountSettings import AccountSettings, NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK, NY_CELEBRITY_DAY_QUESTS_VISITED_MASK, NY_CHALLENGE_LAST_QUEST_COMPLETION_COUNT
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions.cards_formatters import MissionBonusAndPostBattleCondFormatter
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES
from gui.impl import backport
from gui.impl.backport.backport_pop_over import BackportPopOverContent, createPopOverData
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.bonuses.discount_bonus_model import DiscountBonusModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.challenge_mission_model import ChallengeMissionModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_card_model import CardState, NewYearChallengeCardModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_progress_model import NewYearChallengeProgressModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_upcoming_card_model import NewYearChallengeUpcomingCardModel
from gui.impl.lobby.new_year.challenge.helper import fillMasteryProgression, setMasteryProgressionRewardState
from gui.impl.lobby.new_year.states import TournamentState
from gui.impl.lobby.new_year.tooltips.ho_challenge_token_tooltip import NyChallengeTokenTooltip
from gui.impl.lobby.new_year.tooltips.ny_gift_machine_token_tooltip import NyGiftMachineTokenTooltip
from gui.impl.lobby.pet_system.tooltips.pet_tooltip import PetTooltip
from gui.impl.new_year.new_year_bonus_packer import getChallengeBonusPacker, packBonusModelAndTooltipData
from gui.impl.new_year.new_year_helper import backportTooltipDecorator, nyCreateToolTipContentDecorator
from gui.pet_system.requester import INVALID_PET_ID
from gui.server_events.bonuses import PetsBonus
from gui.shared import event_dispatcher, EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showStylePreview, showPetPurchaseDialog
from gui.shared.events import NySelectVehiclePopOver
from gui.shared.money import Currency
from helpers import dependency, time_utils
from items.components.ny_constants import CelebrityQuestTokenParts, NY_PET_TOKEN
from new_year.celebrity.celebrity_quests_helpers import getCelebrityMarathonQuests, getCelebrityQuestBonusesByFullQuestID, getCelebrityQuestByFullID, marathonTokenCountExtractor, getRewardCelebrityQuestBonusesByID, iterAllTypeCelebrityActiveQuestsIDs, getRewardCelebrityQuestByFullID, getSealTokensCount, getCelebrityMasteryQuests
from new_year.ny_constants import SyncDataKeys
from new_year.ny_preview import getVehiclePreviewID
from new_year.ny_trigger_hints import TriggerHintsStates
from shared_utils import findFirst, first
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import ICelebritySceneController, INewYearTriggerHintsController, INewYearController
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_model import NewYearChallengeModel
    from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_tournament_celebrity_model import NewYearTournamentCelebrityModel
    from gui.server_events.event_items import CelebrityQuest
_QuestsParams = typing.NamedTuple('_QuestsParams', (
 (
  'iconKey', str),
 (
  'isCumulative', bool),
 (
  'condCurrent', int),
 (
  'condTotal', int),
 (
  'levelCondition', int)))
_COMPLETED_MASK = {CelebrityQuestTokenParts.QUEST: NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK}
_VISITED_MASK = {CelebrityQuestTokenParts.QUEST: NY_CELEBRITY_DAY_QUESTS_VISITED_MASK}
_ADVANCED_BONUS_ORDER = (
 'items',
 Currency.EQUIP_COIN,
 'dossier')

def _advancedBonusesSortOrder(bonus):
    bonusName = bonus.getName()
    if bonusName in _ADVANCED_BONUS_ORDER:
        return _ADVANCED_BONUS_ORDER.index(bonusName)
    return len(_ADVANCED_BONUS_ORDER)


class HOChallengeTournament(SubModelPresenter):
    __celebritySceneController = dependency.descriptor(ICelebritySceneController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    __nyController = dependency.descriptor(INewYearController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, viewModel, parentView):
        super(HOChallengeTournament, self).__init__(viewModel, parentView)
        self._tooltips = {}
        self.__condFormatter = None
        self.__bonusedPetId = INVALID_PET_ID
        return

    @property
    def viewModel(self):
        model = self.getViewModel()
        if model:
            return model.tournamentCelebrityModel
        else:
            return

    def initialize(self, *args, **kwargs):
        super(HOChallengeTournament, self).initialize(self, *args, **kwargs)
        self.__celebritySceneController.onEnterChallenge()
        self._setQuestCompletion()
        self.__fillProgressionBonusPetID()
        with self.viewModel.transaction() as (model):
            self.__updateModel(model)

    def finalize(self):
        super(HOChallengeTournament, self).finalize()
        self.__celebritySceneController.onExitChallenge()
        self.__condFormatter = None
        return

    @nyCreateToolTipContentDecorator
    def createToolTipContent(self, event, contentID):
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_gift_machine_token_tooltip():
            return NyGiftMachineTokenTooltip()
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_challenge_token_tooltip():
            tokenType = str(event.getArgument('tokenType'))
            return NyChallengeTokenTooltip(tokenType)
        if contentID == R.views.mono.pet_system.tooltips.pet_tooltip():
            if self.__bonusedPetId == INVALID_PET_ID:
                logging.warning('bonused PetId is invalid')
                return
            return PetTooltip(petID=self.__bonusedPetId)
        return super(HOChallengeTournament, self).createToolTipContent(event, contentID)

    def _getListeners(self):
        listeners = super(HOChallengeTournament, self)._getListeners()
        return listeners + (
         (
          NySelectVehiclePopOver.SHOW, self.__onPopoverOpened, EVENT_BUS_SCOPE.DEFAULT),
         (
          NySelectVehiclePopOver.HIDE, self.__onPopoverClosed, EVENT_BUS_SCOPE.DEFAULT))

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(HOChallengeTournament, self).createToolTip(event)

    def createPopOverContent(self, event):
        if event.contentID == R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent():
            if event.getArgument('popoverId') == DiscountBonusModel.NEW_YEAR_DISCOUNT_APPLY_POPOVER_ID:
                alias = VIEW_ALIAS.NY_SELECT_VEHICLE_FOR_DISCOUNT_POPOVER
                variadicID = event.getArgument('variadicID')
                data = createPopOverData(alias, {'variadicID': variadicID, 
                   'parentWindow': self.getParentWindow()})
                return BackportPopOverContent(popOverData=data)
        return super(HOChallengeTournament, self).createPopOverContent(event)

    def _getEvents(self):
        events = super(HOChallengeTournament, self)._getEvents()
        return events + (
         (
          self.viewModel.onUpdateTimeTill, self.__onUpdateTimeTill),
         (
          self.viewModel.onVisited, self.__onVisited),
         (
          self.viewModel.onStylePreviewShow, self.__onStylePreviewShow),
         (
          self.viewModel.masteryProgression.onGoToDetails, self.__onGoToDetails),
         (
          self.__celebritySceneController.onQuestsUpdated, self.__onQuestsUpdated),
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated))

    def _getCallbacks(self):
        return (
         (
          'tokens', self.__onTokensChanged),)

    def __updateModel(self, model):
        self.__setPreviousQuestQuantity(model)
        model.setQuestsQuantity(self.__celebritySceneController.questsCount)
        model.setCompletedQuestsQuantity(getSealTokensCount())
        model.setTimeTill(time_utils.getDayTimeLeft())
        self.__setQuestsInfo()
        self.__fillProgression(model)
        fillMasteryProgression(model.masteryProgression)
        if self.__triggerHintsController.triggerHintsState == TriggerHintsStates.TOURNAMENT and self.__triggerHintsController.checkForTournamentRequirements():
            self.__triggerHintsController.hide()

    def __onTokensChanged(self, tokens):
        with self.viewModel.transaction() as (model):
            if any(token.startswith(CelebrityQuestTokenParts.PREFIX) for token in tokens):
                self.__updateModel(model)
            elif NY_PET_TOKEN in tokens:
                setMasteryProgressionRewardState(model.masteryProgression)

    def __setPreviousQuestQuantity(self, model):
        previousQuestCount = AccountSettings.getUIFlag(NY_CHALLENGE_LAST_QUEST_COMPLETION_COUNT) or 0
        model.setPreviousCompletedQuestsQuantity(previousQuestCount)
        AccountSettings.setUIFlag(NY_CHALLENGE_LAST_QUEST_COMPLETION_COUNT, self.__celebritySceneController.completedQuestsCount)

    def __setQuestsInfo(self):
        if not self.viewModel:
            return
        with self.viewModel.transaction() as (tx):
            dailyCardsModel = tx.getChallengeCards()
            dailyCardsModel.clear()
            upcomingCardsModel = tx.getUpcomingCards()
            upcomingCardsModel.clear()
            for token in iterAllTypeCelebrityActiveQuestsIDs():
                self.__makeChallengeCardModel(dailyCardsModel, token)

            dailyCardsLen = len(dailyCardsModel)
            if dailyCardsLen < self.__celebritySceneController.questsCount:
                self.__makeAndFillUpcomingChallengeCardModel(upcomingCardsModel, dailyCardsLen + 1)
                if dailyCardsLen == 1:
                    self.__makeAndFillUpcomingChallengeCardModel(upcomingCardsModel, dailyCardsLen + 2)
            dailyCardsModel.invalidate()
            upcomingCardsModel.invalidate()

    def __makeChallengeCardModel(self, model, token):
        firstQuestToken = token[0]
        questInfo = CelebrityQuestTokenParts.getFullQuestOrderInfo(firstQuestToken)
        cardModel = NewYearChallengeCardModel()
        qType, qNum = questInfo
        cardModel.setIsVisited(_getQuestVisited(qType, qNum))
        cardModel.setToken(firstQuestToken)
        bonuses = getCelebrityQuestBonusesByFullQuestID(firstQuestToken)
        self.__packBonuses(bonuses, cardModel.getSingleMissionRewards())
        quest = getRewardCelebrityQuestByFullID(firstQuestToken, fullReward=True)
        bonuses = quest.getBonuses()
        self.__packBonuses(bonuses, cardModel.getFullMissionRewards())
        self.__fillChallengeCardModel(cardModel, token)
        model.addViewModel(cardModel)

    def __fillChallengeCardModel(self, cardModel, token):
        hasCompletedQuest, hasIncompleteQuest = False, False
        for missionToken in token:
            quest = getCelebrityQuestByFullID(missionToken)
            if quest is None:
                return
            params = self.__parseQuestsParams(quest)
            missionModel = ChallengeMissionModel()
            missionModel.setCurrentProgress(params.condCurrent)
            missionModel.setFinalProgress(params.condTotal)
            missionModel.setIsCumulative(params.isCumulative)
            missionModel.setIcon(params.iconKey)
            missionModel.setDescription(quest.getDescription())
            missionModel.setGoalValue(params.levelCondition)
            missionModel.setIsCompleted(quest.isCompleted())
            missions = cardModel.getMissions()
            missions.addViewModel(missionModel)
            questCompleted = quest.isCompleted()
            hasCompletedQuest |= questCompleted
            hasIncompleteQuest |= not questCompleted

        completionState = CardState.INPROGRESS if hasCompletedQuest and hasIncompleteQuest else CardState.COMPLETED if hasCompletedQuest else CardState.ACTIVE
        _setState(cardModel, completionState, token)
        return

    def __packBonuses(self, bonuses, rewards):
        packBonusModelAndTooltipData(bonuses, rewards, getChallengeBonusPacker(), self._tooltips)

    def __makeAndFillUpcomingChallengeCardModel(self, model, cardsLen):
        cardModel = NewYearChallengeUpcomingCardModel()
        singleRewardQuestID = CelebrityQuestTokenParts.makeUpcomingRewardsQuestID(cardsLen)
        bonuses = getRewardCelebrityQuestBonusesByID(singleRewardQuestID)
        self.__packBonuses(bonuses, cardModel.getSingleMissionRewards())
        fullRewardQuestID = CelebrityQuestTokenParts.makeUpcomingRewardsQuestID(cardsLen, fullReward=True)
        fullBonuses = getRewardCelebrityQuestBonusesByID(fullRewardQuestID)
        self.__packBonuses(fullBonuses, cardModel.getFullMissionRewards())
        model.addViewModel(cardModel)

    def __fillProgression(self, model):
        marathonQuests = getCelebrityMarathonQuests()
        if not marathonQuests:
            _logger.warning("Can't find marathon quests")
            return
        sortedMarathonQIDs = sorted(marathonQuests.keys(), key=lambda qID: int(qID.split(CelebrityQuestTokenParts.SEPARATOR)[(-1)]))
        progressiveRewards = model.getProgressRewards()
        progressiveRewards.clear()
        for qID in sortedMarathonQIDs:
            quest = marathonQuests[qID]
            progressModel = NewYearChallengeProgressModel()
            progressModel.setRewardLevel(marathonTokenCountExtractor(quest))
            self.__packBonuses(quest.getBonuses(), progressModel.getRewards())
            progressiveRewards.addViewModel(progressModel)

        progressiveRewards.invalidate()

    def __fillProgressionBonusPetID(self):
        quests = getCelebrityMasteryQuests()
        if not quests:
            _logger.warning("Can't find mastery progression quests")
            return
        sortedQIDs = sorted(quests.keys(), key=lambda qID: int(qID.split(CelebrityQuestTokenParts.SEPARATOR)[(-1)]))
        lastQuestID = sortedQIDs[(-1)]
        quest = quests[lastQuestID]
        for bonus in quest.getBonuses():
            if isinstance(bonus, PetsBonus):
                self.__bonusedPetId = first(bonus.getValue())

    def __parseQuestsParams(self, quest):
        activeQuestCurrent = activeQuestTotal = levelCondition = 0
        currConditions = first(self.__getCondFormatter().format(quest))
        postBattleConditions = quest.postBattleCond.getConditions()
        anyCumulative = findFirst(lambda c: c.progressType == MISSIONS_ALIASES.CUMULATIVE, currConditions)
        if anyCumulative is not None:
            activeQuestCurrent, activeQuestTotal = anyCumulative.current, anyCumulative.total
            levelCondition = anyCumulative.total
        else:
            for item in postBattleConditions.items:
                if item.getData().get('max'):
                    levelCondition = item.getData().get('max')[0][1]
                elif item.getData().get('greaterOrEqual'):
                    levelCondition = item.getData().get('greaterOrEqual')[0][1]

        iconKey = currConditions[0].iconKey
        if iconKey == 'battles' and len(currConditions) == 2 and any(c.iconKey == 'win' for c in currConditions):
            iconKey = 'win'
        return _QuestsParams(iconKey, anyCumulative is not None, activeQuestCurrent, activeQuestTotal, levelCondition)

    def __onDataUpdated(self, keys, _):
        if SyncDataKeys.SELECTED_DISCOUNTS in keys:
            with self.viewModel.transaction() as (tx):
                self.__fillProgression(tx)

    def __onVisited(self, args=None):
        with self.viewModel.transaction() as (tx):
            dailyCards = tx.getChallengeCards()
            cardModel = findFirst(lambda c: c.getToken() == args.get('token'), dailyCards, None)
            if cardModel is None:
                return
            qType, qNum = CelebrityQuestTokenParts.getFullQuestOrderInfo(cardModel.getToken())
            cardModel.setIsVisited(True)
            dailyCards.invalidate()
            _setQuestVisited(qType, qNum, True)
        return

    def _setQuestCompletion(self):
        for token in iterAllTypeCelebrityActiveQuestsIDs():
            firstQuestToken = token[0]
            firstQuest = getCelebrityQuestByFullID(firstQuestToken)
            firstQuestInfo = CelebrityQuestTokenParts.getFullQuestOrderInfo(firstQuestToken)
            firstQType, firstQInfo = firstQuestInfo
            _setQuestCompleted(firstQType, firstQInfo, firstQuest.isCompleted())

    def __onPopoverOpened(self, event):
        if event.ctx:
            self.viewModel.setDiscountPopoverId(event.ctx.get('discountID', ''))

    def __onPopoverClosed(self, event):
        self.viewModel.setDiscountPopoverId('')

    def __onStylePreviewShow(self, args):
        styleIntCD = int(args.get('intCD'))
        styleItem = self.__itemsCache.items.getItemByCD(styleIntCD)
        if styleItem is None:
            return
        else:
            backBtnDescrLabel = backport.text(R.strings.ny.tournament.backLabel())

            def _backCallback():
                if not self.__nyController.isEnabled():
                    event_dispatcher.showHangar()
                else:
                    g_currentPreviewVehicle.selectNoVehicle()
                    TournamentState.goTo(instantly=True)

            showStylePreview(getVehiclePreviewID(styleItem), styleItem, styleItem.getDescription(), backCallback=_backCallback, backBtnDescrLabel=backBtnDescrLabel)
            return

    def __onGoToDetails(self):
        showPetPurchaseDialog()

    def __onUpdateTimeTill(self):
        self.viewModel.setTimeTill(time_utils.getDayTimeLeft())

    def __onQuestsUpdated(self):
        with self.viewModel.transaction() as (tx):
            self.__updateModel(tx)

    def __getCondFormatter(self):
        if self.__condFormatter is not None:
            return self.__condFormatter
        else:
            self.__condFormatter = _ChallengeCondFormatter()
            return self.__condFormatter


class _ChallengeCondFormatter(MissionBonusAndPostBattleCondFormatter):

    def _packCondition(self, *args, **kwargs):
        pass

    def _getFormattedField(self, *args, **kwargs):
        pass

    def _packSeparator(self, key):
        pass

    def _packConditions(self, *args, **kwargs):
        pass


def _getQuestVisited(questType, questNum):
    return _getUIFlagBit(_VISITED_MASK[questType], questNum - 1)


def _setQuestVisited(questType, questNum, value):
    return _setUIFlagBit(_VISITED_MASK[questType], questNum - 1, value)


def _setState(cardModel, completionState, token):
    firstQuestToken = token[0]
    firstQuest = getCelebrityQuestByFullID(firstQuestToken)
    firstQuestInfo = CelebrityQuestTokenParts.getFullQuestOrderInfo(firstQuestToken)
    if completionState == CardState.COMPLETED and not _getQuestCompleted(*firstQuestInfo):
        completionState = CardState.JUSTCOMPLETED
    cardModel.setState(completionState)
    firstQType, firstQInfo = firstQuestInfo
    _setQuestCompleted(firstQType, firstQInfo, firstQuest.isCompleted())


def _getQuestCompleted(questType, questNum):
    return _getUIFlagBit(NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK, questNum - 1)


def _setQuestCompleted(questType, questNum, value):
    return _setUIFlagBit(NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK, questNum - 1, value)


def _getUIFlagBit(name, bitNum):
    return bool(AccountSettings.getUIFlag(name) >> bitNum & 1)


def _setUIFlagBit(name, bitNum, value):
    AccountSettings.setUIFlag(name, AccountSettings.getUIFlag(name) & ~(1 << bitNum) | int(value) << bitNum)