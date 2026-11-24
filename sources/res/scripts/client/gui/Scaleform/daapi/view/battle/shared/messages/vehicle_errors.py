from __future__ import absolute_import
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages

class VehicleErrorMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleErrorMessages, self).__init__('VehicleErrorsPanel', 'vehicle_errors_panel.xml')

    def __del__(self):
        LOG_DEBUG('VehicleErrorMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey
        crosshairCtrl = self.sessionProvider.shared.crosshair
        if crosshairCtrl is not None:
            crosshairCtrl.onCrosshairViewChanged += self.__onCrosshairLayoutChanged
            crosshairCtrl.onCrosshairPositionChanged += self.__onCrosshairLayoutChanged
            crosshairCtrl.onCrosshairScaleChanged += self.__onCrosshairLayoutChanged
            self.__onCrosshairLayoutChanged()
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        crosshairCtrl = self.sessionProvider.shared.crosshair
        if crosshairCtrl is not None:
            crosshairCtrl.onCrosshairViewChanged -= self.__onCrosshairLayoutChanged
            crosshairCtrl.onCrosshairPositionChanged -= self.__onCrosshairLayoutChanged
            crosshairCtrl.onCrosshairScaleChanged -= self.__onCrosshairLayoutChanged
        super(VehicleErrorMessages, self)._removeGameListeners()
        return

    def __onShowVehicleErrorByKey(self, key, args=None, extra=None):
        self.showMessage(key, args, extra)

    def __onCrosshairLayoutChanged(self, *_):
        crosshairCtrl = self.sessionProvider.shared.crosshair
        _, posY = crosshairCtrl.getScaledPosition()
        self.as_setCrosshairLayoutS(posY, crosshairCtrl.getViewID())