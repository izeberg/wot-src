from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectMapViewModel(SelectOptionBaseItemViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SelectMapViewModel, self).__init__(properties=properties, commands=commands)

    def getText(self):
        return self._getString(4)

    def setText(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(SelectMapViewModel, self)._initialize()
        self._addStringProperty('text', '')