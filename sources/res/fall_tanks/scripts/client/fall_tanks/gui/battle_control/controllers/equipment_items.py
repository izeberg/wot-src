from __future__ import absolute_import
from gui.battle_control.controllers.consumables.equipment_ctrl import _VisualScriptItem, _ReplayItem

class FallTanksEquipmentItem(_VisualScriptItem):

    @property
    def isReusable(self):
        return bool(self._descriptor)

    def canActivate(self, entityName=None, avatar=None):
        if not self._getComponent():
            return (False, self._getErrorMsg())
        return super(FallTanksEquipmentItem, self).canActivate(entityName, avatar)


class FallTanksReplyEquipmentItem(_ReplayItem, FallTanksEquipmentItem):

    def getAnimationType(self):
        return FallTanksEquipmentItem.getAnimationType(self)

    def update(self, quantity, stage, timeRemaining, totalTime):
        _ReplayItem.update(self, quantity, stage, timeRemaining, totalTime)
        FallTanksEquipmentItem.update(self, quantity, stage, timeRemaining, totalTime)

    def canActivate(self, entityName=None, avatar=None):
        return FallTanksEquipmentItem.canActivate(self, entityName, avatar)

    def _getErrorMsg(self):
        return FallTanksEquipmentItem._getErrorMsg(self)