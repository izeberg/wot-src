from __future__ import absolute_import
import functools
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_taler_tooltip import BattlePassTalerTooltip
from gui.impl.lobby.battle_pass.tooltips.reward_compensation_tooltip import RewardCompensationTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.box_tooltip import BoxTooltip
from gui.impl.lobby.user_missions.tooltips.challenges_shields_tooltip import ChallengesShieldsTooltip

def checkIsEnabled(default=None):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not getattr(self, 'isEnabled', False):
                return default
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


def createTooltipContentDecorator():

    def decorator(func):

        def wrapper(self, event, contentID):
            tooltipData = self.getTooltipData(event)
            if contentID == R.views.mono.user_missions.tooltips.challenges_shields_tooltip():
                return ChallengesShieldsTooltip()
            else:
                if contentID == R.views.mono.battle_pass.tooltips.reward_compensation():
                    return RewardCompensationTooltip(*tooltipData.specialArgs)
                if contentID == R.views.mono.lootbox.tooltips.box_tooltip():
                    if tooltipData is None:
                        return
                    return BoxTooltip(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.bpcoin():
                    return BattlePassCoinTooltipView()
                if contentID == R.views.mono.battle_pass.tooltips.bptaler():
                    return BattlePassTalerTooltip()
                return func(self, event, contentID)

        return wrapper

    return decorator