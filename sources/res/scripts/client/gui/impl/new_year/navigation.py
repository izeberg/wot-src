import Event

class _NavigationState(object):

    def __init__(self):
        self.__currentObject = None
        self.__currentMenuName = None
        self.__isCloseMainViewInProcess = False
        return

    def getCurrentObject(self):
        return self.__currentObject

    def getCurrentMenuName(self):
        return self.__currentMenuName

    @property
    def isCloseMainViewInProcess(self):
        return self.__isCloseMainViewInProcess

    def setCloseMainViewInProcess(self, isClose):
        self.__isCloseMainViewInProcess = isClose

    def setCurrentObject(self, objectName):
        self.__currentObject = objectName

    def setCurrentMenuName(self, currentMenuName):
        self.__currentMenuName = currentMenuName


class NewYearNavigation(object):
    _navigationState = _NavigationState()
    onVSEObjectChanged = Event.Event()

    @classmethod
    def closeMainViewInProcess(cls, isClose):
        cls._navigationState.setCloseMainViewInProcess(isClose)

    @classmethod
    def getCurrentObject(cls):
        return cls._navigationState.getCurrentObject()

    @classmethod
    def setObject(cls, name):
        cls._navigationState.setCurrentObject(name)
        cls.onVSEObjectChanged(name)

    @classmethod
    def getCurrentMenuName(cls):
        return cls._navigationState.getCurrentMenuName()

    @classmethod
    def setCurrentMenuName(cls, name):
        return cls._navigationState.setCurrentMenuName(name)

    @classmethod
    def clear(cls):
        cls._navigationState.setCurrentMenuName(None)
        cls._navigationState.setCurrentObject(None)
        cls.onVSEObjectChanged(None)
        return

    @classmethod
    def getNavigationState(cls):
        return cls._navigationState