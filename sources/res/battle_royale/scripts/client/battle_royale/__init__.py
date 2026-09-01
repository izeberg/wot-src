from __future__ import absolute_import
from chat_shared import SYS_MESSAGE_TYPE
from battle_royale_progression_common.battle_royale_progression_constants import SM_TYPES

def registerSystemMessagesTypes():
    SYS_MESSAGE_TYPE.inject(SM_TYPES)


def initProgression():
    registerSystemMessagesTypes()
    from battle_royale.gui.game_control import registerBRProgressionAwardControllers
    registerBRProgressionAwardControllers()
    from battle_royale.notification import registerClientNotificationHandlers
    registerClientNotificationHandlers()
    from battle_royale.messenger.formatters import registerMessengerServerFormatters
    registerMessengerServerFormatters()