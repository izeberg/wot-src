from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R

class NyVehiclePreview(VehiclePreview):

    def _getBackBtnLabel(self):
        return ''

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(NyVehiclePreview, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_PY_ALIAS:
            viewPy.setPanelTextData(**{'uniqueVehicleTitle': backport.text(R.strings.ny.leaderboard.vehiclePreview.description())})