import typing
from gui.shared.tooltips.advanced import BaseAdvancedTooltip
from gui.shared.tooltips.advanced.data.default_alt_key_data import AltKeyData
from gui.impl import backport
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from gui.goodies.goodie_items import DemountKit

class DemountKitTooltipAdvanced(BaseAdvancedTooltip):

    def _getTooltipData(self, *args, **kwargs):
        demountKit = self.context.buildItem(*args, **kwargs)
        dkType = demountKit.demountKitGuiType
        description = backport.text(R.strings.tooltips.advanced.demountKit.dyn(dkType)())
        return (
         AltKeyData(swfName='demountKit', header=demountKit.userName, description=description),)