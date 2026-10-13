from __future__ import absolute_import
import typing
from gui.shared.gui_items import GUI_ITEM_TYPE
from halloween.gui.halloween_account_settings import setSettings, AccountSettingsKeys, getSettings
from halloween.gui.hw_vehicle_role_helper import getVehicleRole
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from helpers import dependency
from shared_utils import first
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from halloween_common.configs.halloween_bestiary import EnemyModel
    from typing import Optional
    from vehicle_outfit.outfit import Outfit

def getEnemyRole(enemyType):
    return getVehicleRole(enemyType) or enemyType.classTag


@dependency.replace_none_kwargs(c11nService=ICustomizationService, itemsCache=IItemsCache)
def getOutfit(styleID, vehIntCD, c11nService=None, itemsCache=None):
    style = c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
    vehicle = itemsCache.items.getVehicleCopyByCD(vehIntCD)
    if style and vehicle:
        return style.getOutfit(season=first(style.seasons), vehicleCD=vehicle.descriptor.makeCompactDescr())
    else:
        return


@dependency.replace_none_kwargs(hwArtefactsCtrl=IHalloweenArtefactsController)
def getUnlockMissionIdx(enemy, hwArtefactsCtrl=None):
    if hwArtefactsCtrl:
        return hwArtefactsCtrl.getIndex(enemy.unlockedByToken)
    return 0


@dependency.replace_none_kwargs(hwArtefactsCtrl=IHalloweenArtefactsController)
def isEnemyUnlocked(enemy, hwArtefactsCtrl=None):
    if hwArtefactsCtrl:
        return hwArtefactsCtrl.isArtefactReceived(enemy.unlockedByToken)
    return False


def getLastSelectedEnemy():
    return getSettings(AccountSettingsKeys.LAST_SELECTED_BESTIARY_ENEMIES)


def setLastSelectedEnemy(enemyIntCD):
    setSettings(AccountSettingsKeys.LAST_SELECTED_BESTIARY_ENEMIES, enemyIntCD)


def getEnemiesSeenList():
    return getSettings(AccountSettingsKeys.BESTIARY_ENEMIES_SEEN)


def markEnemyAsSeen(enemyIntCD):
    enemiesSeenList = getEnemiesSeenList()
    if enemyIntCD and enemyIntCD not in enemiesSeenList:
        enemiesSeenList.add(enemyIntCD)
        setSettings(AccountSettingsKeys.BESTIARY_ENEMIES_SEEN, enemiesSeenList)