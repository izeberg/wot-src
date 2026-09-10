# Stubs Generator
# import _wulf
# <module '_wulf' (built-in)>


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
	markersManager = property(lambda self: None)
	resourceManager = property(lambda self: None)
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


class PyObjectMarkersManager(PyObjectEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectMarkersManager'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addMarkerDynamic(self, *args, **kwargs): pass
	def addMarkerStatic(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	object = property(lambda self: None)
	def removeMarker(self, *args, **kwargs): pass
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
	def addNumberField(self, *args, **kwargs): pass
	def addRealField(self, *args, **kwargs): pass
	def addResourceField(self, *args, **kwargs): pass
	def addStringField(self, *args, **kwargs): pass
	def addViewModelField(self, *args, **kwargs): pass
	def bindPyObject(self, *args, **kwargs): pass
	def commit(self, *args, **kwargs): pass
	def getArray(self, *args, **kwargs): pass
	def getBool(self, *args, **kwargs): pass
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
	relatedResources = property(lambda self: None)


class PyObjectViewSettings__RelatedResourcesList(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getitem__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	def __len__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyObjectViewSettings::RelatedResourcesList'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setitem__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(self, *args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def append(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass


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


class PyResourceDescriptor(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = '_wulf'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyResourceDescriptor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	index = property(lambda self: None)
	type = property(lambda self: None)


class PyResourceType(pybind11_object):
	ANIMATION = PyResourceType.ANIMATION
	AREA = PyResourceType.AREA
	DYNAMIC_ID = PyResourceType.DYNAMIC_ID
	ENTRY = PyResourceType.ENTRY
	IMAGE = PyResourceType.IMAGE
	LAYOUT = PyResourceType.LAYOUT
	SOUND = PyResourceType.SOUND
	STRING = PyResourceType.STRING
	STYLE = PyResourceType.STYLE
	SUBTITLES = PyResourceType.SUBTITLES
	UNDEFINED = PyResourceType.UNDEFINED
	VIDEO = PyResourceType.VIDEO
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  SOUND\n\n  STYLE\n\n  ANIMATION\n\n  LAYOUT\n\n  STRING\n\n  AREA\n\n  ENTRY\n\n  IMAGE\n\n  DYNAMIC_ID\n\n  VIDEO\n\n  SUBTITLES\n\n  UNDEFINED'
	__entries = {u'SOUND': (PyResourceType.SOUND, None), u'STYLE': (PyResourceType.STYLE, None), u'ANIMATION': (PyResourceType.ANIMATION, None), u'LAYOUT': (PyResourceType.LAYOUT, None), u'STRING': (PyResourceType.STRING, None), u'AREA': (PyResourceType.AREA, None), u'ENTRY': (PyResourceType.ENTRY, None), u'IMAGE': (PyResourceType.IMAGE, None), u'DYNAMIC_ID': (PyResourceType.DYNAMIC_ID, None), u'VIDEO': (PyResourceType.VIDEO, None), u'SUBTITLES': (PyResourceType.SUBTITLES, None), u'UNDEFINED': (PyResourceType.UNDEFINED, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'SOUND': PyResourceType.SOUND, u'STYLE': PyResourceType.STYLE, u'ANIMATION': PyResourceType.ANIMATION, u'LAYOUT': PyResourceType.LAYOUT, u'STRING': PyResourceType.STRING, u'AREA': PyResourceType.AREA, u'ENTRY': PyResourceType.ENTRY, u'IMAGE': PyResourceType.IMAGE, u'DYNAMIC_ID': PyResourceType.DYNAMIC_ID, u'VIDEO': PyResourceType.VIDEO, u'SUBTITLES': PyResourceType.SUBTITLES, u'UNDEFINED': PyResourceType.UNDEFINED}
	__module__ = '_wulf'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyResourceType'
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