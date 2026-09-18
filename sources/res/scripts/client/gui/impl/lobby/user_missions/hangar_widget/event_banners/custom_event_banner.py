from __future__ import absolute_import
import typing
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class CustomEventBanner(BaseEventBanner):

    @classmethod
    def getPluginPath(cls):
        raise NotImplementedError

    def fillModel(self, model):
        super(CustomEventBanner, self).fillModel(model)
        model.setPluginPath(self.getPluginPath())