import logging, typing, nations
from shared_utils import CONST_CONTAINER, findFirst
from constants import SHELL_TYPES, SHELL_MECHANICS_TYPE
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.items_parameters.params_cache import g_paramsCache
from gui.shared.utils.functions import replaceHyphenToUnderscore
from gui.shared.gui_items.fitting_item import FittingItem, ICONS_MASK
from gui.shared.gui_items.vehicle_mechanic_item import extendMechanics, VEHICLE_MECHANICS_GUI_MAP, GUN_MECHANICS_OVERRIDES, CHASSIS_MECHANICS_OVERRIDES, ENGINE_MECHANICS_OVERRIDES
from gui.shared.utils import GUN_CLIP, GUN_CAN_BE_CLIP, GUN_AUTO_RELOAD, GUN_CAN_BE_AUTO_RELOAD, GUN_DUAL_GUN, GUN_CAN_BE_DUAL_GUN, GUN_AUTO_SHOOT, GUN_CAN_BE_AUTO_SHOOT, GUN_CAN_BE_TWIN_GUN, GUN_TWIN_GUN
from gui.shared.money import Currency
from items import vehicles as veh_core
from vehicles.mechanics.mechanic_constants import VehicleMechanic
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescr
MODULE_TYPES_ORDER = ('vehicleGun', 'vehicleTurret', 'vehicleEngine', 'vehicleChassis',
                      'vehicleRadio', 'vehicleFuelTank')
MODULE_TYPES_ORDER_INDICES = dict((n, i) for i, n in enumerate(MODULE_TYPES_ORDER))
SHELL_TYPES_ORDER = (
 SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_CR,
 SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.HIGH_EXPLOSIVE, SHELL_TYPES.SMOKE)
SHELL_TYPES_ORDER_INDICES = dict((n, i) for i, n in enumerate(SHELL_TYPES_ORDER))

class ModulesIconNames(CONST_CONTAINER):
    WHEELED_CHASSIS = 'wheeledChassis'
    CHASSIS = 'chassis'
    TURRET = 'tower'
    GUN = 'gun'
    ENGINE = 'engine'
    RADIO = 'radio'


_logger = logging.getLogger(__name__)

class VehicleModule(FittingItem):
    __slots__ = ('_vehicleModuleDescriptor', )
    _GUI_SUPPORTED_MECHANICS = set()

    def __init__(self, intCompactDescr, proxy=None, descriptor=None):
        super(VehicleModule, self).__init__(intCompactDescr, proxy)
        self._vehicleModuleDescriptor = descriptor

    @property
    def icon(self):
        if not self.iconName:
            return ''
        return backport.image(R.images.gui.maps.icons.modules.dyn(self.iconName)())

    @property
    def iconName(self):
        return ''

    @property
    def descriptor(self):
        if self._vehicleModuleDescriptor is not None:
            return self._vehicleModuleDescriptor
        else:
            return super(VehicleModule, self).descriptor

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        bigIconName = self.iconName + 'Big'
        return backport.image(R.images.gui.maps.icons.modules.dyn(bigIconName)())

    def getGUIEmblemID(self):
        return self.itemTypeName

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        resID = R.images.gui.maps.shop.modules.num(size).dyn(replaceHyphenToUnderscore(self.itemTypeName))()
        if resID != -1:
            return backport.image(resID)
        return ''

    def getVehicleMechanics(self, vehDescr):
        return set()

    def getVehicleMechanicsGuiNames(self, vehDescr):
        return {VEHICLE_MECHANICS_GUI_MAP[mechanic] for mechanic in self.getVehicleMechanics(vehDescr) if mechanic in self._GUI_SUPPORTED_MECHANICS}

    def _sortByType(self, other):
        return MODULE_TYPES_ORDER_INDICES[self.itemTypeName] - MODULE_TYPES_ORDER_INDICES[other.itemTypeName]


class VehicleChassis(VehicleModule):
    __slots__ = ()
    _GUI_SUPPORTED_MECHANICS = {
     VehicleMechanic.HYDRAULIC_WHEELED_CHASSIS,
     VehicleMechanic.HYDRAULIC_CHASSIS,
     VehicleMechanic.TRACK_WITHIN_TRACK}

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.chassis.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.chassis.intCD:
                result.add(vehicle)

        return result

    def isHydraulicChassis(self):
        return g_paramsCache.isChassisHydraulic(self.intCD)

    def isWheeledChassis(self):
        return g_paramsCache.isChassisWheeled(self.intCD)

    def isHydraulicWheeledChassis(self):
        return g_paramsCache.isChassisHydraulic(self.intCD) and g_paramsCache.isChassisWheeled(self.intCD)

    def isWheeledOnSpotRotationChassis(self):
        return g_paramsCache.isChassisWheeledOnSpotRotation(self.intCD)

    def hasAutoSiege(self):
        return g_paramsCache.isChassisAutoSiege(self.intCD)

    def isTrackWithinTrack(self):
        return g_paramsCache.isTrackWithinTrack(self.intCD)

    @property
    def iconName(self):
        if self.isWheeledChassis():
            return ModulesIconNames.WHEELED_CHASSIS
        return ModulesIconNames.CHASSIS

    def getExtraIconInfo(self, vehDescr=None):
        if self.isHydraulicChassis():
            if self.isWheeledChassis():
                return backport.image(R.images.gui.maps.icons.modules.hydraulicWheeledChassisIcon())
            return backport.image(R.images.gui.maps.icons.modules.hydraulicChassisIcon())
        else:
            if self.isTrackWithinTrack():
                return backport.image(R.images.gui.maps.icons.modules.trackWithinTrack())
            return

    def getGUIEmblemID(self):
        if self.isWheeledChassis():
            return FITTING_TYPES.VEHICLE_WHEELED_CHASSIS
        return super(VehicleChassis, self).getGUIEmblemID()

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        if self.isWheeledChassis():
            resID = R.images.gui.maps.shop.modules.num(size).dyn(FITTING_TYPES.VEHICLE_WHEELED_CHASSIS)()
            if resID != -1:
                return backport.image(resID)
            return ''
        return super(VehicleChassis, self).getShopIcon(size)

    def getVehicleMechanics(self, vehDescr):
        mechanics = super(VehicleChassis, self).getVehicleMechanics(vehDescr)
        mechanicChecks = [
         (
          self.isHydraulicWheeledChassis(), VehicleMechanic.HYDRAULIC_WHEELED_CHASSIS),
         (
          self.isHydraulicChassis(), VehicleMechanic.HYDRAULIC_CHASSIS),
         (
          self.isTrackWithinTrack(), VehicleMechanic.TRACK_WITHIN_TRACK)]
        extendMechanics(mechanics, {}, mechanicChecks, CHASSIS_MECHANICS_OVERRIDES)
        return mechanics

    def _getShortInfoKey(self):
        return ('#menu:descriptions/{}').format(FITTING_TYPES.VEHICLE_WHEELED_CHASSIS if self.isWheeledChassis() else self.itemTypeName)


class VehicleTurret(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.turret.intCD

    def mayInstall(self, vehicle, slotIdx=None, gunCD=0):
        if vehicle is None:
            return (False, 'not for current vehicle')
        else:
            optDevicesLayouts = None
            if vehicle.optDevices.setupLayouts.capacity > 1:
                optDevicesLayouts = []
                for setup in vehicle.optDevices.setupLayouts.setups.itervalues():
                    optDevicesLayouts.append(setup.getIntCDs())

            installPossible, reason = vehicle.descriptor.mayInstallTurret(self.intCD, gunCD, optDevicesLayouts=optDevicesLayouts)
            if not installPossible and reason == 'not for this vehicle type':
                return (False, 'need gun')
            return (
             installPossible, reason)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.turret.intCD:
                result.add(vehicle)

        return result

    @property
    def iconName(self):
        return ModulesIconNames.TURRET

    @property
    def isGunCarriage(self):
        return self.descriptor.isGunCarriage


class VehicleGun(VehicleModule):
    __slots__ = ('_defaultAmmo', '_maxAmmo')
    _GUI_SUPPORTED_MECHANICS = {
     VehicleMechanic.AUTO_SHOOT_GUN,
     VehicleMechanic.DUAL_GUN,
     VehicleMechanic.DUAL_ACCURACY,
     VehicleMechanic.TWIN_GUN,
     VehicleMechanic.MAGAZINE_GUN,
     VehicleMechanic.AUTO_LOADER_GUN_BOOST,
     VehicleMechanic.AUTO_LOADER_GUN,
     VehicleMechanic.DAMAGE_MUTABLE,
     VehicleMechanic.STUN}

    def __init__(self, intCompactDescr, proxy=None, descriptor=None):
        super(VehicleGun, self).__init__(intCompactDescr, proxy, descriptor)
        self._defaultAmmo = self._getDefaultAmmo(proxy)
        self._maxAmmo = self._getMaxAmmo()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.gun.intCD

    def mayInstall(self, vehicle, slotIdx=None):
        installPossible, reason = FittingItem.mayInstall(self, vehicle)
        if not installPossible and reason == 'not for current vehicle':
            return (False, 'need turret')
        return (installPossible, reason)

    def getReloadingType(self, vehicleDescr=None):
        return g_paramsCache.getGunReloadingSystemType(self.intCD, vehicleDescr.type.compactDescr if vehicleDescr is not None else None)

    def isClipGun(self, vehicleDescr=None):
        typeToCheck = GUN_CLIP if vehicleDescr is not None else GUN_CAN_BE_CLIP
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isAutoReloadable(self, vehicleDescr=None):
        typeToCheck = GUN_AUTO_RELOAD if vehicleDescr is not None else GUN_CAN_BE_AUTO_RELOAD
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isAutoReloadableWithBoost(self, vehicleDescr=None):
        autoLoaderGunBoost = False
        if vehicleDescr:
            for gun in vehicleDescr.type.getGuns():
                if gun.compactDescr == self.intCD and gun.autoreloadHasBoost:
                    autoLoaderGunBoost = True

        return self.isAutoReloadable(vehicleDescr) and autoLoaderGunBoost

    def isAutoShoot(self, vehicleDescr=None):
        typeToCheck = GUN_AUTO_SHOOT if vehicleDescr is not None else GUN_CAN_BE_AUTO_SHOOT
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isDualGun(self, vehicleDescr=None):
        typeToCheck = GUN_DUAL_GUN if vehicleDescr is not None else GUN_CAN_BE_DUAL_GUN
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isTwinGun(self, vehicleDescr=None):
        typeToCheck = GUN_TWIN_GUN if vehicleDescr is not None else GUN_CAN_BE_TWIN_GUN
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isDamageMutable(self):
        return self.descriptor.isDamageMutable

    def isNonPiercingDamage(self):
        return any(shell.isNonPiercingDamageMechanics for shell in self.defaultAmmo)

    def hasDualAccuracy(self, vehicleDescr=None):
        return vehicleDescr is not None and g_paramsCache.hasDualAccuracy(self.intCD, vehicleDescr.type.compactDescr)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.gun.intCD:
                result.add(vehicle)

        return result

    @property
    def defaultAmmo(self):
        return self._defaultAmmo

    @property
    def maxAmmo(self):
        return self._maxAmmo

    @property
    def iconName(self):
        return ModulesIconNames.GUN

    @property
    def userType(self):
        userType = super(VehicleGun, self).userType
        if self.isDualGun():
            return backport.text(R.strings.item_types.dualGun.name())
        if self.isTwinGun():
            return backport.text(R.strings.item_types.twinGun.name())
        return userType

    def getExtraIconInfo(self, vehDescr=None):
        if self.isClipGun(vehDescr):
            return backport.image(R.images.gui.maps.icons.modules.magazineGunIcon())
        else:
            if self.isAutoReloadable(vehDescr):
                descriptor = self.__getDescriptor(vehDescr)
                if descriptor.autoreloadHasBoost:
                    return backport.image(R.images.gui.maps.icons.modules.autoLoaderGunBoost())
                return backport.image(R.images.gui.maps.icons.modules.autoLoaderGun())
            if self.isAutoShoot(vehDescr):
                return backport.image(R.images.gui.maps.icons.modules.autoShootGun())
            if self.isDualGun(vehDescr):
                return backport.image(R.images.gui.maps.icons.modules.dualGun())
            if self.hasDualAccuracy(vehDescr):
                return backport.image(R.images.gui.maps.icons.modules.dualAccuracy())
            if self.isDamageMutable():
                return backport.image(R.images.gui.maps.icons.modules.damageMutable())
            if self.isTwinGun(vehDescr):
                return backport.image(R.images.gui.maps.icons.modules.twinGun())
            return

    def getGUIEmblemID(self):
        if self.isDualGun():
            return FITTING_TYPES.VEHICLE_DUAL_GUN
        return super(VehicleGun, self).getGUIEmblemID()

    def getVehicleMechanics(self, vehDescr):
        mechanics = super(VehicleGun, self).getVehicleMechanics(vehDescr)
        mechanicChecks = [
         (
          self.isAutoShoot(vehDescr), VehicleMechanic.AUTO_SHOOT_GUN),
         (
          self.isDualGun(vehDescr), VehicleMechanic.DUAL_GUN),
         (
          self.hasDualAccuracy(vehDescr), VehicleMechanic.DUAL_ACCURACY),
         (
          self.isTwinGun(vehDescr), VehicleMechanic.TWIN_GUN),
         (
          self.isClipGun(vehDescr), VehicleMechanic.MAGAZINE_GUN),
         (
          self.isAutoReloadableWithBoost(vehDescr), VehicleMechanic.AUTO_LOADER_GUN_BOOST),
         (
          self.isAutoReloadable(vehDescr) and not self.isAutoReloadableWithBoost(vehDescr),
          VehicleMechanic.AUTO_LOADER_GUN),
         (
          self.isDamageMutable(), VehicleMechanic.DAMAGE_MUTABLE),
         (
          any(shell.descriptor.hasStun for shell in self.defaultAmmo), VehicleMechanic.STUN)]
        descriptor = self.__getDescriptor(vehDescr)
        extendMechanics(mechanics, descriptor.mechanicsParams, mechanicChecks, GUN_MECHANICS_OVERRIDES)
        return mechanics

    def _getMaxAmmo(self):
        return self.descriptor.maxAmmo

    def _getDefaultAmmo(self, proxy):
        result = []
        shells = veh_core.getDefaultAmmoForGun(self.descriptor)
        for i in range(0, len(shells), 2):
            result.append(Shell(shells[i], count=shells[(i + 1)], proxy=proxy))

        return result

    def _getShortInfoKey(self, vehicleDescr=None):
        key = super(VehicleGun, self)._getShortInfoKey()
        if self.isAutoReloadable(vehicleDescr):
            return ('/').join((key, 'autoReload'))
        if self.isAutoShoot(vehicleDescr):
            return ('/').join((key, 'autoShoot'))
        if self.isDualGun(vehicleDescr):
            return ('/').join((key, 'dualGun'))
        if self.isTwinGun(vehicleDescr):
            return ('/').join((key, 'twinGun'))
        return key

    def __getDescriptor(self, vehDescr=None):
        vehicleGuns = vehDescr.type.getGuns() if vehDescr is not None else ()
        descriptor = findFirst(lambda gun: gun.compactDescr == self.intCD, vehicleGuns)
        return descriptor or self.descriptor


class VehicleEngine(VehicleModule):
    __slots__ = ()
    _GUI_SUPPORTED_MECHANICS = {
     VehicleMechanic.TURBOSHAFT_ENGINE,
     VehicleMechanic.ROCKET_ACCELERATION}

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.engine.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.engine.intCD:
                result.add(vehicle)

        return result

    def getConflictedEquipments(self, vehicle):
        conflictEqs = list()
        oldModuleId = vehicle.engine.intCD
        vehicle.descriptor.installComponent(self.intCD)
        for eq in vehicle.consumables.installed.getItems():
            installPossible, _ = eq.descriptor.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(eq)

        vehicle.descriptor.installComponent(oldModuleId)
        return conflictEqs

    def hasTurboshaftEngine(self):
        return g_paramsCache.hasTurboshaftEngine(self.intCD)

    def hasRocketAcceleration(self):
        return g_paramsCache.hasRocketAcceleration(self.intCD)

    def hasRechargeableNitro(self):
        return g_paramsCache.hasRechargeableNitro(self.intCD)

    @property
    def iconName(self):
        return ModulesIconNames.ENGINE

    def getExtraIconInfo(self, vehDescr=None):
        if self.hasTurboshaftEngine():
            return RES_ICONS.MAPS_ICONS_MODULES_TURBINEENGINEICON
        else:
            if self.hasRocketAcceleration():
                return RES_ICONS.MAPS_ICONS_MODULES_ROCKETACCELERATIONICON
            return

    def getVehicleMechanics(self, vehDescr):
        mechanics = super(VehicleEngine, self).getVehicleMechanics(vehDescr)
        mechanicChecks = [
         (
          vehDescr.hasTurboshaftEngine, VehicleMechanic.TURBOSHAFT_ENGINE),
         (
          vehDescr.hasRocketAcceleration, VehicleMechanic.ROCKET_ACCELERATION)]
        extendMechanics(mechanics, {}, mechanicChecks, ENGINE_MECHANICS_OVERRIDES)
        return mechanics


class VehicleFuelTank(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.fuelTank.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.fuelTank.intCD:
                result.add(vehicle)

        return result


class VehicleRadio(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.radio.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.radio.intCD:
                result.add(vehicle)

        return result

    @property
    def iconName(self):
        return ModulesIconNames.RADIO


class Shell(FittingItem):
    __slots__ = ('_count', )

    def __init__(self, intCompactDescr, count=0, proxy=None, isBoughtForCredits=False):
        FittingItem.__init__(self, intCompactDescr, proxy, isBoughtForCredits)
        self._count = count

    @property
    def level(self):
        return 0

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def type(self):
        return self.descriptor.kind

    @property
    def mechanics(self):
        return self.descriptor.type.mechanics

    @property
    def isModernMechanics(self):
        return self.type == SHELL_TYPES.HIGH_EXPLOSIVE and self.mechanics == SHELL_MECHANICS_TYPE.MODERN

    @property
    def isNonPiercingDamageMechanics(self):
        return self.mechanics == SHELL_MECHANICS_TYPE.NON_PIERCING_DAMAGE

    @property
    def longUserName(self):
        return self._getFormatLongUserName('kinds')

    @property
    def longUserNameAbbr(self):
        return self._getFormatLongUserName('kindsAbbreviation')

    @property
    def icon(self):
        return ICONS_MASK[:-4] % {'type': self.itemTypeName, 
           'subtype': 'small/', 
           'unicName': self.descriptor.icon[0]}

    @property
    def defaultLayoutValue(self):
        return ((self.isBoughtForAltPrice or self).intCD if 1 else -self.intCD, self.count)

    def isDamageMutable(self):
        return self.descriptor.isDamageMutable

    def getAdvancedTooltipKey(self):
        return (
         self.type, self.isModernMechanics, self.isNonPiercingDamageMechanics, self.isDamageMutable())

    def getBonusIcon(self, size='small'):
        sizeFldr = R.images.gui.maps.icons.shell.dyn(size)
        if not sizeFldr:
            _logger.warn('Shell %s icon for size %s doesnt exists!', self.descriptor.iconName, size)
            return ''
        return backport.image(sizeFldr.dyn(self.descriptor.iconName)())

    def getGUIEmblemID(self):
        return self.descriptor.iconName

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        resID = R.images.gui.maps.shop.shells.num(size).dyn(replaceHyphenToUnderscore(self.descriptor.iconName))()
        if resID != -1:
            return backport.image(resID)
        return ''

    def isInstalled(self, vehicle, slotIdx=None):
        for shell in vehicle.shells.installed.getItems():
            if self.intCD == shell.intCD:
                return True

        return super(Shell, self).isInstalled(vehicle, slotIdx)

    def isInSetup(self, vehicle, setupIndex=None, slotIdx=None):
        return vehicle.shells.setupLayouts.containsIntCD(self.intCD, setupIndex, slotIdx)

    def isInOtherLayout(self, vehicle):
        return vehicle.shells.setupLayouts.isInOtherLayout(self)

    def _getAltPrice(self, buyPrice, proxy):
        if Currency.GOLD in buyPrice:
            return buyPrice.exchange(Currency.GOLD, Currency.CREDITS, proxy.exchangeRateForShellsAndEqs, useDiscounts=False)
        return super(Shell, self)._getAltPrice(buyPrice, proxy)

    def _getFormatLongUserName(self, kind):
        if self.nationID == nations.INDICES['germany']:
            caliber = float(self.descriptor.caliber) / 10
            dimension = backport.text(R.strings.item_types.shell.dimension.sm())
        elif self.nationID == nations.INDICES['usa']:
            caliber = float(self.descriptor.caliber) / 25.4
            dimension = backport.text(R.strings.item_types.shell.dimension.inch())
        else:
            caliber = self.descriptor.caliber
            dimension = backport.text(R.strings.item_types.shell.dimension.mm())
        return backport.text(R.strings.item_types.shell.name(), kind=backport.text(R.strings.item_types.shell.dyn(kind).dyn(self.descriptor.kind)()), name=self.userName, caliber=backport.getNiceNumberFormat(caliber), dimension=dimension)

    def _getShortInfoKey(self):
        if self.isDamageMutable():
            return '#menu:descriptions/mutableDamageShell'
        return super(Shell, self)._getShortInfoKey()

    def _sortByType(self, other):
        return SHELL_TYPES_ORDER_INDICES[self.type] - SHELL_TYPES_ORDER_INDICES[other.type]