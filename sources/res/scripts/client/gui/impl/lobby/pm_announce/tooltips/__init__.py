from gui.impl.gen.view_models.views.lobby.pm_announce.tooltips.personal_missions_old_campaign_tooltip_rewards_model import RewardStatus

def getRewardStatusForOperation(operation):
    if operation.isCompleted():
        if operation.isAwardAchieved():
            return RewardStatus.COMPLETED
        return RewardStatus.AVAILABLE
    if operation.isAvailable().isValid:
        return RewardStatus.AVAILABLE
    return RewardStatus.LOCKED