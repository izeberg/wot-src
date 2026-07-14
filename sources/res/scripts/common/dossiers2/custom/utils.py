from __future__ import absolute_import
from items import vehicles
import arena_achievements

def getVehicleNationID(vehTypeCompDescr):
    return vehicles.parseIntCompactDescr(vehTypeCompDescr)[1]


def isVehicleSPG(vehTypeCompDescr):
    _, nationID, vehicleID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
    return 'SPG' in vehicles.g_list.getList(nationID)[vehicleID].tags


def getInBattleSeriesIndex(seriesName):
    return arena_achievements.INBATTLE_SERIES_INDICES[seriesName]