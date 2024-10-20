import typing
from helpers import dependency
from skeletons.gui.game_control import IEventLootBoxesController
if typing.TYPE_CHECKING:
    from typing import FrozenSet, Generator, Type
    from skeletons.gui.game_control import IEntitlementsConsumer
LOOT_BOX_COUNTER_ENTITLEMENT = 'loot_box_counter'
ENTITLEMENTS = (
 LOOT_BOX_COUNTER_ENTITLEMENT,)
_CONSUMERS = frozenset((
 IEventLootBoxesController,))

def iterConsumers():
    return (dependency.instance(iConsumer) for iConsumer in _CONSUMERS)