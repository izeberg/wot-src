import typing
from frameworks.wulf import GuiApplication
from gui.impl.optimization_manager import GraphicsOptimizationManager
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    from frameworks.wulf.tutorial import Tutorial
    from frameworks.wulf.ui_logger import UILogger

class GuiLoader(IGuiLoader):
    __slots__ = ('__gui', '__graphicsOptimizationManager')

    def __init__(self):
        super(GuiLoader, self).__init__()
        self.__gui = GuiApplication()
        self.__graphicsOptimizationManager = GraphicsOptimizationManager()

    @property
    def resourceManager(self):
        return self.__gui.resourceManager

    @property
    def windowsManager(self):
        return self.__gui.windowsManager

    @property
    def systemLocale(self):
        return self.__gui.systemLocale

    @property
    def tutorial(self):
        return self.__gui.tutorial

    @property
    def uiLogger(self):
        return self.__gui.uiLogger

    @property
    def scale(self):
        return self.__gui.scale

    def init(self, tutorialModel, uiLoggerModel):
        self.__gui.init(tutorialModel, uiLoggerModel)
        self.__graphicsOptimizationManager.init(self.__gui.windowsManager, self.__gui.scale)

    def fini(self):
        self.__gui.destroy()
        self.__graphicsOptimizationManager.fini()