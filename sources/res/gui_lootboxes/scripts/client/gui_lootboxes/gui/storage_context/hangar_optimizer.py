import logging, AnimationSequence, BigWorld, MTWebBrowser
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.shared.event_dispatcher import showHangar
from helpers import dependency, isPlayerAccount
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared.utils import IHangarSpace
_logger = logging.getLogger(__name__)

class HangarOptimizer(object):
    __slots__ = ('__enabled', )
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __gui = dependency.descriptor(IGuiLoader)
    __appFactory = dependency.descriptor(IAppLoader)

    def __init__(self):
        super(HangarOptimizer, self).__init__()
        self.__enabled = False

    def enable(self):
        if not self.__enabled:
            self.__closeHangarViews()
            self.__setWorldState(enabled=False)
            self.__enabled = True

    def disable(self, needShowHangar=True):
        if self.__enabled:
            if needShowHangar:
                showHangar()
            self.__setWorldState(enabled=True)
            self.__enabled = False

    def clear(self):
        self.__setWorldState(enabled=True)
        self.__enabled = False

    @property
    def isEnabled(self):
        return self.__enabled

    def __setWorldState(self, enabled):
        if not isPlayerAccount():
            _logger.warning('HangarOptimizer: skip world state %s, not a player account', enabled)
            return
        if not self.__hangarSpace.spaceInited:
            _logger.warning('HangarOptimizer: skip world state %s, hangar space is not inited', enabled)
            return
        BigWorld.worldDrawEnabled(enabled)
        AnimationSequence.setEnableAnimationSequenceUpdate(enabled)
        MTWebBrowser.pauseExternalCache(not enabled)

    def __closeHangarViews(self):
        windows = self.__gui.windowsManager.findWindows(lambda w: w.layer == WindowLayer.SUB_VIEW)
        if not windows:
            return
        window = windows[0]
        if isinstance(window, SFWindow) and window.content and window.content.alias == VIEW_ALIAS.LOBBY_HANGAR:
            window.destroy()