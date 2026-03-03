# Stubs Generator
# import Compound
# <module 'Compound' (built-in)>


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


class CompoundBasedComposerComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Compound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CompoundBasedComposerComponent'
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


class CompoundModel(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Compound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CompoundModel'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def collide(self, *args, **kwargs): pass
	def containsAttachment(self, *args, **kwargs): pass
	def findPartHandleByNode(self, *args, **kwargs): pass
	def getBoundsForPart(self, *args, **kwargs): pass
	def getBoundsForRoot(self, *args, **kwargs): pass
	def getNodeNames(self, *args, **kwargs): pass
	def getNodes(self, *args, **kwargs): pass
	def getPartGeometryLink(self, *args, **kwargs): pass
	def getWorldMatrixCalculator(self, *args, **kwargs): pass
	isInWorld = property(lambda self: None)
	def isValid(self, *args, **kwargs): pass
	matrix = property(lambda self: None)
	def node(self, *args, **kwargs): pass
	def nodeByHandle(self, *args, **kwargs): pass
	position = property(lambda self: None)
	def reset(self, *args, **kwargs): pass
	root = property(lambda self: None)
	def setPartBoundingBoxAttachNode(self, *args, **kwargs): pass
	def setPartProperties(self, *args, **kwargs): pass
	def setPartVisible(self, *args, **kwargs): pass
	def setPartVisibleByName(self, *args, **kwargs): pass
	def setWorldTransform(self, *args, **kwargs): pass
	def setupFashions(self, *args, **kwargs): pass
	def setupPartFashion(self, *args, **kwargs): pass
	skipColorPass = property(lambda self: None)
	skipEdgeDrawerPass = property(lambda self: None)
	skipShadowPass = property(lambda self: None)
	visible = property(lambda self: None)

DRIVE = NodeInteractType.DRIVE
FOLLOW = NodeInteractType.FOLLOW
INVALID_NODE = 4294967295L

class LocalTransformNodeFollower(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Compound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'LocalTransformNodeFollower'
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
	nodeHandle = property(lambda self: None)
	def valid(self, *args, **kwargs): pass


class MatrixProvider(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Math'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MatrixProvider'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class ModelNodeAdapter(MatrixProvider):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Compound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ModelNodeAdapter'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def attach(self, *args, **kwargs): pass
	def detach(self, *args, **kwargs): pass
	isDangling = property(lambda self: None)
	local = property(lambda self: None)
	localMatrix = property(lambda self: None)
	name = property(lambda self: None)
	parent = property(lambda self: None)
	position = property(lambda self: None)

NONE = NodeInteractType.NONE

class NodeInteractType(pybind11_object):
	DRIVE = NodeInteractType.DRIVE
	FOLLOW = NodeInteractType.FOLLOW
	NONE = NodeInteractType.NONE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  FOLLOW\n\n  NONE\n\n  DRIVE'
	__entries = {u'FOLLOW': (NodeInteractType.FOLLOW, None), u'NONE': (NodeInteractType.NONE, None), u'DRIVE': (NodeInteractType.DRIVE, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'FOLLOW': NodeInteractType.FOLLOW, u'NONE': NodeInteractType.NONE, u'DRIVE': NodeInteractType.DRIVE}
	__module__ = 'Compound'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NodeInteractType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class NodeLeaderComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Compound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NodeLeaderComponent'
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

ROOT_NODE = 0
__doc__ = None
__name__ = 'Compound'
__package__ = None
def dumpHierarchy(*args, **kwargs): pass
def onClientCompositionAboutToBeRemoved(*args, **kwargs): pass