import uuid
from PlayerEvents import g_playerEvents
from gui.impl.lobby.gf_notifications.cache import getCache
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from notification.listeners import BaseReminderListener
from notification.settings import NOTIFICATION_TYPE, NotificationData
from skeletons.gui.shared import IItemsCache
from one_time_gift.gui.impl.lobby import OTG_REWARD_AVAILABLE_NOTIFICATION
from one_time_gift.gui.shared.lock_overlays import areNotificationsLockedByOTG
from one_time_gift.notification.decorators import RewardAvailableDecorator
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController

class RewardAvailableListener(BaseReminderListener):
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __ENTITY_ID = 0

    def __init__(self):
        super(RewardAvailableListener, self).__init__(NOTIFICATION_TYPE.OTG_REWARD_AVAILABLE, self.__ENTITY_ID)

    def start(self, model):
        result = super(RewardAvailableListener, self).start(model)
        if result:
            self.__oneTimeGiftController.onSettingsChanged += self.__tryNotify
            self.__oneTimeGiftController.onEntryPointUpdated += self.__tryNotify
            self.__oneTimeGiftController.onPlayerOTGStatusChanged += self.__tryNotify
            g_playerEvents.onDossiersResync += self.__tryNotify
            self.__tryNotify()
        return result

    def stop(self):
        g_playerEvents.onDossiersResync -= self.__tryNotify
        self.__oneTimeGiftController.onPlayerOTGStatusChanged -= self.__tryNotify
        self.__oneTimeGiftController.onEntryPointUpdated -= self.__tryNotify
        self.__oneTimeGiftController.onSettingsChanged -= self.__tryNotify
        super(RewardAvailableListener, self).stop()

    def _createNotificationData(self, priority, **ctx):
        gfDataID = str(uuid.uuid4())
        getCache().setPayload(gfDataID, {})
        data = {'gfDataID': gfDataID}
        return NotificationData(self._getNotificationId(), data, priority, None)

    def _createDecorator(self, data):
        return RewardAvailableDecorator(data.entityID, data.savedData, self._model(), OTG_REWARD_AVAILABLE_NOTIFICATION, data.priorityLevel)

    def __tryNotify(self, *args, **kwargs):
        if not self.__oneTimeGiftController.isEntryPointEnabled:
            self._notifyOrRemove(isAdding=False)
            return
        if areNotificationsLockedByOTG():
            return
        self._notifyOrRemove(isAdding=True, priority=NotificationPriorityLevel.LOW)