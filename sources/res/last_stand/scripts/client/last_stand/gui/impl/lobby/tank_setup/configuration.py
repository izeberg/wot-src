from __future__ import absolute_import
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController, ConsumableTabs
from last_stand.gui.impl.lobby.tank_setup.array_provider import LSConsumableProvider

class LastStandTabsController(ConsumableTabsController):
    __slots__ = ()

    def _getAllProviders(self):
        return {ConsumableTabs.DEFAULT: LSConsumableProvider}