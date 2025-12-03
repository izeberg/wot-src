from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_widget_level_progress_model import NyWidgetLevelProgressModel

class HoMainWidgetModel(ViewModel):
    __slots__ = ('onGoToGladeView', 'onEditName')

    def __init__(self, properties=3, commands=2):
        super(HoMainWidgetModel, self).__init__(properties=properties, commands=commands)

    @property
    def widgetLevelProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getWidgetLevelProgressType():
        return NyWidgetLevelProgressModel

    def getHasEditButton(self):
        return self._getBool(1)

    def setHasEditButton(self, value):
        self._setBool(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(HoMainWidgetModel, self)._initialize()
        self._addViewModelProperty('widgetLevelProgress', NyWidgetLevelProgressModel())
        self._addBoolProperty('hasEditButton', True)
        self._addBoolProperty('isEnabled', False)
        self.onGoToGladeView = self._addCommand('onGoToGladeView')
        self.onEditName = self._addCommand('onEditName')