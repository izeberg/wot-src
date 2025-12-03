from helpers import dependency, time_utils
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
from gui.impl.pub import ViewImpl
from frameworks.wulf import ViewFlags, ViewSettings
from one_time_gift.gui.impl.gen.view_models.views.lobby.otg_event_banner_tooltip_view_model import OtgEventBannerTooltipViewModel
from gui.impl.gen import R

class OTGBannerTooltipView(ViewImpl):
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)

    def __init__(self, *_, **__):
        settings = ViewSettings(R.views.one_time_gift.mono.lobby.otg_event_banner_tooltip())
        settings.flags = ViewFlags.VIEW
        settings.model = OtgEventBannerTooltipViewModel()
        super(OTGBannerTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(OTGBannerTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        currentTime = time_utils.getServerUTCTime()
        with self.viewModel.transaction() as (tx):
            tx.setTimeLeft(self.__oneTimeGiftController.getEndTime() - currentTime)
            tx.setIsActive(self.__oneTimeGiftController.isEntryPointActive)