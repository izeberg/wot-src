

class TankItem(list):
    _ITEM_COUNT = 2

    def __init__(self):
        super(TankItem, self).__init__([0] * TankItem._ITEM_COUNT)

    def updateVoiceoverTime(self, value):
        self[0] = max(value, self[0])

    def increaseClickCount(self):
        self[1] += 1