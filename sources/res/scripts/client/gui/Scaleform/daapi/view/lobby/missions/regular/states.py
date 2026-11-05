from __future__ import absolute_import
from frameworks_common.state_machine.transitions import TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import SubScopeSubLayerState, ViewLobbyState, LobbyStateDescription
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController

def registerStates(machine):
    machine.addState(MissionsState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(MissionsState))


@SubScopeSubLayerState.parentOf
class MissionsState(ViewLobbyState):
    STATE_ID = 'missions'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_MISSIONS)
    __appLoader = dependency.descriptor(IAppLoader)
    __battleMattersController = dependency.descriptor(IBattleMattersController)

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub import OverviewState
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import OfferGiftVehiclePreviewState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(ShopState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(OfferGiftVehiclePreviewState), record=True)
        self.addNavigationTransition(self, transitionType=TransitionType.EXTERNAL)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.userMissions()))

    def getBackNavigationDescription(self, params):
        if params.get('ctx', {}).get('openVehicleSelection'):
            return backport.text(R.strings.vehicle_preview.header.backBtn.descrLabel.battleMatters())
        return super(MissionsState, self).getBackNavigationDescription(params)

    def serializeParams(self):
        ctx = {}
        app = self.__appLoader.getApp()
        view = app.containerManager.getViewByKey(self.getViewKey())
        if view:
            ctx['tab'] = view.getCurrentTabAlias()
            currentTab = view.currentTab
            if ctx['tab'] == QUESTS_ALIASES.BATTLE_MATTERS_VIEW_PY_ALIAS and currentTab is not None and currentTab.isVehicleSelectionShown():
                ctx['openVehicleSelection'] = True
        return {'ctx': ctx}

    def _onEntered(self, event):
        if not self.__battleMattersController.isEnabled():
            showHangar()
        else:
            super(MissionsState, self)._onEntered(event)