from frameworks.wulf import ViewModel

class ExtendedNodeStateFlags(ViewModel):
    __slots__ = ()
    DEFAULT = 1
    RESET_FINISHED_PARAGONS = 2
    LOCKED_BY_PARAGONS = 4

    def __init__(self, properties=0, commands=0):
        super(ExtendedNodeStateFlags, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ExtendedNodeStateFlags, self)._initialize()