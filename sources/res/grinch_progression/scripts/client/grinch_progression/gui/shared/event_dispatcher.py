from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from gui import GUI_SETTINGS, SystemMessages
from gui.impl.common.fade_manager import UseFading
from gui.impl.gen import R
from gui.impl.lobby.gf_notifications import pushGFNotification
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared import events, g_eventBus
from gui.shared.event_dispatcher import findAndLoadWindow
from helpers import dependency
from skeletons.gui.impl import IGuiLoader

def showHangar():
    if not isHangarLoaded():
        gpController = dependency.instance(IGrinchProgressionController)
        if gpController.getIsFirstEntry():
            showGameBoardProgressionInfoView()
            return
        showGameBoardView()


def isHangarLoaded():
    return isViewLoaded(R.views.grinch_progression.mono.lobby.game_board())


def isViewLoaded(layoutID):
    uiLoader = dependency.instance(IGuiLoader)
    if uiLoader.windowsManager.getViewByLayoutID(layoutID):
        return True
    return False


def showGameBoardView():
    from grinch_progression.gui.impl.lobby.states import GrinchHangarState
    GrinchHangarState.goTo()


def showGrinchResultsView(arenaUniqueID):
    from grinch_progression.gui.impl.lobby.states import GrinchBattleResultsState
    prbDispatcher = g_prbLoader.getDispatcher()
    if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
        SystemMessages.pushI18nMessage('#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error, priority='high')
        return
    else:
        GrinchBattleResultsState.goTo(arenaUniqueID)
        return


@UseFading(waitForLayoutReady=R.views.grinch_progression.mono.lobby.info_view())
def showGameBoardProgressionInfoView():
    from grinch_progression.gui.impl.lobby.states import GrinchInfoState
    GrinchInfoState.goTo()


def showIntoVideoWindow():
    uiLoader = dependency.instance(IGuiLoader)
    contentResId = R.views.grinch_progression.mono.lobby.intro_video()
    if uiLoader.windowsManager.getViewByLayoutID(contentResId) is None:
        from grinch_progression.gui.impl.lobby.views.intro_video import IntroVideoWindow
        window = IntroVideoWindow()
        window.load()
    return


def showAboutGameBoard():
    url = GUI_SETTINGS.grinchProgressionInfo.get('aboutEventURL')
    if url:
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.SPECIFIED, url))


def showGPStyleRewardNotification(data):
    pushGFNotification('GpStyleReward', data)


def showAttachmentRewardWindow(element, isFirstEntry, useQueue=True):
    from grinch_progression.gui.impl.lobby.attachment_reward_view import AttachmentRewardWindow
    findAndLoadWindow(useQueue, AttachmentRewardWindow, element, isFirstEntry)