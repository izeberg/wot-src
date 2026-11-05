from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.server_events.event_items import Quest
    from Event import Event
    from advent_calendar.helpers.server_settings import AdventCalendarConfig
    from gui.shared.gui_items.loot_box import LootBox
    from helpers.server_settings import LootBoxesTooltipConfig

class IAdventCalendarController(IGameController):
    onConfigChanged = None
    onDoorsStateChanged = None
    onDoorOpened = None
    onLootBoxesConfigChanged = None

    @property
    def isActive(self):
        raise NotImplementedError

    @property
    def isEnabled(self):
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    def isInActivePhase(self):
        raise NotImplementedError

    def isAvailableAndActivePhase(self):
        raise NotImplementedError

    def isAvailableAndPostActivePhase(self):
        raise NotImplementedError

    def isInPostActivePhase(self):
        raise NotImplementedError

    def isFirstEventDay(self):
        raise NotImplementedError

    def awaitDoorOpenQuestCompletion(self, dayID, currency):
        raise NotImplementedError

    def progressionQuestMayBeCompleted(self, openedDoorsAmount=None):
        raise NotImplementedError

    @property
    def config(self):
        raise NotImplementedError

    @property
    def startDate(self):
        raise NotImplementedError

    @property
    def postEventStartDate(self):
        raise NotImplementedError

    @property
    def postEventEndDate(self):
        raise NotImplementedError

    def getDoorOpenQuestName(self, day):
        raise NotImplementedError

    def getDoorOpenTokenName(self, day):
        raise NotImplementedError

    def getDoorOpenTimeUI(self, doorId):
        raise NotImplementedError

    def getCurrentDayNumber(self):
        raise NotImplementedError

    @property
    def getCurrentTime(self):
        raise NotImplementedError

    def getQuestByDayId(self, dayId):
        raise NotImplementedError

    def isDoorOpened(self, dayID):
        raise NotImplementedError

    @property
    def progressionRewardQuestsOrdered(self):
        raise NotImplementedError

    @property
    def completedAwardsQuests(self):
        raise NotImplementedError

    @property
    def lootBoxesTooltipConfig(self):
        raise NotImplementedError

    def getRewardsLootBox(self):
        raise NotImplementedError

    def getAdventCalendarGroupedQuestsRewards(self):
        raise NotImplementedError