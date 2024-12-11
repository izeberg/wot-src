from visual_script import ASPECT
from visual_script.block import Meta, Block
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
clientSelectableCameraObject, dependency, game_control, impl = dependencyImporter('ClientSelectableCameraObject', 'helpers.dependency', 'skeletons.gui.game_control', 'skeletons.gui.impl')

class NewYearMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return 'NewYear'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/arena'


class NavigateTo(Block, NewYearMeta):
    __festivityController = dependency.descriptor(game_control.IFestivityController)
    __newYearNavigation = dependency.descriptor(impl.INewYearNavigation)

    def __init__(self, *args, **kwargs):
        super(NavigateTo, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self._execute)
        self._customizationName = self._makeDataInputSlot('CustomizationName', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot('out')

    def _execute(self):
        if self.__festivityController.isEnabled():
            name = self._customizationName.getValue()
            self.__newYearNavigation.switchByAnchorName(name)
        self._out.call()

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]