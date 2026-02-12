from __future__ import absolute_import
from constants import PREBATTLE_TYPE, QUEUE_TYPE, ARENA_BONUS_TYPE
from fun_random.gui.battle_results.fun_stats_controller import FunBattleResultStatsCtrl
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_tooltip_view import FunRandomProgressionTooltipView
from fun_random.gui.prb_control.formatters.invites import FunPrbInviteHtmlTextFormatter
from fun_random.gui.prb_control.storages.fun_random_storage import FunRandomStorage
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants
from gui.prb_control.storages import makeQueueName
from gui.shared.system_factory import registerPrbInviteHtmlFormatter, registerPrbStorage, registerModeSelectorTooltips, registerModeNameKwargsGetterByPrb, registerModeNameKwargsGetterByQueue, registerModeNameKwargsGetterByBonusType, registerPrebattleConditionIconGetter, registerBattleResultStatsCtrl
from fun_random_common.fun_constants import FunSubModeImpl
from fun_random.gui.shared.fun_system_factory import registerFunBattleResultsPresenter
from fun_random.gui.battle_results.fun_battle_results_sub_presenter import FunBattleResultsSubPresenter

def registerFunRandomOthersPrbParams():
    registerModeSelectorTooltips([
     ModeSelectorTooltipsConstants.FUN_RANDOM_CALENDAR_TOOLTIP,
     ModeSelectorTooltipsConstants.FUN_RANDOM_REWARDS], {R.views.fun_random.mono.lobby.tooltips.progression_tooltip(): FunRandomProgressionTooltipView})
    registerPrbStorage(makeQueueName(QUEUE_TYPE.FUN_RANDOM), FunRandomStorage())
    registerPrbInviteHtmlFormatter(PREBATTLE_TYPE.FUN_RANDOM, FunPrbInviteHtmlTextFormatter)
    registerModeNameKwargsGetterByQueue(QUEUE_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerModeNameKwargsGetterByPrb(PREBATTLE_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerModeNameKwargsGetterByBonusType(ARENA_BONUS_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerPrebattleConditionIconGetter(ARENA_BONUS_TYPE.FUN_RANDOM, FunAssetPacksMixin.getPrebattleConditionIcon)
    registerBattleResultStatsCtrl(ARENA_BONUS_TYPE.FUN_RANDOM, FunBattleResultStatsCtrl)
    registerFunBattleResultsPresenter(FunSubModeImpl.DEFAULT, FunBattleResultsSubPresenter)