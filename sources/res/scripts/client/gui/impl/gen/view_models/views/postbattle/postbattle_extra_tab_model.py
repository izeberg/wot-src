from frameworks.wulf import ViewModel

class PostbattleExtraTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(PostbattleExtraTabModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(PostbattleExtraTabModel, self)._initialize()