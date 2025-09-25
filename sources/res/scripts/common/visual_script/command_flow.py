from visual_script import ASPECT
from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE

class _CommandFlowMeta(Meta):

    @classmethod
    def blockCategory(cls):
        return 'Command Flow'

    @classmethod
    def blockColor(cls):
        return 4367861

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/cycle'

    @classmethod
    def blockAspects(cls):
        return ASPECT.ALL


class MutexGate(Block, _CommandFlowMeta):

    def __init__(self, *args, **kwargs):
        super(MutexGate, self).__init__(*args, **kwargs)
        self._input = self._makeEventInputSlot('in', self.tryActivate)
        self._lockSlot = self._makeEventInputSlot('lock', self.lock)
        self._releaseSlot = self._makeEventInputSlot('release', self.release)
        self._lockedAtStart = self._makeDataInputSlot('lockedAtStart', SLOT_TYPE.BOOL)
        self._outSlot = self._makeEventOutputSlot('out')
        self._isLocked = False
        self._isReady = False

    def onStartScript(self):
        self._isLocked = self._lockedAtStart.getValue()

    def lock(self):
        self._isLocked = False

    def tryActivate(self):
        if self._isLocked:
            self._outSlot.call()
        else:
            self._isReady = True

    def release(self):
        if self._isReady:
            self._outSlot.call()
        self._isReady = False