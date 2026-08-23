from __future__ import absolute_import
from constants import HAS_DEV_RESOURCES
from debug_utils import LOG_CURRENT_EXCEPTION
dev_actions = None
if HAS_DEV_RESOURCES:
    try:
        from journey_marathon.gui.development import dev_actions
        dev_actions.init()
    except ImportError:
        LOG_CURRENT_EXCEPTION()