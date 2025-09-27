from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class ModeSelectorPortalWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ModeSelectorPortalWidgetModel, self).__init__(properties=properties, commands=commands)

    def getPerformance(self):
        return self._getNumber(1)

    def setPerformance(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(ModeSelectorPortalWidgetModel, self)._initialize()
        self._addNumberProperty('performance', 0)