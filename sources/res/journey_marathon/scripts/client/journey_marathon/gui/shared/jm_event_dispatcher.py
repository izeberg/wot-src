from __future__ import absolute_import
from account_helpers.settings_core.settings_constants import OnceOnlyHints
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import findAndLoadWindow, showBrowserOverlayView, showShop
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

def showJmMapView():
    from journey_marathon.gui.impl.lobby.jm_lsm_states import JmMapState
    JmMapState.goTo()


def showJmIntro():
    from journey_marathon.gui.impl.lobby.jm_intro_view import JmIntroWindow
    JmIntroWindow().load()


def showInfoPage():
    from journey_marathon.jm_helpers import jmCtrl
    infoPageUrl = jmCtrl().jmConfig.getJMInfoPageUrl()
    showBrowserOverlayView(infoPageUrl, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def showCustomizationRarityAwardScreen(element, settingsCore=None):
    from journey_marathon.gui.impl.lobby.attachement_reward import AttachmentRewardWindow
    newC11nSectionHintClicked = settingsCore.serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.NEW_C11N_SECTION_HINT)
    findAndLoadWindow(True, AttachmentRewardWindow, element, not newC11nSectionHintClicked)


def showVehicleRewardScreen(nodeID):
    from journey_marathon.gui.impl.lobby.jm_final_reward_view import JmFinalRewardWindow
    findAndLoadWindow(True, JmFinalRewardWindow, nodeID)


def showLoreOverlay(loreNodeId):
    from journey_marathon.gui.impl.lobby.jm_lore_overlay_view import JmLoreOverlayWindow
    JmLoreOverlayWindow(loreNodeId).load()


def openJmShop():
    from journey_marathon.jm_helpers import jmCtrl
    shopLink = jmCtrl().jmConfig.getJmShopLink()
    showShop(path=shopLink)


def showJmAnniversaryPresentScreen(bonuses):
    from journey_marathon.gui.impl.lobby.jm_anniversary_present_view import JmAnniversaryPresentWindow
    return findAndLoadWindow(True, JmAnniversaryPresentWindow, bonuses)