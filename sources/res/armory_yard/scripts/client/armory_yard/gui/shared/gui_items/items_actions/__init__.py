from gui.shared.gui_items.items_actions.factory import registerAction
from armory_yard.gui.shared.gui_items.items_actions.actions import CollectRewardsAction, BuyStepTokensAction, RerollQuestAction, AcceptRerollAction
COLLECT_REWARDS = 'collectRewards'
BUY_STEP_TOKENS = 'buyStepTokens'
BUY_PURCHASE_STAGE_TOKENS = 'buyStepTokens'
REROLL_QUEST = 'rerollQuest'
ACCEPT_REROLL = 'acceptReroll'

def registerActions():
    registerAction(COLLECT_REWARDS, CollectRewardsAction)
    registerAction(BUY_STEP_TOKENS, BuyStepTokensAction)
    registerAction(REROLL_QUEST, RerollQuestAction)
    registerAction(ACCEPT_REROLL, AcceptRerollAction)