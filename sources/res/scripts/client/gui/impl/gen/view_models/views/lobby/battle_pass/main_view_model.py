from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class MainViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty('router', RouterModel())