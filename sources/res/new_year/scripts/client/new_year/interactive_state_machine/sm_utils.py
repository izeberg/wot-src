from gui_lootboxes.gui.lb_gui_constants import GLOW

def isCoolRewards(rewards):
    for reward in rewards:
        meta = reward.get('meta', {})
        if GLOW in meta:
            return True

    return False