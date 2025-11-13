from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R

class NyVehiclePreview(VehiclePreview):

    def __init__(self, ctx=None):
        super(NyVehiclePreview, self).__init__(ctx)
        self.__isVehicleSelectable = ctx.get('isVehicleSelectable', False)
        self.__isShowBackButton = ctx.get('isShowBackButton', False)

    def _populate(self):
        super(NyVehiclePreview, self)._populate()
        self._hangarSpace.setVehicleSelectable(self.__isVehicleSelectable)

    def _getData(self):
        result = super(NyVehiclePreview, self)._getData()
        result['showBackButton'] = self.__isShowBackButton
        return result

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(NyVehiclePreview, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_PY_ALIAS:
            viewPy.setPanelTextData(**{'uniqueVehicleTitle': backport.text(R.strings.ny.leaderboard.vehiclePreview.description())})