from __future__ import absolute_import
import typing
from Event import Event
from frameworks.state_machine import BaseStateObserver, visitor
from frameworks.wulf import WindowLayer
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.page.header.default_model import DefaultModel
from gui.impl.lobby.common.presenters.currnet_vehicles_filter_component import CurrentVehicleFilterComponent
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
from gui.impl.lobby.new_year.states import HolidayOpsState
from gui.impl.lobby.new_year.widgets.ho_balance_widget import HOBalanceWidget
from gui.impl.lobby.new_year.widgets.ho_economic_bonus_widget import HOEconomicBonusWidget
from gui.impl.lobby.page.fight_start import FightStartPresenter
from gui.impl.lobby.page.header_state_presenter import HeaderStatePresenter
from gui.impl.lobby.page.navigation_presenter import NavigationPresenter
from gui.impl.lobby.page.prebattle_presenter import PrebattlePresenter
from gui.impl.lobby.page.prem_shop_presenter import PremShopPresenter
from gui.impl.lobby.page.reserves_entry_point_presenter import ReservesEntryPointPresenter
from gui.impl.lobby.page.user_account_presenter import UserAccountPresenter
from gui.impl.lobby.page.wallet_presenter import WalletPresenter, GoldProvider, CreditsProvider, CrystalProvider, FreeXpProvider
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from skeletons.new_year import INewYearController
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from frameworks.state_machine import StateEvent, State

class _HolidayOpsObserver(BaseStateObserver):

    def __init__(self):
        super(_HolidayOpsObserver, self).__init__()
        self.onNavigationChanged = Event()

    def clear(self):
        super(_HolidayOpsObserver, self).clear()
        self.onNavigationChanged.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return visitor.isDescendantOf(state, lsm.getStateByCls(HolidayOpsState))

    def onStateChanged(self, state, stateEntered, event=None):
        self.onNavigationChanged(stateEntered)
        super(_HolidayOpsObserver, self).onStateChanged(state, stateEntered, event)


class LobbyHeader(ViewComponent[DefaultModel]):
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        self._currentVehicleFilter = CurrentVehicleFilterComponent()
        super(LobbyHeader, self).__init__(R.views.mono.hangar.header(), DefaultModel)
        self.__holidayOpsObserver = _HolidayOpsObserver()
        self.__isHOViewOpened = False

    @property
    def viewModel(self):
        return super(LobbyHeader, self).getViewModel()

    @property
    def isHOEventEnabled(self):
        return self.__nyController.isEnabled()

    @property
    def isHOPanelVisible(self):
        return self.isHOEventEnabled and self.__isHOViewOpened

    def setOldStyleViewFlag(self, value):
        self.viewModel.setOldStyle(value)

    def _onLoading(self, *args, **kwargs):
        self._currentVehicleFilter.initialize()
        lsm = getLobbyStateMachine()
        lsm.connect(self.__holidayOpsObserver)
        self.viewModel.setIsHOPanelVisible(self.isHOPanelVisible)
        super(LobbyHeader, self)._onLoading(*args, **kwargs)

    def _finalize(self):
        super(LobbyHeader, self)._finalize()
        self._currentVehicleFilter.destroy()
        self._currentVehicleFilter = None
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__holidayOpsObserver)
        self.__holidayOpsObserver = None
        return

    def _onLoaded(self, *args, **kwargs):
        self.viewModel.setIsHOEventEnabled(self.isHOEventEnabled)
        super(LobbyHeader, self)._onLoaded()

    def _getEvents(self):
        return (
         (
          self.__nyController.onStateChanged, self.__onHOStateChanged),
         (
          self.__holidayOpsObserver.onNavigationChanged, self.__onHONavigationChanged))

    def _getChildComponents(self):
        header = R.aliases.lobby_header.default
        return {header.FightStart(): FightStartPresenter, 
           header.NavigationBar(): NavigationPresenter, 
           header.Prebattle(): PrebattlePresenter, 
           header.Wallet(): lambda : WalletPresenter((
                           CrystalProvider(),
                           GoldProvider(),
                           CreditsProvider(),
                           FreeXpProvider())), 
           header.UserAccount(): UserAccountPresenter, 
           header.HeaderState(): HeaderStatePresenter, 
           header.ReservesEntryPoint(): ReservesEntryPointPresenter, 
           header.PremShop(): PremShopPresenter, 
           header.CurrentVehicle(): lambda : VehiclesInfoPresenter(self._currentVehicleFilter), 
           R.aliases.holiday_ops.default.BalancePanel(): HOBalanceWidget, 
           R.aliases.holiday_ops.default.EconomicBonusPanel(): HOEconomicBonusWidget}

    def _getPopOverLayer(self):
        return WindowLayer.VIEW

    def __onHOStateChanged(self):
        with self.viewModel.transaction() as (model):
            model.setIsHOPanelVisible(self.isHOPanelVisible)
            model.setIsHOEventEnabled(self.isHOEventEnabled)

    def __onHONavigationChanged(self, stateEntered):
        self.__isHOViewOpened = stateEntered
        self.viewModel.setIsHOPanelVisible(self.isHOPanelVisible)