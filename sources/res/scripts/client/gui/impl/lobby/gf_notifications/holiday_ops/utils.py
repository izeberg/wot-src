import logging
from account_helpers import AccountSettings
from account_helpers.AccountSettings import LAST_SEEN_COLLECTING_NOTIFY_TIME, LAST_SEEN_FRIENDS_NOTIFY_TIME, LAST_SEEN_NO_FRIENDS_NOTIFY_TIME
from helpers import time_utils
from new_year.ny_resource_collecting_helper import getNYResourceCollectingConfig
from gui.impl.lobby.gf_notifications import pushGFNotification
from gui.impl.lobby.gf_notifications.constants import GFNotificationTemplates
_logger = logging.getLogger(__name__)

def __coolDowner(withCoolDown, cdName, notifyTimeout):
    if withCoolDown is not None:
        serverUTCTime = time_utils.getServerUTCTime()
        lastNotifyTime = AccountSettings.getSettings(cdName)
        if withCoolDown:
            AccountSettings.setSettings(cdName, serverUTCTime)
        else:
            sinceAllowed = serverUTCTime - (lastNotifyTime + notifyTimeout)
            if sinceAllowed < 0:
                _logger.info('notification still on cd, left: %d', -sinceAllowed)
                return True
            AccountSettings.setSettings(cdName, serverUTCTime)
    return False


def sendHOResourceCollectingAvailableMessage(resourcesCount, isExtra=False, withCoolDown=None):
    if __coolDowner(withCoolDown, LAST_SEEN_COLLECTING_NOTIFY_TIME, getNYResourceCollectingConfig().getCollectingNotifyTimeout()):
        return
    pushGFNotification(GFNotificationTemplates.HO_RESOURCES_REMINDER, {'resourceCount': resourcesCount, 'isExtra': isExtra, 'viewType': 'Personal'})


def sendHOFriendResourceCollectingAvailableMessage(resourcesCount, friendName, friendSpaID, withCoolDown=None):
    if __coolDowner(withCoolDown, LAST_SEEN_FRIENDS_NOTIFY_TIME, getNYResourceCollectingConfig().getCollectingNotifyTimeout()):
        return
    pushGFNotification(GFNotificationTemplates.HO_RESOURCES_REMINDER, {'resourceCount': resourcesCount, 'friendName': friendName, 'friendID': friendSpaID, 'viewType': 'Friends'})


def sendHONoFriendsAvailableMessage(resourcesCount, withCoolDown=None):
    if __coolDowner(withCoolDown, LAST_SEEN_NO_FRIENDS_NOTIFY_TIME, getNYResourceCollectingConfig().getNoFriendsNotifyTimeout()):
        return
    pushGFNotification(GFNotificationTemplates.HO_RESOURCES_REMINDER, {'resourceCount': resourcesCount, 'viewType': 'FindFriends'})