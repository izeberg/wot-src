from __future__ import absolute_import
from gui.battle_results.components import base

class EventPointsItem(base.StatsItem):

    def _convert(self, value, reusable):
        return value['avatar']['eventPoints']


class VehicleCommanderIDItem(base.StatsItem):

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).vehicleCommanderID


class VehicleDoubleDamage(base.StatsItem):

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).doubleTotalDamage