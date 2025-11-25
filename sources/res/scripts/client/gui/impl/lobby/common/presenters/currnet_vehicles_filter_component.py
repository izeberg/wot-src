import logging, typing, Event
from CurrentVehicle import g_currentVehicle
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class CurrentVehicleFilterComponent(IVehicleFilter):
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        self.onDiff = Event.Event()
        self.__prevVehicle = None
        self._vehicles = {}
        return

    @property
    def criteria(self):
        _logger.warning('Tried to access filter criteria for a current vehicle')
        return

    @property
    def vehicles(self):
        return self._vehicles

    def initialize(self):
        self.__createVehiclesDict()
        if g_currentVehicle.isPresent():
            self.__prevVehicle = g_currentVehicle.item
        g_currentVehicle.onChanged += self.__onVehicleChanged

    def destroy(self):
        g_currentVehicle.onChanged -= self.__onVehicleChanged
        self.__prevVehicle = None
        self._vehicles = None
        self.onDiff.clear()
        return

    def __onVehicleChanged(self):
        oldVehicle = self.__prevVehicle
        self.__createVehiclesDict()
        if oldVehicle is not None:
            self.onDiff({oldVehicle.intCD: oldVehicle})
        self.__prevVehicle = g_currentVehicle.item if g_currentVehicle.isPresent() else None
        self.onDiff(self.vehicles)
        return

    def __createVehiclesDict(self):
        if g_currentVehicle.isPresent():
            self._vehicles = {g_currentVehicle.intCD: g_currentVehicle.item}
        else:
            self._vehicles = {}