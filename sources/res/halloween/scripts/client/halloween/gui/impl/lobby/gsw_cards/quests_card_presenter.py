import typing
from gui.impl.backport import BackportTooltipWindow, createTooltipData
from gui.impl.pub.view_component import ViewComponent
from gui.server_events.event_items import ServerEventAbstract
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency
from halloween.gui.impl.lobby.hw_helpers import getQuestFinishTimeLeft, fillProminentBonus, PROMINENT_REWARD_TOOLTIP_ID
from halloween.gui.impl.lobby.tooltips.daily_quests_tooltip import DailyQuestsTooltip
from frameworks.wulf import View, ViewEvent
from gui.impl.gen import R
from gui.server_events.cond_formatters import postbattle as postbattleFrmt, bonus as bonusFrmt
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from skeletons.gui.server_events import IEventsCache
from halloween.gui.impl.gen.view_models.views.lobby.widgets.quests_card_view_model import QuestsCardViewModel

class QuestsCardPresenter(ViewComponent[QuestsCardViewModel]):
    _hwArtifactsCtrl = dependency.descriptor(IHalloweenArtefactsController)
    _halloweenCtrl = dependency.descriptor(IHalloweenController)
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, isGSW=False):
        super(QuestsCardPresenter, self).__init__(model=QuestsCardViewModel)
        self.__postBattleCondFormatter = postbattleFrmt.MissionsPostBattleConditionsFormatter()
        self.__bonusCondFormatter = bonusFrmt.MissionsBonusConditionsFormatter()
        self.__statusChangeNotifier = SimpleNotifier(self.__getTimeToStatusChange, self.__onNotifyStatusChange)
        self.__prominentBonus = None
        self.__isGSW = isGSW
        return

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            if tooltipId == PROMINENT_REWARD_TOOLTIP_ID and self.__prominentBonus is not None:
                window = BackportTooltipWindow(createTooltipData(tooltip=self.__prominentBonus.tooltip, isSpecial=self.__prominentBonus.isSpecial, specialAlias=self.__prominentBonus.specialAlias, specialArgs=self.__prominentBonus.specialArgs, isWulfTooltip=self.__prominentBonus.isWulfTooltip), self.getParentWindow(), event=event)
                window.load()
                return window
        return super(QuestsCardPresenter, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.halloween.mono.lobby.tooltips.daily_quests_tooltip():
            return DailyQuestsTooltip(self.__quest, True)
        return super(QuestsCardPresenter, self).createToolTipContent(event, contentID)

    def _onLoading(self, *args, **kwargs):
        super(QuestsCardPresenter, self)._onLoading()
        self._init()
        self.__statusChangeNotifier.startNotification()

    def _finalize(self):
        super(QuestsCardPresenter, self)._finalize()
        self.__postBattleCondFormatter = None
        self.__bonusCondFormatter = None
        self.__statusChangeNotifier.stopNotification()
        self.__statusChangeNotifier = None
        return

    def _getEvents(self):
        return [
         (
          self.eventsCache.onSyncCompleted, self.__onUpdate),
         (
          self._halloweenCtrl.onSettingsUpdate, self.__onUpdate)]

    def _init(self):
        self.__initQuest()
        if self.__quest is None:
            self.__setWidgetState(isHidden=True)
            return
        else:
            self.__fillViewModel(self.__quest)
            return

    def __onUpdate(self):
        self._init()

    def __onNotifyStatusChange(self):
        self._init()

    def __getTimeToStatusChange(self):
        return getQuestFinishTimeLeft(self.__quest)

    def __getActiveQuest(self):
        gswQuestList = self._halloweenCtrl.getModeSettings().gsw_quests_progress
        quests = self._halloweenCtrl.getHWQuestsCache()
        if self.__isGSW:
            for questID in gswQuestList:
                quest = quests.get(questID)
                if quest and not quest.isCompleted() and ServerEventAbstract.isAvailable(quest).isValid:
                    return quest

        else:
            questCount = len(gswQuestList) - 1
            for idx, questID in enumerate(gswQuestList):
                quest = quests.get(questID)
                if quest and (not quest.isCompleted() or idx == questCount):
                    return quest

        return

    def __getFirstConditionIcon(self, quest, questConditions, formatter):
        for orItem in formatter.format(questConditions, quest):
            for andItem in orItem:
                return andItem.iconKey

        return ''

    def __getFirstBonusConditionCumulativeProgress(self, quest):
        for orItem in self.__bonusCondFormatter.format(quest.bonusCond, quest):
            for andItem in orItem:
                if andItem.progressType == MISSIONS_ALIASES.CUMULATIVE:
                    return (int(andItem.current), int(andItem.total))

        return (0, 0)

    def __fillViewModel(self, quest):
        with self.getViewModel().transaction() as (tx):
            tx.setName(quest.getUserName().replace('\\n', '\n'))
            tx.setDescription(quest.getDescription())
            tx.setIsCompleted(quest.isCompleted())
            progressCurrent, progressTotal = self.__getFirstBonusConditionCumulativeProgress(quest)
            tx.setMaximumProgress(progressTotal)
            tx.setCurrentProgress(progressCurrent)
            conIcon = self.__getFirstConditionIcon(quest, quest.postBattleCond, self.__postBattleCondFormatter)
            tx.setConditionName(conIcon)
            self.__prominentBonus = fillProminentBonus(quest.getID(), self.__quest.getBonuses(), tx.bonus)
            self.__setWidgetState(isHidden=False)

    def __initQuest(self):
        self.__quest = self.__getActiveQuest()

    @replaceNoneKwargsModel
    def __setWidgetState(self, isHidden, model=None):
        model.setIsHidden(isHidden)