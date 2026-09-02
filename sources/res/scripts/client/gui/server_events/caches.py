

class _NavigationInfo(object):

    def __init__(self):
        self.tabID = None
        self._missionsTab = None
        self._marathonPrefix = None
        self._vehicleSelectorFilters = {}
        return

    def getMissionsTab(self):
        return self._missionsTab

    def getMarathonPrefix(self):
        return self._marathonPrefix

    def setMissionsTab(self, tabID):
        self._missionsTab = tabID

    def setMarathonPrefix(self, marathonPrefix):
        self._marathonPrefix = marathonPrefix

    def getVehicleSelectorFilters(self):
        return self._vehicleSelectorFilters

    def setVehicleSelectorFilters(self, filters):
        self._vehicleSelectorFilters = filters


_g_navInfo = None

def getNavInfo():
    global _g_navInfo
    if _g_navInfo is None:
        _g_navInfo = _NavigationInfo()
    return _g_navInfo


def clearNavInfo():
    global _g_navInfo
    _g_navInfo = None
    return