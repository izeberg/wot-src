import time, typing
from WeakMethod import WeakMethodProxy
from frameworks.state_machine import StateFlags
from gui.Scaleform.daapi.view.lobby.battle_queue.states import BattleQueueContainerState
from gui.Scaleform.daapi.view.lobby.battle_queue.states import CommonBattleQueueState
from gui.Scaleform.daapi.view.lobby.shared.states import BrowserLobbyTopState
from gui.Scaleform.daapi.view.lobby.veh_post_progression.states import VehiclePostProgressionState
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.crew.states import BarracksState
from gui.impl.lobby.hangar.states import HangarState
from gui.impl.lobby.vehicle_hub import OverviewState, ModulesState, VehSkillTreeState, StatsState, ArmorState
from gui.lobby_state_machine.states import GuiImplViewLobbyState, LobbyState, SFViewLobbyState, SubScopeSubLayerState, LobbyStateFlags, SubScopeTopLayerState, TopScopeTopLayerState, LobbyStateDescription
from gui.lobby_state_machine.transitions import HijackTransition
from gui.prb_control import prbEntityProperty
from halloween.gui.impl.lobby.bundle_view import BundleView
from halloween.gui.impl.lobby.hangar_ammunition_setup_view import HWHangarAmmunitionSetupView
from halloween.gui.impl.lobby.pre_battle_queue_view import PreBattleQueueView
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES
from halloween.gui.shared.event_dispatcher import getLoadedViewByLayoutID, showIntroVideo, showMetaIntroView
from halloween.skeletons.halloween_controller import IHalloweenController
from skeletons.gui.app_loader import IAppLoader
from helpers import dependency
from gui.impl.lobby.vehicle_hub.states import VehicleHubState
from wg_async import wg_async, wg_await, await_callback
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine

def registerStates(machine):
    machine.addState(HalloweenModeState())


def registerTransitions(machine):
    halloweenMode = machine.getStateByCls(HalloweenModeState)
    machine.addNavigationTransitionFromParent(halloweenMode)


@SubScopeSubLayerState.parentOf
class HalloweenModeState(LobbyState):
    STATE_ID = 'halloween'
    halloweenCtrl = dependency.descriptor(IHalloweenController)

    def registerStates(self):
        machine = self.getMachine()
        machine.addState(HalloweenHangarState(StateFlags.INITIAL))
        machine.addState(RewardPathState())
        machine.addState(HalloweenVehiclePreviewState())
        machine.addState(HalloweenHeroTankPreviewState())
        machine.addState(HalloweenAmmunitionSetupLoadout())
        machine.addState(HalloweenPreBattleQueueState())
        machine.addState(HalloweenExchangeScreenState())

    def registerTransitions(self):
        machine = self.getMachine()
        parent = self.getParent()
        hangar = machine.getStateByCls(HalloweenHangarState)
        parent.addNavigationTransition(hangar, record=True)
        parent.addTransition(HijackTransition(HangarState, WeakMethodProxy(self._isEventPrb)), hangar)
        ammunitionSetup = machine.getStateByCls(HalloweenAmmunitionSetupLoadout)
        hangar.addNavigationTransition(ammunitionSetup)
        exchangeScreen = machine.getStateByCls(HalloweenExchangeScreenState)
        hangar.addNavigationTransition(exchangeScreen)
        rewardPath = machine.getStateByCls(RewardPathState)
        rewardPath.addNavigationTransition(exchangeScreen)
        hangar.addNavigationTransition(rewardPath, record=True)
        preBattleQueue = machine.getStateByCls(HalloweenPreBattleQueueState)
        hangar.addNavigationTransition(preBattleQueue, record=True)
        parent.addTransition(HijackTransition(CommonBattleQueueState, WeakMethodProxy(self._isEventPrb)), preBattleQueue)
        states = (
         machine.getStateByCls(OverviewState), machine.getStateByCls(ModulesState),
         machine.getStateByCls(VehSkillTreeState), machine.getStateByCls(StatsState),
         machine.getStateByCls(ArmorState),
         machine.getStateByCls(VehiclePostProgressionState),
         machine.getStateByCls(HalloweenVehiclePreviewState),
         machine.getStateByCls(BarracksState))
        self._registrationTransition(hangar, rewardPath, states)
        vehicleHub = machine.getStateByCls(VehicleHubState)
        vehicleHub.addNavigationTransition(hangar)
        vehicleHub.addNavigationTransition(rewardPath)

    def _registrationTransition(self, hangar, rewardPath, states):
        for state in states:
            hangar.addNavigationTransition(state, record=True)
            rewardPath.addNavigationTransition(state, record=True)

    @classmethod
    def _isEventPrb(cls, event):
        return cls.halloweenCtrl.isEnabled() and cls.halloweenCtrl.isEventPrb()


@HalloweenModeState.parentOf
class HalloweenHangarState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HANGAR
    VIEW_KEY = ViewKey(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HANGAR)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HalloweenHangarState, self).__init__(flags=flags | LobbyStateFlags.HANGAR)
        self.__cachedParams = {}

    def registerTransitions(self):
        lsm = self.getMachine()
        confirmState = lsm.getStateByCls(HalloweenAmmunitionConfirmState)
        loadout = lsm.getStateByCls(HalloweenAmmunitionSetupLoadout)
        self.addGuardTransition(confirmState, WeakMethodProxy(loadout.interactorConfirm))

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.headerButtons.battle.types.halloween()))

    def serializeParams(self):
        return self.__cachedParams

    def _onEntered(self, event):
        super(HalloweenHangarState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        self.__cachedParams = {}
        super(HalloweenHangarState, self)._onExited()


@HalloweenModeState.parentOf
class RewardPathState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH
    VIEW_KEY = ViewKey(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH)
    halloweenCtrl = dependency.descriptor(IHalloweenController)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(RewardPathState, self).__init__(flags=flags)
        self.__cachedParams = {}

    def getNavigationDescription(self):
        infos = []
        if self.halloweenCtrl.isInfoMetaEnabled():
            infos.append(LobbyStateDescription.Info(type=LobbyStateDescription.Info.Type.INFO, onMoreInfoRequested=showMetaIntroView, tooltipBody=backport.text(R.strings.halloween_lobby.rewardPath.aboutTooltip())))
        if self.halloweenCtrl.isIntroVideoEnabled():
            infos.append(LobbyStateDescription.Info(type=LobbyStateDescription.Info.Type.VIDEO, onMoreInfoRequested=showIntroVideo, tooltipBody=backport.text(R.strings.halloween_lobby.rewardPath.introTooltip())))
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.metaCmp.name()), infos=infos)

    def getBackNavigationDescription(self, params):
        return backport.text(R.strings.halloween_lobby.common.toRewardPath())

    def serializeParams(self):
        return self.__cachedParams

    def _onEntered(self, event):
        super(RewardPathState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        self.__cachedParams = {}
        super(RewardPathState, self)._onExited()


@BattleQueueContainerState.parentOf
class HalloweenPreBattleQueueState(GuiImplViewLobbyState):
    STATE_ID = 'halloweenPreBattleQueue'
    VIEW_KEY = ViewKey(R.views.halloween.mono.lobby.pre_battle_queue_view())

    def __init__(self):
        super(HalloweenPreBattleQueueState, self).__init__(PreBattleQueueView, ScopeTemplates.LOBBY_SUB_SCOPE)
        self.__startTime = None
        return

    @prbEntityProperty
    def prbEntity(self):
        return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.preBattle.searching()))

    def serializeParams(self):
        return {'startTime': self.__startTime}

    def _getViewLoadCtx(self, event):
        return {'startTime': self.__startTime}

    def _onEntered(self, event):
        self.__startTime = event.params.get('startTime', time.time() * 1000)
        super(HalloweenPreBattleQueueState, self)._onEntered(event)

    def _onExited(self):
        self.__startTime = None
        super(HalloweenPreBattleQueueState, self)._onExited()
        return


@SubScopeTopLayerState.parentOf
class HalloweenAmmunitionSetupLoadout(LobbyState):
    STATE_ID = 'halloweenAmmunitionSetupLoadout'

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HalloweenAmmunitionSetupLoadout, self).__init__(flags)
        self.__transitionWithoutBuying = False

    def registerStates(self):
        self.addChildState(HangarAmmunitionSetupState(flags=StateFlags.INITIAL))
        machine = self.getMachine()
        machine.addState(HalloweenAmmunitionConfirmState())

    def registerTransitions(self):
        machine = self.getMachine()
        ammunitionSetup = machine.getStateByCls(HangarAmmunitionSetupState)
        confirmState = machine.getStateByCls(HalloweenAmmunitionConfirmState)
        browser = machine.getStateByCls(BrowserLobbyTopState)
        ammunitionSetup.addNavigationTransition(browser, record=True)
        ammunitionSetup.addNavigationTransition(confirmState)
        self.addGuardTransition(confirmState, WeakMethodProxy(self.interactorConfirm))

    def interactorConfirm(self, event):
        browserStatID = self.getMachine().getStateByCls(BrowserLobbyTopState).getStateID()
        self.__transitionWithoutBuying = event.targetStateID == browserStatID
        if self.__transitionWithoutBuying:
            return False
        else:
            targetingSelf = event.targetStateID == self.getStateID()
            view = getLoadedViewByLayoutID(R.views.halloween.mono.lobby.ammunition_setup())
            interactor = view.tankSetup.currentInteractor if view and view.tankSetup else None
            return not targetingSelf and interactor and interactor.hasChanged()

    def _onEntered(self, event):
        super(HalloweenAmmunitionSetupLoadout, self)._onEntered(event)
        self.__transitionWithoutBuying = False

    @wg_async
    def _onExited(self):
        if not self.__transitionWithoutBuying:
            view = getLoadedViewByLayoutID(R.views.halloween.mono.lobby.ammunition_setup())
            interactor = view.tankSetup.currentInteractor if view and view.tankSetup else None
            if interactor:
                yield await_callback(interactor.applyQuit)(skipApplyAutoRenewal=False)
        self.__transitionWithoutBuying = False
        super(HalloweenAmmunitionSetupLoadout, self)._onExited()
        return


@HalloweenAmmunitionSetupLoadout.parentOf
class HangarAmmunitionSetupState(GuiImplViewLobbyState):
    STATE_ID = 'halloweenAmmunitionSetup'
    VIEW_KEY = ViewKey(R.views.halloween.mono.lobby.ammunition_setup())

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HangarAmmunitionSetupState, self).__init__(HWHangarAmmunitionSetupView, ScopeTemplates.LOBBY_SUB_SCOPE, flags=flags)
        self.__cachedParams = {}

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.hangarAmmunitionSetup.header()))

    def serializeParams(self):
        return self.__cachedParams

    def _onEntered(self, event):
        super(HangarAmmunitionSetupState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        self.__cachedParams = {}
        super(HangarAmmunitionSetupState, self)._onExited()


@TopScopeTopLayerState.parentOf
class HalloweenAmmunitionConfirmState(LobbyState):
    STATE_ID = 'halloweenAmmunitionConfirmState'

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.hangarAmmunitionSetup.header()))

    @wg_async
    def _onEntered(self, event):
        redirected = event.targetStateID != self.getStateID()
        if not redirected:
            self.goBack()
            return
        view = getLoadedViewByLayoutID(R.views.halloween.mono.lobby.ammunition_setup())
        if not view:
            self.goBack()
            return
        result = yield wg_await(view.tankSetup.canQuit())
        if result:
            view._closeWindow()
            self.getMachine().post(event)
        else:
            self.goBack()


@HalloweenModeState.parentOf
class HalloweenVehiclePreviewState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HalloweenVehiclePreviewState, self).__init__(flags=flags)
        self.__cachedParams = {}

    def registerTransitions(self):
        machine = self.getMachine()
        vehiclePostProgression = machine.getStateByCls(VehiclePostProgressionState)
        self.addNavigationTransition(vehiclePostProgression, record=True)
        heroTankPreview = machine.getStateByCls(HalloweenHeroTankPreviewState)
        self.addNavigationTransition(heroTankPreview, record=True)
        self.addNavigationTransition(machine.getStateByCls(OverviewState), record=True)
        self.addNavigationTransition(machine.getStateByCls(ModulesState), record=True)
        self.addNavigationTransition(machine.getStateByCls(StatsState), record=True)
        self.addNavigationTransition(machine.getStateByCls(ArmorState), record=True)
        self.addNavigationTransition(machine.getStateByCls(VehSkillTreeState), record=True)

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.vehicle_preview.header.title()))

    def _onEntered(self, event):
        from ClientSelectableCameraObject import ClientSelectableCameraObject
        ClientSelectableCameraObject.switchCamera()
        super(HalloweenVehiclePreviewState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        self.__cachedParams = {}
        super(HalloweenVehiclePreviewState, self)._onExited()

    def _getViewLoadCtx(self, event):
        if 'ctx' in event.params:
            return super(HalloweenVehiclePreviewState, self)._getViewLoadCtx(event)
        ctx = {}
        for key, value in event.params.items():
            ctx[key] = value

        return {'ctx': ctx}


@HalloweenModeState.parentOf
class HalloweenHeroTankPreviewState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW
    VIEW_KEY = ViewKey(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HalloweenHeroTankPreviewState, self).__init__(flags=flags)
        self.__cachedParams = {}

    def registerTransitions(self):
        machine = self.getMachine()
        vehiclePostProgression = machine.getStateByCls(VehiclePostProgressionState)
        self.addNavigationTransition(vehiclePostProgression, record=True)

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.vehicle_preview.hero.header.title()))

    def _onEntered(self, event):
        super(HalloweenHeroTankPreviewState, self)._onEntered(event)
        self.__cachedParams = event.params

    def _onExited(self):
        self._prepareExited()
        self.__cachedParams = {}
        super(HalloweenHeroTankPreviewState, self)._onExited()

    def _getViewLoadCtx(self, event):
        if 'ctx' in event.params:
            return super(HalloweenHeroTankPreviewState, self)._getViewLoadCtx(event)
        ctx = {}
        for key, value in event.params.items():
            ctx[key] = value

        return {'ctx': ctx}

    def _prepareExited(self):
        app = dependency.instance(IAppLoader).getApp()
        view = app.containerManager.getViewByKey(self.VIEW_KEY)
        if view is not None:
            view.removeListener(CameraRelatedEvents.CAMERA_ENTITY_UPDATED, view.handleSelectedEntityUpdated)
        return


@SubScopeTopLayerState.parentOf
class HalloweenExchangeScreenState(GuiImplViewLobbyState):
    STATE_ID = 'halloweenExchangeScreenState'
    VIEW_KEY = ViewKey(R.views.halloween.mono.lobby.bundles_shop())

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HalloweenExchangeScreenState, self).__init__(BundleView, ScopeTemplates.LOBBY_SUB_SCOPE, flags=flags)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.halloween_lobby.bundleView.title()))

    def registerTransitions(self):
        machine = self.getMachine()
        exchangeScreenState = machine.getStateByCls(HalloweenExchangeScreenState)
        exchangeScreenState.addNavigationTransition(machine.getStateByCls(BrowserLobbyTopState))
        exchangeScreenState.addNavigationTransition(machine.getStateByCls(BarracksState))