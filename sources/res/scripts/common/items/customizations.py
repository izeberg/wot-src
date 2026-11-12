import base64, copy
from string import lower
from typing import Dict, TypeVar, Optional, TYPE_CHECKING
from constants import IS_CELLAPP, IS_BASEAPP
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
from items import decodeEnum, vehicles
from items.components import c11n_components as cn
from items.components.c11n_constants import ApplyArea, SeasonType, CustomizationType, CustomizationTypeNames, ItemTags, MAX_USERS_PROJECTION_DECALS, EMPTY_ITEM_ID
from serializable_types.customizations import PaintComponent, CamouflageComponent, getAllItemsFromOutfit, AttachmentComponent, ProjectionDecalComponent, SequenceComponent, PersonalNumberComponent, InsigniaComponent, CustomizationOutfit, DecalComponent, CUSTOMIZATION_CLASSES as _CUSTOMIZATION_CLASSES, parseC11sComponentDescr
from serialization import ComponentBinDeserializer, ComponentXmlDeserializer, SerializationException, EmptyComponent, makeCompDescr, FieldTypes, FieldFlags, FieldType, SerializableComponent, intField, intArrayField, xmlOnlyFloatField, xmlOnlyFloatArrayField, applyAreaEnumField, customFieldType, customArrayField, optionsEnumField, arrayField, strField, xmlOnlyApplyAreaEnumField, xmlOnlyIntField, xmlOnlyTagsField
from serialization.serializable_component import SerializableComponentChildType
from soft_exception import SoftException
from .named_vector import NamedVector
from .utils import getEditorOnlySection
parseCompDescr = parseC11sComponentDescr
if TYPE_CHECKING:
    from items.vehicles import VehicleDescrType

def checkItemInCompDescr(item, customizationElementCompDescr):
    item = cn.splitIntDescr(item) if isinstance(item, int) else item
    itemType = item[0]
    if itemType == CustomizationType.STYLE:
        path = ('styleId', None)
    elif itemType == CustomizationType.MODIFICATION:
        path = ('modifications', None)
    else:
        path = (
         ('{}s').format(lower(CustomizationTypeNames[itemType])), ('id', None))
    return ComponentBinDeserializer(_CUSTOMIZATION_CLASSES).hasItem(customizationElementCompDescr, path, item[1])


def parseOutfitDescr(outfitDescr):
    if not outfitDescr:
        return CustomizationOutfit()
    try:
        outfit = parseC11sComponentDescr(outfitDescr)
    except SerializationException:
        LOG_CURRENT_EXCEPTION()
        LOG_ERROR('Bad outfit descr', base64.b64encode(outfitDescr))
        outfit = CustomizationOutfit()

    if outfit.customType != CustomizationOutfit.customType:
        raise SoftException('Wrong customization item type')
    return outfit


if IS_CELLAPP or IS_BASEAPP:
    _itemType = TypeVar('_itemType', bound=cn.BaseCustomizationItem)

def isEditedStyle(outfit):
    styleId = outfit.styleId
    styleProgressLvl = outfit.styleProgressionLevel
    styleSerialNumber = outfit.serial_number
    outfit.styleId = 0
    outfit.styleProgressionLevel = 0
    outfit.serial_number = ''
    isEmpty = not outfit
    outfit.styleId = styleId
    outfit.styleProgressionLevel = styleProgressLvl
    outfit.serial_number = styleSerialNumber
    return not isEmpty


def getNationalEmblemsOutfit(vehDescr):
    decals = createNationalEmblemComponents(vehDescr)
    outfit = CustomizationOutfit(decals=decals)
    return outfit


def getBootcampOutfit(vehDescr, customizationConfig):
    tankCustomization = customizationConfig.get(vehDescr.name, {})
    styleId = tankCustomization.get('styleId', 0)
    cache = vehicles.g_cache.customization20()
    if styleId in cache.styles:
        outfit = copy.deepcopy(cache.styles[styleId].outfits[SeasonType.SUMMER])
        if ItemTags.ADD_NATIONAL_EMBLEM in cache.styles[styleId].tags:
            outfit.decals.extend(createNationalEmblemComponents(vehDescr))
        return outfit
    return CustomizationOutfit(decals=createNationalEmblemComponents(vehDescr))


def __ignoreItem(itemId, cache, ignoreEmpty, ignoreStyleOnly):
    if itemId != EMPTY_ITEM_ID:
        if ignoreStyleOnly and cache[itemId].isStyleOnly:
            return True
    elif ignoreEmpty:
        return True
    return False


def getOutfitType(arenaKind, bonusType):
    return SeasonType.fromArenaKind(arenaKind)


def getBattleOutfit(getter, vehType, arenaKind, bonusType):
    styleOutfitDescr = getter(vehType, SeasonType.EVENT)
    if styleOutfitDescr:
        return parseOutfitDescr(styleOutfitDescr)
    season = getOutfitType(arenaKind, bonusType)
    seasonOutfitDescr = getter(vehType, season)
    if seasonOutfitDescr:
        return parseOutfitDescr(seasonOutfitDescr)
    styleOutfitDescr = getter(vehType, SeasonType.ALL)
    return parseOutfitDescr(styleOutfitDescr)


def parseBattleOutfit(outfit, cache, arenaKind):
    if not outfit.styleId:
        return outfit
    styleOutfit = cache.styles[outfit.styleId].outfits[SeasonType.fromArenaKind(arenaKind)]
    if not isEditedStyle(outfit):
        return styleOutfit
    return copy.deepcopy(styleOutfit).applyDiff(outfit)


class NoneCustomizationItemSelector(object):

    def matches(self, itemObj=None):
        return True


class CustomizationItemSelector(NoneCustomizationItemSelector):
    ANY = ('', '*')
    priceGroups = property(lambda self: self.__priceGroups)
    excludedPriceGroups = property(lambda self: self.__excludedPriceGroups)
    tags = property(lambda self: self.__tags)
    excludedTags = property(lambda self: self.__excludedTags)
    itemCDs = property(lambda self: self.__itemCDs)
    excludedItemCDs = property(lambda self: self.__excludedItemCDs)
    isRented = property(lambda self: self.__isRented)

    def __init__(self, priceGroups=(), excludedPriceGroups=(), tags=(), excludedTags=(), itemCDs=(), excludedItemCDs=(), isRented=None):
        self.__priceGroups = frozenset(str(v) for v in priceGroups if str(v))
        self.__excludedPriceGroups = frozenset(str(v) for v in excludedPriceGroups if str(v))
        self.__tags = frozenset(str(v) for v in tags if str(v))
        self.__excludedTags = frozenset(str(v) for v in excludedTags if str(v))
        self.__itemCDs = frozenset(int(v) for v in itemCDs)
        self.__excludedItemCDs = frozenset(int(v) for v in excludedItemCDs)
        self.__isRented = isRented

    def matches(self, itemObj=None):
        try:
            itemPriceGroups = self._splitPriceGroups(itemObj.priceGroup)
            itemTags = itemObj.tags
            itemCD = itemObj.compactDescr
            itemIsRented = itemObj.isRent if itemObj.itemType == CustomizationType.STYLE else None
        except (AttributeError, TypeError, ValueError):
            return True

        if self._matchSet(itemPriceGroups, self.__priceGroups, self.__excludedPriceGroups):
            return True
        else:
            if self._matchSet(itemTags, self.__tags, self.__excludedTags):
                return True
            if self._matchItemCD(itemCD, self.__itemCDs, self.__excludedItemCDs):
                return True
            if self.__isRented is not None and itemIsRented == self.__isRented:
                return True
            return False

    @staticmethod
    def _splitPriceGroups(value):
        return {token for token in str(value).split() if token if token}

    def __repr__(self):
        return (':').join((
         self._joinPredicate(self.__priceGroups, self.__excludedPriceGroups, '|'),
         self._joinPredicate(self.__tags, self.__excludedTags, '|'),
         self._joinPredicate({str(v) for v in self.__itemCDs}, {str(v) for v in self.__excludedItemCDs}, '|'),
         '' if self.__isRented is None else str(self.__isRented).lower()))

    @staticmethod
    def _matchSet(itemValues, included=(), excluded=()):
        included = set(included)
        excluded = set(excluded)
        itemValues = set(itemValues)
        if not included and not excluded:
            return None
        else:
            hasIncludedMatch = bool(included & itemValues) if included else True
            hasExcludedMatch = bool(excluded & itemValues)
            return hasIncludedMatch and not hasExcludedMatch

    @staticmethod
    def _matchItemCD(itemValue, included=(), excluded=()):
        included = set(included)
        excluded = set(excluded)
        if not included and not excluded:
            return None
        else:
            hasIncludedMatch = itemValue in included if included else True
            hasExcludedMatch = itemValue in excluded
            return hasIncludedMatch and not hasExcludedMatch

    @staticmethod
    def fromString(value):
        try:
            priceGroupStr, tagsStr, itemCDStr, isRentedStr = CustomizationItemSelector._splitTo4(value)
            priceGroups, excludedPriceGroups = CustomizationItemSelector._parsePredicate(priceGroupStr, caster=str)
            tags, excludedTags = CustomizationItemSelector._parsePredicate(tagsStr, caster=str)
            itemCDs, excludedItemCDs = CustomizationItemSelector._parsePredicate(itemCDStr, caster=int)
            isRented = CustomizationItemSelector._parseBoolOrNone(isRentedStr)
        except (SoftException, ValueError):
            LOG_ERROR(('Unable to match any customization item by {}').format(value))
            return NoneCustomizationItemSelector()

        return CustomizationItemSelector(priceGroups=priceGroups, excludedPriceGroups=excludedPriceGroups, tags=tags, excludedTags=excludedTags, itemCDs=itemCDs, excludedItemCDs=excludedItemCDs, isRented=isRented)

    @staticmethod
    def _splitTo4(value):
        parts = str(value).split(':', 3)
        while len(parts) < 4:
            parts.append('')

        return (
         parts[0], parts[1], parts[2], parts[3])

    @staticmethod
    def _parseBoolOrNone(value):
        value = str(value).strip().lower()
        if value in ('', '*'):
            return
        else:
            if value == 'true':
                return True
            if value == 'false':
                return False
            raise SoftException(('Invalid isRented value: {}').format(value))
            return

    @staticmethod
    def _parsePredicate(predicate, separator='|', caster=str):
        included = set()
        excluded = set()
        predicate = str(predicate).strip()
        if predicate in ('', '*'):
            return (included, excluded)
        tokens = predicate.split(separator)
        for token in tokens:
            token = token.strip()
            if not token:
                raise SoftException(('Empty token in predicate: {}').format(predicate))
            if token == '~':
                raise SoftException(('Empty excluded token in predicate: {}').format(predicate))
            if token.startswith('~'):
                raw = token[1:].strip()
                if not raw:
                    raise SoftException(('Empty excluded token in predicate: {}').format(predicate))
                if raw.startswith('~'):
                    raise SoftException(('Invalid excluded token in predicate: {}').format(predicate))
                excluded.add(caster(raw))
            else:
                included.add(caster(token))

        return (
         included, excluded)

    @staticmethod
    def _joinPredicate(included, excluded, separator):
        parts = []
        parts.extend(sorted(str(v) for v in included))
        parts.extend(sorted(('~{}').format(v) for v in excluded))
        return separator.join(parts)


class OutfitLogEntry(object):

    def __init__(self, outfit):
        applyAreaBitmaskToDict = CustomizationOutfit.applyAreaBitmaskToDict
        getPaintCd = self.__getPaintCd
        getCamouflageCd = self.__getCamouflageCd
        getDecalCd = self.__getDecalCd
        getPersonalNumberData = self.__getPersonalNumberData
        self.style_cd = cn.StyleItem.makeIntDescr(outfit.styleId) if outfit.styleId else 0
        self.modification_cd = cn.ModificationItem.makeIntDescr(outfit.modifications[0]) if outfit.modifications else 0
        self._paints = applyAreaBitmaskToDict(outfit.paints)
        self._decals = applyAreaBitmaskToDict(outfit.decals)
        self._projection_decals = outfit.projection_decals
        self._camouflages = applyAreaBitmaskToDict(outfit.camouflages)
        self._personal_numbers = applyAreaBitmaskToDict(outfit.personal_numbers)
        self.chassis_paint_cd = getPaintCd(ApplyArea.CHASSIS)
        self.hull_paint_cd = getPaintCd(ApplyArea.HULL)
        self.turret_paint_cd = getPaintCd(ApplyArea.TURRET)
        self.gun_paint_cd0 = getPaintCd(ApplyArea.GUN)
        self.gun_paint_cd1 = getPaintCd(ApplyArea.GUN_1)
        self.hull_camouflage_cd = getCamouflageCd(ApplyArea.HULL)
        self.turret_camouflage_cd = getCamouflageCd(ApplyArea.TURRET)
        self.gun_camouflage_cd = getCamouflageCd(ApplyArea.GUN)
        self.hull_decal_cd0, self.hull_decal_progression_level0 = getDecalCd(ApplyArea.HULL)
        self.hull_decal_cd1, self.hull_decal_progression_level1 = getDecalCd(ApplyArea.HULL_1)
        self.hull_decal_cd2, self.hull_decal_progression_level2 = getDecalCd(ApplyArea.HULL_2)
        self.hull_decal_cd3, self.hull_decal_progression_level3 = getDecalCd(ApplyArea.HULL_3)
        self.turret_decal_cd0, self.turret_decal_progression_level0 = getDecalCd(ApplyArea.TURRET)
        self.turret_decal_cd1, self.turret_decal_progression_level1 = getDecalCd(ApplyArea.TURRET_1)
        self.turret_decal_cd2, self.turret_decal_progression_level2 = getDecalCd(ApplyArea.TURRET_2)
        self.turret_decal_cd3, self.turret_decal_progression_level3 = getDecalCd(ApplyArea.TURRET_3)
        self.hull_personal_number0 = getPersonalNumberData(ApplyArea.HULL_2)
        self.hull_personal_number1 = getPersonalNumberData(ApplyArea.HULL_3)
        self.turret_personal_number0 = getPersonalNumberData(ApplyArea.TURRET_2)
        self.turret_personal_number1 = getPersonalNumberData(ApplyArea.TURRET_3)
        self.gun_personal_number0 = getPersonalNumberData(ApplyArea.GUN_2)
        self.gun_personal_number1 = getPersonalNumberData(ApplyArea.GUN_3)
        getProjectionDecalData = self.__getProjectionDecalData
        for number in xrange(0, MAX_USERS_PROJECTION_DECALS):
            setattr(self, ('projection_decal{}').format(number), getProjectionDecalData(number))

        self.style_progression_level = outfit.styleProgressionLevel
        self.serial_number = outfit.serial_number

    @staticmethod
    def __getItemCompDescr(storage, area, cdFormatter):
        i = storage.get(area)
        if not i:
            return 0
        return cdFormatter(i[0].id)

    @staticmethod
    def __getItemCompDescrWithProgression(storage, area, cdFormatter):
        i = storage.get(area)
        if not i:
            return (0, 0)
        return (
         cdFormatter(i[0].id), i[0].progressionLevel)

    def __getPaintCd(self, area):
        return OutfitLogEntry.__getItemCompDescr(self._paints, area, cn.PaintItem.makeIntDescr)

    def __getCamouflageCd(self, area):
        return OutfitLogEntry.__getItemCompDescr(self._camouflages, area, cn.CamouflageItem.makeIntDescr)

    def __getDecalCd(self, area):
        return OutfitLogEntry.__getItemCompDescrWithProgression(self._decals, area, cn.DecalItem.makeIntDescr)

    def __getPersonalNumberCd(self, area):
        return OutfitLogEntry.__getItemCompDescr(self._personal_numbers, area, cn.PersonalNumberItem.makeIntDescr)

    def __getProjectionDecalData(self, number):
        value = {'projection_decal_slot': 0, 
           'projection_decal_cd': 0, 
           'projection_decal_options': 0, 
           'projection_decal_scaleFactorId': 0, 
           'projection_decal_progression_level': 0}
        try:
            projectionDecal = self._projection_decals[number]
            value['projection_decal_slot'] = projectionDecal.slotId
            value['projection_decal_cd'] = cn.ProjectionDecalItem.makeIntDescr(projectionDecal.id)
            value['projection_decal_options'] = projectionDecal.options
            value['projection_decal_scaleFactorId'] = projectionDecal.scaleFactorId
            value['projection_decal_progression_level'] = projectionDecal.progressionLevel
        except IndexError:
            pass

        return value

    def __getPersonalNumberData(self, area):
        value = {}
        value['personal_number_cd'] = self.__getPersonalNumberCd(area)
        number = self._personal_numbers.get(area)
        value['number'] = number[0].number if number else ''
        return value

    def toDict(self):
        return {k:v for k, v in self.__dict__.iteritems() if not k.startswith('_') if not k.startswith('_')}


def makeLogOutfitValues(outfitDescr):
    return OutfitLogEntry(parseOutfitDescr(outfitDescr)).toDict()


def getHullCamouflageCd(outfitDescr):
    i = CustomizationOutfit.applyAreaBitmaskToDict(parseOutfitDescr(outfitDescr).camouflages).get(ApplyArea.HULL)
    if not i:
        return 0
    return cn.CamouflageItem.makeIntDescr(i[0].id)


def getVehicleOutfit(outfits, vehTypeDescr, outfitType):
    return outfits.get(vehTypeDescr, {}).get(outfitType, '')


def createNationalEmblemComponents(vehDescr):
    decals = []
    nationalEmblemId = vehDescr.type.defaultPlayerEmblemID
    emblemRegions, _ = cn.getAvailableDecalRegions(vehDescr)
    if emblemRegions:
        decals.append(DecalComponent(id=nationalEmblemId, appliedTo=emblemRegions))
    return decals


def _clamp(value, minValue, maxValue, limit):
    value = int(round((min(max(float(value), minValue), maxValue) - minValue) / (maxValue - minValue) * limit))
    return value


def _unclamp(value, minValue, maxValue, limit):
    return float(value) * (maxValue - minValue) / limit + minValue


def _clamp16(value, minValue, maxValue):
    return _clamp(value, minValue, maxValue, 65535)


def _unclamp16(value, minValue, maxValue):
    return _unclamp(value, minValue, maxValue, 65535)