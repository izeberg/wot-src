from __future__ import absolute_import
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME
from advent_calendar.gui.impl.lobby.feature.notifications.available_doors_view import AvailableDoorsView
from advent_calendar.notification.listeners import DoorsAvailableListener
from advent_calendar.gui.shared.advent_system_factory import collectDoorsAvailableListener
from gui.impl.gen import R
from gui.shared.system_factory import registerNotificationsListeners, registerGamefaceNotifications, ProxyInjection

def registerAdventNotifications():
    registerNotificationsListeners((
     ProxyInjection(collectDoorsAvailableListener, DoorsAvailableListener),))
    registerGamefaceNotifications({ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME: (
                                                         R.views.advent_calendar.mono.lobby.notification_view(), AvailableDoorsView)})