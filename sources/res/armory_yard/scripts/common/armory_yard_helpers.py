from datetime import timedelta
import calendar, time

def getNextFreeRerollUpdateTimestamp(dailyFreeRerollUpdate, freeRerollDaysDelta, currentDatetime):
    datetimeObj = time.strptime(dailyFreeRerollUpdate, '%H:%M')
    nextRerollDatetime = currentDatetime.replace(hour=datetimeObj.tm_hour, minute=datetimeObj.tm_min, second=0, microsecond=0)
    if nextRerollDatetime < currentDatetime:
        nextRerollDatetime += timedelta(days=freeRerollDaysDelta)
    else:
        nextRerollDatetime += timedelta(days=freeRerollDaysDelta - 1)
    return int(calendar.timegm(nextRerollDatetime.utctimetuple()))