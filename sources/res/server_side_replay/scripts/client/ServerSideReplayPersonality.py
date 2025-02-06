from debug_utils import LOG_DEBUG
from server_side_replay.gui.Scaleform import registerLobbyHeaderTabs

def preInit():
    registerLobbyHeaderTabs()


def init():
    LOG_DEBUG('init', __name__)


def start():
    pass


def fini():
    pass