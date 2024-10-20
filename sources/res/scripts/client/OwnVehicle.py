import logging, BigWorld, BattleReplay
from OwnVehicleBase import OwnVehicleBase
from Avatar import PlayerAvatar
_logger = logging.getLogger(__name__)

class OwnVehicle(OwnVehicleBase):

    def _avatar(self):
        avatar = BigWorld.player()
        if avatar.isObserver() and BattleReplay.isServerSideReplay():
            attachedVehicle = avatar.getVehicleAttached()
            if not attachedVehicle or attachedVehicle.id != self.entity.id:
                return None
        return avatar

    def _doLog(self, msg):
        _logger.info(msg)

    def _serverTime(self):
        return BigWorld.serverTime()

    def _entities(self):
        return BigWorld.entities