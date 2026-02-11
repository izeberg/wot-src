from fun_random.gui.battle_control.arena_info.arena_descrs import FunRandomArenaDescription
from gui.impl import backport
from gui.impl.gen import R

class LunarPossessionArenaDescription(FunRandomArenaDescription):
    LUNAR_SCREEN_ICON = 'lunar_possession/gui/maps/icons/battleLoading/lunar_bg.png'

    def getDescriptionString(self, isInBattle=True):
        return backport.text(R.strings.lunar_battle.preBattle.description())

    def getWinString(self, isInBattle=True):
        return backport.text(R.strings.lunar_battle.preBattle.winString())

    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        if sizeFolder == 'c_64x64':
            return backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_mode_logo_small())
        return backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_mode_logo())

    def getBattleTypeIconPathSmall(self):
        return backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_mode_logo_small())

    def getBattleTypeIconPathBig(self):
        return backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_mode_logo())

    def getScreenIcon(self):
        return self.LUNAR_SCREEN_ICON