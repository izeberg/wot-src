from constants import IS_DEVELOPMENT
DEFAULT_ASSETS_PACK = 'undefined'
DEFAULT_SETTINGS_KEY = 'undefined'
DEFAULT_PRIORITY = 0
FUN_EVENT_ID_KEY = 'funEventID'
UNKNOWN_EVENT_ID = 0
UNKNOWN_EVENT_NAME = 'unknown_event'
UNKNOWN_WWISE_REMAPPING = 'unknownRemapping'

class FunSubModeImpl(object):
    DEV_TEST = 0
    DEFAULT = 1
    QUICK_FIRE_GUNS = 2
    ALL = (DEFAULT, QUICK_FIRE_GUNS) + ((DEV_TEST,) if IS_DEVELOPMENT else ())


class FunProgressionCondition(object):
    BATTLES = 'battles'
    TOP = 'top'
    WIN = 'win'
    ALL = (BATTLES, TOP, WIN)