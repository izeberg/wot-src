import typing
from gui.impl.auxiliary.collections_helper import TmanTemplateBonusPacker
from gui.impl.backport import text, createTooltipData
from gui.impl.gen import R
from gui.shared.missions.packers.bonus import BonusUIPacker, TokenBonusUIPacker, VehiclesBonusUIPacker, getDefaultBonusPackersMap, CustomizationBonusUIPacker, SimpleBonusUIPacker, BlueprintBonusUIPacker
from gui.shared.gui_items.Vehicle import getNationLessName
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_attachment_bonus_model import JmAttachmentBonusModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_bonus_model import JmBonusModel
from journey_marathon_common.journey_marathon_constants import isUnlockToken, parseUnlockTokenKey
from shared_utils import first
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.shared.gui_items.Vehicle import Vehicle

class JMLockTokenBonusPacker(TokenBonusUIPacker):
    _JM_LOCK_TOKEN = 'jm_lock_token'

    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        if isUnlockToken(tokenID):
            return cls._JM_LOCK_TOKEN
        return super(JMLockTokenBonusPacker, cls)._getTokenBonusType(tokenID, complexToken)

    @classmethod
    def _getTokenBonusPackers(cls):
        tokenBonusPackers = super(JMLockTokenBonusPacker, cls)._getTokenBonusPackers()
        tokenBonusPackers.update({cls._JM_LOCK_TOKEN: cls.__packJMLockToken})
        return tokenBonusPackers

    @classmethod
    def _getTooltipsPackers(cls):
        tooltipsPackers = super(JMLockTokenBonusPacker, cls)._getTooltipsPackers()
        tooltipsPackers.update({cls._JM_LOCK_TOKEN: lambda *args: createTooltipData(None)})
        return tooltipsPackers

    @classmethod
    def __packJMLockToken(cls, model, bonus, *args):
        name = cls._JM_LOCK_TOKEN
        tokenName = first(bonus.getTokens().keys())
        model.setName(name)
        model.setValue(str(bonus.formatValue()))
        model.setLabel(getJmLockTokenUserName(tokenName))
        return model


class JMVehiclesBonusUIPacker(VehiclesBonusUIPacker):

    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        return [ cls._packVehicle(bonus, vehInfo, vehicle) for vehicle, vehInfo in vehicles ]

    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        model = JmBonusModel()
        model.setName(bonus.getName())
        model.setIcon(getNationLessName(vehicle.name))
        cls.__fillVehicleInfo(model, vehicle)
        return model

    @classmethod
    def __fillVehicleInfo(cls, model, vehicle):
        model.setIsElite(vehicle.isElite)
        model.setVehicleLvl(vehicle.level)
        model.setVehicleShortName(vehicle.shortUserName)
        model.setVehicleType(vehicle.type)
        model.setIsPremium(vehicle.isPremium)


class _JmC11nPacker(CustomizationBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        c11nItem = bonus.getC11nItem(item)
        if item.get('custType') == 'attachment':
            model = JmAttachmentBonusModel()
            model.setRarity(c11nItem.rarity)
        else:
            model = cls._getBonusModel()
        cls._packCommon(bonus, model)
        model.setValue(str(item.get('value', 0)))
        model.setIcon(str(c11nItem.itemTypeName))
        model.setLabel(label)
        return model


class JmPremiumDaysPacker(SimpleBonusUIPacker):
    _ICONS_AVAILABLE = {
     1, 2, 3, 7, 14, 30, 90, 180, 360}

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = super(JmPremiumDaysPacker, cls)._packSingleBonus(bonus, label)
        days = bonus.getValue()
        if days in cls._ICONS_AVAILABLE:
            model.setName(('_').join([bonus.getName(), str(days)]))
        else:
            model.setName('premium_plus_universal')
        return model


class JmBlueprintBonusPacker(BlueprintBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        models = super(JmBlueprintBonusPacker, cls)._pack(bonus)
        model = models[0]
        label = bonus.getBlueprintTooltipName()
        model.setLabel(label)
        return models


def getJmLockTokenUserName(lockToken):
    keyName = parseUnlockTokenKey(lockToken)
    res = R.strings.journey_marathon.lockToken.dyn(keyName)
    if res.isValid():
        return text(res.name())
    else:
        return


def getJmBonusPackersMap():
    blueprintBonusPacker = JmBlueprintBonusPacker()
    mapping = getDefaultBonusPackersMap()
    mapping.update({'vehicles': JMVehiclesBonusUIPacker(), 
       'tokens': JMLockTokenBonusPacker(), 
       'battleToken': JMLockTokenBonusPacker(), 
       'tmanToken': TmanTemplateBonusPacker(), 
       'customizations': _JmC11nPacker(), 
       'premium_plus': JmPremiumDaysPacker(), 
       'blueprints': blueprintBonusPacker, 
       'blueprintsAny': blueprintBonusPacker, 
       'finalBlueprints': blueprintBonusPacker})
    return mapping


def getJMBonusPacker():
    mapping = getJmBonusPackersMap()
    return BonusUIPacker(mapping)