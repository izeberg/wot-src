import typing
from visual_script.type import VScriptEnum
from visual_script import ASPECT
from story_mode_common.story_mode_constants import AwarenessState

class SMAwarenessStateEnum(VScriptEnum):

    @classmethod
    def slotType(cls):
        return 'ESMAwarenessStateEnum'

    @classmethod
    def vs_enum(cls):
        return AwarenessState

    @classmethod
    def vs_aspects(cls):
        return [
         ASPECT.CLIENT]