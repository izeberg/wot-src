from Vehicle import Vehicle
from constants import ROLE_TYPE, ROLE_TYPE_TO_LABEL
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleIcon
from helpers import dependency
from skeletons.gui.shared import IItemsCache

def getRoleMessage(role):
    if role == ROLE_TYPE.NOT_DEFINED:
        return ''
    roleLabel = ROLE_TYPE_TO_LABEL.get(role)
    msg = text_styles.concatStylesToSingleLine(getRoleIcon(roleLabel), ' ', backport.text(R.strings.menu.roleExp.roleName.dyn(roleLabel)(), groupName=backport.text(R.strings.menu.roleExp.roleGroupName.dyn(roleLabel)())))
    return makeHtmlString('html_templates:vehicleStatus', Vehicle.VEHICLE_STATE_LEVEL.ROLE, {'message': msg})


def isSecretExtendedNonInventoryVehicle(vehTypeCompDescr):
    vehicle = dependency.instance(IItemsCache).items.getItemByCD(vehTypeCompDescr)
    return vehicle.isSecretExtended and vehicle.invID == -1


def removeNationFromTechName(string):
    result = string.split(':')
    if len(result) > 1:
        return result[1]
    if result:
        return result[0]
    return ''