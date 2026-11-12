from enum import Enum
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_video_reward_view_model import CustomizationResourceVideoRewardViewModel
from gui.impl.pub import ViewImpl, WindowImpl
from sound_gui_manager import CommonSoundSpaceSettings

class Sounds(Enum):
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'
    CUSTOMIZATION_RESOURCE_REWARD_SCREEN = 'customization_resource_reward_screen'


class CustomizationResourceVideoRewardView(ViewImpl):
    __slots__ = ('__closeCallback', )
    _COMMON_SOUND_SPACE = CommonSoundSpaceSettings(name='customization_resource_view', entranceStates={Sounds.OVERLAY_HANGAR_GENERAL.value: Sounds.OVERLAY_HANGAR_GENERAL_ON.value}, exitStates={Sounds.OVERLAY_HANGAR_GENERAL.value: Sounds.OVERLAY_HANGAR_GENERAL_OFF.value}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.CUSTOMIZATION_RESOURCE_REWARD_SCREEN.value)

    def __init__(self, layoutID, closeCallback):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = CustomizationResourceVideoRewardViewModel()
        self.__closeCallback = closeCallback
        super(CustomizationResourceVideoRewardView, self).__init__(settings)

    def _onLoaded(self, *args, **kwargs):
        super(CustomizationResourceVideoRewardView, self)._onLoaded(*args, **kwargs)
        if Waiting.isOpened('loading'):
            Waiting.hide('loading')

    @property
    def viewModel(self):
        return super(CustomizationResourceVideoRewardView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),)

    def __onClose(self):
        self.__closeCallback()


class CustomizationResourceVideoRewardViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, parent=None, closeCallback=None):
        super(CustomizationResourceVideoRewardViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CustomizationResourceVideoRewardView(R.views.lobby.customization_resource.CustomizationResourceVideoRewardView(), closeCallback), parent=parent, layer=WindowLayer.OVERLAY)