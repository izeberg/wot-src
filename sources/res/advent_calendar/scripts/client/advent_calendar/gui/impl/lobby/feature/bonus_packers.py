from __future__ import absolute_import
import typing
from shared_utils import first
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
from advent_calendar.gui.impl.lobby.feature.progression_reward_packers import LootboxTokensPacker
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker as BaseTmanTemplateBonusPacker
from gui.impl import backport
from gui.impl.backport import TooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN
from gui.server_events.bonuses import C11nProgressTokenBonus
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker, BonusUIPacker
from gui.shared.missions.packers.bonus import CrewSkinBonusUIPacker as BaseCrewSkinBonusUIPacker
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as BaseCustomizationBonusUIPacker
from gui.shared.missions.packers.bonus import SimpleBonusUIPacker
from gui.shared.missions.packers.bonus import TokenBonusUIPacker as BaseTokenBonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap
from helpers import dependency
if typing.TYPE_CHECKING:
    from typing import List
    from gui.shared.gui_items.customization.c11n_items import Style
    from gui.server_events.bonuses import LootBoxTokensBonus
    from gui.server_events.bonuses import TokensBonus

def getRewardBonusMapping():
    mapping = getDefaultBonusPackersMap()
    mapping.update({'customizations': CustomizationBonusUIPacker(), 
       'lootBox': LootBoxPacker(), 
       'tmanToken': TmanTemplateBonusPacker(), 
       'crewSkins': CrewSkinBonusUIPacker(), 
       'tokens': TokenBonusUIPacker(), 
       'freeXP': SimpleBonusUIPacker(), 
       C11nProgressTokenBonus.BONUS_NAME: ProgressionCustomizationBonusUIPacker()})
    return mapping


def getRewardBonusPacker():
    return BonusUIPacker(getRewardBonusMapping())


class TokenBonusUIPacker(BaseTokenBonusUIPacker):

    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        if bonus.getName() == BATTLE_BONUS_X5_TOKEN:
            model = cls._getBonusModel()
        else:
            model = TokenBonusModel()
        cls._packCommon(bonus, model)
        return bonusPacker(model, bonus, *args)

    @classmethod
    def _getTokenBonusPackers(cls):
        tokenBonusPackers = super(TokenBonusUIPacker, cls)._getTokenBonusPackers()
        tokenBonusPackers.update({BATTLE_BONUS_X5_TOKEN: cls.__packBattleBonusX5Token})
        return tokenBonusPackers

    @classmethod
    def _getBonusModel(cls):
        return IconBonusModel()

    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        model.setName(BATTLE_BONUS_X5_TOKEN)
        model.setValue(str(bonus.getCount()))
        model.setLabel(backport.text(R.strings.tooltips.quests.bonuses.token.battle_bonus_x5.header()))
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


class LootBoxPacker(SimpleBonusUIPacker):
    _itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def _pack(cls, bonus):
        lootbox = cls._itemsCache.items.tokens.getLootBoxByTokenID(first(bonus.getTokens().keys()))
        count = bonus.getCount()
        if lootbox is None or count < 0:
            return []
        model = cls._getBonusModel()
        model.setIsCompensation(bonus.isCompensation())
        model.setName(bonus.getName())
        model.setValue(str(count))
        model.setIcon(lootbox.getType())
        return [
         model]

    @classmethod
    def _getBonusModel(cls):
        return IconBonusModel()

    @classmethod
    def _getToolTip(cls, bonus):
        return [
         TooltipData(specialArgs=(LootboxTokensPacker.packTooltipPayload(),))]

    @classmethod
    def _getContentId(cls, bonus):
        return [
         R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip()]