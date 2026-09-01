

class IGeneratorMarker(object):

    def onGeneratorCapture(self, generatorIndex, progress, timeLeft, numInvaders):
        pass

    def onGeneratorStopCapture(self, generatorIndex):
        pass

    def onGeneratorLocked(self, generatorID, isLocked):
        pass