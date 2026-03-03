from __future__ import absolute_import
import typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle
    from gui.impl.lobby.vehicle_hub.vehicle_hub_main_view import VehicleHubCtx

class SubPresenterBase(SubModelPresenter):
    __slots__ = ('__vhCtx', )
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, model, parentView):
        self.__vhCtx = None
        super(SubPresenterBase, self).__init__(model, parentView)
        return

    @property
    def vehicleHubCtx(self):
        return self.__vhCtx

    @property
    def currentVehicle(self):
        if self.vehicleHubCtx:
            return self._itemsCache.items.getItemByCD(self.__vhCtx.intCD)
        else:
            return

    def setVehicleHubCtx(self, vhCtx):
        self.__vhCtx = vhCtx

    def initialize(self, vhCtx, *args, **kwargs):
        super(SubPresenterBase, self).initialize(*args, **kwargs)
        self.setVehicleHubCtx(vhCtx)