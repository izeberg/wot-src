from helpers import dependency
from lootboxes_common import makeLootboxTokenID
from new_year.helpers.server_settings import getNewYearMachineConfig
from skeletons.gui.shared import IItemsCache

def isMachineEnabled():
    return getNewYearMachineConfig().isEnabled()


def getMachineLootboxTokenId():
    return getNewYearMachineConfig().getLootboxID()


def getMachineLootboxToken():
    tokenId = getMachineLootboxTokenId()
    if tokenId:
        return makeLootboxTokenID(tokenId)
    else:
        return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getMachineKeysCount(itemsCache=None):
    return itemsCache.items.tokens.getTokenCount(getMachineLootboxToken())