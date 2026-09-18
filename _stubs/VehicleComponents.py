# Stubs Generator
# import VehicleComponents
# <module 'VehicleComponents' (built-in)>


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


class IComponent(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'CGF'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'IComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class AreaVehiclesPrefabsSpawnerComponent(IComponent):
	ANY = TeamFilters.ANY
	OTHER = TeamFilters.OTHER
	OWN = TeamFilters.OWN
	
	class TeamFilters(pybind11_object):
		ANY = TeamFilters.ANY
		OTHER = TeamFilters.OTHER
		OWN = TeamFilters.OWN
		def __delattr__(*args, **kwargs): pass
		__doc__ = u'Members:\n\n  ANY\n\n  OTHER\n\n  OWN'
		__entries = {u'ANY': (TeamFilters.ANY, None), u'OTHER': (TeamFilters.OTHER, None), u'OWN': (TeamFilters.OWN, None)}
		def __eq__(self, *args, **kwargs): pass
		def __format__(*args, **kwargs): pass
		def __getattribute__(*args, **kwargs): pass
		def __getstate__(self, *args, **kwargs): pass
		def __hash__(self, *args, **kwargs): pass
		def __init__(self, *args, **kwargs): pass
		def __int__(self, *args, **kwargs): pass
		def __long__(self, *args, **kwargs): pass
		__members__ = {u'ANY': TeamFilters.ANY, u'OWN': TeamFilters.OWN, u'OTHER': TeamFilters.OTHER}
		__module__ = 'VehicleComponents'
		def __ne__(self, *args, **kwargs): pass
		def __new__(*args, **kwargs): pass
		__qualname__ = u'AreaVehiclesPrefabsSpawnerComponent.TeamFilters'
		def __reduce__(*args, **kwargs): pass
		def __reduce_ex__(*args, **kwargs): pass
		def __repr__(self, *args, **kwargs): pass
		def __setattr__(*args, **kwargs): pass
		def __setstate__(self, *args, **kwargs): pass
		def __sizeof__(*args, **kwargs): pass
		def __str__(*args, **kwargs): pass
		def __subclasshook__(*args, **kwargs): pass
		name = property(lambda self: None)
	
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AreaVehiclesPrefabsSpawnerComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	excludeSelf = property(lambda self: None)
	def isSpawnOnEnemies(self, *args, **kwargs): pass
	def isSpawnOnTeammates(self, *args, **kwargs): pass
	maxCount = property(lambda self: None)
	radius = property(lambda self: None)
	standardSpawner = property(lambda self: None)
	teamFilter = property(lambda self: None)
	transform = property(lambda self: None)
	uniqueSpawner = property(lambda self: None)
	useStandardSpawner = property(lambda self: None)
	useUniqueSpawner = property(lambda self: None)


class VehicleDamageResist(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleDamageResist'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	attackReason = property(lambda self: None)
	target = property(lambda self: None)
	value = property(lambda self: None)


class VehicleDamageResistsComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleDamageResistsComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	resistReason = property(lambda self: None)
	resists = property(lambda self: None)


class VehicleDamageResistsVector(pybind11_object):
	def __contains__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	def __delitem__(self, *args, **kwargs): pass
	__doc__ = None
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getitem__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	def __len__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__qualname__ = 'VehicleDamageResistsVector'
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
	def count(self, *args, **kwargs): pass
	def extend(self, *args, **kwargs): pass
	def insert(self, *args, **kwargs): pass
	def pop(self, *args, **kwargs): pass
	def remove(self, *args, **kwargs): pass


class VehicleLimitAttributeComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleLimitAttributeComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	modifiers = property(lambda self: None)


class VehiclePrefabParameters(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehiclePrefabParameters'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	path = property(lambda self: None)


class VehiclePrefabParametersVector(pybind11_object):
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
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	
	class PyCapsule(object):
		def __delattr__(*args, **kwargs): pass
		__doc__ = 'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
		def __format__(*args, **kwargs): pass
		def __getattribute__(*args, **kwargs): pass
		def __hash__(*args, **kwargs): pass
		def __init__(*args, **kwargs): pass
		def __new__(*args, **kwargs): pass
		def __reduce__(*args, **kwargs): pass
		def __reduce_ex__(*args, **kwargs): pass
		def __repr__(*args, **kwargs): pass
		def __setattr__(*args, **kwargs): pass
		def __sizeof__(*args, **kwargs): pass
		def __str__(*args, **kwargs): pass
		def __subclasshook__(*args, **kwargs): pass
	
	__pybind11_module_local_v5_msvc__ = PyCapsule()
	__qualname__ = 'VehiclePrefabParametersVector'
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


class VehiclePrefabsFilter(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehiclePrefabsFilter'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)
	prefabs = property(lambda self: None)


class VehiclePrefabsFilterVector(pybind11_object):
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
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__pybind11_module_local_v5_msvc__ = PyCapsule()
	__qualname__ = 'VehiclePrefabsFilterVector'
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


class VehiclePrefabsSpawner(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'VehicleComponents'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehiclePrefabsSpawner'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	defaultPrefabs = property(lambda self: None)
	filters = property(lambda self: None)
	name = property(lambda self: None)

__doc__ = None
__name__ = 'VehicleComponents'
__package__ = None