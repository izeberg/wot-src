from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class DailyRewardViewModel(NotificationBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DailyRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(DailyRewardViewModel, self)._initialize()
        self._addNumberProperty('amount', 0)