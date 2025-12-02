import weakref, logging, sound_helpers, BigWorld, CGF
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, onProcessQuery
from constants import IS_CLIENT, NULL_ENTITY_ID
from grinch.cgf import getVehicleFromGO
from grinch_common.grinch_constants import ARENA_BONUS_TYPE_CAPS
from helpers import dependency
_logger = logging.getLogger(__name__)
if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from gui.battle_control import battle_constants
    from grinch.gui.battle_control import grinch_battle_constants
else:

    class IBattleSessionProvider(object):
        pass


    class battle_constants(object):

        class DestroyTimerViewState(object):

            def __init__(self, *args, **kwargs):
                pass

        class VEHICLE_VIEW_STATE(object):
            STEALTH_RADAR = 17592186044416
            SHOT_PASSION = 2251799813685248
            DANGER_ZONE = 590295810358705651712

        class TIMER_VIEW_STATE(object):
            CRITICAL = 'critical'
            WARNING = 'warning'


    class grinch_battle_constants(object):

        class DestroyTimerViewState(object):

            def __init__(self, *args, **kwargs):
                pass

        class VEHICLE_VIEW_STATE(object):
            SONAR = 618970019642690137449562112
            DART_STUN = 1237940039285380274899124224
            HEALING_INTERRUPTED = 2475880078570760549798248448
            BEING_CHASED_BY_MISSILE = 4951760157141521099596496896


_VEHICLE_IN_HEALBASE = 'vehicle_in_healbase'

def _setupCmp(spaceID, go, marker):
    vehicle = getVehicleFromGO(spaceID, go)
    if vehicle and marker.source in vehicle.components:
        marker.vehicleID = vehicle.id
        marker.sourceComponent = weakref.proxy(vehicle.components.get(marker.source))
    else:
        _logger.warning('The necessary settings for a provided CGF are not specified!')


@dependency.replace_none_kwargs(guiSessionProvider=IBattleSessionProvider)
def _hideStatusEffect(marker, status, guiSessionProvider=None):
    if not marker.vehicleID or marker.vehicleID != getattr(BigWorld.player(), 'playerVehicleID', 0):
        return
    guiSessionProvider.invalidateVehicleState(status, battle_constants.DestroyTimerViewState(status, 0.0, None))
    return


@dependency.replace_none_kwargs(guiSessionProvider=IBattleSessionProvider)
def _showStatusEffect(go, marker, cmpType, status, level, guiSessionProvider=None):
    playerAvatar = BigWorld.player()
    if not playerAvatar:
        return
    if not playerAvatar.isVehicleAlive:
        if go.findComponentByType(cmpType):
            go.removeComponentByType(cmpType)
        return
    endtime = marker.sourceComponent.endtime
    if marker.currentEndTime != endtime:
        marker.currentEndTime = endtime
        startTime = BigWorld.serverTime()
        timeLeft = endtime - startTime
        guiSessionProvider.invalidateVehicleState(status, battle_constants.DestroyTimerViewState(status, level=level, startTime=startTime, totalTime=timeLeft))


@registerComponent
class GrinchDartStunnedStatusEffect(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchDartStunnedStatusEffect, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        self.currentEndTime = 0.0
        return


@registerComponent
class GrinchFlareVehicleStatusEffect(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchFlareVehicleStatusEffect, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        self.currentEndTime = 0.0
        return


@registerComponent
class GrinchFreezedVehicleStatusEffect(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchFreezedVehicleStatusEffect, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        self.currentEndTime = 0.0
        return


@registerComponent
class GrinchHealingInterruptedVehicleStatusEffect(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchHealingInterruptedVehicleStatusEffect, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        self.currentEndTime = 0.0
        return


@registerComponent
class GrinchChasedByMissileVehicleStatusEffect(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchChasedByMissileVehicleStatusEffect, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        return


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudFlareVehicleStatusEffectManager(CGF.ComponentManager):
    _VIEW_STATE_ID = grinch_battle_constants.VEHICLE_VIEW_STATE.SONAR

    @onAddedQuery(CGF.GameObject, GrinchFlareVehicleStatusEffect)
    def onAddedGrinchFlareVehicleStatusEffect(self, go, marker):
        _setupCmp(self.spaceID, go, marker)

    @onRemovedQuery(GrinchFlareVehicleStatusEffect)
    def onRemovedGrinchFlareVehicleStatusEffect(self, marker):
        _hideStatusEffect(marker, status=self._VIEW_STATE_ID)

    @onProcessQuery(CGF.GameObject, GrinchFlareVehicleStatusEffect, updatePeriod=0.1)
    def onProcessGrinchFlareVehicleStatusEffect(self, go, marker):
        _showStatusEffect(go, marker, GrinchFlareVehicleStatusEffect, self._VIEW_STATE_ID, battle_constants.TIMER_VIEW_STATE.CRITICAL)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudFreezedVehicleStatusEffectManager(CGF.ComponentManager):
    _VIEW_STATE_ID = battle_constants.VEHICLE_VIEW_STATE.DANGER_ZONE

    @onAddedQuery(CGF.GameObject, GrinchFreezedVehicleStatusEffect)
    def onAddedGrinchFreezedVehicleStatusEffect(self, go, marker):
        _setupCmp(self.spaceID, go, marker)

    @onRemovedQuery(GrinchFreezedVehicleStatusEffect)
    def onRemovedGrinchFreezedVehicleStatusEffect(self, marker):
        _hideStatusEffect(marker, status=self._VIEW_STATE_ID)

    @onProcessQuery(CGF.GameObject, GrinchFreezedVehicleStatusEffect, updatePeriod=0.1)
    def onProcessGrinchFreezedVehicleStatusEffect(self, go, marker):
        _showStatusEffect(go, marker, GrinchFreezedVehicleStatusEffect, self._VIEW_STATE_ID, battle_constants.TIMER_VIEW_STATE.CRITICAL)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudDartStunnedVehicleStatusEffectManager(CGF.ComponentManager):
    _VIEW_STATE_ID = grinch_battle_constants.VEHICLE_VIEW_STATE.DART_STUN

    @onAddedQuery(CGF.GameObject, GrinchDartStunnedStatusEffect)
    def onAddedGrinchDartStunnedStatusEffect(self, go, marker):
        _setupCmp(self.spaceID, go, marker)

    @onRemovedQuery(GrinchDartStunnedStatusEffect)
    def onRemovedGrinchDartStunnedStatusEffect(self, marker):
        _hideStatusEffect(marker, status=self._VIEW_STATE_ID)

    @onProcessQuery(CGF.GameObject, GrinchDartStunnedStatusEffect, updatePeriod=0.1)
    def onProcessGrinchDartStunnedStatusEffect(self, go, marker):
        _showStatusEffect(go, marker, GrinchDartStunnedStatusEffect, self._VIEW_STATE_ID, battle_constants.TIMER_VIEW_STATE.CRITICAL)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudGrinchHealingInterruptedStatusEffectManager(CGF.ComponentManager):
    _VIEW_STATE_ID = grinch_battle_constants.VEHICLE_VIEW_STATE.HEALING_INTERRUPTED
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @onAddedQuery(CGF.GameObject, GrinchHealingInterruptedVehicleStatusEffect)
    def onAddedGrinchHealingInterruptedVehicleStatusEffect(self, go, marker):
        _setupCmp(self.spaceID, go, marker)

    @onRemovedQuery(GrinchHealingInterruptedVehicleStatusEffect)
    def onRemovedGrinchHealingInterruptedVehicleStatusEffect(self, marker):
        _hideStatusEffect(marker, status=self._VIEW_STATE_ID)

    @onProcessQuery(CGF.GameObject, GrinchHealingInterruptedVehicleStatusEffect, updatePeriod=0.1)
    def onProcessGrinchHealingInterruptedVehicleStatusEffect(self, go, marker):
        self._processHealingInterruption(go, marker)

    def _processHealingInterruption(self, go, marker):
        vehicle = getVehicleFromGO(self.spaceID, go)
        if vehicle:
            if _VEHICLE_IN_HEALBASE in vehicle.dynamicComponents:
                playerAvatar = BigWorld.player()
                if not playerAvatar:
                    return
                if not playerAvatar.isVehicleAlive:
                    if go.findComponentByType(GrinchHealingInterruptedVehicleStatusEffect):
                        go.removeComponentByType(GrinchHealingInterruptedVehicleStatusEffect)
                    return
                endtime = marker.sourceComponent.endtime
                if marker.currentEndTime != endtime:
                    marker.currentEndTime = endtime
                    startTime = marker.sourceComponent.startTime
                    timeLeft = endtime - startTime
                    self._guiSessionProvider.invalidateVehicleState(self._VIEW_STATE_ID, battle_constants.DestroyTimerViewState(self._VIEW_STATE_ID, level=battle_constants.TIMER_VIEW_STATE.CRITICAL, startTime=startTime, totalTime=timeLeft))
            elif marker.currentEndTime:
                _hideStatusEffect(marker, status=self._VIEW_STATE_ID)
                marker.currentEndTime = 0.0


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudChasedByMissileVehicleStatusEffectManager(CGF.ComponentManager):
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    _VIEW_STATE_ID = grinch_battle_constants.VEHICLE_VIEW_STATE.BEING_CHASED_BY_MISSILE
    _GRINCH_INCOMING_GUIDED_MISSILE_SOUND = 'ev_grinch_ui_ability_guided_missile_incoming'

    @onAddedQuery(CGF.GameObject, GrinchChasedByMissileVehicleStatusEffect)
    def onAddedChasedByMissileStatusEffect(self, go, marker):
        _setupCmp(self.spaceID, go, marker)
        self._guiSessionProvider.invalidateVehicleState(self._VIEW_STATE_ID, battle_constants.DestroyTimerViewState(self._VIEW_STATE_ID, 0.0, battle_constants.TIMER_VIEW_STATE.WARNING, startTime=0.0))
        sound_helpers.play2d(self._GRINCH_INCOMING_GUIDED_MISSILE_SOUND)

    @onRemovedQuery(GrinchChasedByMissileVehicleStatusEffect)
    def onRemovedChasedByMissileStatusEffect(self, marker):
        _hideStatusEffect(marker, status=self._VIEW_STATE_ID)