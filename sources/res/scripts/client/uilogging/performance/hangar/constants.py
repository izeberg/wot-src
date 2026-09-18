from __future__ import absolute_import
from enum import Enum

class Features(str, Enum):
    METRICS = 'hangar_metrics'


class Groups(str, Enum):
    SPACE = 'space'
    VIEWS = 'views'


class LogActions(str, Enum):
    SPACE_DISPOSED = 'space_disposed'