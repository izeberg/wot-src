from helpers import dependency
from constants import DEFAULT_HANGAR_SCENE
from CurrentVehicle import g_currentPreviewVehicle
from gui.impl.lobby.gf_notifications.holiday_ops.notifications_utils import createNavigationAction, createStylePreviewAction
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase
from gui.prb_control.entities.base.listener import IPrbListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from skeletons.new_year import INewYearController
from skeletons.gui.game_control import IHangarSpaceSwitchController, IGFNotificationsController
from skeletons.new_year import IFriendServiceController

def _isRandomPrbActive(prbEntity):
    if prbEntity is None:
        return False
    else:
        return bool(prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANDOM)


class HONotification(NotificationBase, IPrbListener):
    _nyController = dependency.descriptor(INewYearController)
    __hangarSwitchController = dependency.descriptor(IHangarSpaceSwitchController)
    _gfNotificationController = dependency.descriptor(IGFNotificationsController)
    __friendController = dependency.descriptor(IFriendServiceController)

    @property
    def currentHangarAcceptable(self):
        return self.__hangarSwitchController.currentSceneName == DEFAULT_HANGAR_SCENE and _isRandomPrbActive(self.prbEntity)

    def _onLoading(self, *args, **kwargs):
        super(HONotification, self)._onLoading(*args, **kwargs)
        self._gfNotificationController.onBattleQueueStateUpdated += self._update

    def _finalize(self):
        self._gfNotificationController.onBattleQueueStateUpdated -= self._update
        super(HONotification, self)._finalize()

    def _update(self):
        pass

    def _navigateToNy(self, objectName, executeBeforeSwitch=None):
        if self._canNavigate():
            action = createNavigationAction(objectName, executeBeforeSwitch=executeBeforeSwitch)
            if self.currentHangarAcceptable:
                action()
            else:
                self._gfNotificationController.selectRandomBattle(action)

    def _canShowStyle(self):
        return not g_currentPreviewVehicle.isPresent()

    def _showStylePreview(self, style):
        if self._canNavigate():
            action = createStylePreviewAction(style)
            if self.currentHangarAcceptable:
                if self.__friendController.isInFriendHangar:
                    self.__friendController.leaveFriendHangar()
                action()
            else:
                self._gfNotificationController.selectRandomBattle(action)