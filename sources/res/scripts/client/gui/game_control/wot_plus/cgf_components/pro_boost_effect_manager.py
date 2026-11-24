from __future__ import absolute_import
import logging
from functools import partial
from helpers.CallbackDelayer import CallbackDelayer
from typing import TYPE_CHECKING, Optional, Callable, Dict, List, Set, Tuple
import BigWorld, CGF, Math
from CurrentVehicle import g_currentPreviewVehicle, g_currentVehicle
from frameworks.wulf import WindowStatus
from gui.game_control.wot_plus.cgf_components.pro_boost_effects_config_component import ProBoostEffectsConfigComponent
from gui.game_control.wot_plus.utils import ProBoostUtils
from gui.lobby_state_machine.states import isInHangarState
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from helpers import dependency
from renewable_subscription_common.settings_constants import PRO_BOOST_PDATA_KEY, PRO_BOOSTED_VEHICLE
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.impl import IGuiLoader
from cgf_script.registration import registerModule
if TYPE_CHECKING:
    from gui.game_control.wot_plus_controller import WotPlusController
    from gui.impl.gui_loader import GuiLoader
_ACTIVATION_TIMEOUT = 0.5
_ACTIVATION_WAIT_LIMIT = 15.0
_EFFECT_CREATION_TIMEOUT = 5.0
_DEFAULT_ACTIVATION_PREFAB = 'content/CGFPrefabs/Lobby/proboost_activation.prefab'
_DEFAULT_DEACTIVATION_PREFAB = 'content/CGFPrefabs/Lobby/proboost_deactivation.prefab'

class _EffectRole(object):
    ACTIVATION = 'activation'
    DEACTIVATION = 'deactivation'


_logger = logging.getLogger(__name__)

class WotPlusProBoostSystem(CGF.System):
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)
    _uiLoader = dependency.descriptor(IGuiLoader)
    ConfigActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRo(ProBoostEffectsConfigComponent))
    ConfigDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRo(ProBoostEffectsConfigComponent))
    Reactions = CGF.Reactions(ConfigDeactivated, ConfigActivated)

    def __init__(self):
        super(WotPlusProBoostSystem, self).__init__()
        self._boostedVehicleInvID = self._wotPlusCtrl.getProBoostedVehicleInvID()
        self._delayer = CallbackDelayer()
        self._effectGOs = {}
        self._loadingInProgress = set()
        self._creationDeadline = 0.0
        self._activationDeadline = 0.0
        self._activeConfig = None
        self._shownRole = None
        self._windowsManager = self._uiLoader.windowsManager
        return

    def onMappingLoaded(self):
        self._wotPlusCtrl.onDataChanged += self._onControllerDataChanged
        g_currentVehicle.onChanged += self._activateEffect
        g_currentVehicle.onChangeStarted += self._deactivateEffect
        g_eventBus.addListener(events.PrebattleEvent.SWITCHED, self._onPrbSwitch, scope=EVENT_BUS_SCOPE.LOBBY)
        self._windowsManager.onWindowStatusChanged += self._onWindowStatusChanged
        if not g_currentPreviewVehicle.vehicleEntityID and self._wotPlusCtrl.hasSubscription():
            self._activationDeadline = BigWorld.time() + _ACTIVATION_WAIT_LIMIT
            self._delayer.delayCallback(_ACTIVATION_TIMEOUT, self._activateEffectOnVehicleReady)

    def onMappingUnloaded(self):
        self._wotPlusCtrl.onDataChanged -= self._onControllerDataChanged
        g_currentVehicle.onChanged -= self._activateEffect
        g_currentVehicle.onChangeStarted -= self._deactivateEffect
        g_eventBus.removeListener(events.PrebattleEvent.SWITCHED, self._onPrbSwitch, scope=EVENT_BUS_SCOPE.LOBBY)
        self._windowsManager.onWindowStatusChanged -= self._onWindowStatusChanged
        self._removeEffects()
        self._effectGOs = {}
        self._loadingInProgress = set()
        self._activeConfig = None
        self._shownRole = None
        self._windowsManager = None
        self._delayer.destroy()
        return

    def update(self):
        prevPaths = self._effectPaths()
        for go, _ in self.reaction(self.ConfigDeactivated):
            if self._activeConfig is not None and self._activeConfig[0] == go:
                self._activeConfig = None

        for go, config in self.reaction(self.ConfigActivated):
            if self._activeConfig is not None and self._activeConfig[0] != go:
                _logger.error('Several ProBoostEffectsConfigComponent are active in space %s: %s is replaced by %s', self.spaceID, self._activeConfig[0].name, go.name)
            self._activeConfig = (go, config.activationPrefab, config.deactivationPrefab)

        if self._effectPaths() != prevPaths:
            self._onConfigChanged()
        return

    @property
    def isCurrentVehicleAvailableAndBoosted(self):
        return g_currentPreviewVehicle.vehicleEntityID and self._boostedVehicleInvID and g_currentVehicle.isInHangar() and g_currentVehicle.invID == self._boostedVehicleInvID

    def _prefabPath(self, role):
        if self._activeConfig is not None:
            _, activationPrefab, deactivationPrefab = self._activeConfig
            path = activationPrefab if role == _EffectRole.ACTIVATION else deactivationPrefab
            if path:
                return path
        if role == _EffectRole.ACTIVATION:
            return _DEFAULT_ACTIVATION_PREFAB
        else:
            return _DEFAULT_DEACTIVATION_PREFAB

    def _effectPaths(self):
        return (
         self._prefabPath(_EffectRole.ACTIVATION), self._prefabPath(_EffectRole.DEACTIVATION))

    def _onConfigChanged(self):
        wasActivationShown = self._shownRole == _EffectRole.ACTIVATION
        self._removeEffects()
        self._shownRole = None
        if wasActivationShown:
            self._activateEffect()
        return

    def _removeEffects(self):
        queue = CGF.CommandQueue(self.spaceID)
        for path, go in list(self._effectGOs.items()):
            if go.valid:
                queue.removeGameObject(go)
                self._loadingInProgress.discard(path)
                self._effectGOs.pop(path, None)
            elif path not in self._loadingInProgress:
                self._effectGOs.pop(path, None)

        return

    def _loadEffect(self, path):
        if path in self._loadingInProgress:
            _logger.debug('Proboost effect %s is already loading', path)
            return
        self._loadingInProgress.add(path)
        self._loadPrefabWithCallback(path, partial(self._onPrefabLoaded, path))

    def _loadPrefabWithCallback(self, prefab, callback):
        CGF.loadAndCreatePrefabWithParent(prefab, BigWorld.entity(g_currentPreviewVehicle.vehicleEntityID).entityGameObject, Math.Vector3(), callback)

    def _onControllerDataChanged(self, diff):
        proBoostDiff = diff.get(PRO_BOOST_PDATA_KEY, None)
        if proBoostDiff and PRO_BOOSTED_VEHICLE in proBoostDiff:
            newBoostedVehicle = proBoostDiff[PRO_BOOSTED_VEHICLE]
            if self._boostedVehicleInvID and not newBoostedVehicle:
                self._deactivateEffect()
                self._boostedVehicleInvID = None
                return
            self._boostedVehicleInvID = newBoostedVehicle
            self._activateEffect()
        return

    def _activateEffect(self):
        if not isInHangarState() or not ProBoostUtils.isGameModeCompatibleForProBoost():
            return
        self.__toggleEffects(_EffectRole.ACTIVATION)

    def _deactivateEffect(self):
        self.__toggleEffects(_EffectRole.DEACTIVATION)

    def __toggleEffects(self, roleToShow):
        if not self.isCurrentVehicleAvailableAndBoosted:
            return
        self._shownRole = roleToShow
        pathToShow = self._prefabPath(roleToShow)
        self._effectGOs = {path:go for path, go in self._effectGOs.items() if go.valid or path in self._loadingInProgress}
        for path, go in self._effectGOs.items():
            if not go.valid:
                continue
            if path == pathToShow:
                go.activate()
            else:
                go.deactivate()

        if pathToShow not in self._effectGOs:
            self._loadEffect(pathToShow)

    def _onPrefabLoaded(self, path, objects, queue):
        if not objects:
            _logger.error('Proboost effect prefab %s has no objects', path)
            self._loadingInProgress.discard(path)
            return
        if path not in self._loadingInProgress or path not in self._effectPaths() or path in self._effectGOs:
            self._loadingInProgress.discard(path)
            queue.removeGameObject(objects[0])
            return
        self._effectGOs[path] = queue.gameObject(objects[0])
        self._creationDeadline = BigWorld.time() + _EFFECT_CREATION_TIMEOUT
        self._delayer.delayCallback(0.0, self._syncCreatedEffects)

    def _syncCreatedEffects(self):
        shownPath = self._prefabPath(self._shownRole) if self._shownRole else None
        queue = CGF.CommandQueue(self.spaceID)
        for path, go in list(self._effectGOs.items()):
            if path not in self._loadingInProgress or not go.valid:
                continue
            self._loadingInProgress.discard(path)
            if path not in self._effectPaths():
                queue.removeGameObject(go)
                self._effectGOs.pop(path, None)
            elif path != shownPath:
                go.deactivate()

        notCreatedPaths = self._loadingInProgress.intersection(self._effectGOs)
        if not notCreatedPaths:
            return
        else:
            if BigWorld.time() < self._creationDeadline:
                return 0.0
            _logger.warning('Proboost effects were not created: %s', notCreatedPaths)
            self._loadingInProgress -= notCreatedPaths
            for path in notCreatedPaths:
                self._effectGOs.pop(path, None)

            return

    def _activateEffectOnVehicleReady(self):
        if not g_currentPreviewVehicle.vehicleEntityID and BigWorld.time() < self._activationDeadline:
            return _ACTIVATION_TIMEOUT
        else:
            self._activateEffect()
            return

    def _onWindowStatusChanged(self, _, status):
        if not self.isCurrentVehicleAvailableAndBoosted:
            return
        if status == WindowStatus.DESTROYED and isInHangarState():
            self._activateEffect()
        elif status == WindowStatus.LOADED and not isInHangarState():
            self._deactivateEffect()

    def _onPrbSwitch(self, _):
        if not self.isCurrentVehicleAvailableAndBoosted:
            return
        if not ProBoostUtils.isGameModeCompatibleForProBoost():
            self._deactivateEffect()
        else:
            self._activateEffect()


@registerModule
class WotPlusProBoostModule(object):
    name = 'WoT plus boost'
    group = 'Hangar'
    systems = [
     CGF.RegisterSystem(WotPlusProBoostSystem, domain=CGF.Domain.Client)]
    components = [
     ProBoostEffectsConfigComponent]