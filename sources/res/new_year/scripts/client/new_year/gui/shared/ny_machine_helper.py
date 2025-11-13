from new_year.helpers.server_settings import getNewYearMachineConfig
from lootboxes_common import makeLootboxTokenID
from skeletons.gui.shared import IItemsCache
from constants import LOOTBOX_TOKEN_PREFIX
from helpers import dependency

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


def stripOpenedLootboxTokens(rewardsDict):
    tokens = rewardsDict.get('tokens')
    if not tokens:
        return rewardsDict
    filtered = {t:v for t, v in tokens.iteritems() if not (t.startswith(LOOTBOX_TOKEN_PREFIX) and v.get('count', 0) < 0) if not t.startswith(LOOTBOX_TOKEN_PREFIX) and v.get('count', 0) < 0}
    if len(filtered) == len(tokens):
        return rewardsDict
    out = rewardsDict.copy()
    out['tokens'] = filtered
    return out