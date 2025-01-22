import typing
from CurrentVehicle import g_currentVehicle
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class _BobVehicle(object):
    __slots__ = ('__customVehicle', )

    def __init__(self):
        super(_BobVehicle, self).__init__()
        self.__customVehicle = None
        return

    def setCustomVehicle(self, value):
        self.__customVehicle = value

    @property
    def defaultItem(self):
        return g_currentVehicle.item

    @property
    def item(self):
        return self.__customVehicle

    def isPresent(self):
        return self.item is not None

    def clear(self):
        self.__customVehicle = None
        return


g_bobVehicle = _BobVehicle()