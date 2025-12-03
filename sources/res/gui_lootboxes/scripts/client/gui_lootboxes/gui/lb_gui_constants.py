from enum import IntEnum
from constants_utils import ConstInjector
from messenger import m_constants

class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    LB_OPENED = 30001


SHOW_GIFT_PHRASE_TAG = 'showGiftPhrase'
GLOW = 'glow'

class TRIGGER_HINT_STATES(IntEnum):
    HIDE = 0
    HAVE_TO_SHOW = 1
    SHOWN = 2