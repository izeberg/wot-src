import typing
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates
from gui.impl.new_year.navigation import NewYearNavigation
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from helpers.events_handler import EventsHandler
from hangar_selectable_objects import HangarSelectableLogic
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class HOSelectableLogicPresenter(SubModelPresenter, EventsHandler):
    _VEHICLE_COLLISION_AUTO_ACTIVATE = False

    def __init__(self, model, parentView=None, *args, **kwargs):
        super(HOSelectableLogicPresenter, self).__init__(model, parentView)
        self.__selectableLogic = None
        self.__isActive = False
        self.__isVehicleEntitySelected = False
        return

    def initialize(self, *args, **kwargs):
        super(HOSelectableLogicPresenter, self).initialize(*args, **kwargs)
        self._activateSelectableLogic()
        if self._VEHICLE_COLLISION_AUTO_ACTIVATE:
            self._selectVehicleEntity()

    def finalize(self):
        super(HOSelectableLogicPresenter, self).finalize()
        self._deactivateSelectableLogic()
        self.__selectableLogic = None
        if not NewYearNavigation.getNavigationState().isCloseMainViewInProcess:
            self._deselectVehicleEntity()
        return

    def _activateSelectableLogic(self):
        if self.__selectableLogic is None:
            self.__selectableLogic = HangarSelectableLogic()
        if not self.__isActive:
            self.__selectableLogic.init()
            self.__isActive = True
        return

    def _deactivateSelectableLogic(self):
        if self.__isActive:
            self.__selectableLogic.fini()
            self.__isActive = False

    def _updateSelectVehicleEntity(self, isSelect):
        if isSelect:
            self._selectVehicleEntity()
        else:
            self._deselectVehicleEntity()

    @dependency.replace_none_kwargs(hangarSpace=IHangarSpace)
    def _selectVehicleEntity(self, hangarSpace=None):
        if self.__isVehicleEntitySelected:
            return
        if not hangarSpace.spaceInited or not hangarSpace.space.getVehicleEntity():
            return
        vehicleEntity = hangarSpace.space.getVehicleEntity()
        vehicleEntity.setEnable(False)
        vehicleEntity.setState(CameraMovementStates.ON_OBJECT)
        self.__isVehicleEntitySelected = True

    @dependency.replace_none_kwargs(hangarSpace=IHangarSpace)
    def _deselectVehicleEntity(self, hangarSpace=None):
        if self.__isVehicleEntitySelected is False:
            return
        if not hangarSpace.spaceInited or not hangarSpace.space.getVehicleEntity():
            return
        hangarSpace.space.getVehicleEntity().onDeselect()
        self.__isVehicleEntitySelected = False