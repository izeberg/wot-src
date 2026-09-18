# Stubs Generator
# import Sound
# <module 'Sound' (built-in)>


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


class Audition2D(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Audition2D'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	isPlayer = property(lambda self: None)

DISTANCE_TO_CANNON = RTPCSourceType.DISTANCE_TO_CANNON
REMAINING_AMMO_CLIP_PERCENT = RTPCSourceType.REMAINING_AMMO_CLIP_PERCENT

class RTPCComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RTPCComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getRTPCs(self, *args, **kwargs): pass
	def setRTPC(self, *args, **kwargs): pass
	def setRTPCsBySourceType(self, *args, **kwargs): pass
	def trySetRTPC(self, *args, **kwargs): pass


class RTPCSourceType(pybind11_object):
	DISTANCE_TO_CANNON = RTPCSourceType.DISTANCE_TO_CANNON
	REMAINING_AMMO_CLIP_PERCENT = RTPCSourceType.REMAINING_AMMO_CLIP_PERCENT
	VALUE = RTPCSourceType.VALUE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  DISTANCE_TO_CANNON\n\n  VALUE\n\n  REMAINING_AMMO_CLIP_PERCENT'
	__entries = {u'DISTANCE_TO_CANNON': (RTPCSourceType.DISTANCE_TO_CANNON, None), u'VALUE': (RTPCSourceType.VALUE, None), u'REMAINING_AMMO_CLIP_PERCENT': (RTPCSourceType.REMAINING_AMMO_CLIP_PERCENT, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'REMAINING_AMMO_CLIP_PERCENT': RTPCSourceType.REMAINING_AMMO_CLIP_PERCENT, u'VALUE': RTPCSourceType.VALUE, u'DISTANCE_TO_CANNON': RTPCSourceType.DISTANCE_TO_CANNON}
	__module__ = 'Sound'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RTPCSourceType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class Sound2DComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Sound2DComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getEventName(self, *args, **kwargs): pass
	def isAutoStart(self, *args, **kwargs): pass
	def play(self, *args, **kwargs): pass


class Sound3DComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Sound3DComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPlaying(self, *args, **kwargs): pass
	objectName = property(lambda self: None)
	def play(self, *args, **kwargs): pass
	def stop(self, *args, **kwargs): pass


class SoundObject3DComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SoundObject3DComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def play(self, *args, **kwargs): pass
	def setRTPC(self, *args, **kwargs): pass
	def stop(self, *args, **kwargs): pass


class SoundZoneComponent(IComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Sound'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SoundZoneComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass

VALUE = RTPCSourceType.VALUE
__doc__ = None
__name__ = 'Sound'
__package__ = None
def getRecommendedPreset(*args, **kwargs): pass
def getSpatialAudioPreset(*args, **kwargs): pass
def reloadSoundEngine(*args, **kwargs): pass
def setSpatialAudioEnabled(*args, **kwargs): pass
def setSpatialAudioPreset(*args, **kwargs): pass