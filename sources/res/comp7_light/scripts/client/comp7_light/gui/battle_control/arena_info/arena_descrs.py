from gui.battle_control.arena_info.arena_descrs import ArenaDescriptionWithInvitation
from gui.impl import backport
from gui.impl.gen import R

class Comp7LightBattlesDescription(ArenaDescriptionWithInvitation):

    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        iconRes = R.images.comp7_light.gui.maps.icons.battleTypes.dyn(sizeFolder).dyn(self.getFrameLabel())
        if iconRes.exists():
            return backport.image(iconRes())
        return ''