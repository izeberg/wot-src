from account_helpers import AccountSettings
from account_helpers.AccountSettings import BR_UI_SECTION, BR_PROGRESSION_SEEN_QUESTS

def getLastSeenQuestData(questID):
    settings = AccountSettings.getUIFlag(BR_UI_SECTION)
    settings.setdefault(BR_PROGRESSION_SEEN_QUESTS, {}).setdefault(questID, (0, True))
    return settings[BR_PROGRESSION_SEEN_QUESTS][questID]


def setLastSeenQuestData(questID, questData):
    settings = AccountSettings.getUIFlag(BR_UI_SECTION)
    settings.setdefault(BR_PROGRESSION_SEEN_QUESTS, {})
    settings[BR_PROGRESSION_SEEN_QUESTS][questID] = questData
    AccountSettings.setUIFlag(BR_UI_SECTION, settings)