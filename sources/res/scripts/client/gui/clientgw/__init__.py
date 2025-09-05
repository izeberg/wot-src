from skeletons.gui.web import IWebController
__all__ = ('getWebServicesConfig', )

def getWebServicesConfig(manager):
    from gui.clientgw.web_controller import WebController
    ctrl = WebController()
    ctrl.init()
    manager.addInstance(IWebController, ctrl, finalizer='fini')