import typing
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_taler_tooltip import BattlePassTalerTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.box_tooltip import BoxTooltip
if typing.TYPE_CHECKING:
    from gui.impl.backport import TooltipData

def createTooltipContentDecorator():

    def decorator(func):

        def wrapper(self, event, contentID):
            tooltipData = self.getTooltipData(event)
            if contentID == R.views.lobby.battle_pass.tooltips.BattlePassCoinTooltipView():
                return BattlePassCoinTooltipView()
            else:
                if contentID == R.views.lobby.battle_pass.tooltips.BattlePassTalerTooltip():
                    return BattlePassTalerTooltip()
                if contentID == R.views.mono.lootbox.tooltips.box_tooltip():
                    if tooltipData is None:
                        return
                    return BoxTooltip(*tooltipData.specialArgs)
                return func(self, event, contentID)

        return wrapper

    return decorator