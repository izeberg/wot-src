from gui.shared.events import HasCtxEvent

class ResourceWellLoadingViewEvent(HasCtxEvent):
    LOAD = 'load'
    DESTROY = 'destroy'