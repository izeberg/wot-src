from uilogging.lootboxes import constants
from uilogging.lootboxes.loggers import LootboxFlowLogger
from uilogging.lootboxes.loggers import LootboxStorageLogger
from uilogging.lootboxes.loggers import LootboxProbabilityViewLogger
from wotdecorators import noexcept

@noexcept
def logLootboxStorageOpen(source, item):
    destination = constants.Views.STORAGE
    LootboxFlowLogger().log(action=constants.Actions.OPEN, sourceItem=source, destinationItem=destination, transitionMethod=item)