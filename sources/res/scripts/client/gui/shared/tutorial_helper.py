from __future__ import absolute_import
from debug_utils import LOG_ERROR

def getTutorialGlobalStorage():
    try:
        from tutorial.control.context import GlobalStorage
    except ImportError:
        LOG_ERROR('Can not load package tutorial')
        GlobalStorage = None

    return GlobalStorage