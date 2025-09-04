import typing
from gui.impl.pub.notification_commands import WindowNotificationCommand
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController

def showClanSupplyView(tabId=None, *args, **kwargs):
    from gui.impl.lobby.clan_supply.states import ClanSupplyState
    ClanSupplyState.goTo(tabId=tabId)


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showClanSupplyRewardWindow(isElite, rewards, notificationMgr=None):
    from gui.impl.lobby.clan_supply.rewards_view import RewardsViewWindow
    window = RewardsViewWindow(isElite, rewards)
    notificationMgr.append(WindowNotificationCommand(window))