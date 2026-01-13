import enum, typing, BigWorld
from dyn_components_groups import groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from xml_config_specs import StrParam, EnumParam, ListParam, ObjParam

@enum.unique
class SMSoundComponentPlayMode(str, enum.Enum):
    NONE = 'none'
    SELF = 'self'
    OTHERS = 'others'
    ALL = 'all'


@groupComponent(soundEvents=ListParam(valueParam=ObjParam(activation=StrParam(), deactivation=StrParam(), playTo=EnumParam(enum=SMSoundComponentPlayMode, default=SMSoundComponentPlayMode.SELF))))
class SMSoundAbstractComponent(DynamicScriptComponent):

    def __init__(self, *_, **__):
        super(SMSoundAbstractComponent, self).__init__()
        self._activationIsPlayed = False

    def onDestroy(self):
        if self._activationIsPlayed:
            for config in self.groupComponentConfig.soundEvents:
                self._playSound(config.playTo, config.deactivation)

        super(SMSoundAbstractComponent, self).onDestroy()

    def _onAvatarReady(self):
        self._activationIsPlayed = True
        for config in self.groupComponentConfig.soundEvents:
            self._playSound(config.playTo, config.activation)

    def _isPlayerVehicle(self):
        avatar = BigWorld.player()
        if not avatar:
            return False
        return self.entity.id == avatar.playerVehicleID

    def _needToPlay(self, param):
        playTo = getattr(SMSoundComponentPlayMode, param.upper())
        if playTo == SMSoundComponentPlayMode.ALL:
            return True
        if playTo == SMSoundComponentPlayMode.SELF and self._isPlayerVehicle():
            return True
        if playTo == SMSoundComponentPlayMode.OTHERS and not self._isPlayerVehicle():
            return True
        return False

    def _playSound(self, playTo, soundName):
        if soundName and self._needToPlay(playTo):
            self._play(soundName)

    def _play(self, soundName):
        raise NotImplementedError