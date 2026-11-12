from enum import Enum
FEATURE = 'newyear'
DEFAULT_TIME_LIMIT = 1.0

class Actions(str, Enum):
    OPEN = 'open'
    CLICK = 'click'
    CLOSE = 'close'


class Items(str, Enum):
    ENV_SWITCHER = 'env_switcher'
    QUESTS = 'quests'
    VOICEOVER_SWITCH = 'voiceover_switch'
    MACHINE = 'machine'
    MACHINE_BUY_BTN = 'machine_buy_btn'
    MACHINE_APPLY_BTN = 'machine_apply_btn'
    LEADERBOARD = 'leaderboard'
    WEEKLY_REWARDS = 'weekly_rewards'
    PET = 'pet'
    PET_REPEAT_ONBOARDING_BTN = 'pet_repeat_onboarding_btn'
    RAID_REPEAT_ONBOARDING_BTN = 'raid_repeat_onboarding_btn'
    EASTER_EGG_VIDEO = 'easter_egg_video'


class Views(str, Enum):
    HANGAR = 'hangar'
    SURPRISE_MACHINE = 'surprise_machine'
    LEADERBOARD = 'leaderboard'
    QUESTS = 'quests'
    PET = 'pet'
    PET_RAID = 'pet_raid'