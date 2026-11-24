from __future__ import absolute_import
from gui.shared.system_factory import CollectEventsManager
DOORS_AVAILABLE_LISTENER = 0
REWARD_WINDOW = 1
CALENDAR_WINDOW = 2
PURCHASE_DIALOG_VIEW = 3
QUEST_CALENDAR_FORMATTER = 4
__collectAdventEM = CollectEventsManager()

def registerDoorsAvailableListener(listener):

    def onCollect(ctx):
        ctx['doorsAvailableListener'] = listener

    __collectAdventEM.addListener(DOORS_AVAILABLE_LISTENER, onCollect)


def collectDoorsAvailableListener():
    return __collectAdventEM.handleEvent(DOORS_AVAILABLE_LISTENER, {}).get('doorsAvailableListener')


def registerRewardWindow(validator, viewType):

    def onCollect(ctx):
        ctx['rewardWindow'].extend([(validator, viewType)])

    __collectAdventEM.addListener(REWARD_WINDOW, onCollect)


def collectRewardWindow():
    return __collectAdventEM.handleEvent(REWARD_WINDOW, {'rewardWindow': []})['rewardWindow']


def registerCalendarWindow(validator, windowCls):

    def onCollect(ctx):
        ctx['calendarWindow'].extend([(validator, windowCls)])

    __collectAdventEM.addListener(CALENDAR_WINDOW, onCollect)


def collectCalendarWindow():
    return __collectAdventEM.handleEvent(CALENDAR_WINDOW, {'calendarWindow': []})['calendarWindow']


def registerPurchaseDialogView(validator, viewCls):

    def onCollect(ctx):
        ctx['purchaseDialogView'].extend([(validator, viewCls)])

    __collectAdventEM.addListener(PURCHASE_DIALOG_VIEW, onCollect)


def collectPurchaseDialogView():
    return __collectAdventEM.handleEvent(PURCHASE_DIALOG_VIEW, {'purchaseDialogView': []})['purchaseDialogView']


def registerQuestRewardFormatter(formatter):

    def onCollect(ctx):
        ctx['formatter'] = formatter

    __collectAdventEM.addListener(QUEST_CALENDAR_FORMATTER, onCollect)


def collectQuestRewardFormatter():
    return __collectAdventEM.handleEvent(QUEST_CALENDAR_FORMATTER, ctx={}).get('formatter')