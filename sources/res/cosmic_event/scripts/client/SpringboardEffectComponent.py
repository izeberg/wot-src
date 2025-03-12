import BigWorld
from cosmic_sound import CosmicBattleSounds

class SpringboardEffectComponent(BigWorld.DynamicScriptComponent):

    def set_timeApply(self, _):
        CosmicBattleSounds.playBoardJump(self.entity.position)