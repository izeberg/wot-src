from __future__ import absolute_import
import logging
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig
from gui.shared.system_factory import registerBannerEntryPointValidator
from journey_marathon.gui.game_control import registerJMSystemHandlers
from journey_marathon.gui.impl.lobby.gf_notifications import registerJMNotifications
from system_events import g_systemEvents
_info = logging.getLogger(__name__).info

def preInit():
    _info('preInit personality: %s', __name__)
    registerJMSystemHandlers()
    registerJMNotifications()
    g_systemEvents.onDependencyConfigReady += _updateServicesConfigAndRegisterBanner


def init():
    g_overrideScaleFormViewsConfig.initExtensionLobbyPackages(__name__, ('journey_marathon.gui.impl.lobby', ))


def start():
    pass


def fini():
    _info('fini personality: %s', __name__)
    from jm_services_config import updateServicesConfig
    g_systemEvents.onDependencyConfigReady -= updateServicesConfig


def _updateServicesConfigAndRegisterBanner(manager):
    from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
    from jm_services_config import updateServicesConfig
    from journey_marathon.gui.impl.lobby.jm_event_banner import JmEventBanner
    updateServicesConfig(manager)
    banners = EventBannersContainer()
    banners.registerEventBanner(JmEventBanner)
    registerBannerEntryPointValidator(JmEventBanner.NAME, JmEventBanner.isEnabled)