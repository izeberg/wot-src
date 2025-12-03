import typing
if typing.TYPE_CHECKING:
    from gui.impl.pub import ViewImpl
    from frameworks.wulf import ViewEvent

class RegisteredTooltips(object):
    REGISTERED_SIMPLE_TOOLTIPS = {}
    REGISTERED_TOOLTIPS = {}

    @classmethod
    def registerLootBoxSimpleTooltipHandler(cls, tooltipResID, view):
        cls.REGISTERED_SIMPLE_TOOLTIPS[tooltipResID] = view

    @classmethod
    def registerLootBoxTooltipHandler(cls, tooltipResID, viewHandler):
        cls.REGISTERED_TOOLTIPS[tooltipResID] = viewHandler

    @classmethod
    def unregisterLootBoxTooltipHandler(cls, tooltipResID):
        if tooltipResID in cls.REGISTERED_TOOLTIPS:
            del cls.REGISTERED_TOOLTIPS[tooltipResID]
        if tooltipResID in cls.REGISTERED_SIMPLE_TOOLTIPS:
            del cls.REGISTERED_SIMPLE_TOOLTIPS[tooltipResID]


class LootBoxTooltipBaseHandler(object):

    def __init__(self, view):
        self.__view = view

    @property
    def view(self):
        return self.__view

    def __call__(self, event):
        raise NotImplementedError