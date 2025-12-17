from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class ResourceWellLoadingViewEvent(HasCtxEvent):
    LOAD = 'load'
    DESTROY = 'destroy'