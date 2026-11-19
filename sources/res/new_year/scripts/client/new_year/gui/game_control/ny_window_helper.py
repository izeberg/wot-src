from new_year.skeletons.new_year import INyWindowHelper

class NyWindowHelper(INyWindowHelper):
    __slots__ = ('__windowLocks', )

    def __init__(self):
        self.__windowLocks = set()

    def isLocked(self, windowTag):
        return windowTag in self.__windowLocks

    def lock(self, windowTag):
        self.__windowLocks.add(windowTag)

    def unlock(self, windowTag):
        self.__windowLocks.remove(windowTag)