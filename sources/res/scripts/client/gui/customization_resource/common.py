from gui.impl.gen import R
from gui.shared.missions.packers.bonus import BonusUIPacker, CurrenciesBonusUIPacker, getDefaultBonusPackersMap
from shared_utils import first

def getCustomizationResourceRewardsBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update({'currencies': CustomizationResourceCurrenciesBonusUIPacker})
    return BonusUIPacker(mapping)


class CustomizationResourceCurrenciesBonusUIPacker(CurrenciesBonusUIPacker):

    @classmethod
    def _getToolTip(cls, bonus):
        result = []
        wrapped = first(bonus.getWrappedEpicBonusList())
        if wrapped:
            result.append({'currencyType': wrapped['type']})
        return result

    @classmethod
    def _getContentId(cls, bonus):
        return [R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView()]