from __future__ import absolute_import
from fort_rush.helpers.utils import isFREventProgressionQuest
from messenger.formatters.service_channel_helpers import MessageData
from messenger.formatters.token_quest_subformatters import SyncTokenQuestsSubFormatter

class FortRushProgressionQuestFormatter(SyncTokenQuestsSubFormatter):

    def format(self, message, *args):
        return [
         MessageData(None, None)]

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return isFREventProgressionQuest(questID)