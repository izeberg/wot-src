from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import NyIndicatorType

class NyPetTokenStepperTooltipModel(NyIndicatorType):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyPetTokenStepperTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(NyPetTokenStepperTooltipModel, self)._initialize()