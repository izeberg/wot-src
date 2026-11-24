from __future__ import absolute_import
import json, logging
from typing import TYPE_CHECKING, List
from constants import LOOTBOX_TOKEN_PREFIX
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getHolidayOpsStartTime, getProgressionRewardType
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl import backport
from gui.impl.backport import TooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum
from gui.shared.formatters.date_time import getRegionalDateTime
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker, BonusUIPacker
from helpers import dependency
if TYPE_CHECKING:
    from gui.server_events.bonuses import TmanTemplateTokensBonus, CustomizationsBonus, TokensBonus, SimpleBonus
_logger = logging.getLogger(__name__)

def getProgressionBonusMapping():
    return {'customizations': CustomizationPacker(), 
       'tmanToken': TmanTemplatePacker(), 
       'lootBox': LootboxTokensPacker()}


def getProgressionBonusPacker():
    return ProgressionBonusUIPacker(getProgressionBonusMapping())


class ProgressionBonusUIPacker(BonusUIPacker):

    def getCustomToolTip(self, bonus, questID):
        packer = self._getBonusPacker(bonus.getName())
        if packer:
            return packer.getCustomToolTip(bonus, questID)
        _logger.error('Bonus packer for bonus type %s was not implemented yet.', bonus.getName())
        return []


class BaseProgressionRewardPacker(BaseBonusUIPacker):

    @classmethod
    def _createModel(cls, bonus):
        model = ProgressionRewardItemViewModel()
        model.setRewardType(getProgressionRewardType(bonus))
        return model

    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        return cls._getToolTip(bonus)


class TmanTemplatePacker(BaseProgressionRewardPacker):

    @classmethod
    def _pack(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                packed = cls._createModel(bonus)
                if packed is None:
                    _logger.error('Received wrong tman_template token from server: %s', tokenID)
                else:
                    result.append(packed)

        return result

    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        tooltipData = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.ADVENT_CALENDAR_TANKMAN_NOT_RECRUITED, specialArgs=[
                 tokenID, questID]))

        return tooltipData

    @classmethod
    def _getContentId(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                result.append(BACKPORT_TOOLTIP_CONTENT_ID)

        return result


class CustomizationPacker(BaseProgressionRewardPacker):

    @classmethod
    def _pack(cls, bonus):
        result = []
        for item in bonus.getCustomizations():
            if item is not None:
                result.append(cls._createModel(bonus))

        return result

    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        item = first(bonus.getCustomizations())
        itemCustomization = bonus.getC11nItem(item)
        tooltipData = [
         TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.ADVENT_CALENDAR_CUSTOMIZATION_ITEM, specialArgs=(
          questID,) + CustomizationTooltipContext(itemCD=itemCustomization.intCD))]
        return tooltipData


class LootboxTokensPacker(BaseProgressionRewardPacker):
    _adventController = dependency.descriptor(IAdventCalendarController)

    @classmethod
    def _pack(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                result.append(cls._createModel(bonus))

        return result

    @classmethod
    def _getContentId(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                result.append(R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip())

        return result

    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        result = []
        for tokenID in bonus.getTokens().keys():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                result.append(TooltipData(specialArgs=(cls.packTooltipPayload(),)))

        return result

    @classmethod
    def packTooltipPayload(cls):
        hoStartTime = getHolidayOpsStartTime(adventController=cls._adventController)
        return json.dumps({'header': backport.text(R.strings.advent_calendar.progressionRewards.tooltip.lootbox.simple.header()), 
           'body': backport.text(R.strings.advent_calendar.progressionRewards.tooltip.lootbox.simple.body(), date=getRegionalDateTime(hoStartTime, DateTimeFormatsEnum.DAYMONTHFULL))})