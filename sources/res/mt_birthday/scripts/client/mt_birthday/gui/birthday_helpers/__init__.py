from helpers import dependency
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getLootBoxByID(lootboxID, itemsCache=None):
    lb = itemsCache.items.tokens.getLootBoxByID(lootboxID)
    if lb and lb.isVisible():
        return lb
    else:
        return


def isBirthdayOrdinaryQuest(questID):
    return questID.startswith('mt_birthday_quest_giver:quests')