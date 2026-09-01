from frameworks.wulf import ViewModel

class ModeSelectorTooltipsConstants(ViewModel):
    __slots__ = ()
    WHITE_TIGER_BATTLES_CALENDAR_TOOLTIP = 'whiteTigerCalendarTooltip'
    WHITE_TIGER_PROGRESSION_VIEW = 'whiteTigerProgressionView'

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorTooltipsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorTooltipsConstants, self)._initialize()