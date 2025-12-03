from gui.impl.gen import R
from gui.shared.system_factory import registerGamefaceNotifications
from gui.impl.lobby.gf_notifications.holiday_ops.ho_sack_rare_loot import HOSackRareLoot
from gui.impl.lobby.gf_notifications.holiday_ops.ho_new_reward_kit import HONewRewardKit
from gui.impl.lobby.gf_notifications.holiday_ops.ho_dog_reminder import HODogReminder
from gui.impl.lobby.gf_notifications.holiday_ops.ho_dog_mission_completed import HODogMissionCompleted
from gui.impl.lobby.gf_notifications.holiday_ops.receiving_awards import HOReceivingAwards
from gui.impl.lobby.gf_notifications.holiday_ops.ho_challenge_rewards import HOChallengeRewards
from gui.impl.lobby.gf_notifications.holiday_ops.ho_quest_rewards import HOQuestReward
from gui.impl.lobby.gf_notifications.holiday_ops.ho_resources_reminder import HOResourcesReminder
from gui.impl.lobby.gf_notifications.holiday_ops.ho_piggy_bank import HOPiggyBankSingleReward, HOPiggyBankMultipleRewards
from gui.impl.lobby.gf_notifications.holiday_ops.ho_attached_3d_rewards import HOAttached3DRewards
from grinch_progression.gui.impl.lobby.notifications.gp_style_reward import GpStyleReward
registerGamefaceNotifications({'HOResourcesReminder': (
                         R.views.mono.holiday_ops.notifications.ho_resources_reminder(), HOResourcesReminder), 
   'HOSackRareLoot': (
                    R.views.mono.holiday_ops.notifications.ho_sack_rare_loot(), HOSackRareLoot), 
   'HONewRewardKit': (
                    R.views.mono.holiday_ops.notifications.ho_new_reward_kit(), HONewRewardKit), 
   'HODogReminder': (
                   R.views.mono.holiday_ops.notifications.ho_dog_reminder(), HODogReminder), 
   'HODogMissionCompleted': (
                           R.views.mono.holiday_ops.notifications.ho_dog_mission_completed(), HODogMissionCompleted), 
   'HOReceivingAwards': (
                       R.views.mono.holiday_ops.notifications.ho_receiving_awards(), HOReceivingAwards), 
   'HOChallengeRewards': (
                        R.views.mono.holiday_ops.notifications.ho_challenge_rewards(), HOChallengeRewards), 
   'HOQuestRewards': (
                    R.views.mono.holiday_ops.notifications.ho_assignments_rewards(), HOQuestReward), 
   'HOPiggyBankSingleReward': (
                             R.views.mono.holiday_ops.notifications.ho_piggy_bank_single_reward(), HOPiggyBankSingleReward), 
   'HOPiggyBankMultipleRewards': (
                                R.views.mono.holiday_ops.notifications.ho_piggy_bank_multiple_rewards(), HOPiggyBankMultipleRewards), 
   'HOAttached3DRewards': (
                         R.views.mono.holiday_ops.notifications.ho_attached3drewards(), HOAttached3DRewards), 
   'GpStyleReward': (
                   R.views.grinch_progression.mono.lobby.notifications.gp_style_reward(), GpStyleReward)})