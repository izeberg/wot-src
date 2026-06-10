from items import vehicles

def getVehicleNationID(vehTypeCompDescr):
    return vehicles.parseIntCompactDescr(vehTypeCompDescr)[1]