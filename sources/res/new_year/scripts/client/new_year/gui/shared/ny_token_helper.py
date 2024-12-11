from lootboxes_common import makeLootboxTokenID
from new_year.helpers.server_settings import getNewYearGeneralConfig

def getSmallLootBoxTokenId():
    return getNewYearGeneralConfig().getSmallLootboxID()


def getSmallLootBoxToken():
    tokenId = getSmallLootBoxTokenId()
    if tokenId:
        return makeLootboxTokenID(tokenId)
    else:
        return