from debug_utils import LOG_WARNING
from gui.impl import backport
from gui.impl.gen import R
from items.vehicles import getVehicleType
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData

class BattleRoyaletSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'BattleRoyaletSystemMessageFormatter'

    def format(self, message, *args):
        vehTypeCD = message.data.get('vehTypeCD', -1)
        if vehTypeCD < 1:
            LOG_WARNING('Cannot convert invalid vehTypeCD to vehicle user name.')
            return []
        vehUserName = getVehicleType(vehTypeCD).userString
        msg = R.strings.br_texts.serviceChannelMessages
        header = backport.text(msg.header())
        body = backport.text(msg.body(), vehicle=vehUserName)
        formatted = g_settings.msgTemplates.format(self.__TEMPLATE, {'header': header, 'body': body})
        settings = self._getGuiSettings(message, self.__TEMPLATE)
        return [
         MessageData(formatted, settings)]