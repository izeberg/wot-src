import BigWorld
from PortalVehicleChangeShotComponent import PortalVehicleChangeShotComponent
from portal.gui.Scaleform.daapi.view.meta.PortalInterceptionWidgetMeta import PortalInterceptionWidgetMeta

class InterceptionWidget(PortalInterceptionWidgetMeta):

    def _populate(self):
        super(InterceptionWidget, self)._populate()
        PortalVehicleChangeShotComponent.onControlStarted += self.__onControlStarted

    def _dispose(self):
        PortalVehicleChangeShotComponent.onControlStarted -= self.__onControlStarted
        super(InterceptionWidget, self)._dispose()

    def __onControlStarted(self, avatarID, timeLeft):
        if avatarID == BigWorld.player().id:
            self.as_updateTimeS(int(timeLeft))