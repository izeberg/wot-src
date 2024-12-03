from gui.shared.system_factory import registerGamefaceNotifications
from gui.impl.gen import R

def registerGPNotifications():
    from grinch_progression.gui.impl.lobby.notifications.gp_style_reward import GpStyleReward
    gpStyleReward = (
     R.views.grinch_progression.lobby.notifications.GpStyleReward(), GpStyleReward)
    registerGamefaceNotifications({'GpStyleReward': gpStyleReward})