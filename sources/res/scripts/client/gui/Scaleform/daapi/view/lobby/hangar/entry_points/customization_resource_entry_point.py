from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta
from gui.impl.lobby.customization_resource.customization_resource_entry_point_view import CustomizationResourceEntryPointView

class CustomizationResourceEntryPoint(ResizableEntryPointMeta):

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)

    def _makeInjectView(self):
        self.__view = CustomizationResourceEntryPointView()
        return self.__view