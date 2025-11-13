import logging, typing
from operator import attrgetter
from account_helpers.AccountSettings import ArmoryYard, AccountSettings
from armory_yard.gui.shared.models_helpers import updateArmoryConditionQuestsModel
from armory_yard.skeletons.armory_yard_reroll_controller import IArmoryYardRerollController
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_quest_sub_model import ArmoryYardQuestSubModel, QuestStatus
from gui.shared.view_helpers.blur_manager import CachedBlur
from Event import SuspendableEventSubscriber
from helpers import dependency, time_utils
from shared_utils import findFirst
from skeletons.gui.game_control import IArmoryYardController
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_chapter_model import ArmoryYardChapterModel, ChapterState, ChapterTokenState
from armory_yard.gui.window_events import showArmoryYardInfoPage
from wotdecorators import noexcept
if typing.TYPE_CHECKING:
    from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_main_view_model import ArmoryYardMainViewModel
    from frameworks.wulf import Array
_logger = logging.getLogger(__name__)

class _QuestsTabPresenter(object):
    __slots__ = ('__viewModel', '__tooltipData', '__closeCB', '__eventsSubscriber',
                 '__blur', '__mainViewlayer', '__parent', '__isProgressCompleted')
    __armoryYardCtrl = dependency.descriptor(IArmoryYardController)
    __armoryYardRerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    def __init__(self, viewModel, closeCB, parentViewLayer):
        self.__viewModel = viewModel
        self.__tooltipData = {}
        self.__closeCB = closeCB
        self.__eventsSubscriber = SuspendableEventSubscriber()
        self.__mainViewlayer = parentViewLayer
        self.__parent = None
        self.__blur = CachedBlur(enabled=False, ownLayer=self.__mainViewlayer)
        self.__isProgressCompleted = False
        return

    def init(self, parent):
        self.__parent = parent
        self.__eventsSubscriber.subscribeToEvents((
         self.__armoryYardCtrl.serverSettings.onUpdated, self.__updateData), (
         self.__armoryYardCtrl.serverSettings.seasonProvider.onUpdated, self.__updateData), (
         self.__armoryYardCtrl.onProgressUpdated, self.__progressUpdate), (
         self.__armoryYardCtrl.onQuestsUpdated, self.__updateData), (
         self.__viewModel.onAboutEvent, self.__onAboutEvent), (
         self.__armoryYardCtrl.onStatusChange, self.__updateData), (
         self.__viewModel.onClose, self.__closeView), (
         self.__armoryYardRerollCtrl.onQuestConditionUpdated, self.__onQuestConditionUpdated))
        self.__eventsSubscriber.pause()

    def onLoad(self):
        self.__blur.enable()
        self.__eventsSubscriber.resume()
        self.__updateData()
        self.__isProgressCompleted = self.__armoryYardCtrl.isCompleted()

    def onUnload(self):
        self.__blur.disable()
        self.__eventsSubscriber.pause()

    def fini(self):
        self.__eventsSubscriber.unsubscribeFromAllEvents()
        self.__blur.fini()
        self.__blur = None
        self.__parent = None
        return

    def getTooltipData(self, tooltipID, _):
        return self.__tooltipData.get(int(tooltipID))

    def __closeView(self, *args):
        self.__closeCB(*args)

    def __progressUpdate(self):
        if not self.__armoryYardCtrl.isQuestActive():
            self.__closeView()
            return
        progressIsCompleted = self.__armoryYardCtrl.isCompleted()
        if self.__isProgressCompleted != progressIsCompleted:
            self.__isProgressCompleted = progressIsCompleted
            self.__updateData()

    def __updateData(self):
        if not self.__armoryYardCtrl.isQuestActive():
            self.__closeView()
            return
        with self.__viewModel.transaction() as (model):
            model.setCurrentLevel(self.__armoryYardCtrl.getProgressionTokenCount())
            model.setViewedLevel(self.__armoryYardCtrl.getProgressionLevel())
            model.setState(self.__armoryYardCtrl.getState())
            startProgressionTime, endSeasonTime = self.__armoryYardCtrl.getProgressionTimes()
            model.setToTimestamp(endSeasonTime)
            model.setFromTimestamp(startProgressionTime)
            self.__updateChapters(model)

    def __updateChapters(self, model):
        ctrl = self.__armoryYardCtrl
        currentSeason = ctrl.serverSettings.getCurrentSeason()
        chaptersArray = model.getChapters()
        questsArray = model.getQuests()
        chaptersArray.clear()
        questsArray.clear()
        isPrevChapterFinished = True
        nowTime = time_utils.getServerUTCTime()
        for cycle in sorted(currentSeason.getAllCycles().values(), key=attrgetter('ID')):
            chapter = ArmoryYardChapterModel()
            chapter.setId(cycle.ID)
            isChapterDisabled = not isPrevChapterFinished or cycle.startDate > nowTime
            self.__updateQuests(questsArray, cycle.ID, chapter, isChapterDisabled, False)
            state = ChapterState.ACTIVE
            if isChapterDisabled:
                state = ChapterState.DISABLED
            elif chapter.getCompletedQuestsAll() == chapter.getTotalQuests():
                state = ChapterState.COMPLETED
            chapter.setState(state)
            isPrevChapterFinished = ctrl.isChapterFinished(cycle.ID)
            totalChapterTokens = ctrl.totalTokensInChapter(cycle.ID)
            receivedTokens = totalChapterTokens if isPrevChapterFinished else ctrl.receivedTokensInChapter(cycle.ID)
            chapter.setReceivedTokens(receivedTokens)
            chapter.setTotalTokens(totalChapterTokens)
            chapter.setTokenState(ChapterTokenState.HIDDEN)
            chaptersArray.addViewModel(chapter)

        ppCycleID = max([ x.ID for x in ctrl.serverSettings.getCurrentSeason().getAllCycles().values() ]) + 1
        self.__makePostProgressionChapter(ppCycleID, questsArray, chaptersArray)
        chaptersArray.invalidate()

    def __makePostProgressionChapter(self, cycleID, questsArray, chaptersArray):
        chapter = ArmoryYardChapterModel()
        chapter.setId(cycleID)
        chapter.setIsPostProgression(True)
        isChapterDisabled = not self.__armoryYardCtrl.isPostProgressionState
        self.__updateQuests(questsArray, cycleID, chapter, isChapterDisabled, True)
        state = ChapterState.ACTIVE
        if isChapterDisabled:
            state = ChapterState.DISABLED
        elif chapter.getCompletedQuestsAll() == chapter.getTotalQuests():
            state = ChapterState.COMPLETED
        chapter.setState(state)
        totalChapterTokens = self.__armoryYardCtrl.totalTokensInPostProgressionChapter()
        receivedTokens = self.__armoryYardCtrl.receivedTokensInPostProgressionChapter()
        chapter.setReceivedTokens(receivedTokens)
        chapter.setTotalTokens(totalChapterTokens)
        chaptersArray.addViewModel(chapter)
        chapter.setTokenState(ChapterTokenState.HIDDEN)

    def __updateQuests(self, arrayQuestsModel, cycleID, chapter, isChapterDisabled, isPostProgression=False):
        totalQuests = 0
        completedQuests = 0
        if isPostProgression:
            questIterator = self.__armoryYardCtrl.iterCyclePostProgressionQuests()
        else:
            questIterator = self.__armoryYardCtrl.iterCycleProgressionQuests(cycleID)
        for quests in questIterator:
            totalQuests += 1
            questSubModel = ArmoryYardQuestSubModel()
            questsModel = questSubModel.getQuests()
            questsCompleted, tokenQuestID = updateArmoryConditionQuestsModel(questsModel, quests, self.__tooltipData, cycleID, not self.__armoryYardCtrl.isPostProgressionState)
            questsModel.invalidate()
            questSubModel.setTokenQuestID(tokenQuestID)
            questSubModel.setStatus(QuestStatus.ACTIVE)
            if questsCompleted:
                completedQuests += 1
                questSubModel.setStatus(QuestStatus.DONE)
            elif isPostProgression:
                ppAvailableQuestAtOneTime = self.__armoryYardCtrl.serverSettings.getPostProgressionData().get('availableQuestAtOneTime', 1)
                if totalQuests > ppAvailableQuestAtOneTime + completedQuests:
                    questSubModel.setStatus(QuestStatus.LOCKED)
            if isChapterDisabled:
                questSubModel.setStatus(QuestStatus.LOCKED)
            arrayQuestsModel.addViewModel(questSubModel)

        arrayQuestsModel.invalidate()
        previousCompletedQuests = chapter.getCompletedQuestsAll()
        if not previousCompletedQuests:
            previousCompletedQuests = AccountSettings.getArmoryYard(ArmoryYard.ARMORY_YARD_PREV_COMPLETED_QUESTS).get(cycleID, 0)
        settings = AccountSettings.getArmoryYard(ArmoryYard.ARMORY_YARD_PREV_COMPLETED_QUESTS)
        settings[cycleID] = completedQuests
        AccountSettings.setArmoryYard(ArmoryYard.ARMORY_YARD_PREV_COMPLETED_QUESTS, settings)
        chapter.setCompletedQuestsNew(previousCompletedQuests)
        chapter.setCompletedQuestsAll(completedQuests)
        chapter.setTotalQuests(totalQuests)

    def __onAboutEvent(self):
        self.__blur.disable()
        showArmoryYardInfoPage(parent=self.__parent, closeCallback=lambda *_, **__: self.__blur.enable())

    @noexcept
    def __onQuestConditionUpdated(self, questID, _):
        armoryQuests = self.__viewModel.getQuests()
        armoryQuest = findFirst(lambda d: d.getTokenQuestID() == questID, armoryQuests, None)
        if armoryQuest is not None:
            tokenQuest = self.__armoryYardRerollCtrl.getArmoryTokenQuestByID(questID)
            if tokenQuest is not None:
                questsModel = armoryQuest.getQuests()
                chapterID = questsModel[0].getChapterId()
                questsModel.clear()
                condQuests = self.__armoryYardRerollCtrl.getConditionQuestsByTokenQuest(tokenQuest)
                updateArmoryConditionQuestsModel(questsModel, condQuests, self.__tooltipData, chapterID, not self.__armoryYardCtrl.isPostProgressionState)
                questsModel.invalidate()
        return