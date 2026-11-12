import typing
from account_helpers.settings_core.settings_constants import GAME
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleTextWithIcon
from gui.shared.gui_items.Vehicle import getNationLessName, getIconResourceName
from gui.shared.gui_items.artefacts import getAbilityVO
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.shared.gui_items.Vehicle import Vehicle

def getBaseButtonsVO(vehicle):
    iconName = getIconResourceName(getNationLessName(vehicle.name))
    return {'shopIconPath': backport.image(R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)()), 
       'compareBtnVisible': True, 
       'goToVehicleViewBtnVisible': True, 
       'isPremium': vehicle.isPremium, 
       'vehicleId': vehicle.intCD, 
       'isEarlyAccess': vehicle.isEarlyAccess}


def getBaseDataVO(vehicle):
    return {'showDemountAllPairsBtn': False, 
       'showExpBlock': False, 
       'vehicleButton': {}, 'vehicleInfo': {}, 'nation': vehicle.nationName}


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def getBaseTitleVO(vehicle, settingsCore=None):
    tankUserName = vehicle.userName
    difficulty = vehicle.difficulty
    if not settingsCore.getSetting(GAME.SHOW_VEHICLE_DIFFICULTY_IN_RESEARCH):
        difficulty = 0
    return {'intCD': vehicle.intCD, 
       'tankNameStr': text_styles.grandTitle(tankUserName), 
       'tankNameStrSmall': text_styles.promoTitle(tankUserName), 
       'statusStr': '', 
       'roleText': getRoleTextWithIcon(vehicle.role, vehicle.roleLabel), 
       'difficulty': difficulty, 
       'showInfoIcon': False, 
       'ability': getAbilityVO(vehicle)}