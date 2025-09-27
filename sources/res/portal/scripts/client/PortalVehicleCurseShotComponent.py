import BigWorld
from portal.sounds.sound_helpers import playVoiceover
from portal.sounds.sound_constants import PortalAbilityVoiceovers

class PortalVehicleCurseShotComponent(BigWorld.DynamicScriptComponent):

    def set_isAnyHarmCaused(self, _):
        if self.isAnyHarmCaused:
            if self.entity.id == BigWorld.player().playerVehicleID:
                playVoiceover(PortalAbilityVoiceovers.CURSE_SHOT_VOICEOVER)