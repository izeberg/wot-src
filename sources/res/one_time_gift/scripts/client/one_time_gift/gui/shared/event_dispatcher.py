import logging, typing
from BWUtil import AsyncReturn
from gui.impl.gen import R
from gui.impl.pub.notification_commands import EventNotificationCommand, NotificationEvent, WindowNotificationCommand
from helpers import dependency
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
from skeletons.gui.impl import IGuiLoader, INotificationWindowController
from wg_async import wg_async, wg_await
from one_time_gift_common.one_time_gift_constants import BranchListType
if typing.TYPE_CHECKING:
    from typing import Callable, Optional
_logger = logging.getLogger(__name__)

def _switchOrLoadOneTimeGiftView(viewType, *args, **kwargs):
    guiLoader = dependency.instance(IGuiLoader)
    view = guiLoader.windowsManager.getViewByLayoutID(R.views.one_time_gift.mono.lobby.one_time_gift_view())
    if view is not None:
        _logger.info('Found existing OTG view, switching content to %s', viewType)
        view.switchContent(viewType, *args, **kwargs)
        return
    else:
        notificationMgr = dependency.instance(INotificationWindowController)
        from one_time_gift.gui.impl.lobby.meta_view.one_time_gift_view import OneTimeGiftViewWindow
        window = OneTimeGiftViewWindow(viewType, *args, **kwargs)
        notificationMgr.append(WindowNotificationCommand(window))
        return


def showBranchSelectionWindow(branchListType, allVehiclesPurchased=False, onConfirmCallback=None, onCloseCallback=None, onErrorCallback=None):
    _logger.debug('showBranchSelectionWindow(%s, %s, %s, %s, %s)', branchListType, allVehiclesPurchased, onConfirmCallback, onCloseCallback, onErrorCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.BRANCH_SELECTION, branchListType, allVehiclesPurchased, onConfirmCallback, onCloseCallback, onErrorCallback)


def showNewbieBranchRewardWindow(rewards, onCloseCallback=None):
    _logger.debug('showNewbieBranchRewardWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.BRANCH_REWARD, rewards, onCloseCallback=onCloseCallback)


def showFullBranchRewardWindow(rewards, onCloseCallback=None):
    _logger.debug('showFullBranchRewardWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.BRANCH_REWARD, rewards, onCloseCallback=onCloseCallback)


def showNewbieAdditionalRewardWindow(rewards, onCloseCallback=None):
    _logger.debug('showNewbieAdditionalRewardWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.lobby.awards.packers import composeVehicleBonuses, filterNonOwnedVehicles
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    vehicles = list(filter(filterNonOwnedVehicles, composeVehicleBonuses(rewards)))
    if vehicles:
        _switchOrLoadOneTimeGiftView(MainViews.PREMIUM_VEHICLES_REWARD, rewards, onCloseCallback=onCloseCallback)
    elif onCloseCallback is not None:
        onCloseCallback()
    return


def showFullAdditionalRewardWindow(rewards, onCloseCallback=None):
    _logger.debug('showFullAdditionalRewardWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.ADDITIONAL_REWARD, rewards, onCloseCallback=onCloseCallback)


def showCollectorsCompensationWindow(rewards, onCloseCallback=None):
    _logger.debug('showCollectorsCompensationWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.COLLECTORS_COMPENSATION_REWARD, rewards, onCloseCallback=onCloseCallback)


def showIntroWindow(onConfirmCallback=None, onCloseCallback=None, onErrorCallback=None, showAnimation=False):
    _logger.debug('showIntroWindow(%s, %s, %s, %s)', onConfirmCallback, onErrorCallback, onCloseCallback, showAnimation)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.INTRO, onConfirmCallback, onCloseCallback, onErrorCallback, showAnimation=showAnimation)


@wg_async
def showConfirmSelectionDialog(vehCDs, parent=None):
    from gui.impl.dialogs import dialogs
    from one_time_gift.gui.impl.lobby.awards.confirm_selection_view import ConfirmSelectionView
    result = yield wg_await(dialogs.showCustomBlurSingleDialog(layoutID=R.views.one_time_gift.mono.lobby.confirm_selection_view(), parent=parent, wrappedViewClass=ConfirmSelectionView, vehCDs=vehCDs))
    raise AsyncReturn(result)


def getOneTimeGiftView():
    guiLoader = dependency.instance(IGuiLoader)
    return guiLoader.windowsManager.getViewByLayoutID(R.views.one_time_gift.mono.lobby.one_time_gift_view())


def closeOneTimeGiftWindow():
    _logger.debug('closeOneTimeGiftWindow()')
    view = getOneTimeGiftView()
    if view is None:
        _logger.debug('OneTimeGiftView is not found')
        return
    else:
        view.destroyWindow()
        return


def showWDRBranchSelectionWindow(onConfirmCallback=None, onCloseCallback=None, onErrorCallback=None):
    _logger.debug('showWDRBranchSelectionWindow(%s, %s, %s)', onConfirmCallback, onCloseCallback, onErrorCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.BRANCH_SELECTION, BranchListType.ALL, False, onConfirmCallback, onCloseCallback, onErrorCallback, isWDR=True)


def showWDRBranchRewardWindow(rewards, onCloseCallback=None):
    _logger.debug('showWDRBranchRewardWindow(%s, %s)', rewards, onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    _switchOrLoadOneTimeGiftView(MainViews.BRANCH_REWARD, rewards, onCloseCallback=onCloseCallback, isWDR=True)


def showWDRCompensationWindow(onCloseCallback=None):
    _logger.debug('showWDRCompensationWindow(%s)', onCloseCallback)
    from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
    from one_time_gift.gui.impl.lobby.meta_view.one_time_gift_view import OneTimeGiftViewWindow
    OneTimeGiftViewWindow(MainViews.WDR_REWARD_COMPENSATION, onCloseCallback=onCloseCallback, isWDR=True).load()


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def processWDRCompensation(method, notificationMgr=None):
    _logger.debug('processWDRCompensation(%s)', method)
    otgView = getOneTimeGiftView()
    if otgView:
        _logger.warning('OneTimeGift WDR compensation requested with OTG view opened, this should not happen.')
        return
    event = NotificationEvent(method=method)
    notificationMgr.append(EventNotificationCommand(event))


@dependency.replace_none_kwargs(otgCtrl=IOneTimeGiftController)
def tryEnterOneTimeGift(otgCtrl=None):
    if getOneTimeGiftView() is not None:
        return
    else:
        otgCtrl = dependency.instance(IOneTimeGiftController)
        if otgCtrl.isEntryPointEnabled and otgCtrl.isEntryPointActive:
            otgCtrl.onEntryPointClicked()
        return