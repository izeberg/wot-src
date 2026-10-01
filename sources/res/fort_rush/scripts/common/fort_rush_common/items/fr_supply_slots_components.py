from __future__ import absolute_import
from items import vehicles
from items.components.supply_slots_components import EquipmentSlot

class FortRushEquipmentSlot(EquipmentSlot):
    __slots__ = ('excludeTags', )

    def __init__(self):
        super(FortRushEquipmentSlot, self).__init__()
        self.excludeTags = frozenset()

    def readFromSection(self, section):
        super(FortRushEquipmentSlot, self).readFromSection(section)
        self.excludeTags = frozenset(section.readString('excludeTags').split())

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        item = descr
        if item is None:
            _, _, itemID = parsedCompDescr
            item = vehicles.g_cache.equipments()[itemID]
        itemTags = getattr(item, 'tags', frozenset())
        excluded = self.excludeTags.intersection(itemTags)
        if excluded:
            return (False,
             ('Equipment tags ({}) are excluded from this slot ({})').format(sorted(itemTags), sorted(excluded)))
        else:
            return super(FortRushEquipmentSlot, self)._checkSlotCompatibility(parsedCompDescr, descr)