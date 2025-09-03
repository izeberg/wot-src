from comp7_light.gui.shared.tooltips import TOOLTIP_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips.battle_selector import SeasonalBattleSelectorTooltip
_R_COMP7_LIGHT_SELECTOR_TOOLTIP = R.strings.comp7_light.selectorTooltip
_TOOLTIP_MIN_WIDTH = 280

class Comp7LightSelectorTooltip(SeasonalBattleSelectorTooltip):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_LIGHT_SELECTOR_INFO
    _TOOLTIP_WIDTH = _TOOLTIP_MIN_WIDTH

    @staticmethod
    def _getTitle():
        return backport.text(_R_COMP7_LIGHT_SELECTOR_TOOLTIP.title())

    @staticmethod
    def _getDescription():
        return backport.text(_R_COMP7_LIGHT_SELECTOR_TOOLTIP.desc())