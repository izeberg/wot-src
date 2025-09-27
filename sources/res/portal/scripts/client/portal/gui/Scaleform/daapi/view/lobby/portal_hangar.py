from helpers import dependency
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar
from portal_common.portal_constants import QUEUE_TYPE, GameSeasonType
from portal.skeletons.portal_event_controller import IPortalEventController
from skeletons.gui.game_control import ISeasonsController
from skeletons.gui.system_messages import ISystemMessages

class PortalHangar(Hangar):
    __seasonsController = dependency.descriptor(ISeasonsController)
    __portalBattlesCtrl = dependency.descriptor(IPortalEventController)
    __systemMessages = dependency.descriptor(ISystemMessages)

    def _populate(self):
        super(PortalHangar, self)._populate()
        self.__portalBattlesCtrl.onPortalBattleConfigChanged += self.__onConfigChanged

    def _dispose(self):
        self.__portalBattlesCtrl.onPortalBattleConfigChanged -= self.__onConfigChanged
        super(PortalHangar, self)._dispose()

    def __onConfigChanged(self, diff):
        if self.__getCurrentQueueType() != QUEUE_TYPE.PORTAL:
            return
        if not self.__seasonsController.getCurrentSeason(GameSeasonType.PORTAL):
            self.__portalBattlesCtrl.selectRandomBattle()

    def __getCurrentQueueType(self):
        if self.prbEntity:
            return self.prbEntity.getQueueType()
        return QUEUE_TYPE.UNKNOWN