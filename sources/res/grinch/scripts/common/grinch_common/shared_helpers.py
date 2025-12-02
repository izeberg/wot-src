import typing, weakref
if typing.TYPE_CHECKING:
    from typing import List, Tuple

def safeWeakProxy(entity):
    if type(entity).__name__ == 'weakproxy':
        return entity
    return weakref.proxy(entity)


def splitVehiclePresentPoints(presents):
    return (
     (presents or []).count(False), (presents or []).count(True))