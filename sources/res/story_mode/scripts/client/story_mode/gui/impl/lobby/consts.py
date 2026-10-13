from __future__ import absolute_import
from enum import IntEnum

class EntryPointStates(IntEnum):
    UNKNOWN = 0
    NEW_EVENT = 1
    TASKS_UNLOCKED = 2