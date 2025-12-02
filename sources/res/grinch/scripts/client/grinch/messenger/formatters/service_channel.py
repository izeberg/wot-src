import logging
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from grinch_common.grinch_constants import EventStates
from messenger.formatters.service_channel_helpers import MessageData
_logger = logging.getLogger(__name__)

class GrinchBattleResultsFormatter(BattleResultsFormatter):

    def _prepareFormatData(self, message):
        _, ctx = super(GrinchBattleResultsFormatter, self)._prepareFormatData(message)
        ctx['progressionPoints'] = self.__makeTotalPointsString(message)
        return ('GrinchBattleResults', ctx)

    @staticmethod
    def __makeTotalPointsString(message):
        tokens = message.data.get('tokens', {})
        gp = dependency.instance(IGrinchProgressionController)
        grinchProgressionTokens = tokens.get(gp.token, {})
        totalValue = message.data.get('grinch/progressionPoints', 0) + grinchProgressionTokens.get('count', 0)
        return backport.getIntegralFormat(totalValue)


class GrinchCongratulationsMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'GrinchCongratulationsMessage'

    def format(self, message, *args):
        medal = message.get('medal', None)
        if not medal:
            return []
        else:
            formatted = g_settings.msgTemplates.format(self.__TEMPLATE, ctx={'medal': backport.text(R.strings.achievements.dyn(medal)())})
            return [MessageData(formatted, self._getGuiSettings(message, self.__TEMPLATE))]


class GrinchEventStateMessageFormatter(ServiceChannelFormatter):
    _grinchProgressionCtrl = dependency.descriptor(IGrinchProgressionController)
    __TEMPLATES = {EventStates.SUSPEND: 'GrinchEventSuspendedMessage', 
       EventStates.RESUME: 'GrinchEventResumedMessage', 
       EventStates.BATTLES_FINISH: 'GrinchBattlesFinishMessage', 
       EventStates.START: 'GrinchEventStartMessage', 
       EventStates.ENDED: 'GrinchEventEndedMessage'}

    def format(self, message, *args):
        state = message.get('state', None)
        if state is None:
            _logger.error('[GrinchEventStateMessageFormatter] message.state is missing')
            return []
        else:
            template = self.__TEMPLATES.get(state, None)
            if template is None:
                _logger.error('[GrinchEventStateMessageFormatter] Missing template for state %s', state)
                return []
            ctx = {}
            if state == EventStates.BATTLES_FINISH:
                dateValue = self._grinchProgressionCtrl.getEndEventDate()
                ctx.update({'date': backport.getShortDateFormat(dateValue)})
            formatted = g_settings.msgTemplates.format(template, ctx=ctx)
            return [MessageData(formatted, self._getGuiSettings(message, template))]