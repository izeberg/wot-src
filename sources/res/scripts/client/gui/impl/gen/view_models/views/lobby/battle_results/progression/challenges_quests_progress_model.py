from frameworks.wulf import ViewModel

class ChallengesQuestsProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(ChallengesQuestsProgressModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ChallengesQuestsProgressModel, self)._initialize()