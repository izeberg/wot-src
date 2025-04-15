import typing
from live_tags_constants import LIVE_TAG_TYPES
from visual_script.type import VScriptEnum

class LiveTagTypes(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return 'LiveTagTypesT'

    @classmethod
    def vs_enum(cls):
        return LIVE_TAG_TYPES