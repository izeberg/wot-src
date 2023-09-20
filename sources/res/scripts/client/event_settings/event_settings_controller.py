from copy import deepcopy
import BigWorld
from event_settings.event_disabled_settings import EventDisabledSettings
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
from helpers import dependency, aop
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IEventSettingsController
from aop import PointcutDisableSettingsControls

class EventSettingsController(IEventSettingsController):
    __settingsCore = dependency.descriptor(ISettingsCore)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _DAMAGE_INDICATOR_SETTINGS_FOR_BOSS = {'damageIndicatorType': 0, 
       'damageIndicatorCrits': 1, 
       'damageIndicatorAllies': 1, 
       'damageIndicatorDamageValue': 0, 
       'damageIndicatorDynamicIndicator': 0, 
       'damageIndicatorVehicleInfo': 0, 
       'damageIndicatorAnimation': 0}
    _DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS = {'damageIndicatorType': 1, 
       'damageIndicatorCrits': 1, 
       'damageIndicatorAllies': 1, 
       'damageIndicatorDamageValue': 1, 
       'damageIndicatorDynamicIndicator': 1, 
       'damageIndicatorVehicleInfo': 1, 
       'damageIndicatorAnimation': 1}
    _BATTLE_EVENTS_SETTINGS = {'battleEventsEnemyBurning': 1, 
       'battleEventsEnemyWorldCollision': 1, 'battleEventsBaseCapture': 0, 'battleEventsEnemyCriticalHit': 1, 
       'battleEventsBaseCaptureDrop': 0, 'battleEventsReceivedDamage': 1, 'battleEventsEnemyAssistStun': 0, 
       'battleEventsEnemyRamAttack': 1, 'battleEventsShowInBattle': 1, 'battleEventsEnemyKill': 1, 
       'battleEventsVehicleInfo': 1, 'battleEventsEnemyHpDamage': 1, 'battleEventsEnemyDetection': 1, 
       'battleEventsEnemyDetectionDamage': 1, 'battleEventsEnemyTrackDamage': 1, 'battleEventsBlockedDamage': 1, 
       'battleEventsReceivedCrits': 1, 'battleEventsEventName': 1, 'battleEventsEnemyStun': 0, 
       'battleEventsHealthAdded': 1}
    _DAMAGE_LOG_SETTINGS = {'damageLogShowDetails': 2, 
       'damageLogShowEventTypes': 0, 'damageLogAssistStun': 0, 'damageLogEventsPosition': 0, 
       'damageLogAssistDamage': 1, 'damageLogBlockedDamage': 1, 'damageLogTotalDamage': 1}
    _QUESTS_PROGRESS = {'progressViewType': 1, 'progressViewConditions': 1, 'showHPBar': 0, 
       'showHPValues': 0, 'enableTierGrouping': 0, 'showHPDifference': 0}
    _COMMON_MARKER_VALUES = {'markerBaseIcon': 0, 
       'markerAltIcon': 1, 
       'markerBaseLevel': 0, 
       'markerAltLevel': 0, 
       'markerBaseVehicleName': 1, 
       'markerAltVehicleName': 1, 
       'markerBasePlayerName': 1, 
       'markerAltPlayerName': 1, 
       'markerBaseDamage': 1, 
       'markerAltDamage': 1}
    _MARKERS = {'enemy': deepcopy(_COMMON_MARKER_VALUES), 
       'ally': deepcopy(_COMMON_MARKER_VALUES), 
       'dead': deepcopy(_COMMON_MARKER_VALUES)}
    _MARKERS['enemy'].update({'markerBaseHpIndicator': 1, 
       'markerAltHpIndicator': 1, 
       'markerBaseAimMarker2D': 1, 
       'markerAltAimMarker2D': 1, 
       'markerBaseHp': 1, 
       'markerAltHp': 1})
    _MARKERS['ally'].update({'markerBaseHpIndicator': 1, 
       'markerAltHpIndicator': 1, 
       'markerBaseHp': 1, 
       'markerAltHp': 1})
    _MARKERS['dead'].update({'markerBaseHpIndicator': 0, 
       'markerAltHpIndicator': 1, 
       'markerBaseHp': 0, 
       'markerAltHp': 1})
    _ALL_EVENT_SETTINGS = {}
    _ALL_EVENT_SETTINGS.update(_DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS)
    _ALL_EVENT_SETTINGS.update(_BATTLE_EVENTS_SETTINGS)
    _ALL_EVENT_SETTINGS.update(_DAMAGE_LOG_SETTINGS)
    _ALL_EVENT_SETTINGS.update(_QUESTS_PROGRESS)
    _ALL_EVENT_SETTINGS.update(_MARKERS)
    _DISABLED_STORAGES = ('damageIndicator', 'damageLog', 'battleEvents', 'questsProgress',
                          'battleHud', 'markers')

    def __init__(self):
        self.__userSettings = None
        self.__disabledSettings = None
        self.__weaver = None
        self.__eventSettingEnabled = False
        self.__settingsChanged = False
        return

    def init(self):
        self.__disabledSettings = EventDisabledSettings()
        self.__weaver = aop.Weaver()

    def fini(self):
        self.__weaver.clear()
        self.__weaver = None
        self.__disabledSettings = None
        self.__userSettings = None
        self.__eventSettingEnabled = False
        self.__settingsChanged = False
        self.__settingsCore.onSettingsReady -= self.__swapAfter
        return

    @property
    def disabledSettings(self):
        return self.__disabledSettings.disabledSetting

    def onAvatarBecomePlayer(self):
        self.__swapSettings()
        vehicle = BigWorld.player().vehicle
        if vehicle:
            self.__applyIndicatorSettings(vehicle.typeDescriptor.type)

    def onAvatarBecomeNonPlayer(self):
        if self.__weaver is not None:
            self.__weaver.clear()
        if self.__userSettings is not None:
            self.__settingsCore.unsetOverrideSettings()
            self.__settingsCore.clearStorages()
            self.__userSettings = None
        self.__eventSettingEnabled = False
        return

    @property
    def __isInEvent(self):
        return self.__sessionProvider.arenaVisitor.gui.isEventBattle()

    def __applyIndicatorSettings(self, vehicleType):
        if not vehicleType or not self.__isInEvent:
            return
        isBoss = VEHICLE_TAGS.EVENT_BOSS in vehicleType.tags
        settings = self._DAMAGE_INDICATOR_SETTINGS_FOR_BOSS if isBoss else self._DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS
        self.__settingsCore.applySettings(settings)

    def __swapSettings(self):
        if not self.__settingsCore.isReady:
            self.__settingsCore.onSettingsReady += self.__swapAfter
            return
        if self.__isInEvent == self.__eventSettingEnabled:
            return
        if self.__isInEvent:
            self.__disable()
        else:
            self.__enable()

    def __swapAfter(self):
        self.__settingsCore.onSettingsReady -= self.__swapAfter
        self.__swapSettings()

    def __disable(self):
        self.__userSettings = {setting:self.__settingsCore.getSetting(setting) for setting in self._ALL_EVENT_SETTINGS}
        self.__settingsCore.setOverrideSettings(self._ALL_EVENT_SETTINGS, self._DISABLED_STORAGES)
        if self.__weaver.findPointcut(PointcutDisableSettingsControls) == -1:
            self.__weaver.weave(pointcut=PointcutDisableSettingsControls)
        self.__eventSettingEnabled = True

    def __enable(self):
        if self.__weaver is not None:
            self.__weaver.clear()
        if self.__userSettings is not None:
            self.__settingsCore.unsetOverrideSettings()
            self.__settingsCore.clearStorages()
            self.__userSettings = None
        self.__eventSettingEnabled = False
        return