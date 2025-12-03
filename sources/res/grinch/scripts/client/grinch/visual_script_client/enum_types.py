from typing import Any
from visual_script.type import VScriptEnum
from grinch_common.grinch_constants import MissileLauncherStatuses
from visual_script.misc import ASPECT

class MissileLauncherStateEnum(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return 'EMissileLauncherState'

    @classmethod
    def vs_enum(cls):
        return MissileLauncherStatuses

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.CLIENT]