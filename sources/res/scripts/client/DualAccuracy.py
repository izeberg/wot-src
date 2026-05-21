import BigWorld
from DualAccuracyBase import DualAccuracyBase

class DualAccuracy(DualAccuracyBase):

    def __init__(self):
        super(DualAccuracy, self).__init__()
        self.__coolingEndTime = 0.0

    def getGunCoolingLeftTime(self):
        curTime = BigWorld.time()
        endTime = self.__coolingEndTime
        if endTime <= curTime:
            return 0.0
        return float(endTime - curTime)

    def onCoolingDataUpdated(self, coolingTime):
        self.__coolingEndTime = BigWorld.time() + coolingTime
        self.updateDualAccuracyData()