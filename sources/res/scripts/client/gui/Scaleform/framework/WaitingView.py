import Keys
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui import InputHandler
from gui.Scaleform.daapi.view.meta.WaitingViewMeta import WaitingViewMeta
from gui.impl import backport
from skeletons.gui.app_loader import IWaitingWidget

class WaitingView(WaitingViewMeta, IWaitingWidget):

    def __init__(self):
        super(WaitingView, self).__init__()
        InputHandler.g_instance.onKeyUp += self.handleKeyUpEvent
        self.__callback = None
        return

    def handleKeyUpEvent(self, event):
        if event.key == Keys.KEY_ESCAPE:
            if self.__callback:
                self.__callback()

    def destroy(self):
        self.__callback = None
        InputHandler.g_instance.onKeyUp -= self.handleKeyUpEvent
        super(WaitingView, self).destroy()
        return

    def setCallback(self, value=None):
        self.__callback = value

    def cancelCallback(self):
        self.__callback = None
        return

    def showWaiting(self, messageID, softStart=False, showBg=True):
        self.as_showWaitingS(backport.text(messageID), softStart, showBg)

    def hideWaiting(self):
        self.__callback = None
        try:
            self.as_hideWaitingS()
        except Exception:
            LOG_ERROR('There is error while trying to close waiting')
            LOG_CURRENT_EXCEPTION()

        return

    def setBackgroundImage(self, image):
        if image:
            self.as_showBackgroundImgS(image)