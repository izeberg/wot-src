from datetime import timedelta
import calendar, time
from armory_yard_constants import COMPARE_TOKEN_OPERATIONS

def evaluatePrerequisiteToken(prerequisiteToken, tokenCount):
    tokenId = prerequisiteToken.get('id')
    expectedAmount = prerequisiteToken.get('expectedAmount')
    operationType = prerequisiteToken.get('operationType')
    if not (tokenId and expectedAmount is not None and operationType):
        return (False, 0)
    else:
        op = COMPARE_TOKEN_OPERATIONS[operationType]
        isBlocked = op(tokenCount, expectedAmount)
        diff = expectedAmount - tokenCount
        return (isBlocked, diff)


def getNextFreeRerollUpdateTimestamp(dailyFreeRerollUpdate, freeRerollDaysDelta, currentDatetime):
    datetimeObj = time.strptime(dailyFreeRerollUpdate, '%H:%M')
    nextRerollDatetime = currentDatetime.replace(hour=datetimeObj.tm_hour, minute=datetimeObj.tm_min, second=0, microsecond=0)
    if nextRerollDatetime < currentDatetime:
        nextRerollDatetime += timedelta(days=freeRerollDaysDelta)
    else:
        nextRerollDatetime += timedelta(days=freeRerollDaysDelta - 1)
    return int(calendar.timegm(nextRerollDatetime.utctimetuple()))