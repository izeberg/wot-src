from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.ny_decoration_slot_model import NyDecorationSlotModel

class NyBreakDecorationSlotModel(NyDecorationSlotModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(NyBreakDecorationSlotModel, self).__init__(properties=properties, commands=commands)

    def getIsNew(self):
        return self._getBool(9)

    def setIsNew(self, value):
        self._setBool(9, value)

    def _initialize(self):
        super(NyBreakDecorationSlotModel, self)._initialize()
        self._addBoolProperty('isNew', False)