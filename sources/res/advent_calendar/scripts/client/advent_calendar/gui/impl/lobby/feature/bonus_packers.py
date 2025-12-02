from __future__ import absolute_import
from typing import TYPE_CHECKING, List
from constants import LOOTBOX_TOKEN_PREFIX
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker as BaseTmanTemplateBonusPacker
from gui.impl import backport
from gui.impl.backport import createTooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel
from gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.new_year_toy_icon_bonus_model import NewYearToyIconBonusModel
from gui.impl.new_year.new_year_bonus_packer import NYToyBonusUIPacker as BaseNYToyBonusUIPacker
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN
from gui.server_events.bonuses import C11nProgressTokenBonus
from gui.server_events.formatters import parseComplexToken
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID, getDefaultBonusPackersMap, BaseBonusUIPacker, BonusUIPacker, SimpleBonusUIPacker, CustomizationBonusUIPacker as BaseCustomizationBonusUIPacker, CrewSkinBonusUIPacker as BaseCrewSkinBonusUIPacker, TokenBonusUIPacker as BaseTokenBonusUIPacker
from helpers import dependency
from new_year.ny_toy_info import NewYearCurrentToyInfo
from shared_utils import first
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
if TYPE_CHECKING:
    from gui.server_events.bonuses import TokensBonus
    from gui.impl.backport import TooltipData

def getRewardBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update({'customizations': CustomizationBonusUIPacker(), 
       'lootBox': LootBoxPacker(), 
       'battleToken': TokenBonusUIPacker(), 
       'tmanToken': TmanTemplateBonusPacker(), 
       'crewSkins': CrewSkinBonusUIPacker(), 
       'tokens': TokenBonusUIPacker(), 
       'freeXP': SimpleBonusUIPacker(), 
       C11nProgressTokenBonus.BONUS_NAME: ProgressionCustomizationBonusUIPacker(), 
       'ny26Toys': NYToyBonusUIPacker()})
    return BonusUIPacker(mapping)


class NYToyBonusUIPacker(BaseNYToyBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, toyId, count, newCount):
        toyInfo = NewYearCurrentToyInfo(toyId)
        model = NewYearToyIconBonusModel()
        model.setName(bonus.getName())
        model.setValue(str(count))
        model.setLabel(backport.text(toyInfo.getName()))
        return model


class TokenBonusUIPacker(BaseTokenBonusUIPacker):
    _NY_GP_TOKEN = 'ny_gp'
    _NY_COIN_TOKEN = 'nyCoin'

    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        model = IconBonusModel()
        cls._packCommon(bonus, model)
        return bonusPacker(model, bonus, *args)

    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        if tokenID.startswith(cls._NY_GP_TOKEN):
            return cls._NY_GP_TOKEN
        if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
            return cls._NY_COIN_TOKEN
        return super(TokenBonusUIPacker, cls)._getTokenBonusType(tokenID, complexToken)

    @classmethod
    def _getContentId(cls, bonus):
        bonusTokens = bonus.getTokens()
        result = []
        for tokenID, _ in bonusTokens.items():
            complexToken = parseComplexToken(tokenID)
            tokenType = cls._getTokenBonusType(tokenID, complexToken)
            tooltipID = cls.__getTooltipId(tokenType)
            if tooltipID:
                result.append(tooltipID)
            else:
                result.extend(super(TokenBonusUIPacker, cls)._getContentId(bonus))

        return result

    @classmethod
    def __getTooltipId(cls, tokenType):
        if tokenType == cls._NY_COIN_TOKEN:
            return str(R.views.mono.holiday_ops.tooltips.ho_gift_machine_token_tooltip())
        else:
            return

    @classmethod
    def _getTokenBonusPackers(cls):
        tokenBonusPackers = super(TokenBonusUIPacker, cls)._getTokenBonusPackers()
        tokenBonusPackers.update({BATTLE_BONUS_X5_TOKEN: cls.__packBattleBonusX5Token, 
           cls._NY_GP_TOKEN: cls.__packNYGPToken, 
           cls._NY_COIN_TOKEN: cls.__packNYCoinToken})
        return tokenBonusPackers

    @classmethod
    def _getTooltipsPackers(cls):
        mapping = super(TokenBonusUIPacker, cls)._getTooltipsPackers()
        mapping.update({cls._NY_GP_TOKEN: createTooltipData, 
           cls._NY_COIN_TOKEN: createTooltipData})
        return mapping

    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        model.setName(BATTLE_BONUS_X5_TOKEN)
        model.setValue(str(bonus.getCount()))
        model.setLabel(backport.text(R.strings.tooltips.quests.bonuses.token.battle_bonus_x5.header()))
        return model

    @classmethod
    def __packNYGPToken(cls, model, bonus, *_):
        model.setName(cls._NY_GP_TOKEN)
        model.setValue(str(bonus.getCount()))
        model.setLabel(backport.text(R.strings.quests.bonusName.ny_gp()))
        return model

    @classmethod
    def __packNYCoinToken(cls, model, bonus, *_):
        model.setValue(str(bonus.getCount()))
        model.setIcon(cls._NY_COIN_TOKEN)
        model.setLabel(bonus.getUserName())
        return model


class CrewSkinBonusUIPacker(BaseCrewSkinBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        model = super(CrewSkinBonusUIPacker, cls)._packSingleBonus(bonus, crewSkin, count, label)
        model.setIcon(crewSkin.getIconName())
        return model


class CustomizationBonusUIPacker(BaseCustomizationBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        model = super(CustomizationBonusUIPacker, cls)._packSingleBonus(bonus, item, label)
        item = bonus.getC11nItem(item)
        model.setLabel(item.userName)
        if item.itemTypeID == GUI_ITEM_TYPE.STYLE and item.isQuestsProgression:
            model.setIcon('progressionStyle')
        else:
            model.setIcon(('{}_{}').format(item.itemTypeName, item.id))
        return model


class ProgressionCustomizationBonusUIPacker(BaseBonusUIPacker):
    _c11nService = dependency.descriptor(ICustomizationService)

    @classmethod
    def _pack(cls, bonus):
        return [cls._packSingleBonus(bonus)]

    @classmethod
    def _packSingleBonus(cls, bonus, level=None):
        styleID = bonus.getStyleID()
        level = bonus.getProgressLevel()
        style = cls._c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
        model = IconBonusModel()
        cls._packCommon(bonus, model)
        model.setIcon(('style_progress_{}_{}').format(styleID, level))
        model.setValue(style.userName)
        return model

    @classmethod
    def _getToolTip(cls, bonus):
        styleID = bonus.getStyleID()
        level = bonus.getProgressLevel()
        style = cls._c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
        return [
         TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_AWARD, specialArgs=CustomizationTooltipContext(itemCD=style.intCD, level=level))]

    @classmethod
    def _getContentId(cls, bonus):
        return [BACKPORT_TOOLTIP_CONTENT_ID]


class TmanTemplateBonusPacker(BaseTmanTemplateBonusPacker):

    @classmethod
    def _getBonusModel(cls):
        return RewardItemModel()

    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus):
        recruitInfo = getRecruitInfo(tokenID)
        if recruitInfo is None:
            return
        else:
            model = RewardItemModel()
            cls._packCommon(bonus, model)
            model.setIcon(getRecruitInfo(tokenID).getDynIconName())
            model.setLabel(recruitInfo.getFullUserName())
            return model


class LootBoxPacker(BaseBonusUIPacker):
    _itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def _pack(cls, bonus):
        lootbox = cls._itemsCache.items.tokens.getLootBoxByTokenID(first(bonus.getTokens().keys()))
        count = bonus.getCount()
        if lootbox is None or count < 0:
            return []
        model = IconBonusModel()
        model.setIsCompensation(bonus.isCompensation())
        model.setName(bonus.getName())
        model.setValue(str(count))
        model.setIcon(lootbox.getType())
        return [
         model]

    @classmethod
    def _getContentId(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                result.append(str(R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_big_loot_box_tooltip()))

        return result