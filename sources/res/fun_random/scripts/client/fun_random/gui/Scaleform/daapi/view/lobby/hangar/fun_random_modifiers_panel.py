from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from fun_random.gui.impl.lobby.feature.fun_random_modifiers_panel_view import FunRandomModifiersPanel

class FunRandomModifiersPanelInject(InjectComponentAdaptor):
    __slots__ = ('__view', )

    def __init__(self):
        super(FunRandomModifiersPanelInject, self).__init__()
        self.__view = None
        return

    def _makeInjectView(self, *args):
        self.__view = FunRandomModifiersPanel()
        return self.__view

    def _dispose(self):
        self.__view = None
        super(FunRandomModifiersPanelInject, self)._dispose()
        return