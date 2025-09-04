from __future__ import absolute_import
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import VehicleParamsPresenter
from gui.impl.gen import R
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.items_parameters import params_helper

class VehicleHubCharacteristicsPresenter(VehicleParamsPresenter):

    def __init__(self, vehIntCD):
        super(VehicleHubCharacteristicsPresenter, self).__init__(vehIntCD, layoutID=R.aliases.common.none(), applyFormatting=False)

    def _getComparator(self):
        vehicle = self._getVehicle()
        return params_helper.tankSetupVehiclesComparator(vehicle, vehicle)

    def _isExtraParamEnabled(self):
        return True

    def _isAdditionalValueEnabled(self):
        return True

    def _getIsOpened(self, groupName):
        return True

    def _getParamTooltips(self):
        parentTooltips = super(VehicleHubCharacteristicsPresenter, self)._getParamTooltips()
        return parentTooltips | {TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_ADVANCED_PARAMETERS}