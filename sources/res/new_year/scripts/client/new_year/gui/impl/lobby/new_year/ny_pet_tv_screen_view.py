from new_year.gui.impl.gen.view_models.views.lobby.new_year.ny_pet_tv_screen_view_model import NyPetTvScreenViewModel, PetTvAnimation
from new_year.skeletons.new_year import IRaccoonAnimationController
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from helpers import dependency
from gui.impl.gen import R

class NyPetTvScreenView(ViewImpl):
    __slots__ = ()
    __raccoonCtrl = dependency.descriptor(IRaccoonAnimationController)

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.new_year.lobby.new_year.NyPetTvScreenView(), model=NyPetTvScreenViewModel())
        super(NyPetTvScreenView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyPetTvScreenView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(NyPetTvScreenView, self)._onLoading(*args, **kwargs)
        self.__syncState()

    def _getEvents(self):
        return (
         (
          self.__raccoonCtrl.onTvRaidPresentationChanged, self.__onTvRaidPresentationChanged),
         (
          self.__raccoonCtrl.onTvAnimationChanged, self.__onTvAnimationChanged),
         (
          self.viewModel.onAnimationFinished, self.__onAnimationFinished),
         (
          self.viewModel.onResetToIdle, self.__onResetToIdle))

    def __syncState(self):
        with self.viewModel.transaction() as (model):
            model.setIsRaidActive(self.__raccoonCtrl.isRaidActive)
            model.setAnimation(self.__raccoonCtrl.tvAnimation)

    def __onTvRaidPresentationChanged(self, isActive):
        self.viewModel.setIsRaidActive(isActive)

    def __onTvAnimationChanged(self, animation):
        self.viewModel.setAnimation(animation)

    def __onAnimationFinished(self):
        self.__raccoonCtrl.onTvPresentationFinished()

    def __onResetToIdle(self):
        if self.__raccoonCtrl.isRaidStarted and self.__raccoonCtrl.isRaidActive:
            self.__raccoonCtrl.setTvAnimation(PetTvAnimation.WALK)