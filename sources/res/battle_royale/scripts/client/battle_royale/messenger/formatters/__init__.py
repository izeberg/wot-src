from chat_shared import SYS_MESSAGE_TYPE
from gui.shared.system_factory import registerMessengerServerFormatter
from battle_royale.messenger.formatters.service_channel import BRProgressionSystemMessageFormatter
serverFormatters = {SYS_MESSAGE_TYPE.BRProgressionNotification.index(): BRProgressionSystemMessageFormatter()}

def registerMessengerServerFormatters():
    for sysMsgType, formatter in serverFormatters.iteritems():
        registerMessengerServerFormatter(sysMsgType, formatter)