# Stubs Generator
# import cgf_network
# <module 'cgf_network' (built-in)>

C_INVALID_NETWORK_OBJECT_ID = 0

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


class ISingleton(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'CGF'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ISingleton'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class ClientReplicableDataSingleton(ISingleton):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ClientReplicableDataSingleton'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def add(self, *args, **kwargs): pass
	def remove(self, *args, **kwargs): pass
	def update(self, *args, **kwargs): pass


class PyComponentWrapperBase(pybind11_object):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'CGF'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyComponentWrapperBase'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass


class NetworkComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NetworkComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	id = property(lambda self: None)
	def valid(self, *args, **kwargs): pass


class NetworkEntity(PyComponentWrapperBase):
	"entity" = property(lambda self: None)
	"isConnected" = property(lambda self: None)
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NetworkEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass


class NetworkKinematicTransformComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NetworkKinematicTransformComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass


class NetworkTransformComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NetworkTransformComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass


class ObjectCommand(pybind11_object):
	Add = ObjectCommand.Add
	Remove = ObjectCommand.Remove
	Update = ObjectCommand.Update
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Remove\n\n  Add\n\n  Update'
	__entries = {u'Remove': (ObjectCommand.Remove, None), u'Add': (ObjectCommand.Add, None), u'Update': (ObjectCommand.Update, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Add': ObjectCommand.Add, u'Remove': ObjectCommand.Remove, u'Update': ObjectCommand.Update}
	__module__ = 'cgf_network'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ObjectCommand'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class PredefinedReplicablesRegistrySingleton(ISingleton):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PredefinedReplicablesRegistrySingleton'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	hash = property(lambda self: None)


class RecreateMethod(pybind11_object):
	FromScratch = RecreateMethod.FromScratch
	PrefabChild = RecreateMethod.PrefabChild
	PrefabRoot = RecreateMethod.PrefabRoot
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  PrefabRoot\n\n  FromScratch\n\n  PrefabChild'
	__entries = {u'PrefabRoot': (RecreateMethod.PrefabRoot, None), u'FromScratch': (RecreateMethod.FromScratch, None), u'PrefabChild': (RecreateMethod.PrefabChild, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'PrefabRoot': RecreateMethod.PrefabRoot, u'FromScratch': RecreateMethod.FromScratch, u'PrefabChild': RecreateMethod.PrefabChild}
	__module__ = 'cgf_network'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RecreateMethod'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ReplicableComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReplicableComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	networkID = property(lambda self: None)
	def valid(self, *args, **kwargs): pass


class ReplicableStateVector(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	def __delitem__(self, *args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getitem__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	def __len__(self, *args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__qualname__ = 'ReplicableStateVector'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setitem__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def append(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def extend(self, *args, **kwargs): pass
	def insert(self, *args, **kwargs): pass
	def pop(self, *args, **kwargs): pass


class ReplicationPointComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReplicationPointComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	updates = property(lambda self: None)
	def valid(self, *args, **kwargs): pass


class ReplicationState(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReplicationState'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	active = property(lambda self: None)
	commandType = property(lambda self: None)
	networkID = property(lambda self: None)
	parentID = property(lambda self: None)
	prefabPath = property(lambda self: None)
	recreateMethod = property(lambda self: None)


class SpaceReplicationPointTag(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'cgf_network'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SpaceReplicationPointTag'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass

__doc__ = None
__name__ = 'cgf_network'
__package__ = None
def activateGameObject(*args, **kwargs): pass
def activateGameObjectByUniqueID(*args, **kwargs): pass
def createGameObject(*args, **kwargs): pass
def createReplicablePrefabInstance(*args, **kwargs): pass
def deactivateGameObject(*args, **kwargs): pass
def deactivateGameObjectByUniqueID(*args, **kwargs): pass
def findGameObject(*args, **kwargs): pass
def findReplicableComponentPropertiesByType(*args, **kwargs): pass
def getGameObject(*args, **kwargs): pass
def getGameObjectByNetworkID(*args, **kwargs): pass
def getNetworkID(*args, **kwargs): pass
def processCreateDynamicComponent(*args, **kwargs): pass
def processDestroyDynamicComponent(*args, **kwargs): pass
def removeGameObject(*args, **kwargs): pass
def removeGameObjectByUniqueID(*args, **kwargs): pass