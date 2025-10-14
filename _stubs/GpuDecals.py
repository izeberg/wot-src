# Stubs Generator
# import GpuDecals
# <module 'GpuDecals' (built-in)>


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


class AnimationConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AnimationConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	animationMask = property(lambda self: None)
	count = property(lambda self: None)
	duration = property(lambda self: None)
	enabled = property(lambda self: None)
	grid = property(lambda self: None)


class AnimationMask(pybind11_object):
	ALBEDO = AnimationMask.ALBEDO
	ALL = AnimationMask.ALL
	EMISSIVE = AnimationMask.EMISSIVE
	GLOSS_METALLIC = AnimationMask.GLOSS_METALLIC
	NONE = AnimationMask.NONE
	NORMAL = AnimationMask.NORMAL
	TEMPERATURE = AnimationMask.TEMPERATURE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  ALL\n\n  NONE\n\n  TEMPERATURE\n\n  NORMAL\n\n  GLOSS_METALLIC\n\n  EMISSIVE\n\n  ALBEDO'
	__entries = {u'ALL': (AnimationMask.ALL, None), u'NONE': (AnimationMask.NONE, None), u'TEMPERATURE': (AnimationMask.TEMPERATURE, None), u'NORMAL': (AnimationMask.NORMAL, None), u'GLOSS_METALLIC': (AnimationMask.GLOSS_METALLIC, None), u'EMISSIVE': (AnimationMask.EMISSIVE, None), u'ALBEDO': (AnimationMask.ALBEDO, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'ALL': AnimationMask.ALL, u'NONE': AnimationMask.NONE, u'TEMPERATURE': AnimationMask.TEMPERATURE, u'NORMAL': AnimationMask.NORMAL, u'GLOSS_METALLIC': AnimationMask.GLOSS_METALLIC, u'EMISSIVE': AnimationMask.EMISSIVE, u'ALBEDO': AnimationMask.ALBEDO}
	__module__ = 'GpuDecals'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AnimationMask'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ApplyMask(pybind11_object):
	ALBEDO = ApplyMask.ALBEDO
	ALL = ApplyMask.ALL
	BAKED_AO = ApplyMask.BAKED_AO
	EMISSIVE = ApplyMask.EMISSIVE
	GLOSS = ApplyMask.GLOSS
	METALLIC = ApplyMask.METALLIC
	NONE = ApplyMask.NONE
	NORMAL = ApplyMask.NORMAL
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  BAKED_AO\n\n  NONE\n\n  ALL\n\n  NORMAL\n\n  EMISSIVE\n\n  GLOSS\n\n  ALBEDO\n\n  METALLIC'
	__entries = {u'BAKED_AO': (ApplyMask.BAKED_AO, None), u'NONE': (ApplyMask.NONE, None), u'ALL': (ApplyMask.ALL, None), u'NORMAL': (ApplyMask.NORMAL, None), u'EMISSIVE': (ApplyMask.EMISSIVE, None), u'GLOSS': (ApplyMask.GLOSS, None), u'ALBEDO': (ApplyMask.ALBEDO, None), u'METALLIC': (ApplyMask.METALLIC, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'BAKED_AO': ApplyMask.BAKED_AO, u'ALL': ApplyMask.ALL, u'NONE': ApplyMask.NONE, u'METALLIC': ApplyMask.METALLIC, u'GLOSS': ApplyMask.GLOSS, u'NORMAL': ApplyMask.NORMAL, u'EMISSIVE': ApplyMask.EMISSIVE, u'ALBEDO': ApplyMask.ALBEDO}
	__module__ = 'GpuDecals'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ApplyMask'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class EmissionConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'EmissionConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	attenuationFactor = property(lambda self: None)
	emissionType = property(lambda self: None)
	enabled = property(lambda self: None)
	power = property(lambda self: None)


class EmissionType(pybind11_object):
	COLOR = EmissionType.COLOR
	TEMPERATURE = EmissionType.TEMPERATURE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  COLOR\n\n  TEMPERATURE'
	__entries = {u'COLOR': (EmissionType.COLOR, None), u'TEMPERATURE': (EmissionType.TEMPERATURE, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'COLOR': EmissionType.COLOR, u'TEMPERATURE': EmissionType.TEMPERATURE}
	__module__ = 'GpuDecals'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'EmissionType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class GeneralConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'GeneralConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	applyMask = property(lambda self: None)
	compoundOverlay = property(lambda self: None)
	cutoffAngle = property(lambda self: None)
	influenceMask = property(lambda self: None)
	projectionType = property(lambda self: None)
	tintColor = property(lambda self: None)


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


class GpuDecalComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'GpuDecalComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	animationConfig = property(lambda self: None)
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	emissionConfig = property(lambda self: None)
	generalConfig = property(lambda self: None)
	def id(self, *args, **kwargs): pass
	mapsConfig = property(lambda self: None)
	parallaxConfig = property(lambda self: None)
	def valid(self, *args, **kwargs): pass


class GpuDecalsReceiverComponent(PyComponentWrapperBase):
	def __cmp__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'GpuDecalsReceiverComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	blockIdx = property(lambda self: None)
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def id(self, *args, **kwargs): pass
	def valid(self, *args, **kwargs): pass

INVALID_BLOCK_IDX = 65535L
INVALID_DECAL_IDX = 65535L

class InfluenceMask(pybind11_object):
	ALL = InfluenceMask.ALL
	DYNAMIC = InfluenceMask.DYNAMIC
	FLORA = InfluenceMask.FLORA
	NONE = InfluenceMask.NONE
	STATIC = InfluenceMask.STATIC
	TERRAIN = InfluenceMask.TERRAIN
	TREE = InfluenceMask.TREE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  NONE\n\n  FLORA\n\n  STATIC\n\n  TERRAIN\n\n  DYNAMIC\n\n  TREE\n\n  ALL'
	__entries = {u'NONE': (InfluenceMask.NONE, None), u'FLORA': (InfluenceMask.FLORA, None), u'STATIC': (InfluenceMask.STATIC, None), u'TERRAIN': (InfluenceMask.TERRAIN, None), u'DYNAMIC': (InfluenceMask.DYNAMIC, None), u'TREE': (InfluenceMask.TREE, None), u'ALL': (InfluenceMask.ALL, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'ALL': InfluenceMask.ALL, u'FLORA': InfluenceMask.FLORA, u'STATIC': InfluenceMask.STATIC, u'TREE': InfluenceMask.TREE, u'DYNAMIC': InfluenceMask.DYNAMIC, u'TERRAIN': InfluenceMask.TERRAIN, u'NONE': InfluenceMask.NONE}
	__module__ = 'GpuDecals'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InfluenceMask'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class MapsConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MapsConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	albedo = property(lambda self: None)
	emissive = property(lambda self: None)
	glossMetallic = property(lambda self: None)
	normal = property(lambda self: None)
	temperature = property(lambda self: None)


class ParallaxConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'GpuDecals'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ParallaxConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	amplitude = property(lambda self: None)
	enabled = property(lambda self: None)
	offset = property(lambda self: None)


class ProjectionType(pybind11_object):
	CYLINDRICAL = ProjectionType.CYLINDRICAL
	ORTHONORMAL = ProjectionType.ORTHONORMAL
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  ORTHONORMAL\n\n  CYLINDRICAL'
	__entries = {u'ORTHONORMAL': (ProjectionType.ORTHONORMAL, None), u'CYLINDRICAL': (ProjectionType.CYLINDRICAL, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'ORTHONORMAL': ProjectionType.ORTHONORMAL, u'CYLINDRICAL': ProjectionType.CYLINDRICAL}
	__module__ = 'GpuDecals'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ProjectionType'
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
__name__ = 'GpuDecals'
__package__ = None