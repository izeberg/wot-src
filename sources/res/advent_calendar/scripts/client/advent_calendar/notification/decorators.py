from __future__ import absolute_import
from gui.shared.notifications import NotificationGroup, NotificationGuiSettings
from messenger import g_settings
from notification.decorators import MessageDecorator
from notification.settings import NOTIFICATION_TYPE

class DoorsAvailableDecorator(MessageDecorator):

    def __init__(self, entityID, model, notificationData, notificationName):
        self.__notificationName = notificationName
        super(DoorsAvailableDecorator, self).__init__(entityID, self.__makeEntity(**notificationData.savedData), self.__makeSettings(notificationData.priorityLevel), model)

    def getGroup(self):
        return NotificationGroup.OFFER

    def getType(self):
        return NOTIFICATION_TYPE.ADVENT_CALENDAR_DOORS_AVAILABLE

    def __makeEntity(self, linkageData):
        return g_settings.msgTemplates.format(self.__notificationName, data={'linkageData': linkageData})

    @staticmethod
    def __makeSettings(priority):
        return NotificationGuiSettings(isNotify=True, priorityLevel=priority)