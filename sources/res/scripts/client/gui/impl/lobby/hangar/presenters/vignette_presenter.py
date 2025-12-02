from __future__ import absolute_import
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vignette_model import VignetteModel
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from skeletons.new_year import INewYearController

class VignettePresenter(ViewComponent[VignetteModel]):
    _hoController = dependency.descriptor(INewYearController)

    def __init__(self):
        super(VignettePresenter, self).__init__(model=VignetteModel)

    @property
    def viewModel(self):
        return super(VignettePresenter, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(VignettePresenter, self)._onLoading(*args, **kwargs)
        self.__fillModel()

    def _getEvents(self):
        return (
         (
          self._hoController.onStateChanged, self.__fillModel),
         (
          self._hoController.onStateInitialized, self.__fillModel))

    def __fillModel(self):
        with self.getViewModel().transaction() as (model):
            isHOHangarActive = self._hoController.isEnabled() or self._hoController.isSuspended()
            model.setIsHolidayOpsHangarActive(isHOHangarActive)