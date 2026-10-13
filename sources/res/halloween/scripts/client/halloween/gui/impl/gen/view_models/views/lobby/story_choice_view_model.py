from frameworks.wulf import ViewModel

class StoryChoiceViewModel(ViewModel):
    __slots__ = ('onClose', 'onSelectSide')
    OPTION_1 = 'option_1'
    OPTION_2 = 'option_2'

    def __init__(self, properties=0, commands=2):
        super(StoryChoiceViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(StoryChoiceViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')
        self.onSelectSide = self._addCommand('onSelectSide')