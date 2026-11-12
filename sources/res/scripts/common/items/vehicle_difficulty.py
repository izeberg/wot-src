import typing, ResMgr, resource_helper
from constants import ITEM_DEFS_PATH, VEHICLE_DIFFICULTY
from items import _xml, vehicles
from soft_exception import SoftException
_VEHICLE_DIFFICULTY_XML_PATH = ITEM_DEFS_PATH + 'vehicle_difficulty.xml'
_g_baseVehicleDifficulties = None

def _readDifficulties():
    reader = ResMgr.openSection(_VEHICLE_DIFFICULTY_XML_PATH)
    xmlCtx = (None, _VEHICLE_DIFFICULTY_XML_PATH)
    if reader is None:
        _xml.raiseWrongXml(xmlCtx, '', 'Vehicle difficulty config is missing')
    xmlCtx, difficultiesSection = _xml.getSubSectionWithContext(xmlCtx, reader, 'difficulties')
    difficulties = {}
    for tag, vehicleSection in difficultiesSection.items():
        if tag != 'vehicle':
            _xml.raiseWrongXml(xmlCtx, tag, "Section name != 'vehicle'")
        vehicleName = _xml.readString(xmlCtx, vehicleSection, 'name')
        vehicleCtx = (xmlCtx, vehicleName)
        try:
            vehicleCD = vehicles.makeVehicleTypeCompDescrByName(vehicleName)
        except SoftException as error:
            _xml.raiseWrongXml(vehicleCtx, 'name', str(error))

        difficulty = _xml.readInt(vehicleCtx, vehicleSection, 'difficulty')
        if difficulty not in VEHICLE_DIFFICULTY.ALL:
            _xml.raiseWrongXml(vehicleCtx, 'difficulty', ('Invalid vehicle difficulty: {}').format(difficulty))
        difficulties[vehicleCD] = difficulty

    resource_helper.purgeResource(_VEHICLE_DIFFICULTY_XML_PATH)
    return difficulties


def getDefaultDifficulties():
    global _g_baseVehicleDifficulties
    if _g_baseVehicleDifficulties is None:
        _g_baseVehicleDifficulties = _readDifficulties()
    return _g_baseVehicleDifficulties