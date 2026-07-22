from frameworks.wulf import ViewModel

class HeaderWidgetViewModel(ViewModel):
    __slots__ = ('onChangeLayout', )
    ARG_TOP = 'top'
    ARG_RIGHT = 'right'
    ARG_LEFT = 'left'

    def __init__(self, properties=0, commands=1):
        super(HeaderWidgetViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(HeaderWidgetViewModel, self)._initialize()
        self.onChangeLayout = self._addCommand('onChangeLayout')