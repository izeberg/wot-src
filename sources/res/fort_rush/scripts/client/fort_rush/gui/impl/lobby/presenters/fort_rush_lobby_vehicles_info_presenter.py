from __future__ import absolute_import
import typing
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
from helpers import dependency
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle

class FortRushLobbyVehiclesInfoPresenter(VehiclesInfoPresenter):
    __battleController = dependency.descriptor(IFortRushBattleController)

    def _toModelItem(self, vehicle):
        modelItem = super(FortRushLobbyVehiclesInfoPresenter, self)._toModelItem(vehicle)
        modelItem['isSuitableVehicle'] = self.__battleController.isSuitableVehicle(vehicle) is None
        return modelItem