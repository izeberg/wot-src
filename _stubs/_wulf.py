# Stubs Generator
# import _wulf
# <module '_wulf' (built-in)>

ARRAY = ValueType.ARRAY
BOOL = ValueType.BOOL
MAP = ValueType.MAP
NONE = ValueType.NONE
NUMBER = ValueType.NUMBER

class pybind11_object(object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = u'pybind11_builtins'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'pybind11_object'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyGuiApplication(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyGuiApplication'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def initialize(self, *args, **kwargs): pass
	def isInitialized(self, *args, **kwargs): pass
	resourceManager = property(lambda self: None)
	scale = property(lambda self: None)
	def setServerTimeCallback(self, *args, **kwargs): pass
	systemLocale = property(lambda self: None)
	tutorial = property(lambda self: None)
	uiLogger = property(lambda self: None)
	windowsManager = property(lambda self: None)


class PyObjectEntity(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectArray(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectArray'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addArray(self, *args, **kwargs): pass
	def addBool(self, *args, **kwargs): pass
	def addMap(self, *args, **kwargs): pass
	def addNumber(self, *args, **kwargs): pass
	def addReal(self, *args, **kwargs): pass
	def addResource(self, *args, **kwargs): pass
	def addString(self, *args, **kwargs): pass
	def addViewModel(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def invalidate(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeValue(self, *args, **kwargs): pass
	def removeValues(self, *args, **kwargs): pass
	def reserve(self, *args, **kwargs): pass
	def setArray(self, *args, **kwargs): pass
	def setBool(self, *args, **kwargs): pass
	def setMap(self, *args, **kwargs): pass
	def setNumber(self, *args, **kwargs): pass
	def setReal(self, *args, **kwargs): pass
	def setResource(self, *args, **kwargs): pass
	def setString(self, *args, **kwargs): pass
	def setViewModel(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectCommand(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectCommand'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def execute(self, *args, **kwargs): pass
	name = property(lambda self: None)
	object = property(lambda self: None)
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def rollback(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_ARRAY(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_ARRAY'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_BOOL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_BOOL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_MAP(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_MAP'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_NUMBER(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_NUMBER'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_REAL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_REAL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_RESOURCE(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_RESOURCE'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_STRING(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_STRING'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_NUMBER_VIEW_MODEL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_NUMBER_VIEW_MODEL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_ARRAY(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_ARRAY'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_BOOL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_BOOL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_MAP(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_MAP'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_NUMBER(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_NUMBER'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_REAL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_REAL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_RESOURCE(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_RESOURCE'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_STRING(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_STRING'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_RESOURCE_VIEW_MODEL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_RESOURCE_VIEW_MODEL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_ARRAY(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_ARRAY'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_BOOL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_BOOL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_MAP(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_MAP'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_NUMBER(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_NUMBER'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_REAL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_REAL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_RESOURCE(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_RESOURCE'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_STRING(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_STRING'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectMap_STRING_VIEW_MODEL(PyObjectMap):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMap_STRING_VIEW_MODEL'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def contains(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def getSize(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeItem(self, *args, **kwargs): pass
	def rollback(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectResourceManager(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectResourceManager'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def getImagePath(self, *args, **kwargs): pass
	def getSoundEffectId(self, *args, **kwargs): pass
	def getTranslatedPluralText(self, *args, **kwargs): pass
	def getTranslatedText(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectSystemLocale(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectSystemLocale'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def caseMap(self, *args, **kwargs): pass
	def getDateFormat(self, *args, **kwargs): pass
	def getNumberFormat(self, *args, **kwargs): pass
	def getRealFormat(self, *args, **kwargs): pass
	def getTimeFormat(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectTutorial(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectTutorial'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def getModel(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def setModel(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectUILogger(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectUILogger'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def getModel(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def setModel(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectView(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectView'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def checkViewFlags(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def getChild(self, *args, **kwargs): pass
	def getParent(self, *args, **kwargs): pass
	def getParentWindow(self, *args, **kwargs): pass
	def getSubView(self, *args, **kwargs): pass
	def getWindow(self, *args, **kwargs): pass
	layoutID = property(lambda self: None)
	def load(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeChild(self, *args, **kwargs): pass
	def setSubView(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass
	uniqueID = property(lambda self: None)
	viewFlags = property(lambda self: None)
	viewModel = property(lambda self: None)
	viewStatus = property(lambda self: None)


class PyObjectViewEvent(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectViewEvent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	bbox = property(lambda self: None)
	contentID = property(lambda self: None)
	decoratorID = property(lambda self: None)
	direction = property(lambda self: None)
	eventType = property(lambda self: None)
	def getArgument(self, *args, **kwargs): pass
	def hasArgument(self, *args, **kwargs): pass
	isOn = property(lambda self: None)
	mouse = property(lambda self: None)
	targetViewID = property(lambda self: None)


class PyObjectViewModel(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectViewModel'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addArrayField(self, *args, **kwargs): pass
	def addBoolField(self, *args, **kwargs): pass
	def addCommand(self, *args, **kwargs): pass
	def addField(self, *args, **kwargs): pass
	def addMapField(self, *args, **kwargs): pass
	def addNumberField(self, *args, **kwargs): pass
	def addRealField(self, *args, **kwargs): pass
	def addResourceField(self, *args, **kwargs): pass
	def addStringField(self, *args, **kwargs): pass
	def addViewModelField(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def getArray(self, *args, **kwargs): pass
	def getBool(self, *args, **kwargs): pass
	def getMap(self, *args, **kwargs): pass
	def getNumber(self, *args, **kwargs): pass
	def getReal(self, *args, **kwargs): pass
	def getResource(self, *args, **kwargs): pass
	def getString(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def getViewModel(self, *args, **kwargs): pass
	def hold(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def rollback(self, *args, **kwargs): pass
	def setArray(self, *args, **kwargs): pass
	def setBool(self, *args, **kwargs): pass
	def setMap(self, *args, **kwargs): pass
	def setNumber(self, *args, **kwargs): pass
	def setReal(self, *args, **kwargs): pass
	def setResource(self, *args, **kwargs): pass
	def setString(self, *args, **kwargs): pass
	def setValue(self, *args, **kwargs): pass
	def setViewModel(self, *args, **kwargs): pass
	def toString(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectViewSettings(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectViewSettings'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	flags = property(lambda self: None)
	layoutID = property(lambda self: None)
	model = property(lambda self: None)


class PyObjectWindow(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectWindow'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	areaID = property(lambda self: None)
	def bindPyObject(self, *args, **kwargs): pass
	calculateGlobalPosition = property(lambda self: None)
	def checkWindowFlags(self, *args, **kwargs): pass
	content = property(lambda self: None)
	decorator = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def hide(self, *args, **kwargs): pass
	def isHidden(self, *args, **kwargs): pass
	def isModal(self, *args, **kwargs): pass
	layer = property(lambda self: None)
	def load(self, *args, **kwargs): pass
	object = property(lambda self: None)
	parent = property(lambda self: None)
	def reload(self, *args, **kwargs): pass
	def resetLayer(self, *args, **kwargs): pass
	def setContent(self, *args, **kwargs): pass
	def setDecorator(self, *args, **kwargs): pass
	def setLayer(self, *args, **kwargs): pass
	def setParent(self, *args, **kwargs): pass
	def show(self, *args, **kwargs): pass
	def tryFocus(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass
	uniqueID = property(lambda self: None)
	windowFlags = property(lambda self: None)
	windowPosition = property(lambda self: None)
	windowSize = property(lambda self: None)
	windowStatus = property(lambda self: None)


class PyObjectWindowSettings(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectWindowSettings'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	areaID = property(lambda self: None)
	content = property(lambda self: None)
	decorator = property(lambda self: None)
	flags = property(lambda self: None)
	layer = property(lambda self: None)
	name = property(lambda self: None)
	ownerViewID = property(lambda self: None)
	parent = property(lambda self: None)


class PyObjectWindowsArea(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectWindowsArea'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addPyWindow(self, *args, **kwargs): pass
	areaID = property(lambda self: None)
	def bindPyObject(self, *args, **kwargs): pass
	def cascadePyWindow(self, *args, **kwargs): pass
	def centerPyWindow(self, *args, **kwargs): pass
	def getFirstPyWindow(self, *args, **kwargs): pass
	def getLastPyWindow(self, *args, **kwargs): pass
	def getNextPyNeighbor(self, *args, **kwargs): pass
	def getPreviousPyNeighbor(self, *args, **kwargs): pass
	def movePyWindow(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removePyWindow(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass


class PyObjectWindowsManager(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectWindowsManager'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addPyWindowsArea(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def findPyViews(self, *args, **kwargs): pass
	def findPyWindows(self, *args, **kwargs): pass
	def getMainWindow(self, *args, **kwargs): pass
	def getPyView(self, *args, **kwargs): pass
	def getPyViewsByLayoutId(self, *args, **kwargs): pass
	def getPyWindow(self, *args, **kwargs): pass
	def getPyWindowsArea(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def pyClear(self, *args, **kwargs): pass
	def removePyWindowsArea(self, *args, **kwargs): pass
	def unbindPyObject(self, *args, **kwargs): pass

REAL = ValueType.REAL
RESOURCE = ValueType.RESOURCE

class Resource(pybind11_object):
	def __call__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__qualname__ = 'Resource'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(self, *args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass

STRING = ValueType.STRING
VIEW_MODEL = ValueType.VIEW_MODEL

class ValueType(pybind11_object):
	ARRAY = ValueType.ARRAY
	BOOL = ValueType.BOOL
	MAP = ValueType.MAP
	NONE = ValueType.NONE
	NUMBER = ValueType.NUMBER
	REAL = ValueType.REAL
	RESOURCE = ValueType.RESOURCE
	STRING = ValueType.STRING
	VIEW_MODEL = ValueType.VIEW_MODEL
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  REAL\n\n  MAP\n\n  NONE\n\n  RESOURCE\n\n  STRING\n\n  VIEW_MODEL\n\n  BOOL\n\n  ARRAY\n\n  NUMBER'
	__entries = {u'REAL': (ValueType.REAL, None), u'MAP': (ValueType.MAP, None), u'NONE': (ValueType.NONE, None), u'RESOURCE': (ValueType.RESOURCE, None), u'STRING': (ValueType.STRING, None), u'VIEW_MODEL': (ValueType.VIEW_MODEL, None), u'BOOL': (ValueType.BOOL, None), u'ARRAY': (ValueType.ARRAY, None), u'NUMBER': (ValueType.NUMBER, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'REAL': ValueType.REAL, u'MAP': ValueType.MAP, u'NONE': ValueType.NONE, u'BOOL': ValueType.BOOL, u'STRING': ValueType.STRING, u'VIEW_MODEL': ValueType.VIEW_MODEL, u'RESOURCE': ValueType.RESOURCE, u'ARRAY': ValueType.ARRAY, u'NUMBER': ValueType.NUMBER}
	__module__ = '_wulf'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ValueType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)

__doc__ = None
__name__ = '_wulf'
__package__ = None
def caseMap(*args, **kwargs): pass
def getDateFormat(*args, **kwargs): pass
def getImagePath(*args, **kwargs): pass
def getLayoutPath(*args, **kwargs): pass
def getNumberFormat(*args, **kwargs): pass
def getRealFormat(*args, **kwargs): pass
def getSoundEffectId(*args, **kwargs): pass
def getTimeFormat(*args, **kwargs): pass
def getTranslatedKey(*args, **kwargs): pass
def getTranslatedPluralText(*args, **kwargs): pass
def getTranslatedPluralTextByResId(*args, **kwargs): pass
def getTranslatedText(*args, **kwargs): pass
def getTranslatedTextByResId(*args, **kwargs): pass
def isTranslatedKeyValid(*args, **kwargs): pass
def isTranslatedTextExisted(*args, **kwargs): pass