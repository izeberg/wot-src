import Event
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.env_switcher_btn_tip_model import EnvSwitcherBtnTipModel
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from new_year.skeletons.new_year import INewYearEnvironmentSwitchController
from frameworks.wulf import ViewFlags, ViewSettings
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.shared.utils import IHangarSpace
from gui.impl.pub import ViewImpl
from helpers import dependency
from gui.impl.gen import R

class EnvSwitcherBtnTipInject(InjectComponentAdaptor):
    __nyEnvSwitcherController = dependency.descriptor(INewYearEnvironmentSwitchController)

    def _makeInjectView(self):
        return EnvSwitcherBtnTip()


class EnvSwitcherBtnTip(ViewImpl):
    __slots__ = ('__tipDelayer', 'onTipClosed')
    __nyEnvSwitcherController = dependency.descriptor(INewYearEnvironmentSwitchController)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    TIP_FADE_OUT_TIME = 0.2

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.new_year.lobby.new_year.EnvSwitcherBtnTip(), flags=ViewFlags.VIEW, model=EnvSwitcherBtnTipModel())
        self.onTipClosed = Event.Event()
        self.__tipDelayer = CallbackDelayer()
        super(EnvSwitcherBtnTip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EnvSwitcherBtnTip, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClosed, self.__onClosed),
         (
          self.__hangarSpace.onSpaceCreate, self.__onSpaceCreate),
         (
          self.__nyEnvSwitcherController.onEnvSwitcherBtnPressed, self.__onClosed))

    def _onLoading(self, *args, **kwargs):
        super(EnvSwitcherBtnTip, self)._onLoading(*args, **kwargs)
        if self.__hangarSpace.spaceInited:
            self.__showTip()

    def _finalize(self):
        self.__tipDelayer.clearCallbacks()
        super(EnvSwitcherBtnTip, self)._finalize()

    def __onSpaceCreate(self):
        if self.__nyEnvSwitcherController.needToShowTip:
            self.__showTip()

    def __onClosed(self):
        self.viewModel.setShowTip(False)
        self.__nyEnvSwitcherController.skipSwitcherTip()
        self.__tipDelayer.clearCallbacks()
        self.__tipDelayer.delayCallback(self.TIP_FADE_OUT_TIME, self.__destroyTip)

    def __destroyTip(self):
        self.onTipClosed()
        self.destroy()

    def __showTip(self):
        self.viewModel.setShowTip(True)