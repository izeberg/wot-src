from CurrentVehicle import HeroTankPreviewAppearance
from frameworks.wulf import WindowLayer
from BWUtil import AsyncReturn
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.gen import R
from frameworks.wulf import WindowFlags
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events
from gui.shared.event_dispatcher import showShop, _getModuleInfoViewName, showBrowserOverlayView, findAndLoadWindow
from gui.shared.lock_overlays import lockNotificationManager
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from halloween.gui.halloween_gui_constants import HW_LOCK_SOURCE_NAME
from halloween.gui.halloween_account_settings import AccountSettingsKeys, getSettings
from halloween.gui.impl.lobby.tank_setup.dialogs.confirm_dialog import HWTankSetupConfirmDialog
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency
from gui.impl.pub.notification_commands import WindowNotificationCommand
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.impl import INotificationWindowController
from wg_async import wg_await, wg_async

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _getUrl(urlName=None, url=None, lobbyContext=None):
    hostUrl = lobbyContext.getServerSettings().shop.hostUrl
    if url:
        return hostUrl + url
    else:
        return hostUrl + ('' if urlName is None else GUI_SETTINGS.lookup('hwShop').get(urlName))


def getLoadedViewByLayoutID(layoutID):
    uiLoader = dependency.instance(IGuiLoader)
    if uiLoader and uiLoader.windowsManager:
        return uiLoader.windowsManager.getViewByLayoutID(layoutID)
    else:
        return


def isViewLoaded(layoutID):
    uiLoader = dependency.instance(IGuiLoader)
    if not uiLoader or not uiLoader.windowsManager or uiLoader.windowsManager.getViewByLayoutID(layoutID):
        return True
    return False


def isViewLoadedWrap(layoutID):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if isViewLoaded(layoutID=layoutID):
                return None
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator


def showHangar():
    from halloween.gui.impl.lobby.states import HalloweenHangarState
    HalloweenHangarState.goTo()


def isHangarLoaded():
    return isViewLoaded(R.views.halloween.mono.lobby.hangar())


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showMetaIntroView(forceOpen=True, parent=None, hwCtrl=None):
    if not hwCtrl.isInfoMetaEnabled():
        return
    from halloween.gui.impl.lobby.meta_intro_view import MetaIntroWindow
    layoutID = R.views.halloween.mono.lobby.meta_intro()
    isShowed = getSettings(AccountSettingsKeys.META_INTRO_VIEW_SHOWED)
    if isViewLoaded(layoutID) or isShowed and not forceOpen:
        return
    wnd = MetaIntroWindow(parent)
    wnd.load()


def showVehiclePreview(**kwargs):
    kwargs.update({'isHiddenMenu': True})
    from halloween.gui.impl.lobby.states import HalloweenVehiclePreviewState
    HalloweenVehiclePreviewState.goTo(ctx=kwargs)


def showHeroTankPreview(vehTypeCompDescr, previewAlias=VIEW_ALIAS.LOBBY_HANGAR, previousBackAlias=None, previewBackCb=None, hangarVehicleCD=None, backOutfit=None, backBtnLabel='', isHiddenMenu=True, isKingReward=False):
    ctx = {'itemCD': vehTypeCompDescr, 
       'previewAlias': previewAlias, 
       'previewAppearance': HeroTankPreviewAppearance(), 
       'isHeroTank': True, 
       'previousBackAlias': previousBackAlias, 
       'previewBackCb': previewBackCb, 
       'hangarVehicleCD': hangarVehicleCD, 
       'backOutfit': backOutfit, 
       'backBtnLabel': backBtnLabel, 
       'isHiddenMenu': isHiddenMenu, 
       'isKingReward': isKingReward}
    from halloween.gui.impl.lobby.states import HalloweenHeroTankPreviewState
    HalloweenHeroTankPreviewState.goTo(ctx=ctx)


def showRewardPathView():
    from halloween.gui.impl.lobby.states import RewardPathState
    RewardPathState.goTo()


@dependency.replace_none_kwargs(notificationsMgr=INotificationWindowController)
def showPromoWindowView(forceOpen=False, notificationsMgr=None):
    from halloween.gui.impl.lobby.promo_window_view import PromoWindow
    layoutID = R.views.halloween.mono.lobby.promo()
    isShowed = getSettings(AccountSettingsKeys.PROMO_SCREEN_SHOWED)
    if isViewLoaded(layoutID=layoutID) or isShowed and not forceOpen:
        return
    window = PromoWindow(layoutID)
    notificationsMgr.append(WindowNotificationCommand(window))


def showDifficultyView(level, useQueue=False):
    from halloween.gui.impl.lobby.difficulty_window_view import DifficultyWindow
    layoutID = R.views.halloween.mono.lobby.difficulty_congrat()
    findAndLoadWindow(useQueue, DifficultyWindow, layoutID, level)


def showComparisonWindow():
    from halloween.gui.impl.lobby.comparison_window_view import ComparisonWindow
    layoutID = R.views.halloween.mono.lobby.comparison()
    if isViewLoaded(layoutID=layoutID):
        return
    wnd = ComparisonWindow(layoutID)
    wnd.load()


def showKingRewardCongratsView(artefactID, useQueue=False):
    from halloween.gui.impl.lobby.king_reward_congrats_view import KingRewardCongratsWindow
    layoutID = R.views.halloween.mono.lobby.king_reward_congrat()
    findAndLoadWindow(useQueue, KingRewardCongratsWindow, layoutID, artefactID)


def showCrewSelectionWindow():
    from halloween.gui.impl.lobby.crew_showcase_view import CrewShowcaseWindow
    wnd = CrewShowcaseWindow()
    wnd.load()


def showDecryptWindowView(artefactID, useQueue=False, isReward=False):
    from halloween.gui.impl.lobby.decrypt_view import DecryptWindow
    findAndLoadWindow(useQueue, DecryptWindow, artefactID, isReward)


def showAttachmentRewardView(element, isFirstEntry, useQueue=True):
    from halloween.gui.impl.lobby.attachment_reward_view import AttachmentRewardWindow
    findAndLoadWindow(useQueue, AttachmentRewardWindow, element, isFirstEntry)


def showTwitchConExchangeView(useQueue=True):
    from halloween.gui.impl.lobby.reward_selection_view import RewardSelectionWindow
    layoutID = R.views.halloween.mono.lobby.reward_selection()
    findAndLoadWindow(useQueue, RewardSelectionWindow, layoutID)


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showIntroVideo(hwCtrl=None):
    if not hwCtrl.isIntroVideoEnabled():
        return
    url = GUI_SETTINGS.lookup('hwIntroVideo')
    showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showInfoPage(hwCtrl=None):
    if not hwCtrl.isInfoPageEnabled():
        return
    url = GUI_SETTINGS.lookup('infoPageHalloween')
    showBrowserOverlayView(url, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BROWSER, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


def showHWHangarAmmunitionSetupView(**kwargs):
    from halloween.gui.impl.lobby.states import HalloweenAmmunitionSetupLoadout
    HalloweenAmmunitionSetupLoadout.goTo(**kwargs)


@dependency.replace_none_kwargs(notificationsMgr=INotificationWindowController)
def showBattleResult(arenaUniqueID, notificationsMgr=None):
    from halloween.gui.impl.lobby.battle_result_view import BattleResultView as BattleResultViewInLobby
    layoutID = R.views.halloween.mono.lobby.battle_result()
    if isViewLoaded(layoutID=layoutID):
        return
    ctx = {'arenaUniqueID': arenaUniqueID}
    view = BattleResultViewInLobby(layoutID, ctx)
    window = LobbyNotificationWindow(WindowFlags.WINDOW_FULLSCREEN, content=view, layer=WindowLayer.FULLSCREEN_WINDOW)
    lockNotificationManager(True, source=HW_LOCK_SOURCE_NAME, postponeActive=True)
    notificationsMgr.append(WindowNotificationCommand(window))
    lockNotificationManager(False, source=HW_LOCK_SOURCE_NAME, releasePostponed=True)


@dependency.replace_none_kwargs(hwArtefactsController=IHalloweenArtefactsController)
def showHalloweenShopAll(hwArtefactsController=None):
    hwArtefactsController.resetSelectedArtefactID()
    showShop(_getUrl('hwShopAll'))


@dependency.replace_none_kwargs(hwArtefactsController=IHalloweenArtefactsController)
def showHalloweenShopVehicle(hwArtefactsController=None):
    hwArtefactsController.resetSelectedArtefactID()
    showShop(_getUrl('hwShopVehicle'))


@dependency.replace_none_kwargs(hwArtefactsController=IHalloweenArtefactsController)
def showHalloweenShopBundle(bundleUrl, hwArtefactsController=None):
    hwArtefactsController.resetSelectedArtefactID()
    showShop(_getUrl(url=bundleUrl))


def showBundleWindow(**kwargs):
    from halloween.gui.impl.lobby.states import HalloweenExchangeScreenState
    HalloweenExchangeScreenState.goTo(**kwargs)


@wg_async
def showHWTankSetupConfirmDialog(items, vehicle=None, startState=None, parent=None):
    from gui.impl.dialogs import dialogs
    result = yield wg_await(dialogs.showSingleDialogWithResultData(layoutID=R.views.lobby.tanksetup.dialogs.Confirm(), wrappedViewClass=HWTankSetupConfirmDialog, items=items, vehicle=vehicle, startState=startState, parent=parent))
    raise AsyncReturn(result)


def showModuleInfo(itemCD, vehicleDescr):
    itemCD = int(itemCD)
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_MODULE_INFO, _getModuleInfoViewName(itemCD, vehicleDescr)), ctx={'moduleCompactDescr': itemCD, 
       'vehicleDescr': vehicleDescr}), EVENT_BUS_SCOPE.LOBBY)


def closeViewsByID(layoutIDs):
    uiLoader = dependency.instance(IGuiLoader)
    if not uiLoader or not uiLoader.windowsManager:
        return
    for layoutID in layoutIDs:
        view = uiLoader.windowsManager.getViewByLayoutID(layoutID)
        if view:
            view.destroyWindow()