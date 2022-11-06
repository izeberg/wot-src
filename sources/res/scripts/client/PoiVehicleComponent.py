from PoiBaseComponent import PoiBaseComponent
from points_of_interest.components import PoiVehicleStateComponent

class PoiVehicleComponent(PoiBaseComponent):

    def __init__(self):
        super(PoiVehicleComponent, self).__init__()
        self.__stateComponent = None
        return

    def onDestroy(self):
        self._poiGameObject.removeComponent(self.__stateComponent)
        self.__stateComponent = None
        super(PoiVehicleComponent, self).onDestroy()
        return

    def _onAvatarReady(self):
        self.__stateComponent = self._poiGameObject.createComponent(PoiVehicleStateComponent, self.pointID)