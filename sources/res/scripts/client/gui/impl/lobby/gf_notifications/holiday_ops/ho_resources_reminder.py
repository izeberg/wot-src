from adisp import adisp_process, adisp_async
from frameworks.wulf.gui_constants import ViewStatus
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_resources_reminder_model import NyResourcesReminderModel, reminderType
from gui.impl.lobby.gf_notifications.holiday_ops.notifications_utils import isAcceptableState
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.lobby.new_year.states import FriendsState
from gui.shared import g_eventBus, events as events_constants
from helpers import dependency
from new_year.ny_constants import NYObjects, NyWidgetTopMenu
from ho_notification import HONotification
from skeletons.new_year import IFriendServiceController
reminderReverseMapper = {reminderType.PERSONAL.value: reminderType.PERSONAL, 
   reminderType.FRIENDS.value: reminderType.FRIENDS, 
   reminderType.FINDFRIENDS.value: reminderType.FINDFRIENDS}

class HOResourcesReminder(HONotification):
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, resId, *args, **kwargs):
        model = NyResourcesReminderModel()
        super(HOResourcesReminder, self).__init__(resId, model, *args, **kwargs)
        self.__data = self._getPayload()
        self.__viewType = self.__data['viewType']

    @property
    def viewModel(self):
        return super(HOResourcesReminder, self).getViewModel()

    def _getEvents(self):
        events = super(HOResourcesReminder, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),)

    def _canNavigate(self):
        viewType = reminderReverseMapper[self.__viewType]
        if viewType == reminderType.FRIENDS or viewType == reminderType.FINDFRIENDS:
            return super(HOResourcesReminder, self)._canNavigate() and self.__friendsService.isServiceEnabled and self._nyController.isEnabled()
        return super(HOResourcesReminder, self)._canNavigate() and self._nyController.isEnabled()

    def _update(self):
        with self.viewModel.transaction() as (model):
            viewType = reminderReverseMapper[self.__viewType]
            isValid = True
            if viewType == reminderType.PERSONAL:
                model.setIsExtra(self.__data['isExtra'])
            elif viewType == reminderType.FRIENDS:
                model.setFriendName(unicode(self.__data['friendName']))
                isValid = self.__data['friendID'] in self.__friendsService.bestFriendList
            model.setViewType(viewType)
            model.setIsPopUp(self._isPopUp)
            model.setResourcesCount(self.__data['resourceCount'])
            model.setIsButtonDisabled(not self._canNavigate() or not isValid or not isAcceptableState(self.prbEntity))

    @adisp_process
    def __onClick(self):
        self.viewModel.setIsButtonDisabled(True)
        menuName = NewYearNavigation.getCurrentMenuName()
        viewObj = NewYearNavigation.getCurrentObject()
        if self._canNavigate():
            g_eventBus.handleEvent(events_constants.HidePopoverEvent(events_constants.HidePopoverEvent.HIDE_POPOVER))
            if self.viewModel.getViewType() == reminderType.FINDFRIENDS:
                if menuName != NyWidgetTopMenu.FRIENDS:
                    FriendsState.goTo(instantly=False)
            elif self.viewModel.getViewType() == reminderType.PERSONAL:
                if viewObj != NYObjects.RESOURCES or menuName != NyWidgetTopMenu.GLADE:
                    if self.__friendsService.isInFriendHangar:
                        self.__friendsService.leaveFriendHangar()
                    self._navigateToNy(NYObjects.RESOURCES)
            else:
                self.__friendSpaId = self.__data['friendID']
                isSuccess = yield self.__friendsService.updateFriendList()
                if isSuccess and self.__friendSpaId in self.__friendsService.bestFriendList:
                    if not (self.__friendsService.isInFriendHangar and self.__friendsService.friendHangarSpaId == self.__friendSpaId and viewObj == NYObjects.RESOURCES and menuName == NyWidgetTopMenu.FRIEND_GLADE):
                        self._navigateToNy(NYObjects.RESOURCES, executeBeforeSwitch=self.__enterFriendHangar)
                elif self.viewStatus == ViewStatus.LOADED:
                    self.viewModel.setIsButtonDisabled(True)
                    return
            if self.viewStatus == ViewStatus.LOADED:
                self.viewModel.setIsButtonDisabled(False)

    @adisp_async
    @adisp_process
    def __enterFriendHangar(self, callback):
        result = yield self.__friendsService.enterFriendHangar(self.__friendSpaId)
        callback(result)