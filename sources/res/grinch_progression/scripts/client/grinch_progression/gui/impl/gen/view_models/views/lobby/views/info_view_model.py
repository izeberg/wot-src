from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.region_model import RegionModel

class InfoViewModel(ViewModel):
    __slots__ = ('onVideoClick', 'onClose', 'onShowAboutEvent', 'onViewLoaded')

    def __init__(self, properties=3, commands=4):
        super(InfoViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def region(self):
        return self._getViewModel(0)

    @staticmethod
    def getRegionType():
        return RegionModel

    def getEventStartDate(self):
        return self._getNumber(1)

    def setEventStartDate(self, value):
        self._setNumber(1, value)

    def getEventEndDate(self):
        return self._getNumber(2)

    def setEventEndDate(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(InfoViewModel, self)._initialize()
        self._addViewModelProperty('region', RegionModel())
        self._addNumberProperty('eventStartDate', 0)
        self._addNumberProperty('eventEndDate', 0)
        self.onVideoClick = self._addCommand('onVideoClick')
        self.onClose = self._addCommand('onClose')
        self.onShowAboutEvent = self._addCommand('onShowAboutEvent')
        self.onViewLoaded = self._addCommand('onViewLoaded')