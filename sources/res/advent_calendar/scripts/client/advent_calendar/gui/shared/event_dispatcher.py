from __future__ import absolute_import
import logging
from BWUtil import AsyncReturn
from advent_calendar.gui.shared.advent_system_factory import collectPurchaseDialogView, collectRewardWindow, collectCalendarWindow
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from frameworks.wulf import WindowLayer
from gui.impl.pub.dialog_window import DialogButtons
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper
from gui.impl.dialogs import dialogs
from helpers import dependency
from wg_async import wg_async, wg_await
_logger = logging.getLogger(__name__)

def getCalendarWindowType():
    from advent_calendar.gui.impl.lobby.feature.calendar_view import CalendarWindow
    for validator, windowCls in collectCalendarWindow():
        if validator():
            return windowCls

    return CalendarWindow


@dependency.replace_none_kwargs(controller=IAdventCalendarController)
def showAdventCalendarMainWindow(controller=None):
    windowCls = getCalendarWindowType()
    if windowCls.getInstances() or not controller.isAvailable():
        _logger.warning('Can not open the AdventMainView. Feature is not active or view is already opened.')
        return
    windowCls().load()


def showAdventCalendarIntroWindow(**kwargs):
    from advent_calendar.gui.impl.lobby.feature.intro_view import AdventCalendarIntroWindow
    if not AdventCalendarIntroWindow.getInstances():
        AdventCalendarIntroWindow(**kwargs).load()


def showRewardWindow(**kwargs):
    from advent_calendar.gui.impl.lobby.feature.reward_view import RewardWindow
    rewardWindow = RewardWindow
    for validator, viewType in collectRewardWindow():
        if validator():
            rewardWindow = viewType
            break

    if rewardWindow.getInstances():
        _logger.warning('Can not open the advent calendar RewardWindow. View is already opened.')
        return
    rewardWindow(**kwargs).load()


@wg_async
def showPurchaseDialogWindow(dayId, price, currencyProvider, parent=None):
    from advent_calendar.gui.impl.lobby.feature.purchase_dialog_view import PurchaseDialogView
    purchaseDialogView = PurchaseDialogView
    for validator, viewType in collectPurchaseDialogView():
        if validator():
            purchaseDialogView = viewType
            break

    wrapper = FullScreenDialogWindowWrapper(purchaseDialogView(dayId, price, currencyProvider), parent=parent, layer=WindowLayer.FULLSCREEN_WINDOW, doBlur=False)
    dialogResult = yield wg_await(dialogs.show(wrapper))
    result = None if dialogResult.result == DialogButtons.CANCEL else dialogResult.data
    raise AsyncReturn(result)
    return