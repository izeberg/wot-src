from __future__ import absolute_import
import logging, typing
from functools import partial
import BigWorld
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from advent_calendar.gui.impl.gen.view_models.views.lobby.reward_view_model import AwardDayState, OpenDoorStatus, RewardViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import isAdventAnimationEnabled, openAndWaitDoor
from advent_calendar.gui.impl.lobby.feature.bonus_grouper import RewardBonusGrouper, RewardsBonusGroups
from advent_calendar.gui.impl.lobby.feature.bonus_packers import getRewardBonusPacker
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip
from advent_calendar.gui.shared import events
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.impl.gen import R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.server_events.bonuses import BattleTokensBonus, LootBoxTokensBonus
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from helpers import dependency
if typing.TYPE_CHECKING:
    from typing import Any, Dict, List, Tuple
    from gui.impl.backport import TooltipData
    from gui.server_events.bonuses import SimpleBonus
_logger = logging.getLogger(__name__)
_EXCLUDED_CLASSES = (
 BattleTokensBonus,)
_BONUSES_ORDER = (
 RewardsBonusGroups.LOOTBOX,
 RewardsBonusGroups.EXPERIMENTAL_EQUIPMENT,
 RewardsBonusGroups.MENTORING_LICENSE,
 RewardsBonusGroups.CREW_MEMBER,
 RewardsBonusGroups.STYLE_2D,
 RewardsBonusGroups.FREEXP,
 RewardsBonusGroups.PREMIUM,
 RewardsBonusGroups.COMPONENTS,
 RewardsBonusGroups.CREDITS,
 RewardsBonusGroups.RESERVE_CREDITS,
 RewardsBonusGroups.RESERVE_EXP,
 RewardsBonusGroups.CREW_BONUSES,
 RewardsBonusGroups.BATTLE_BONUS_5X,
 RewardsBonusGroups.RECERTIFICATION_FORM,
 RewardsBonusGroups.DECAL,
 RewardsBonusGroups.RESERVE_COMBINED_EXP)

def sortBonuses(groupedBonuses, excluded=(), excludedCls=(), bonusesOrder=()):
    sortedGroupedBonuses = sorted(groupedBonuses, key=lambda b: bonusesOrder.index(b[0]) if b[0] in bonusesOrder else len(bonusesOrder))
    bonuses = []
    for _, bonus in sortedGroupedBonuses:
        if bonus.getName() in excluded or isinstance(bonus, excludedCls):
            continue
        bonuses.append(bonus)

    return bonuses


class RewardView(ViewImpl):
    _adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.reward_view(), model=RewardViewModel(), args=args, kwargs=kwargs)
        super(RewardView, self).__init__(settings)
        self._tooltips = {}
        self._isProgressionReward = False
        self._currency = kwargs.get('currency', '')

    @property
    def viewModel(self):
        return self.getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip():
            tooltipData = self.getTooltipData(event)
            if tooltipData is None:
                _logger.error('Tooltip data is not found for event %r', event.getArgument('tooltipId'))
                return
            return AdventCalendarSimpleTooltip(*tooltipData.specialArgs)
        else:
            return super(RewardView, self).createToolTipContent(event, contentID)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(RewardView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self._tooltips.get(tooltipId)

    def _isLootBoxInBonuses(self, bonuses):
        for bonus in bonuses:
            if bonus.getName() == 'lootBox' and isinstance(bonus, LootBoxTokensBonus):
                return True

        return False

    def _onLoading(self, dayId, isProgressionReward, bonuses, *args, **kwargs):
        super(RewardView, self)._onLoading(*args, **kwargs)
        self._isProgressionReward = isProgressionReward
        openedDoors = len(self._adventController.completedAwardsQuests)
        openedDoors = (isProgressionReward or openedDoors) + 1 if 1 else openedDoors
        with self.viewModel.transaction() as (vm):
            packBonusModelAndTooltipData(self._getSortedBonuses(bonuses), vm.getBonuses(), self._tooltips, packer=self._getRewardBonusPacker())
            vm.setDayId(dayId)
            vm.setDoorsOpenedAm(openedDoors)
            vm.setShowBoxesButton(self._isLootBoxInBonuses(bonuses))
            vm.setIsAnimationEnabled(isAdventAnimationEnabled())
            vm.setOpenDoorStatus(OpenDoorStatus.OPEN_DOOR_UNDEFINED)
            if self._isProgressionReward:
                vm.setAwardDayState(AwardDayState.PROGRESSIONQUEST)
            elif self._adventController.config.isSpecialDay(dayId):
                vm.setAwardDayState(AwardDayState.SPECIALDAY)
            else:
                vm.setAwardDayState(AwardDayState.REGULARDAY)

    def _finalize(self):
        g_eventBus.handleEvent(events.AdventCalendarEvent(events.AdventCalendarEvent.PROGRESSION_REWARD_VIEWED, {'isProgressionRewardCompleted': self._isProgressionReward, 
           'doorIsOpened': self.viewModel.getOpenDoorStatus() == OpenDoorStatus.OPEN_DOOR_SUCCESS}), scope=EVENT_BUS_SCOPE.LOBBY)
        self._tooltips.clear()
        super(RewardView, self)._finalize()

    @staticmethod
    def _getSortedBonuses(bonuses):
        return sortBonuses(RewardBonusGrouper(RewardsBonusGroups).group(bonuses), excludedCls=_EXCLUDED_CLASSES, bonusesOrder=_BONUSES_ORDER)

    @staticmethod
    def _getRewardBonusPacker():
        return getRewardBonusPacker()

    def _getEvents(self):
        return (
         (
          self.viewModel.onCloseBtnClick, self._onClose),
         (
          self.viewModel.onGoToBoxesBtnClick, self._onOpenBoxes),
         (
          self.viewModel.onSetBlur, self._onSetBlur),
         (
          self.viewModel.onRewardsShown, self._onRequestOpenDoor))

    def _onClose(self, *args, **kwargs):
        self.destroyWindow()

    def _onOpenBoxes(self):
        self.destroyWindow()

    def _onSetBlur(self, event):
        param = event.get('setBlur', '')
        g_eventBus.handleEvent(events.AdventCalendarEvent(events.AdventCalendarEvent.CHANGE_BLUR_STATUS, {'setBlur': param}), scope=EVENT_BUS_SCOPE.LOBBY)

    def _onRequestOpenDoor(self, event):
        if self._isProgressionReward:
            self.viewModel.setOpenDoorStatus(OpenDoorStatus.OPEN_DOOR_SUCCESS)
            return
        else:
            doorId = int(event.get('dayId', 0))
            if not doorId:
                _logger.error('Parameter dayId is missing')
                return
            if BigWorld.player() is not None:
                self._requestOpenDoor(doorId=doorId)
            return

    def _requestOpenDoor(self, doorId):
        _logger.debug('Created open request for doorId=%d', doorId)
        openDoorClb = partial(self._processServerDoorOpen, dayId=doorId)
        openAndWaitDoor(dayID=doorId, currency=self._currency, callback=openDoorClb)

    def _processServerDoorOpen(self, dayId, result):
        _logger.debug('Waiting for reward window finished, doorId=%d', dayId)
        status = OpenDoorStatus.OPEN_DOOR_SUCCESS if result else OpenDoorStatus.OPEN_DOOR_FAILED
        self.viewModel.setOpenDoorStatus(status)
        if not result:
            self._onSetBlur({'setBlur': False})
            self.destroyWindow()


class RewardWindow(LobbyWindow):

    def __init__(self, dayId, isProgressionReward, data, currency='', parent=None):
        super(RewardWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.FULLSCREEN_WINDOW, content=RewardView(dayId, isProgressionReward, data, currency=currency), parent=parent)