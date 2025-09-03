import constants
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared, comp7_i18n_helpers
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7QueueProvider(RandomQueueProvider):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def processQueueInfo(self, qInfo):
        info = dict(qInfo)
        ranks = info.get('ranks', {})
        qualPlayers = info.get('qualPlayers', 0)
        allPlayersCount = info.get('players', sum(ranks.values()) + qualPlayers)
        self._createCommonPlayerString(allPlayersCount)
        if ranks:
            ranksData = []
            isInQualification = comp7_shared.isQualification()
            playerRankIdx = (isInQualification or comp7_shared.getPlayerDivision()).rank if 1 else None
            for rankIdx, playersCount in ranks.items():
                rankName = comp7_i18n_helpers.RANK_MAP[rankIdx]
                ranksData.append(self.__getRankData(rankName, playersCount, rankIdx == playerRankIdx))

            ranksData.append(self.__getRankData('qualification', qualPlayers, isInQualification))
            self._proxy.as_setDPS(ranksData)
        self._proxy.as_showStartS(constants.IS_DEVELOPMENT and allPlayersCount > 1)
        return

    def getLayoutStr(self):
        return 'comp7'

    def getIconPath(self, iconlabel):
        return backport.image(R.images.comp7.gui.maps.icons.battleTypes.c_136x136.comp7())

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

    def __getRankData(self, rankName, playersCount, isHighlight):
        seasonName = comp7_core_model_helpers.getSeasonNameEnum(self.__comp7Controller, SeasonName).value
        rankImg = R.images.comp7.gui.maps.icons.ranks.dyn(seasonName).c_40.dyn(rankName)
        rankStr = R.strings.comp7_ext.rank.dyn(rankName)
        return {'type': backport.text(rankStr()), 
           'icon': backport.image(rankImg()), 
           'count': playersCount, 
           'highlight': isHighlight}