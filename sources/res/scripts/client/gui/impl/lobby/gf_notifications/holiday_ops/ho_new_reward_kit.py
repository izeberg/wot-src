from gui.shared import g_eventBus, events as events_constants
from ho_notification import HONotification
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_new_reward_kit_model import NyNewRewardKitModel
from gui.shared.gui_items.loot_box import NewYearLootBoxes
from new_year.ny_navigation_helper import showLootBox
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import ILootBoxSystemController
from skeletons.gui.shared import IItemsCache

class HONewRewardKit(HONotification):
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __lootBoxesCtrl = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, resId, *args, **kwargs):
        model = NyNewRewardKitModel()
        super(HONewRewardKit, self).__init__(resId, model, *args, **kwargs)

    @property
    def viewModel(self):
        return super(HONewRewardKit, self).getViewModel()

    def _getEvents(self):
        events = super(HONewRewardKit, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),)

    def _update(self):
        data = self._getPayload()
        with self.viewModel.transaction() as (model):
            model.setIsButtonDisabled(not self._canNavigate())
            model.setIsPopUp(self._isPopUp)
            model.setKitsCount(data['count'])
            model.setCategory(data['category'])

    def _canNavigate(self):
        return super(HONewRewardKit, self)._canNavigate() and self.__lobbyContext.getServerSettings().isLootBoxesEnabled() and self._nyController.isEnabled() and self.__lootBoxesCtrl.isActive(NewYearLootBoxes.PREMIUM)

    def __onClick(self):
        if self._canNavigate():
            g_eventBus.handleEvent(events_constants.HidePopoverEvent(events_constants.HidePopoverEvent.HIDE_POPOVER))
            showLootBox(lootBoxType=NewYearLootBoxes.PREMIUM)