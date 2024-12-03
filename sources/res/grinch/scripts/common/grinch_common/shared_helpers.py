import weakref

def safeWeakProxy(entity):
    if type(entity).__name__ == 'weakproxy':
        return entity
    return weakref.proxy(entity)