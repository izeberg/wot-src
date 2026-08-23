from __future__ import absolute_import
from frameworks.wulf import WindowFlags, WindowLayer, ViewSettings, ViewFlags
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_intro_view_model import JmIntroViewModel

class JmIntroWindow(WindowImpl):

    def __init__(self):
        super(JmIntroWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=JmIntroView())


class JmIntroView(ViewImpl):

    def __init__(self):
        super(JmIntroView, self).__init__(ViewSettings(R.views.journey_marathon.mono.lobby.intro_view(), ViewFlags.VIEW, JmIntroViewModel()))

    def _getEvents(self):
        return (
         (
          self.getViewModel().onClose, self.destroyWindow),)