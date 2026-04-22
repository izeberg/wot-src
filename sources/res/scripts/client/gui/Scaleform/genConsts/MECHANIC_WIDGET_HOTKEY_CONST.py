

class MECHANIC_WIDGET_HOTKEY_CONST(object):
    NORMAL = 'normal'
    WARNING = 'warning'
    ALERT = 'alert'
    INACTIVE = 'inactive'
    INVALID_KEY = 'invalidKey'
    HOT_KEY_STATES = [NORMAL, WARNING, ALERT, INACTIVE, INVALID_KEY]
    COMMAND_ACTIVATE = 'activate'
    ALTERNATIVE_ACTIVATE = 'altActivate'
    PREPARING = 'preparing'
    CANCELLED = 'cancelled'
    COMMANDS = [COMMAND_ACTIVATE, ALTERNATIVE_ACTIVATE, PREPARING, CANCELLED]