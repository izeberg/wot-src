from __future__ import absolute_import
from helpers import dependency
from gui.impl.pub import ViewImpl
from gui.prb_control.entities.listener import IGlobalListener
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController

class BaseView(ViewImpl, IGlobalListener):
    DESTROY_ON_EVENT_DISABLED = True
    _wtController = dependency.descriptor(IWhiteTigerController)

    def onPrbEntitySwitched(self):
        if not self._wtController.isAvailable():
            self._onClose()

    @property
    def isHiddenMenu(self):
        return True

    def _onLoading(self, *args, **kwargs):
        super(BaseView, self)._onLoading(*args, **kwargs)
        self.startGlobalListening()

    def _finalize(self):
        self.stopGlobalListening()
        super(BaseView, self)._finalize()

    def _onClose(self):
        self.destroyWindow()