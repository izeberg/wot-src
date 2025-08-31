from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport
from gui.impl.gen import R

class Comp7LightQueueProvider(RandomQueueProvider):

    def processQueueInfo(self, qInfo):
        info = dict(qInfo)
        allPlayersCount = info.get('players', 0)
        self._proxy.as_setDPS([
         {'type': backport.text(R.strings.menu.prebattle.playersLabel()), 
            'icon': backport.image(R.images.comp7_light.gui.maps.icons.icons.playersTotalIcon()), 
            'count': allPlayersCount, 
            'highlight': False}])

    def getLayoutStr(self):
        return 'comp7Light'

    def getIconPath(self, iconlabel):
        return backport.image(R.images.comp7_light.gui.maps.icons.battleTypes.c_136x136.comp7_light())

    def getTankInfoLabel(self):
        return ''

    def getTankIcon(self, vehicle):
        return ''

    def getTankName(self, vehicle):
        return ''

    def needAdditionalInfo(self):
        return False

    def additionalInfo(self):
        return ''