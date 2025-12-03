from messenger.formatters.service_channel import ClientSysMessageFormatter
from new_year.tamagotchi.sys_msg.decorators.tutorial import NyTutorialMsgDecorator

class NyTutorialFormatter(ClientSysMessageFormatter):

    def _getGuiSettings(self, data, key=None, priorityLevel=None, groupID=None):
        result = super(NyTutorialFormatter, self)._getGuiSettings(data, key, priorityLevel, groupID)
        result.decorator = NyTutorialMsgDecorator
        return result