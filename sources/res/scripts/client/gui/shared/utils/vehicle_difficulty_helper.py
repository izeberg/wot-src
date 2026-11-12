import typing
from ab_feature_test_token_based_shared import getGroupByFeature
from helpers.dependency import replace_none_kwargs
from items.vehicle_difficulty import getDefaultDifficulties
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
AB_TEST_FEATURE_NAME = 'tanks_difficulty'
AB_TEST_UNLOCKED_GROUP_NAME = 'unlocked'

@replace_none_kwargs(itemsCache=IItemsCache, lobbyContext=ILobbyContext)
def isVehicleDifficultyEnabled(itemsCache=None, lobbyContext=None):
    config = lobbyContext.getServerSettings().vehicleDifficultyConfig
    if not config.isEnabled:
        return False
    tokenNames = itemsCache.items.tokens.getTokens().keys()
    group = getGroupByFeature(tokenNames, AB_TEST_FEATURE_NAME)
    return group == AB_TEST_UNLOCKED_GROUP_NAME


@replace_none_kwargs(itemsCache=IItemsCache, lobbyContext=ILobbyContext)
def getVehicleDifficulty(vehicleCD, itemsCache=None, lobbyContext=None):
    if not isVehicleDifficultyEnabled(itemsCache=itemsCache, lobbyContext=lobbyContext):
        return None
    else:
        config = lobbyContext.getServerSettings().vehicleDifficultyConfig
        if vehicleCD in config.overrides:
            return config.overrides[vehicleCD]
        return getDefaultDifficulties().get(vehicleCD)