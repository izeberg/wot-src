from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.tooltips.advanced import BaseAdvancedTooltip
from gui.shared.tooltips.advanced.data.default_alt_key_data import AltKeyData

class MoneyAndXpAdvanced(BaseAdvancedTooltip):
    _moviesOrDescriptions = {'crystal': 'economyBonds', 
       'credits': 'economyCredits', 
       'gold': 'economyGold', 
       'freeXP': 'economyConvertExp'}

    def _getTooltipData(self, *args, **kwargs):
        _type = args[0]
        swfName = self._moviesOrDescriptions[_type]
        header = TOOLTIPS.getHeaderBtnTitle(_type)
        description = self._moviesOrDescriptions[_type]
        return (AltKeyData(swfName=swfName, header=header, description=description),)