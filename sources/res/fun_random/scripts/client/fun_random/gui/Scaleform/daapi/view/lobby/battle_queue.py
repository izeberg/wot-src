from __future__ import absolute_import
import constants
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.shared.gui_items.Vehicle import getTypeBigIconPath
TYPES_ORDERED = (
 (
  'heavyTank', ITEM_TYPES.VEHICLE_TAGS_HEAVY_TANK_NAME),
 (
  'mediumTank', ITEM_TYPES.VEHICLE_TAGS_MEDIUM_TANK_NAME),
 (
  'lightTank', ITEM_TYPES.VEHICLE_TAGS_LIGHT_TANK_NAME),
 (
  'AT-SPG', ITEM_TYPES.VEHICLE_TAGS_AT_SPG_NAME))

class FunRandomQueueProvider(RandomQueueProvider, FunAssetPacksMixin, FunSubModesWatcher):

    def getIconPath(self, iconlabel):
        return backport.image(self.getModeIconsResRoot().battleTypes.c_136x136.fun_random())

    def getTitle(self, guiType):
        return self.__getTitle() or self.getModeUserName()

    def processQueueInfo(self, qInfo):
        info = dict(qInfo)
        if 'classes' in info:
            vClasses = info['classes']
            vClassesLen = len(vClasses)
        else:
            vClasses = []
            vClassesLen = 0
        self._createCommonPlayerString(sum(vClasses))
        if vClassesLen > 0:
            vClassesData = []
            for vClass, message in TYPES_ORDERED:
                idx = constants.VEHICLE_CLASS_INDICES[vClass]
                vClassesData.append({'type': message, 
                   'icon': getTypeBigIconPath(vClass), 
                   'count': vClasses[idx] if idx < vClassesLen else 0})

            self._proxy.as_setDPS(vClassesData)
        self._proxy.as_showStartS(self._isStartButtonDisplayed(vClasses))

    @hasDesiredSubMode()
    def _doRequestQueueInfo(self, currPlayer):
        super(FunRandomQueueProvider, self)._doRequestQueueInfo(currPlayer)

    def _getRequestQueueInfoParams(self):
        return (
         self._queueType, self.getDesiredSubMode().getSubModeID())

    @hasDesiredSubMode(defReturn='')
    def __getTitle(self):
        subModeName = backport.text(self.getDesiredSubMode().getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)