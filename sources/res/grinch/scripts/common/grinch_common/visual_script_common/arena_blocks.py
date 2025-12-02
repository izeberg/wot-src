import GenericComponents
from grinch_common.shared_helpers import safeWeakProxy
from visual_script.block import Block
from visual_script.cgf_blocks import CGFMeta
from visual_script.contexts.cgf_context import GameObjectWrapper
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE

class GrinchGenericComponentsFindSlots(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(GrinchGenericComponentsFindSlots, self).__init__(*args, **kwargs)
        self._gameObject = self._makeDataInputSlot('gameObject', SLOT_TYPE.GAME_OBJECT)
        self._name = self._makeDataInputSlot('name', SLOT_TYPE.STR)
        self._foundGameObject = self._makeDataOutputSlot('foundGameObject', SLOT_TYPE.GAME_OBJECT, self._execute)

    def _execute(self):
        vehicle = self._gameObject.getValue()
        name = self._name.getValue()
        gameObject = GenericComponents.findSlot(vehicle, name)
        goWrapper = GameObjectWrapper(gameObject)
        self._foundGameObject.setValue(safeWeakProxy(goWrapper))

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]