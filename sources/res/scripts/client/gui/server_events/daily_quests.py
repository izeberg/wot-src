import logging
from functools import partial
import BigWorld, AccountCommands
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from gui.server_events.events_helpers import isPremiumPlusAccount
from gui.server_events.events_helpers import isRerollEnabled
from gui.shared.event_dispatcher import showDailyQuestsConfirmDialog
from gui.shared.gui_items.processors import Processor, makeSimpleTextSuccess, makeSimpleTextError
from gui.shared.gui_items.processors.plugins import SyncValidator, makeSuccess, makeError, MessageConfirmator
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
_logger = logging.getLogger(__name__)
_SYS_MESSAGE_DQ_R = R.strings.system_messages.daily_quests

class DQRerollEnabledValidator(SyncValidator):

    def _validate(self):
        if not isRerollEnabled():
            return makeError('reroll_disabled')
        return makeSuccess()


class DQRerollCooldown(SyncValidator):
    eventsCache = dependency.descriptor(IEventsCache)

    def _validate(self):
        if self.eventsCache.dailyQuests.isRerollInCooldown():
            return makeError('reroll_in_cooldown')
        return makeSuccess()


class DQRerollCooldownPrem(SyncValidator):
    eventsCache = dependency.descriptor(IEventsCache)

    def _validate(self):
        if self.eventsCache.dailyQuests.isRerollInCooldownPrem():
            return makeError('reroll_in_cooldown')
        return makeSuccess()


class DQPremiumAccount(SyncValidator):
    eventsCache = dependency.descriptor(IEventsCache)

    def _validate(self):
        if not isPremiumPlusAccount():
            return makeError()
        return makeSuccess()


class DQNotCompletedValidator(SyncValidator):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, levels, isEnabled=True):
        super(DQNotCompletedValidator, self).__init__(isEnabled)
        self.__levels = levels

    def _validate(self):
        if all(quest.isCompleted() for quest in self.eventsCache.getDailyQuests(filterLevels=self.__levels).itervalues()):
            return makeError('quest_is_already_completed')
        return makeSuccess()


class DQRerollConfirmator(MessageConfirmator):

    def __init__(self, rerollPremium):
        super(DQRerollConfirmator, self).__init__(None)
        self.__rerollPremium = rerollPremium
        return

    def _gfMakeMeta(self):
        return partial(showDailyQuestsConfirmDialog, self.__rerollPremium)


class DailyQuestReroll(Processor):
    eventsCache = dependency.descriptor(IEventsCache)
    __WAITING_TEXT = 'dailyQuests/waitReroll'

    def __init__(self, levels, rerollPremium):
        super(DailyQuestReroll, self).__init__(plugins=(
         DQRerollCooldown(isEnabled=not rerollPremium),
         DQRerollCooldownPrem(isEnabled=rerollPremium),
         DQPremiumAccount(isEnabled=rerollPremium),
         DQNotCompletedValidator(levels),
         DQRerollEnabledValidator(),
         DQRerollConfirmator(rerollPremium)))
        self._questsLevel = levels
        self._callback = None
        self._rerollPremium = rerollPremium
        return

    def _errorHandler(self, code, errStr='', ctx=None):
        Waiting.hide(self.__WAITING_TEXT)
        if self._rerollPremium:
            return makeSimpleTextError(_SYS_MESSAGE_DQ_R.premium.reroll.dyn(errStr), defTextRes=_SYS_MESSAGE_DQ_R.premium.reroll.unknown_error)
        return makeSimpleTextError(_SYS_MESSAGE_DQ_R.simple.reroll.dyn(errStr), defTextRes=_SYS_MESSAGE_DQ_R.simple.reroll.unknown_error)

    def _successHandler(self, code, ctx=None):
        Waiting.hide(self.__WAITING_TEXT)
        if self._rerollPremium:
            return makeSimpleTextSuccess(_SYS_MESSAGE_DQ_R.premium.reroll.success)
        return makeSimpleTextSuccess(_SYS_MESSAGE_DQ_R.simple.reroll.success)

    def _request(self, callback):
        Waiting.show(self.__WAITING_TEXT)
        _logger.debug('Make server request to reroll quest: %s', self._questsLevel)
        self._startListeningForResponse(callback)
        BigWorld.player().stats.rerollDailyQuest(self._questsLevel, self._onRerolCmdResponseReceived)

    def _onRerolCmdResponseReceived(self, resID):
        if not AccountCommands.isCodeValid(resID):
            self.__response(resID)

    def _startListeningForResponse(self, callback):
        self._callback = callback
        self.eventsCache.onSyncCompleted += self._onEventsSyncCompleted

    def _stopListeningForResponse(self):
        self._callback = None
        self.eventsCache.onSyncCompleted -= self._onEventsSyncCompleted
        return

    def _onEventsSyncCompleted(self):
        self.__response(AccountCommands.RES_SUCCESS)

    def __response(self, resID):
        self._response(resID, self._callback or (lambda *args: None), errStr=self.__resID2ErrStr(resID))
        self._stopListeningForResponse()

    def __resID2ErrStr(self, resID):
        if resID == AccountCommands.RES_COOLDOWN:
            return 'reroll_in_cooldown'
        return ''