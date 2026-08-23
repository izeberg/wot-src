from __future__ import absolute_import
from gui.shared.system_factory import registerAwardControllerHandlers, registerTokenQuestsSubFormatter
from journey_marathon.gui.game_control.award_handlers import JMDailyQuestHandler, JmAnniversaryPresentFormatter, JmAnniversaryPresentQuestHandler

def registerJMSystemHandlers():
    registerAwardControllerHandlers((
     JMDailyQuestHandler,
     JmAnniversaryPresentQuestHandler))
    registerTokenQuestsSubFormatter(JmAnniversaryPresentFormatter())