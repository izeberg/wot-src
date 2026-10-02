SESSION_PROGRESS_REWARDS_PDATA_KEY = 'sessionProgressRewards'
CURRENT_STEP_PDATA_KEY = 'currentStep'
LAST_REWARD_GAME_DAY_PDATA_KEY = 'lastRewardGameDay'
AB_TEST_FEATURE_NAME = 'rewards'
AB_TEST_DEFAULT_GROUP_NAME = 'default'

def sessionProgressRewardsInitialData():
    return {CURRENT_STEP_PDATA_KEY: 0, 
       LAST_REWARD_GAME_DAY_PDATA_KEY: 0}