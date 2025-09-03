# Stubs Generator
# import Input
# <module 'Input' (built-in)>


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


class InputAction(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputAction'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindEventReaction(self, *args, **kwargs): pass
	def unbindEventReaction(self, *args, **kwargs): pass


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


class InputSingleton(ISingleton):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputSingleton'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addAction(self, *args, **kwargs): pass
	def detach(self, *args, **kwargs): pass
	def handleKeyEvent(self, *args, **kwargs): pass
	def removeAction(self, *args, **kwargs): pass
	def setCommandMappingImpl(self, *args, **kwargs): pass


class InputTrigger(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTrigger'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerContinuous(InputTrigger):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerContinuous'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerDown(InputTriggerContinuous):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerDown'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerHold(InputTriggerContinuous):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerHold'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerHoldAndRelease(InputTriggerContinuous):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerHoldAndRelease'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerPressed(InputTrigger):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerPressed'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerPulse(InputTriggerContinuous):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerPulse'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerReleased(InputTrigger):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerReleased'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InputTriggerTap(InputTriggerContinuous):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'Input'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InputTriggerTap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass

LANGUAGE_CHS = Language.LANGUAGE_CHS
LANGUAGE_CHT = Language.LANGUAGE_CHT
LANGUAGE_JAPANESE = Language.LANGUAGE_JAPANESE
LANGUAGE_KOREAN = Language.LANGUAGE_KOREAN
LANGUAGE_NON_IME = Language.LANGUAGE_NON_IME

class Language(pybind11_object):
	LANGUAGE_CHS = Language.LANGUAGE_CHS
	LANGUAGE_CHT = Language.LANGUAGE_CHT
	LANGUAGE_JAPANESE = Language.LANGUAGE_JAPANESE
	LANGUAGE_KOREAN = Language.LANGUAGE_KOREAN
	LANGUAGE_NON_IME = Language.LANGUAGE_NON_IME
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  LANGUAGE_CHT\n\n  LANGUAGE_CHS\n\n  LANGUAGE_NON_IME\n\n  LANGUAGE_KOREAN\n\n  LANGUAGE_JAPANESE'
	__entries = {u'LANGUAGE_CHT': (Language.LANGUAGE_CHT, None), u'LANGUAGE_CHS': (Language.LANGUAGE_CHS, None), u'LANGUAGE_NON_IME': (Language.LANGUAGE_NON_IME, None), u'LANGUAGE_KOREAN': (Language.LANGUAGE_KOREAN, None), u'LANGUAGE_JAPANESE': (Language.LANGUAGE_JAPANESE, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'LANGUAGE_NON_IME': Language.LANGUAGE_NON_IME, u'LANGUAGE_CHS': Language.LANGUAGE_CHS, u'LANGUAGE_CHT': Language.LANGUAGE_CHT, u'LANGUAGE_KOREAN': Language.LANGUAGE_KOREAN, u'LANGUAGE_JAPANESE': Language.LANGUAGE_JAPANESE}
	__module__ = 'Input'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Language'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)

STATE_ENGLISH = State.STATE_ENGLISH
STATE_OFF = State.STATE_OFF
STATE_ON = State.STATE_ON

class State(pybind11_object):
	STATE_ENGLISH = State.STATE_ENGLISH
	STATE_OFF = State.STATE_OFF
	STATE_ON = State.STATE_ON
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  STATE_OFF\n\n  STATE_ON\n\n  STATE_ENGLISH'
	__entries = {u'STATE_OFF': (State.STATE_OFF, None), u'STATE_ON': (State.STATE_ON, None), u'STATE_ENGLISH': (State.STATE_ENGLISH, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'STATE_OFF': State.STATE_OFF, u'STATE_ON': State.STATE_ON, u'STATE_ENGLISH': State.STATE_ENGLISH}
	__module__ = 'Input'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'State'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class TriggerEvent(pybind11_object):
	Canceled = TriggerEvent.Canceled
	Completed = TriggerEvent.Completed
	OnProcess = TriggerEvent.OnProcess
	Started = TriggerEvent.Started
	Triggered = TriggerEvent.Triggered
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Started\n\n  Canceled\n\n  Completed\n\n  OnProcess\n\n  Triggered'
	__entries = {u'Started': (TriggerEvent.Started, None), u'Canceled': (TriggerEvent.Canceled, None), u'Completed': (TriggerEvent.Completed, None), u'OnProcess': (TriggerEvent.OnProcess, None), u'Triggered': (TriggerEvent.Triggered, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __ge__(self, *args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __gt__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __le__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	def __lt__(self, *args, **kwargs): pass
	__members__ = {u'Started': TriggerEvent.Started, u'Canceled': TriggerEvent.Canceled, u'Completed': TriggerEvent.Completed, u'OnProcess': TriggerEvent.OnProcess, u'Triggered': TriggerEvent.Triggered}
	__module__ = 'Input'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TriggerEvent'
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
__name__ = 'Input'
__package__ = None