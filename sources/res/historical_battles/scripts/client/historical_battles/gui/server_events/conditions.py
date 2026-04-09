from gui.server_events.conditions import _ConditionsGroup as ConditionsGroup

def getTokenNeededCountInCondition(quest, tokenName, default=None):
    if quest is None:
        return default
    else:
        return _getTokenNeededCountInCondition(quest.accountReqs.getConditions().items, tokenName, default)


def _getTokenNeededCountInCondition(items, tokenName, default=None):
    item = _getTokenItemInCondition(items, tokenName)
    if item is None:
        return default
    else:
        return item.getNeededCount()


def getTokenReceivedCountInCondition(quest, tokenName, default=None):
    if quest is None:
        return default
    else:
        return _getTokenReceivedCountInCondition(quest.accountReqs.getConditions().items, tokenName, default)


def _getTokenReceivedCountInCondition(items, tokenName, default=None):
    item = _getTokenItemInCondition(items, tokenName)
    if item is None:
        return default
    else:
        return item.getReceivedCount()


def _getTokenItemInCondition(items, tokenName):
    res = None
    for item in items:
        if isinstance(item, ConditionsGroup):
            res = _getTokenItemInCondition(item.items, tokenName)
        elif item.getName() == 'token' and item.getID() == tokenName:
            return item

    return res