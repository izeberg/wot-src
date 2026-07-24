# Stubs Generator
# import AI_Common.UtilityCommon
# <module 'AI_Common' (built-in)>


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


class AIBlackBoard(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIBlackBoard'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def add(self, *args, **kwargs): pass
	def addMultiple(self, *args, **kwargs): pass
	def delete(self, *args, **kwargs): pass
	def exist(self, *args, **kwargs): pass
	def read(self, *args, **kwargs): pass
	def write(self, *args, **kwargs): pass


class AICircling(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AICircling'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getCirclingPosition(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	onDebugPoints = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def selectTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass


class AICirclingParams(pybind11_object):
	ALLIES_FLANK_SCORE = property(lambda self: None)
	BONUS_CURRENT_TARGET = property(lambda self: None)
	CIRCLING_RADIUSES = property(lambda self: None)
	CIRCLING_RADIUS_SCORES = property(lambda self: None)
	CIRCLING_TARGET_SELECTION_THRESHOLD = property(lambda self: None)
	CIRCLING_TARGET_STICKNESS_TIME = property(lambda self: None)
	CIRCLING_TOLERANCE = property(lambda self: None)
	CIRCLING_TOLERANCE_SQR = property(lambda self: None)
	CURVATURE_PATH_FACTOR = property(lambda self: None)
	HORIZONTAL_REACH_TOLERANCE = property(lambda self: None)
	HORIZONTAL_REACH_TOLERANCE_SQR = property(lambda self: None)
	HULL_DIRECTION_SCORE = property(lambda self: None)
	INCOMPLETE_PATH_RANGEPENALTY = property(lambda self: None)
	MAX_CIRCLING_RADIUS = property(lambda self: None)
	MAX_RADIUS_SCORE = property(lambda self: None)
	MID_CIRCLING_RADIUS = property(lambda self: None)
	MID_RADIUS_SCORE = property(lambda self: None)
	MIN_CIRCLING_RADIUS = property(lambda self: None)
	MIN_RADIUS_SCORE = property(lambda self: None)
	MOVEMENT_DIRECTION_SCORE = property(lambda self: None)
	NAVMESH_TOL = property(lambda self: None)
	OCCUPY_RADIUS = property(lambda self: None)
	OCCUPY_RADIUS_SQR = property(lambda self: None)
	PENALTY_FORBID_SELECTION = property(lambda self: None)
	PENALTY_OCCUPIED_RADIUS = property(lambda self: None)
	PENALTY_UNDETECTED_MAX = property(lambda self: None)
	PENALTY_UNDETECTED_MIN = property(lambda self: None)
	POINTS_ANGLE_STEP_DEGREE = property(lambda self: None)
	POINTS_ANGLE_STEP_RAD = property(lambda self: None)
	POINT_HIT_PROBABILITY_THRESHOLD = property(lambda self: None)
	SCORE_FORBIDDEN_TO_SELECT = property(lambda self: None)
	SCORING_MAX_DIST_TO_ADD_TO_SCORE = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MAXSPEED = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MINSPEED = property(lambda self: None)
	SCORING_UNDETECTED_MAX_SPEED = property(lambda self: None)
	SCORING_UNDETECTED_TIME_TO_IGNORE_TARGET = property(lambda self: None)
	TARGET_TURRET_DIRECTION_SCORE = property(lambda self: None)
	VERTICAL_REACH_TOLERANCE = property(lambda self: None)
	VISIBILITY_SCORE = property(lambda self: None)
	WEIGHT_CLOSE_DISTANCE = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AICirclingParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class AIData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def asyncDestroy(self, *args, **kwargs): pass
	covers = property(lambda self: None)
	gameplayName = property(lambda self: None)
	def getZoneEntryRoute(self, *args, **kwargs): pass
	isLoaded = property(lambda self: None)
	isLoading = property(lambda self: None)
	def loadAsync(self, *args, **kwargs): pass
	maps = property(lambda self: None)
	navmeshes = property(lambda self: None)
	recon = property(lambda self: None)
	udo = property(lambda self: None)
	zoneEntryRouteMap = property(lambda self: None)
	zonePath = property(lambda self: None)


class AIDataMaps(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIDataMaps'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	exposureMap = property(lambda self: None)
	heightMap = property(lambda self: None)
	stealthGrid = property(lambda self: None)
	visibilityGrid = property(lambda self: None)
	zones = property(lambda self: None)


class AIDebugParams(pybind11_object):
	COVER_PERFDIAG_ENABLED = property(lambda self: None)
	COVER_PERFDIAG_MAX_RADIUS = property(lambda self: None)
	COVER_PERFDIAG_MIN_RADIUS = property(lambda self: None)
	DEBUG_DRAW_ALLIES_COLLISION = property(lambda self: None)
	DEBUG_DRAW_CIRCLING_POINTS = property(lambda self: None)
	DEBUG_DRAW_CURRENT_TARGET_POINT = property(lambda self: None)
	DEBUG_DRAW_GUN_DISPERSION = property(lambda self: None)
	DEBUG_DRAW_GUN_POINT_AT_TARGET = property(lambda self: None)
	DEBUG_DRAW_SPG_TRAJECTORY = property(lambda self: None)
	ENABLE_BT_STACKS_TRACE = property(lambda self: None)
	ENABLE_BT_TRACE = property(lambda self: None)
	ENABLE_DEBUG_LOGGING = property(lambda self: None)
	ENABLE_FRAMETIME_STATS = property(lambda self: None)
	ENABLE_MOVEMENT_LOGGING = property(lambda self: None)
	ENABLE_RANGE_RECON_DEBUG_LOGGING = property(lambda self: None)
	ENABLE_TRACE_SYSTEM = property(lambda self: None)
	ENABLE_WEAKSPOT_SETUP_HELPER = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_AVOIDANCE = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_ENABLED = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_ENDPOINT = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_MAX_PATH_POINTS = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_PATH = property(lambda self: None)
	MOVEMENT_DEBUG_DRAW_SPEED_DT = property(lambda self: None)
	OBSTACLE_TRACKER_DEBUG_DRAW = property(lambda self: None)
	RELOAD_AI_XMLS_AFTER_BATTLE = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_CHASSIS = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_ENABLED = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_GUN = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_HULL = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_OVERRIDES_ONLY = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_SIZE = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_TANK = property(lambda self: None)
	WEAKSPOT_DEBUG_DRAW_TURRET = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIDebugParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def updateCalculatedParams(self, *args, **kwargs): pass


class AIFireController(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIFireController'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def _calculateHitChance(self, *args, **kwargs): pass
	_callForFireTime = property(lambda self: None)
	def _checkHitChance(self, *args, **kwargs): pass
	_firingDelay = property(lambda self: None)
	def _getAllowableAccuracy(self, *args, **kwargs): pass
	def _getAllowableAimingMode(self, *args, **kwargs): pass
	def _getTargetSize(self, *args, **kwargs): pass
	def _getUndetectedTargetChanceToStayAtLastKnownPosition(self, *args, **kwargs): pass
	def _hasBoredomTimerExpired(self, *args, **kwargs): pass
	_lastFireTime = property(lambda self: None)
	_lockTargetTime = property(lambda self: None)
	def _shouldRandomlyFireWithoutGoodAiming(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableFiring(self, *args, **kwargs): pass
	def getHitChance(self, *args, **kwargs): pass
	def getLastFireTime(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isFiringEnabled = property(lambda self: None)
	def isReloaded(self, *args, **kwargs): pass
	def setAccuracy(self, *args, **kwargs): pass
	def setAimingMode(self, *args, **kwargs): pass
	def setBoredomTimer(self, *args, **kwargs): pass
	def setFiringDelay(self, *args, **kwargs): pass
	def setUseBoredomTimerFlag(self, *args, **kwargs): pass


class AIFireControllerParams(pybind11_object):
	AIMING_MODE = property(lambda self: None)
	AIMING_MODE_VALUE = property(lambda self: None)
	DEFAULT_ACCURACY_SHOOT_ALWAYS = property(lambda self: None)
	DEFAULT_ACCURACY_SHOOT_AT_MAX_AIMING = property(lambda self: None)
	DEFAULT_ACCURACY_SHOOT_AT_STAND_STILL = property(lambda self: None)
	DEFAULT_FIRING_DELAY = property(lambda self: None)
	DEFAULT_NON_RESPONSIVE_BOREDOM_TIME = property(lambda self: None)
	UNDETECTED_TARGET_SHOOT_CHANCE_FADEOFF_TIME_MAXSPEED = property(lambda self: None)
	UNDETECTED_TARGET_SHOOT_CHANCE_FADEOFF_TIME_MINSPEED = property(lambda self: None)
	UNDETECTED_TARGET_SHOOT_CHANCE_MAX = property(lambda self: None)
	UNDETECTED_TARGET_SHOOT_CHANCE_MAX_SPEED = property(lambda self: None)
	UPDATE_RATE = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIFireControllerParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class AISensorParams(pybind11_object):
	EXIST_VISIBLE_RECHECK_TIME_DIRECT = property(lambda self: None)
	EXIST_VISIBLE_RECHECK_TIME_INDIRECT = property(lambda self: None)
	MAX_START_CIRCLING_TIME = property(lambda self: None)
	MIN_CIRCLER_CURRENT_TO_MAX_SPEED_RATIO = property(lambda self: None)
	MIN_CIRCLER_TO_VICTIM_SPEED_RATIO = property(lambda self: None)
	NO_VISIBLE_RECHECK_TIME_DIRECT = property(lambda self: None)
	NO_VISIBLE_RECHECK_TIME_INDIRECT = property(lambda self: None)
	SHOTS_MEMORY_SIZE = property(lambda self: None)
	START_CIRCLING_DISTANCE = property(lambda self: None)
	STOP_CIRCLING_DISTANCE = property(lambda self: None)
	STOP_CIRCLING_DISTANCE_SQR = property(lambda self: None)
	UNDETECTED_ATTACKER_POSITION_DEVIATION = property(lambda self: None)
	UNDETECTED_ATTACKER_POSITION_DEVIATION_SPG = property(lambda self: None)
	UNDETECTED_ATTACKER_SPG_MAX_DEVIATION_TIME = property(lambda self: None)
	UPDATE_BASE_TICK_TIME = property(lambda self: None)
	UPDATE_CIRCLERS_TICK_TIME = property(lambda self: None)
	UPDATE_EXPOSURE_TICK_TIME = property(lambda self: None)
	UPDATE_HP_TIME = property(lambda self: None)
	UPDATE_TICK_TIME = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISensorParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class AISpotHitCheckers(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISpotHitCheckers'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def calculateProjectileTrajectory(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def estimateTargetArmor(self, *args, **kwargs): pass
	def findCollisionsOnTrajectory(self, *args, **kwargs): pass
	def isTargetLineCollideStatic(self, *args, **kwargs): pass
	def isTargetLineCollideVehicles(self, *args, **kwargs): pass
	def onConfigUpdated(self, *args, **kwargs): pass
	def onVehicleKilled(self, *args, **kwargs): pass
	penetrationConfig = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass
	def setDebugDrawAlliesCollision(self, *args, **kwargs): pass
	def setDebugDrawSPGTrajectory(self, *args, **kwargs): pass
	def targetPointWithinTurretLimits(self, *args, **kwargs): pass


class AISpotHitCheckersSPG(AISpotHitCheckers):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISpotHitCheckersSPG'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def calculateProjectileTrajectory(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def estimateTargetArmor(self, *args, **kwargs): pass
	def findCollisionsOnTrajectory(self, *args, **kwargs): pass
	def isTargetLineCollideStatic(self, *args, **kwargs): pass
	def isTargetLineCollideVehicles(self, *args, **kwargs): pass
	def onConfigUpdated(self, *args, **kwargs): pass
	def onVehicleKilled(self, *args, **kwargs): pass
	penetrationConfig = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass
	def setDebugDrawAlliesCollision(self, *args, **kwargs): pass
	def setDebugDrawSPGTrajectory(self, *args, **kwargs): pass
	def targetPointWithinTurretLimits(self, *args, **kwargs): pass


class AISpotSelector(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISpotSelector'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkCurrentGunDirection(self, *args, **kwargs): pass
	def checkVehicleVisibility(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getNoneResult(*args, **kwargs): pass
	isCurrentSpotPotentiallyTargetable = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass


class AISpotSelectorHighFidelity(AISpotSelector):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISpotSelectorHighFidelity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkCurrentGunDirection(self, *args, **kwargs): pass
	def checkVehicleVisibility(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getNoneResult(*args, **kwargs): pass
	isCurrentSpotPotentiallyTargetable = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass


class AISpotTargeting(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AISpotTargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def canHitTarget(self, *args, **kwargs): pass
	def clearOverrideAimFlag(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getCurrentTargetingMode(self, *args, **kwargs): pass
	def getTargetPoint(self, *args, **kwargs): pass
	def getTargetSpotSize(self, *args, **kwargs): pass
	overrideAim = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass
	def setCurrentTargetingMode(self, *args, **kwargs): pass
	def setHitCheckers(self, *args, **kwargs): pass
	def setOverrideAim(self, *args, **kwargs): pass
	def setProcessTargetPoint(self, *args, **kwargs): pass
	def setSpotSelector(self, *args, **kwargs): pass
	def setTargetPointData(self, *args, **kwargs): pass


class AITargeting(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AITargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class AITargetingParams(pybind11_object):
	BONUS_AUTOLOADER_ENEMY = property(lambda self: None)
	BONUS_CURRENT_TARGET = property(lambda self: None)
	BONUS_IN_PRIORITY_AREA = property(lambda self: None)
	BONUS_ONE_SHOT_ENEMY = property(lambda self: None)
	ENEMY_EXPOSURE_SELF_RADIUS = property(lambda self: None)
	MAX_TIME_FOCUS_TARGET = property(lambda self: None)
	PENALTY_CANT_TURN = property(lambda self: None)
	PENALTY_ENEMY_SPEED = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_RADIUS = property(lambda self: None)
	PENALTY_EXPOSURE_THRESHOLD = property(lambda self: None)
	PENALTY_FORBID_SELECTION = property(lambda self: None)
	PENALTY_LONG_TURN = property(lambda self: None)
	PENALTY_LOW_HIT_CHANCE = property(lambda self: None)
	PENALTY_OUT_OF_YAW_SCOPE = property(lambda self: None)
	PENALTY_SLIGHTLY_OUT_OF_DRAW_RADIUS = property(lambda self: None)
	PENALTY_TARGET_FOCUS_EXCEEDED = property(lambda self: None)
	PENALTY_UNDETECTED_MAX = property(lambda self: None)
	PENALTY_UNDETECTED_MIN = property(lambda self: None)
	SCORE_BASE = property(lambda self: None)
	SCORE_FORBIDDEN_TO_SELECT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_TD = property(lambda self: None)
	SCORE_TANK_TYPE = property(lambda self: None)
	SCORING_AIMING_TIME_MULTIPLIER = property(lambda self: None)
	SCORING_ASSIST_DURATION = property(lambda self: None)
	SCORING_ASSIST_RADIUS = property(lambda self: None)
	SCORING_ASSIST_REDUCE_DURATION = property(lambda self: None)
	SCORING_DIST_TO_MOVE_TARGET = property(lambda self: None)
	SCORING_EXPOSURE_ARMOR_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_UNDEFINED_PENALTY_MULTIPLIER = property(lambda self: None)
	SCORING_MAX_DIST_TO_ADD_TO_SCORE = property(lambda self: None)
	SCORING_MAX_GLASS_CANNON = property(lambda self: None)
	SCORING_MAX_MOVE_BEFORE_SHOT = property(lambda self: None)
	SCORING_MAX_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MAX_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MAX_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME_NO_PENALTY = property(lambda self: None)
	SCORING_MIN_GLASS_CANNON = property(lambda self: None)
	SCORING_MIN_HIT_CHANCE = property(lambda self: None)
	SCORING_MIN_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MIN_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MIN_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_OUT_OF_DRAW_RADIUS_EXTRA = property(lambda self: None)
	SCORING_TARGET_HEIGHT = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MAX = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MIN = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MAXSPEED = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MINSPEED = property(lambda self: None)
	SCORING_UNDETECTED_MAX_SPEED = property(lambda self: None)
	SCORING_UNDETECTED_TIME_TO_IGNORE_TARGET = property(lambda self: None)
	TARGET_SELECTION_THRESHOLD = property(lambda self: None)
	UPDATE_RATE = property(lambda self: None)
	WEIGHT_ASSIST_BONUS = property(lambda self: None)
	WEIGHT_CLOSE_DISTANCE = property(lambda self: None)
	WEIGHT_DAMAGING_VEHICLE = property(lambda self: None)
	WEIGHT_DIRECTION = property(lambda self: None)
	WEIGHT_GLASS_CANNON = property(lambda self: None)
	WEIGHT_HIT_CHANCE = property(lambda self: None)
	WEIGHT_INVADER = property(lambda self: None)
	WEIGHT_PENETRATION = property(lambda self: None)
	WEIGHT_PENETRATION_HE = property(lambda self: None)
	WEIGHT_PIERCING_POWER = property(lambda self: None)
	WEIGHT_PLAYER_VEHICLE = property(lambda self: None)
	WEIGH_ENEMY_DISTRACTION = property(lambda self: None)
	WEIGH_ENEMY_HP = property(lambda self: None)
	WEIGH_TAKE_DAMAGE_RECENTLY = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AITargetingParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class AITeamInfluenceMaps(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AITeamInfluenceMaps'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	battleFront = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	enemy = property(lambda self: None)
	def init(self, *args, **kwargs): pass
	def onChangeVehicleInfluence(self, *args, **kwargs): pass
	own = property(lambda self: None)
	def update(self, *args, **kwargs): pass


class AITeamVehiclesProcessor(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AITeamVehiclesProcessor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdates(self, *args, **kwargs): pass
	def addVehicle(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def handleBeingVisiblyHitByLostEnemy(self, *args, **kwargs): pass
	onAllyAgentsUpdated = property(lambda self: None)
	onVehicleAdded = property(lambda self: None)
	def onVehicleGroupChanged(self, *args, **kwargs): pass
	onVehicleTeamDataUpdated = property(lambda self: None)
	onVisibilityDataUpdated = property(lambda self: None)
	def predictEnemyPositionsByEntryPoints(self, *args, **kwargs): pass
	def predictEnemyPositionsBySpawnPoints(self, *args, **kwargs): pass
	def predictRespawnedEnemyPosition(self, *args, **kwargs): pass
	def removeUpdates(self, *args, **kwargs): pass
	def removeVehicle(self, *args, **kwargs): pass


class AITeamVehiclesProcessorConfig(pybind11_object):
	UNDETECTED_ENEMY_MAX_POSITION_DIFF = property(lambda self: None)
	UNDETECTED_ENEMY_MAX_POSITION_DIFF_SQR = property(lambda self: None)
	UNDETECTED_TIME_TO_BECOME_LOST = property(lambda self: None)
	UPDATE_RATE_VEHICLES_DATA = property(lambda self: None)
	XRAY_RANGE_SQR_TO_BECOME_LOST = property(lambda self: None)
	XRAY_RANGE_TO_BECOME_LOST = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AITeamVehiclesProcessorConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class AIVehiclePoint(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIVehiclePoint'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindToLocalSpace(self, *args, **kwargs): pass
	def clone(self, *args, **kwargs): pass
	def computeWorldSpacePos(self, *args, **kwargs): pass
	def copyPosFrom(self, *args, **kwargs): pass
	localSpacePos = property(lambda self: None)
	name = property(lambda self: None)


class AIWeakSpot(AIVehiclePoint):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIWeakSpot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bindToLocalSpace(self, *args, **kwargs): pass
	def clone(self, *args, **kwargs): pass
	componentName = property(lambda self: None)
	def computeWorldSpacePos(self, *args, **kwargs): pass
	def copyPosFrom(self, *args, **kwargs): pass
	isOverride = property(lambda self: None)
	localName = property(lambda self: None)
	localSpacePos = property(lambda self: None)
	name = property(lambda self: None)
	numericID = property(lambda self: None)
	relativePos = property(lambda self: None)
	subComponentName = property(lambda self: None)


class AIWeakSpotsContainer(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIWeakSpotsContainer'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addPoint(self, *args, **kwargs): pass
	def addSequence(self, *args, **kwargs): pass
	allPoints = property(lambda self: None)
	def bindToLocalSpace(self, *args, **kwargs): pass
	def copyFrom(self, *args, **kwargs): pass
	defaultPoint = property(lambda self: None)
	def getPoint(self, *args, **kwargs): pass
	def getPointsCount(self, *args, **kwargs): pass
	def getSequence(self, *args, **kwargs): pass
	gunDamageableRearPart = property(lambda self: None)
	gunRandomChance = property(lambda self: None)
	def setDefaultPoint(self, *args, **kwargs): pass
	turretRandomChance = property(lambda self: None)


class AIWeakSpotsSequence(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIWeakSpotsSequence'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addPoint(self, *args, **kwargs): pass
	def getPoint(self, *args, **kwargs): pass
	def getPoints(self, *args, **kwargs): pass
	def getPointsCount(self, *args, **kwargs): pass
	numBestPoints = property(lambda self: None)


class AIZoneParams(pybind11_object):
	LONG_RANGE_MOVEMENT_IGNORE_SAFE_ROUTE = property(lambda self: None)
	MAX_ROUTE_COST = property(lambda self: None)
	MAX_TIME_TO_COMPUTE_PLAYER_MOVEMENT_PREDICTION = property(lambda self: None)
	MOVEMENT_PREDICTION_RANGE_TO_COUNT_MOVING_AWAY = property(lambda self: None)
	MOVEMENT_PREDICTION_SCORE_CURRENT_PRIMARY_ZONE = property(lambda self: None)
	MOVEMENT_PREDICTION_SCORE_CURRENT_SECONDARY_ZONE = property(lambda self: None)
	MOVEMENT_PREDICTION_SCORE_MULTIPLIER_MOVEMENT_DIRECTION = property(lambda self: None)
	MOVEMENT_PREDICTION_SCORE_NOT_RECOMMENDED_ZONE = property(lambda self: None)
	MOVEMENT_PREDICTION_SCORE_TOP_RECOMMENDED_ZONE = property(lambda self: None)
	UPDATE_RATE_PLAYERS_PREDICTION = property(lambda self: None)
	UPDATE_RATE_ZONE_ENTITIES = property(lambda self: None)
	UPDATE_RATE_ZONE_STATE = property(lambda self: None)
	ZONE_2_ZONE_DISTANCE_FACTOR = property(lambda self: None)
	ZONE_2_ZONE_MAX_HEIGHT_FACTOR = property(lambda self: None)
	ZONE_2_ZONE_MAX_MIGHTINESS_FACTOR = property(lambda self: None)
	ZONE_2_ZONE_MIN_HEIGHT_FACTOR = property(lambda self: None)
	ZONE_2_ZONE_MIN_MIGHTINESS_FACTOR = property(lambda self: None)
	ZONE_2_ZONE_ROUTE_ENEMIES_FACTOR = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AIZoneParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class CoverAgentCore(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverAgentCore'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def onBTReset(self, *args, **kwargs): pass


class ActiveReconAgentCore(CoverAgentCore):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ActiveReconAgentCore'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def findActiveReconCoverPairs(self, *args, **kwargs): pass
	def occupyActiveReconCovers(self, *args, **kwargs): pass
	def onBTReset(self, *args, **kwargs): pass
	def onFinishActiveReconRoute(self, *args, **kwargs): pass
	def onReachActiveReconWaypoint(self, *args, **kwargs): pass
	def resetActiveRecon(self, *args, **kwargs): pass


class ActiveReconQueryParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ActiveReconQueryParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	endCoverMinProtection = property(lambda self: None)
	expectTargetsToShoot = property(lambda self: None)
	maxCoverPairsToCheck = property(lambda self: None)
	maxDistance = property(lambda self: None)
	maxResults = property(lambda self: None)
	minDistance = property(lambda self: None)
	origin = property(lambda self: None)
	peekOnly = property(lambda self: None)
	startCoverMinProtection = property(lambda self: None)
	targets = property(lambda self: None)


class ActiveReconQueryResult(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ActiveReconQueryResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	cost = property(lambda self: None)
	endCoverInfo = property(lambda self: None)
	pathLength = property(lambda self: None)
	pathToStart = property(lambda self: None)
	reconAngles = property(lambda self: None)
	reconPoint = property(lambda self: None)
	startCoverInfo = property(lambda self: None)


class ActiveReconQueryResult__CoverInfo(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ActiveReconQueryResult::CoverInfo'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	arcs = property(lambda self: None)
	coverPoint = property(lambda self: None)
	id = property(lambda self: None)
	type = property(lambda self: None)


class PyUtilityNode(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyUtilityNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass


class ConditionNode(PyUtilityNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ConditionNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getDebugInfo(self, *args, **kwargs): pass
	def getNode(self, *args, **kwargs): pass
	def getTraceInfo(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass


class AggregationConditionNodeHolder(ConditionNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AggregationConditionNodeHolder'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getDebugInfo(self, *args, **kwargs): pass
	def getNode(self, *args, **kwargs): pass
	def getTraceInfo(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass


class AimingMode(pybind11_object):
	DontWait = 0
	WaitForAiming = 1
	WaitForStandAndHeal = 3
	WaitForStanding = 2
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'AimingMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def fromString(*args, **kwargs): pass


class PyScene(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyScene'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addEntity(self, *args, **kwargs): pass
	def addProcessor(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def getEntities(self, *args, **kwargs): pass
	def getEntity(self, *args, **kwargs): pass
	id = property(lambda self: None)
	def removeEntity(self, *args, **kwargs): pass
	def removeProcessor(self, *args, **kwargs): pass
	spaceID = property(lambda self: None)
	def update(self, *args, **kwargs): pass


class Arena(PyScene):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Arena'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addEntity(self, *args, **kwargs): pass
	def addProcessor(self, *args, **kwargs): pass
	def addTeam(self, *args, **kwargs): pass
	aiData = property(lambda self: None)
	def clear(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	endTime = property(lambda self: None)
	gameplayID = property(lambda self: None)
	gameplayMask = property(lambda self: None)
	def getEntities(self, *args, **kwargs): pass
	def getEntity(self, *args, **kwargs): pass
	def getTeam(self, *args, **kwargs): pass
	def getTimeSinceGameStart(self, *args, **kwargs): pass
	def getTimeToGameEnd(self, *args, **kwargs): pass
	id = property(lambda self: None)
	isStarted = property(lambda self: None)
	def removeEntity(self, *args, **kwargs): pass
	def removeProcessor(self, *args, **kwargs): pass
	roundLength = property(lambda self: None)
	def setStats(self, *args, **kwargs): pass
	spaceID = property(lambda self: None)
	startTime = property(lambda self: None)
	startTimers = property(lambda self: None)
	def update(self, *args, **kwargs): pass
	zones = property(lambda self: None)

BT = <module 'AI_Common.BT' (built-in)>

class BaseTankDescriptorComponent(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'BaseTankDescriptorComponent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armorHomogenization = property(lambda self: None)
	hitTester = property(lambda self: None)
	materials = property(lambda self: None)


class BaseTankDescriptorComponent__HitTester(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'BaseTankDescriptorComponent::HitTester'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	collision = property(lambda self: None)
	def getModel(self, *args, **kwargs): pass


class BattleFrontMap(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'BattleFrontMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getDebugData(self, *args, **kwargs): pass
	def queryBattleFrontDistance(self, *args, **kwargs): pass
	def queryNearestBattleFrontPoint(self, *args, **kwargs): pass
	def updateBattleFrontMap(self, *args, **kwargs): pass


class PVESpotSelectorHighFidelity(AISpotSelectorHighFidelity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVESpotSelectorHighFidelity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkCurrentGunDirection(self, *args, **kwargs): pass
	def checkVehicleVisibility(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getNoneResult(*args, **kwargs): pass
	isCurrentSpotPotentiallyTargetable = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass


class BootcampSpotSelector(PVESpotSelectorHighFidelity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'BootcampSpotSelector'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkCurrentGunDirection(self, *args, **kwargs): pass
	def checkVehicleVisibility(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getNoneResult(*args, **kwargs): pass
	isCurrentSpotPotentiallyTargetable = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass


class UAIRemovableObstacle(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIRemovableObstacle'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class BoxShapeRemovableObstacle(UAIRemovableObstacle):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'BoxShapeRemovableObstacle'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PVETargeting(AITargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVETargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class ClingBranderTargeting(PVETargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ClingBranderTargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def addCirclingComponent(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class CombatCoverAgentCore(CoverAgentCore):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CombatCoverAgentCore'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkIsCoverValid(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def findAndReserveBestCover(self, *args, **kwargs): pass
	def occupyCover(self, *args, **kwargs): pass
	def onBTReset(self, *args, **kwargs): pass
	def resetCover(self, *args, **kwargs): pass


class uai.CombatantInfo(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'uai.CombatantInfo'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	entity = property(lambda self: None)
	frontArmorThreat = property(lambda self: None)
	def getPosition(self, *args, **kwargs): pass
	def isAlive(self, *args, **kwargs): pass
	def isAliveThreat(self, *args, **kwargs): pass
	def isAliveValidAlly(self, *args, **kwargs): pass
	def isAliveValidThreat(self, *args, **kwargs): pass
	isThreat = property(lambda self: None)
	def isValid(self, *args, **kwargs): pass
	lastKnownPosition = property(lambda self: None)
	lost = property(lambda self: None)
	rearArmorThreat = property(lambda self: None)
	visible = property(lambda self: None)


class CombatantInfo(uai.CombatantInfo):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CombatantInfo'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	entity = property(lambda self: None)
	frontArmorThreat = property(lambda self: None)
	def getPosition(self, *args, **kwargs): pass
	def isAlive(self, *args, **kwargs): pass
	def isAliveThreat(self, *args, **kwargs): pass
	def isAliveValidAlly(self, *args, **kwargs): pass
	def isAliveValidThreat(self, *args, **kwargs): pass
	isThreat = property(lambda self: None)
	def isValid(self, *args, **kwargs): pass
	lastKnownPosition = property(lambda self: None)
	lost = property(lambda self: None)
	rearArmorThreat = property(lambda self: None)
	visible = property(lambda self: None)


class CoverAdapter(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__qualname__ = 'CoverAdapter'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	coverInstanceID = property(lambda self: None)
	def getCoverMode(self, *args, **kwargs): pass
	def getCoverSequence(self, *args, **kwargs): pass
	def getCoverStyles(self, *args, **kwargs): pass
	def getCoverType(self, *args, **kwargs): pass
	def getSingleCover(self, *args, **kwargs): pass
	def hasAllCoverStyles(self, *args, **kwargs): pass
	def hasAnyCoverStyle(self, *args, **kwargs): pass
	hasCover = property(lambda self: None)
	hasCoverSequence = property(lambda self: None)
	hasOccupiedCover = property(lambda self: None)
	hasSingleCover = property(lambda self: None)
	mediator = property(lambda self: None)


class CoverAgentState(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverAgentState'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	adapter = property(lambda self: None)
	findCoverArea = property(lambda self: None)
	def resetCover(self, *args, **kwargs): pass
	def switchStyle(self, *args, **kwargs): pass
	def validateStyle(self, *args, **kwargs): pass


class CoverAggressiveMode(pybind11_object):
	AggressiveFirst = CoverAggressiveMode.AggressiveFirst
	AggressiveOnly = CoverAggressiveMode.AggressiveOnly
	Default = CoverAggressiveMode.Default
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Default\n\n  AggressiveOnly\n\n  AggressiveFirst'
	__entries = {u'Default': (CoverAggressiveMode.Default, None), u'AggressiveOnly': (CoverAggressiveMode.AggressiveOnly, None), u'AggressiveFirst': (CoverAggressiveMode.AggressiveFirst, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Default': CoverAggressiveMode.Default, u'AggressiveOnly': CoverAggressiveMode.AggressiveOnly, u'AggressiveFirst': CoverAggressiveMode.AggressiveFirst}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverAggressiveMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class CoverArc(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverArc'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	antiSPGAngle = property(lambda self: None)
	def includesAngle(self, *args, **kwargs): pass
	startAngle = property(lambda self: None)
	stopAngle = property(lambda self: None)


class CoverMode(pybind11_object):
	Blind = CoverMode.Blind
	Defensive = CoverMode.Defensive
	Normal = CoverMode.Normal
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Blind\n\n  Defensive\n\n  Normal'
	__entries = {u'Blind': (CoverMode.Blind, None), u'Defensive': (CoverMode.Defensive, None), u'Normal': (CoverMode.Normal, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Blind': CoverMode.Blind, u'Defensive': CoverMode.Defensive, u'Normal': CoverMode.Normal}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class CoverQueryParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverQueryParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	arbitraryThreats = property(lambda self: None)
	checkCollisions = property(lambda self: None)
	checkCollisionsDistance = property(lambda self: None)
	collisionMargin = property(lambda self: None)
	collisionYOffset = property(lambda self: None)
	coverScoreWeight = property(lambda self: None)
	coverType = property(lambda self: None)
	enablePerfDiagnostics = property(lambda self: None)
	excludedIDs = property(lambda self: None)
	findCoversFromArbitraryThreats = property(lambda self: None)
	floraCoverSafetyRange = property(lambda self: None)
	maxCandidates = property(lambda self: None)
	maxDistance = property(lambda self: None)
	maxResults = property(lambda self: None)
	minDistance = property(lambda self: None)
	modePriorities = property(lambda self: None)
	origin = property(lambda self: None)
	pathScoreWeight = property(lambda self: None)
	safetyMargin = property(lambda self: None)
	shootingForwardClearance = property(lambda self: None)
	shootingSideClearance = property(lambda self: None)


class CoverResources(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverResources'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def empty(self, *args, **kwargs): pass
	def enableAllCovers(self, *args, **kwargs): pass
	def findCovers(self, *args, **kwargs): pass
	def isCoverValid(self, *args, **kwargs): pass


class CoverSequenceWaypoint(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverSequenceWaypoint'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	coverToRelease = property(lambda self: None)
	position = property(lambda self: None)


class CoverStyle(pybind11_object):
	Combat = 1
	ReconActive = 4
	ReconActivePeekOnly = 8
	ReconPassive = 2
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverStyle'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class CoverType(pybind11_object):
	Destructible = 4
	Flora = 2
	Low = 16
	Slope = 8
	Static = 1
	Unknown = 2147483648L
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoverType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class CoversArea(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoversArea'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	aggro = property(lambda self: None)
	maxDist = property(lambda self: None)
	minDist = property(lambda self: None)
	origin = property(lambda self: None)


class CoversGameplayParams(pybind11_object):
	ACTIVE_RECON_DAMAGE_SCORE_WEIGHT = property(lambda self: None)
	ACTIVE_RECON_DISTANCE_SCORE_WEIGHT = property(lambda self: None)
	ACTIVE_RECON_QUERY_PARAMS_MAX_RESULT = property(lambda self: None)
	ACTIVE_RECON_SKIP_START_MAX_ANGLE_COS = property(lambda self: None)
	ACTIVE_RECON_SKIP_START_MAX_ANGLE_DEGREE = property(lambda self: None)
	ACTIVE_RECON_TURN_COMPLEXITY_SCORE_MAX = property(lambda self: None)
	ACTIVE_RECON_TURN_COMPLEXITY_SCORE_MIN = property(lambda self: None)
	ACTIVE_RECON_TURN_COMPLEXITY_SCORE_WEIGHT = property(lambda self: None)
	BEST_COVER_SPG_PROTECTION_SCORE = property(lambda self: None)
	COVER_AGGRESSIVENESS_COVER_TO_CLOSE_TO_BOT_DIST = property(lambda self: None)
	COVER_AGGRESSIVENESS_COVER_TO_CLOSE_TO_ENEMY_DIST = property(lambda self: None)
	COVER_AGGRESSIVENESS_DIST_FACTOR_MAX_DIST = property(lambda self: None)
	COVER_AGGRESSIVENESS_DIST_FACTOR_MAX_FACTOR = property(lambda self: None)
	COVER_AGGRESSIVENESS_DIST_FACTOR_MIN_DIST = property(lambda self: None)
	COVER_AGGRESSIVENESS_DIST_FACTOR_MIN_FACTOR = property(lambda self: None)
	COVER_AGGRESSIVENESS_ENEMY_TO_CLOSE_DIST = property(lambda self: None)
	COVER_ARMOR_BEST_ANGLING_COS = property(lambda self: None)
	COVER_ARMOR_BEST_ANGLING_DEGREE = property(lambda self: None)
	COVER_ARMOR_SCORE_AT_DIAMOND_FACTOR = property(lambda self: None)
	COVER_ARMOR_SCORE_AT_FRONT_FACTOR = property(lambda self: None)
	COVER_DIST_TO_TARGET_MAX_DIST = property(lambda self: None)
	COVER_DIST_TO_TARGET_MIN_DIST = property(lambda self: None)
	COVER_FLANKING_ALLY_TO_CLOSE_TO_ENEMY = property(lambda self: None)
	COVER_FLANKING_ALLY_TO_CLOSE_TO_ENEMY_SQR = property(lambda self: None)
	COVER_FLANKING_ALLY_TO_FAR_FROM_ENEMY = property(lambda self: None)
	COVER_FLANKING_ALLY_TO_FAR_FROM_ENEMY_SQR = property(lambda self: None)
	COVER_GUN_PITCH_LIMIT_BAN_ANGLE_DEGREE = property(lambda self: None)
	COVER_GUN_PITCH_LIMIT_BAN_ANGLE_RAD = property(lambda self: None)
	COVER_GUN_PITCH_LIMIT_SAFETY_ANGLE_DEGREE = property(lambda self: None)
	COVER_GUN_PITCH_LIMIT_SAFETY_ANGLE_RAD = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_BAN_ANGLE_DEGREE = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_BAN_ANGLE_RAD = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_SAFETY_ANGLE_MAX_DEGREE = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_SAFETY_ANGLE_MAX_RAD = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_SAFETY_ANGLE_MIN_DEGREE = property(lambda self: None)
	COVER_GUN_YAW_LIMIT_SAFETY_ANGLE_MIN_RAD = property(lambda self: None)
	COVER_QUERY_PARAMS_MAX_CANDIDATES = property(lambda self: None)
	COVER_QUERY_PARAMS_MAX_RESULT = property(lambda self: None)
	COVER_QUERY_PARAMS_SHOOTING_FORWARD_CLEARANCE = property(lambda self: None)
	COVER_QUERY_PARAMS_SHOOTING_SIDE_CLEARANCE_MODIFIER = property(lambda self: None)
	COVER_SPG_PROTECTION_EXACT_MATCH_SCORE = property(lambda self: None)
	COVER_SPG_PROTECTION_MAX_ANGLE_RATION = property(lambda self: None)
	COVER_SPG_PROTECTION_MAX_ANTI_SPG_ANGLE = property(lambda self: None)
	COVER_SPG_PROTECTION_MAX_ANTI_SPG_ANGLE_RAD = property(lambda self: None)
	COVER_SPG_PROTECTION_MIN_ANGLE_RATION = property(lambda self: None)
	COVER_SPG_PROTECTION_NON_DAMAGING_SPG_FACTOR = property(lambda self: None)
	COVER_SPG_PROTECTION_NON_DAMAGING_SPG_RANGE = property(lambda self: None)
	COVER_SPG_PROTECTION_NON_DAMAGING_SPG_TIMEOUT = property(lambda self: None)
	DISABLE_TWO_TICKS_FIND_COVER = property(lambda self: None)
	ENEMY_REPOSITION_RANGE_DEFENSIVE_COVER = property(lambda self: None)
	ENEMY_REPOSITION_RANGE_NORMAL_COVER = property(lambda self: None)
	FACTOR_COVER_AGGRESSIVENESS = property(lambda self: None)
	FACTOR_COVER_AGGRESSIVENESS2 = property(lambda self: None)
	FACTOR_COVER_AGGRESSIVENESS2_OUT_OF_AREA = property(lambda self: None)
	FACTOR_COVER_ARMOR_ANGLING = property(lambda self: None)
	FACTOR_COVER_CROWD = property(lambda self: None)
	FACTOR_COVER_CROWD_MAX_DIST = property(lambda self: None)
	FACTOR_COVER_CROWD_MIN_DIST = property(lambda self: None)
	FACTOR_COVER_DAMAGE_TAKEN_MAX = property(lambda self: None)
	FACTOR_COVER_DAMAGE_TAKEN_MIN = property(lambda self: None)
	FACTOR_COVER_FLANKING = property(lambda self: None)
	FACTOR_COVER_GUN_PITCH_LIMITS = property(lambda self: None)
	FACTOR_COVER_GUN_YAW_LIMITS = property(lambda self: None)
	FACTOR_COVER_REAR_TURRET = property(lambda self: None)
	FACTOR_COVER_ROUTE_LENGTH = property(lambda self: None)
	FACTOR_COVER_ROUTE_LENGTH_MULTIPLIER = property(lambda self: None)
	FACTOR_COVER_SPG_PROTECTION = property(lambda self: None)
	FACTOR_COVER_STICK_ON_TARGET = property(lambda self: None)
	MAX_REAR_TURRET_TO_HULL_RELATIVE_POSITION = property(lambda self: None)
	NO_COVER_SPG_PROTECTION_SCORE = property(lambda self: None)
	OCCUPY_COVER_RADIUS = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MAX_ANGLE = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MAX_ANGLE_RAD = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MAX_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MIN_ANGLE = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MIN_ANGLE_RAD = property(lambda self: None)
	RECON_FLORA_COVER_ARC_PROTECTION_MIN_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_DETECT_ENEMIES_COUNT_MAX_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_DETECT_ENEMIES_COUNT_MIN_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_NEAREST_ENEMIES_MAX_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_NEAREST_ENEMIES_MIN_SCORE = property(lambda self: None)
	RECON_FLORA_COVER_NO_STEALTH_ROUTE_SCORE_PENALTY = property(lambda self: None)
	RECON_FLORA_COVER_ZERO_DETECT_ENEMIES_PENALTY = property(lambda self: None)
	REVERSE_PEEKING_LINE_ANGLE = property(lambda self: None)
	REVERSE_PEEKING_LINE_ANGLE_COS = property(lambda self: None)
	SCORE_COVER_IGNORE = property(lambda self: None)
	SIDE_PEEKING_LINE_ANGLE_NORMAL_TURRET = property(lambda self: None)
	SIDE_PEEKING_LINE_ANGLE_NORMAL_TURRET_RAD = property(lambda self: None)
	SIDE_PEEKING_LINE_ANGLE_REAR_TURRET = property(lambda self: None)
	SIDE_PEEKING_LINE_ANGLE_REAR_TURRET_RAD = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'CoversGameplayParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass

DEFAULT_EPSILON = 0.00039999998989515007

class DebugDraw(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'DebugDraw'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def create(*args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def drawCross(self, *args, **kwargs): pass
	def drawLines(self, *args, **kwargs): pass
	def drawPath(self, *args, **kwargs): pass
	ref = property(lambda self: None)
	def setDebugDrawFactory(*args, **kwargs): pass


class EnemySensorData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'EnemySensorData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	detected = property(lambda self: None)
	detection = property(lambda self: None)
	distanceSqr = property(lambda self: None)
	exposure = property(lambda self: None)
	exposureCheckIteration = property(lambda self: None)
	exposureCheckTime = property(lambda self: None)
	def getPosition(self, *args, **kwargs): pass
	isInvader = property(lambda self: None)
	lastDetectionTime = property(lambda self: None)
	lastExposedTime = property(lambda self: None)
	lastPenetrableTime = property(lambda self: None)
	lastUpdateDirectDetectionStatusTime = property(lambda self: None)
	personalThreatData = property(lambda self: None)
	potentialExposedPosition = property(lambda self: None)
	def resetUndetectedData(self, *args, **kwargs): pass
	def setUndetectedData(self, *args, **kwargs): pass
	def setUndetectedDataFromTeam(self, *args, **kwargs): pass
	tankEntity = property(lambda self: None)
	targetPrevHP = property(lambda self: None)
	targetTakeDamageLastTime = property(lambda self: None)
	undetectedPosition = property(lambda self: None)
	undetectedSpeed = property(lambda self: None)
	undetectedTime = property(lambda self: None)
	unexposedDepth = property(lambda self: None)
	def updateExposureData(self, *args, **kwargs): pass


class ExposureMap(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ExposureMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def queryExposure(self, *args, **kwargs): pass


class FaceParameters(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'FaceParameters'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	currentTarget = property(lambda self: None)
	faceDirectionPrecisionRough = property(lambda self: None)
	options = property(lambda self: None)
	safeTurnMovementSafetyMargin = property(lambda self: None)
	safeTurnStartCompensateThreshold = property(lambda self: None)
	safeTurnStopCompensateThreshold = property(lambda self: None)
	safeTurnWallDistanceThresholdMul = property(lambda self: None)


class FuzzyConditionNodeHolder(ConditionNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'FuzzyConditionNodeHolder'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getDebugInfo(self, *args, **kwargs): pass
	def getNode(self, *args, **kwargs): pass
	def getTraceInfo(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass

Goals = <module 'AI_Common.Goals' (built-in)>

class HitAngleNormalization(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'HitAngleNormalization'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	angle_mp = 0.05235987901687622
	angle_sub = 1.0
	def getHitAngleCosWithNormalization(*args, **kwargs): pass
	thresholdCaliber = 1.0


class ICoverAgentsMediator(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ICoverAgentsMediator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addOccupiedCoverID(self, *args, **kwargs): pass
	def addReservedCoverID(self, *args, **kwargs): pass
	def getAllUnusableCoverIDs(self, *args, **kwargs): pass
	def getInvalidCoverIDs(self, *args, **kwargs): pass
	def getOccupiedAndReservedCoverIDs(self, *args, **kwargs): pass
	def getOccupiedCoverIDs(self, *args, **kwargs): pass
	def getReservedCoverIDs(self, *args, **kwargs): pass
	def invalidateCover(self, *args, **kwargs): pass
	def isCoverBeingUsed(self, *args, **kwargs): pass
	def isCoverInvalid(self, *args, **kwargs): pass
	def isCoverUsable(self, *args, **kwargs): pass
	def removeOccupiedCoverID(self, *args, **kwargs): pass
	def removeReservedCoverID(self, *args, **kwargs): pass


class IUpdatable(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'IUpdatable'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class InfluenceMap(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'InfluenceMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getDebugData(self, *args, **kwargs): pass
	def queryInfluence(self, *args, **kwargs): pass
	def updateInfluenceMap(self, *args, **kwargs): pass


class IsCoverValidResult(pybind11_object):
	CoverInvalid = IsCoverValidResult.CoverInvalid
	CoverValid = IsCoverValidResult.CoverValid
	NoCover = IsCoverValidResult.NoCover
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  NoCover\n\n  CoverInvalid\n\n  CoverValid'
	__entries = {u'NoCover': (IsCoverValidResult.NoCover, None), u'CoverInvalid': (IsCoverValidResult.CoverInvalid, None), u'CoverValid': (IsCoverValidResult.CoverValid, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'NoCover': IsCoverValidResult.NoCover, u'CoverInvalid': IsCoverValidResult.CoverInvalid, u'CoverValid': IsCoverValidResult.CoverValid}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'IsCoverValidResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)

LOST_ENEMY_DEFAULT_AREA_RADIUS = 200.0
LOST_ENEMY_MAX_TIME_MUL_TO_LEAVE_AREA = 5.0
LOST_ENEMY_MIN_TIME_MUL_TO_LEAVE_AREA = 2.0

class MapsTrainingBotSpotHitCheckers(AITargetingParams):
	BONUS_AUTOLOADER_ENEMY = property(lambda self: None)
	BONUS_CURRENT_TARGET = property(lambda self: None)
	BONUS_IN_PRIORITY_AREA = property(lambda self: None)
	BONUS_ONE_SHOT_ENEMY = property(lambda self: None)
	ENEMY_EXPOSURE_SELF_RADIUS = property(lambda self: None)
	MAX_TIME_FOCUS_TARGET = property(lambda self: None)
	PENALTY_CANT_TURN = property(lambda self: None)
	PENALTY_ENEMY_SPEED = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_RADIUS = property(lambda self: None)
	PENALTY_EXPOSURE_THRESHOLD = property(lambda self: None)
	PENALTY_FORBID_SELECTION = property(lambda self: None)
	PENALTY_LONG_TURN = property(lambda self: None)
	PENALTY_LOW_HIT_CHANCE = property(lambda self: None)
	PENALTY_OUT_OF_YAW_SCOPE = property(lambda self: None)
	PENALTY_SLIGHTLY_OUT_OF_DRAW_RADIUS = property(lambda self: None)
	PENALTY_TARGET_FOCUS_EXCEEDED = property(lambda self: None)
	PENALTY_UNDETECTED_MAX = property(lambda self: None)
	PENALTY_UNDETECTED_MIN = property(lambda self: None)
	SCORE_BASE = property(lambda self: None)
	SCORE_FORBIDDEN_TO_SELECT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_TD = property(lambda self: None)
	SCORE_TANK_TYPE = property(lambda self: None)
	SCORING_AIMING_TIME_MULTIPLIER = property(lambda self: None)
	SCORING_ASSIST_DURATION = property(lambda self: None)
	SCORING_ASSIST_RADIUS = property(lambda self: None)
	SCORING_ASSIST_REDUCE_DURATION = property(lambda self: None)
	SCORING_DIST_TO_MOVE_TARGET = property(lambda self: None)
	SCORING_EXPOSURE_ARMOR_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_UNDEFINED_PENALTY_MULTIPLIER = property(lambda self: None)
	SCORING_MAX_DIST_TO_ADD_TO_SCORE = property(lambda self: None)
	SCORING_MAX_GLASS_CANNON = property(lambda self: None)
	SCORING_MAX_MOVE_BEFORE_SHOT = property(lambda self: None)
	SCORING_MAX_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MAX_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MAX_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME_NO_PENALTY = property(lambda self: None)
	SCORING_MIN_GLASS_CANNON = property(lambda self: None)
	SCORING_MIN_HIT_CHANCE = property(lambda self: None)
	SCORING_MIN_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MIN_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MIN_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_OUT_OF_DRAW_RADIUS_EXTRA = property(lambda self: None)
	SCORING_TARGET_HEIGHT = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MAX = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MIN = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MAXSPEED = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MINSPEED = property(lambda self: None)
	SCORING_UNDETECTED_MAX_SPEED = property(lambda self: None)
	SCORING_UNDETECTED_TIME_TO_IGNORE_TARGET = property(lambda self: None)
	SELECT_TARGET_MAX_DISTANCE = property(lambda self: None)
	TARGET_SELECTION_THRESHOLD = property(lambda self: None)
	UPDATE_RATE = property(lambda self: None)
	WEIGHT_ASSIST_BONUS = property(lambda self: None)
	WEIGHT_CLOSE_DISTANCE = property(lambda self: None)
	WEIGHT_DAMAGING_VEHICLE = property(lambda self: None)
	WEIGHT_DIRECTION = property(lambda self: None)
	WEIGHT_GLASS_CANNON = property(lambda self: None)
	WEIGHT_HIT_CHANCE = property(lambda self: None)
	WEIGHT_INVADER = property(lambda self: None)
	WEIGHT_PENETRATION = property(lambda self: None)
	WEIGHT_PENETRATION_HE = property(lambda self: None)
	WEIGHT_PIERCING_POWER = property(lambda self: None)
	WEIGHT_PLAYER_VEHICLE = property(lambda self: None)
	WEIGH_ENEMY_DISTRACTION = property(lambda self: None)
	WEIGH_ENEMY_HP = property(lambda self: None)
	WEIGH_TAKE_DAMAGE_RECENTLY = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MapsTrainingBotSpotHitCheckers'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class MapsTrainingBotTargeting(AITargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MapsTrainingBotTargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class MoveParameters(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MoveParameters'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	arrivalPartialPathToleranceSq = property(lambda self: None)
	currentTarget = property(lambda self: None)
	extraObstaclesToIgnore = property(lambda self: None)
	handbrakeSpeedThreshold = property(lambda self: None)
	handbrakeTurnAngleThresholdCos = property(lambda self: None)
	kTurnAllowedDistance = property(lambda self: None)
	longDistance = property(lambda self: None)
	lookDirectionPrecisionPrecise = property(lambda self: None)
	lookDirectionPrecisionRough = property(lambda self: None)
	maxSlopeUpAngle = property(lambda self: None)
	options = property(lambda self: None)
	precision = property(lambda self: None)
	roughLookPrecisionMaxSpeed = property(lambda self: None)
	roughLookPrecisionMinSpeed = property(lambda self: None)
	safeTurnAngleCosThreshold = property(lambda self: None)
	safeTurnMovementSafetyMargin = property(lambda self: None)
	safeTurnStartCompensateThresholdOnTheMove = property(lambda self: None)
	safeTurnStartCompensateThresholdStationary = property(lambda self: None)
	safeTurnStopCompensateThresholdOnTheMove = property(lambda self: None)
	safeTurnStopCompensateThresholdStationary = property(lambda self: None)
	safeTurnWallDistanceThresholdMul = property(lambda self: None)
	slopeCompensation = property(lambda self: None)
	stopAccelerationMaxWallDistance = property(lambda self: None)
	stopAccelerationMinWallDistance = property(lambda self: None)
	stopAccelerationReverseMovementAngleMul = property(lambda self: None)
	stopAccelerationThreshold = property(lambda self: None)
	usePreciseTargetCalculations = property(lambda self: None)


class MoveTweakParameters(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MoveTweakParameters'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	areaCostFunctorWeight = property(lambda self: None)
	avoidDetectionCostFunctorWeight = property(lambda self: None)
	avoidEnemyCostFunctorWeight = property(lambda self: None)
	avoidExposureCostFunctorWeight = property(lambda self: None)
	avoidanceMaxHeightDiffMul = property(lambda self: None)
	backToNavmeshSafetyCooldown = property(lambda self: None)
	bufferRadius = property(lambda self: None)
	bypassDestructibleCostFunctorWeight = property(lambda self: None)
	currentVelocityFactor = property(lambda self: None)
	cutUpDetectionMinSpeed = property(lambda self: None)
	deadPassCostFunctorWeight = property(lambda self: None)
	desiredVelocityFactor = property(lambda self: None)
	distanceToWallCheckPrecisionIdle = property(lambda self: None)
	distanceToWallCheckPrecisionMax = property(lambda self: None)
	distanceToWallCheckPrecisionMin = property(lambda self: None)
	errorMargin = property(lambda self: None)
	maxDistanceSquared = property(lambda self: None)
	movingObstacleLookAheadStep = property(lambda self: None)
	movingObstacleParallelThreshold = property(lambda self: None)
	navmeshCheckPositionIntervalSq = property(lambda self: None)
	pendulumDesiredDirDiffThresholdCos = property(lambda self: None)
	pendulumHistoryLimit = property(lambda self: None)
	pendulumMaxDirSwitches = property(lambda self: None)
	pendulumPositionDiffThresholdSq = property(lambda self: None)
	reverseMinDesiredSpeed = property(lambda self: None)
	rightHandFactor = property(lambda self: None)
	safeRouteCostFunctorWeight = property(lambda self: None)
	waterCostFunctorWeight = property(lambda self: None)


class MovementConstants(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MovementConstants'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	collisionTestMaxDistance = property(lambda self: None)
	maxSpeedOnSharpTurns = property(lambda self: None)
	maxSpeedPossible = property(lambda self: None)
	openGoalRadius = property(lambda self: None)
	pathFollowExtraLookaheadTime = property(lambda self: None)
	pathFollowLookaheadDistance = property(lambda self: None)
	pathFollowLookaheadTime = property(lambda self: None)
	pathGridCellCost = property(lambda self: None)
	pathLookupInFutureTime = property(lambda self: None)
	pathOptimizeTime = property(lambda self: None)
	pathPrefixCells = property(lambda self: None)
	pathReplanTime = property(lambda self: None)
	sharpTurnThreshold = property(lambda self: None)


class MovementLimits(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MovementLimits'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def makeValidator(self, *args, **kwargs): pass


class MovementOutput(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'MovementOutput'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	isInPendulum = property(lambda self: None)
	movementOutput = property(lambda self: None)


class NavHeightMapPack(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'NavHeightMapPack'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getHeights(self, *args, **kwargs): pass
	def getMaxHeight(self, *args, **kwargs): pass
	def getMinHeight(self, *args, **kwargs): pass


class ObstacleIDType(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ObstacleIDType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class OverMatchMechanicsVersion(pybind11_object):
	Default = 0
	Revised = 1
	Standard = 0
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'OverMatchMechanicsVersion'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PVECircling(AICircling):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVECircling'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getCirclingPosition(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	onDebugPoints = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def selectTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass


class PVEOverrideAimingFlag(pybind11_object):
	DoDamage = 1
	DontPenetrate = 2
	HitDestructibleByHE = 32
	HitObstacle = 16
	HitOther = 8
	Miss = 4
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVEOverrideAimingFlag'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PVEOverrideTargetingModes(pybind11_object):
	LocalDirection = PVEOverrideTargetingModes.LocalDirection
	Null = PVEOverrideTargetingModes.Null
	WorldDirection = PVEOverrideTargetingModes.WorldDirection
	WorldPosition = PVEOverrideTargetingModes.WorldPosition
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  WorldPosition\n\n  WorldDirection\n\n  LocalDirection\n\n  Null'
	__entries = {u'WorldPosition': (PVEOverrideTargetingModes.WorldPosition, None), u'WorldDirection': (PVEOverrideTargetingModes.WorldDirection, None), u'LocalDirection': (PVEOverrideTargetingModes.LocalDirection, None), u'Null': (PVEOverrideTargetingModes.Null, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'WorldPosition': PVEOverrideTargetingModes.WorldPosition, u'WorldDirection': PVEOverrideTargetingModes.WorldDirection, u'LocalDirection': PVEOverrideTargetingModes.LocalDirection, u'Null': PVEOverrideTargetingModes.Null}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVEOverrideTargetingModes'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class PVESpotHitCheckers(AISpotHitCheckers):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVESpotHitCheckers'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def calculateProjectileTrajectory(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def estimateTargetArmor(self, *args, **kwargs): pass
	def findCollisionsOnTrajectory(self, *args, **kwargs): pass
	def isTargetLineCollideStatic(self, *args, **kwargs): pass
	def isTargetLineCollideVehicles(self, *args, **kwargs): pass
	def onConfigUpdated(self, *args, **kwargs): pass
	def onVehicleKilled(self, *args, **kwargs): pass
	penetrationConfig = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass
	def setDebugDrawAlliesCollision(self, *args, **kwargs): pass
	def setDebugDrawSPGTrajectory(self, *args, **kwargs): pass
	def targetPointWithinTurretLimits(self, *args, **kwargs): pass


class PVESpotTargetingParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVESpotTargetingParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	aimingModes = u'PVE.shootingModes'
	overrideTargetingCanHit = u'PVE.overrideTargetingCanHit'
	overrideTargetingMode = u'PVE.overrideTargetingMode'
	overrideTargetingVector = u'PVE.overrideTargetingVector'
	shootingModes = u'PVE.aimingModes'


class TankEntitySensor(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankEntitySensor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addTeamBase(self, *args, **kwargs): pass
	allEnemies = property(lambda self: None)
	def checkDataUpdate(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	directDetectedEnemies = property(lambda self: None)
	enemyBasesWasDeleted = property(lambda self: None)
	def flushSensorDebugInfo(self, *args, **kwargs): pass
	def getActiveAllyList(self, *args, **kwargs): pass
	def getActiveEnemyVehicleList(self, *args, **kwargs): pass
	def getActiveEnemyVehicleListSensorData(self, *args, **kwargs): pass
	def getAliveAlliesCount(self, *args, **kwargs): pass
	def getAliveEnemyCount(self, *args, **kwargs): pass
	def getAlliesInArea(self, *args, **kwargs): pass
	def getAlliesInRadius(self, *args, **kwargs): pass
	def getClosestAlliedBaseDataToPosition(self, *args, **kwargs): pass
	def getClosestAlliedBasePosition(self, *args, **kwargs): pass
	def getClosestAlliedBaseUnderAttackData(self, *args, **kwargs): pass
	def getClosestEnemies(self, *args, **kwargs): pass
	def getClosestEnemyBaseDataToPosition(self, *args, **kwargs): pass
	def getClosestEnemyBasePosition(self, *args, **kwargs): pass
	def getClosestFriends(self, *args, **kwargs): pass
	def getDestroyedEnemiesList(self, *args, **kwargs): pass
	def getDestroyedVehicleList(self, *args, **kwargs): pass
	def getEnemiesAdvanced(self, *args, **kwargs): pass
	def getEnemiesInArea(self, *args, **kwargs): pass
	def getEnemiesInRadius(self, *args, **kwargs): pass
	def getEnemyPosition(self, *args, **kwargs): pass
	def getEnemySensorDataDict(self, *args, **kwargs): pass
	def getEnemyThreatsForPositions(self, *args, **kwargs): pass
	def getLastSomeoneAliveWasDirectlyDetectedTime(self, *args, **kwargs): pass
	def getNumberOfAlliesInArea(self, *args, **kwargs): pass
	def getNumberOfAlliesInRadius(self, *args, **kwargs): pass
	def getNumberOfEnemiesInArea(self, *args, **kwargs): pass
	def getNumberOfEnemiesInRadius(self, *args, **kwargs): pass
	def getNumberOfVisibleEnemies(self, *args, **kwargs): pass
	def getShotsForTime(self, *args, **kwargs): pass
	def getTeamBases(self, *args, **kwargs): pass
	def hasEnemies(self, *args, **kwargs): pass
	indirectDetectedEnemies = property(lambda self: None)
	def init(self, *args, **kwargs): pass
	def isAlliedBaseUnderAttack(self, *args, **kwargs): pass
	isAllyBaseUnderAttack = property(lambda self: None)
	def isCirclingMe(self, *args, **kwargs): pass
	def isEnemyAlive(self, *args, **kwargs): pass
	def isEnemyDetected(self, *args, **kwargs): pass
	def isEnemyInRadius(self, *args, **kwargs): pass
	def isEnemyInvader(self, *args, **kwargs): pass
	logger = property(lambda self: None)
	lostEnemies = property(lambda self: None)
	neverDetectedEnemies = property(lambda self: None)
	nonLostEnemies = property(lambda self: None)
	def onEntitySet(self, *args, **kwargs): pass
	def onTankAlive(self, *args, **kwargs): pass
	def onTankEntityCreated(self, *args, **kwargs): pass
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def onTankEntitySwitchedTeam(self, *args, **kwargs): pass
	def onTankKilled(self, *args, **kwargs): pass
	def receiveLostEnemiesUpdate(self, *args, **kwargs): pass
	def receiveShot(self, *args, **kwargs): pass
	def receiveVisibilityUpdate(self, *args, **kwargs): pass
	def removeTeamBase(self, *args, **kwargs): pass
	def resume(self, *args, **kwargs): pass
	def setEnemyExposedPosition(self, *args, **kwargs): pass
	def setEnemyExposure(self, *args, **kwargs): pass
	def setRecheckTargetExposureCallback(self, *args, **kwargs): pass
	def setTeamBaseCaptureInfo(self, *args, **kwargs): pass
	def setTryToSelectCallback(self, *args, **kwargs): pass
	def suspend(self, *args, **kwargs): pass
	undetectedEnemies = property(lambda self: None)
	def updateInvadersList(self, *args, **kwargs): pass


class PVETankEntitySensor(TankEntitySensor):
	CustomParameter_IgnoreShotsFromStealth = u'IgnoreShotsFromStealth'
	CustomParameter_NoStartDisposition = u'NoStartDisposition'
	CustomParameter_SeeAllEnemies = u'SeeAllEnemies'
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PVETankEntitySensor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addTeamBase(self, *args, **kwargs): pass
	allEnemies = property(lambda self: None)
	def checkDataUpdate(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	directDetectedEnemies = property(lambda self: None)
	enemyBasesWasDeleted = property(lambda self: None)
	def flushSensorDebugInfo(self, *args, **kwargs): pass
	def getActiveAllyList(self, *args, **kwargs): pass
	def getActiveEnemyVehicleList(self, *args, **kwargs): pass
	def getActiveEnemyVehicleListSensorData(self, *args, **kwargs): pass
	def getAliveAlliesCount(self, *args, **kwargs): pass
	def getAliveEnemyCount(self, *args, **kwargs): pass
	def getAlliesInArea(self, *args, **kwargs): pass
	def getAlliesInRadius(self, *args, **kwargs): pass
	def getClosestAlliedBaseDataToPosition(self, *args, **kwargs): pass
	def getClosestAlliedBasePosition(self, *args, **kwargs): pass
	def getClosestAlliedBaseUnderAttackData(self, *args, **kwargs): pass
	def getClosestEnemies(self, *args, **kwargs): pass
	def getClosestEnemyBaseDataToPosition(self, *args, **kwargs): pass
	def getClosestEnemyBasePosition(self, *args, **kwargs): pass
	def getClosestFriends(self, *args, **kwargs): pass
	def getDestroyedEnemiesList(self, *args, **kwargs): pass
	def getDestroyedVehicleList(self, *args, **kwargs): pass
	def getEnemiesAdvanced(self, *args, **kwargs): pass
	def getEnemiesInArea(self, *args, **kwargs): pass
	def getEnemiesInRadius(self, *args, **kwargs): pass
	def getEnemyPosition(self, *args, **kwargs): pass
	def getEnemySensorDataDict(self, *args, **kwargs): pass
	def getEnemyThreatsForPositions(self, *args, **kwargs): pass
	def getLastSomeoneAliveWasDirectlyDetectedTime(self, *args, **kwargs): pass
	def getNumberOfAlliesInArea(self, *args, **kwargs): pass
	def getNumberOfAlliesInRadius(self, *args, **kwargs): pass
	def getNumberOfEnemiesInArea(self, *args, **kwargs): pass
	def getNumberOfEnemiesInRadius(self, *args, **kwargs): pass
	def getNumberOfVisibleEnemies(self, *args, **kwargs): pass
	def getShotsForTime(self, *args, **kwargs): pass
	def getTeamBases(self, *args, **kwargs): pass
	def hasEnemies(self, *args, **kwargs): pass
	indirectDetectedEnemies = property(lambda self: None)
	def init(self, *args, **kwargs): pass
	def isAlliedBaseUnderAttack(self, *args, **kwargs): pass
	isAllyBaseUnderAttack = property(lambda self: None)
	def isCirclingMe(self, *args, **kwargs): pass
	def isEnemyAlive(self, *args, **kwargs): pass
	def isEnemyDetected(self, *args, **kwargs): pass
	def isEnemyInRadius(self, *args, **kwargs): pass
	def isEnemyInvader(self, *args, **kwargs): pass
	logger = property(lambda self: None)
	lostEnemies = property(lambda self: None)
	neverDetectedEnemies = property(lambda self: None)
	nonLostEnemies = property(lambda self: None)
	def onEntitySet(self, *args, **kwargs): pass
	def onTankAlive(self, *args, **kwargs): pass
	def onTankEntityCreated(self, *args, **kwargs): pass
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def onTankEntitySwitchedTeam(self, *args, **kwargs): pass
	def onTankKilled(self, *args, **kwargs): pass
	def receiveLostEnemiesUpdate(self, *args, **kwargs): pass
	def receiveShot(self, *args, **kwargs): pass
	def receiveVisibilityUpdate(self, *args, **kwargs): pass
	def removeTeamBase(self, *args, **kwargs): pass
	def resume(self, *args, **kwargs): pass
	def setEnemyExposedPosition(self, *args, **kwargs): pass
	def setEnemyExposure(self, *args, **kwargs): pass
	def setRecheckTargetExposureCallback(self, *args, **kwargs): pass
	def setTeamBaseCaptureInfo(self, *args, **kwargs): pass
	def setTryToSelectCallback(self, *args, **kwargs): pass
	def suspend(self, *args, **kwargs): pass
	undetectedEnemies = property(lambda self: None)
	def updateInvadersList(self, *args, **kwargs): pass


class PassiveReconAgentCore(CombatCoverAgentCore):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PassiveReconAgentCore'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkIsCoverValid(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def findAndReserveBestCover(self, *args, **kwargs): pass
	def occupyCover(self, *args, **kwargs): pass
	def onBTReset(self, *args, **kwargs): pass
	def resetCover(self, *args, **kwargs): pass


class PathPointValidator(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathPointValidator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPointAcceptable(self, *args, **kwargs): pass


class PathPointValidatorAvoidDetection(PathPointValidator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathPointValidatorAvoidDetection'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPointAcceptable(self, *args, **kwargs): pass


class PathPointValidatorCombo(PathPointValidator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathPointValidatorCombo'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPointAcceptable(self, *args, **kwargs): pass


class PathPointValidatorRadius(PathPointValidator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathPointValidatorRadius'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPointAcceptable(self, *args, **kwargs): pass


class PathPointValidatorZone(PathPointValidator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathPointValidatorZone'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def isPointAcceptable(self, *args, **kwargs): pass


class uai__DetourPathQuery(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'uai::DetourPathQuery'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def findCorridorPath(self, *args, **kwargs): pass
	def findDistanceToWall(self, *args, **kwargs): pass
	def getClosestGoal(self, *args, **kwargs): pass
	def getClosestNavmeshPoint(self, *args, **kwargs): pass
	def getPath(self, *args, **kwargs): pass
	def getPathAndCostToMultipleGoals(self, *args, **kwargs): pass
	def getPathToBestPosition(self, *args, **kwargs): pass
	def getRandomPointOnNavmesh(self, *args, **kwargs): pass
	def initPathCorridor(self, *args, **kwargs): pass
	def initialize(self, *args, **kwargs): pass
	def isValidNavmeshPoint(self, *args, **kwargs): pass
	def movePositionCorridor(self, *args, **kwargs): pass
	def navmeshRaycast(self, *args, **kwargs): pass
	def optimizeCorridorPath(self, *args, **kwargs): pass
	def setSlopeCostFunctorWeight(self, *args, **kwargs): pass


class PathQuery(uai__DetourPathQuery):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathQuery'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def findCorridorPath(self, *args, **kwargs): pass
	def findDistanceToWall(self, *args, **kwargs): pass
	def getClosestGoal(self, *args, **kwargs): pass
	def getClosestNavmeshPoint(self, *args, **kwargs): pass
	def getPath(self, *args, **kwargs): pass
	def getPathAndCostToMultipleGoals(self, *args, **kwargs): pass
	def getPathToBestPosition(self, *args, **kwargs): pass
	def getRandomPointOnNavmesh(self, *args, **kwargs): pass
	def initPathCorridor(self, *args, **kwargs): pass
	def initialize(self, *args, **kwargs): pass
	def isValidNavmeshPoint(self, *args, **kwargs): pass
	def movePositionCorridor(self, *args, **kwargs): pass
	def navmeshRaycast(self, *args, **kwargs): pass
	def optimizeCorridorPath(self, *args, **kwargs): pass
	def setNearbyEnemiesCostFunctorWeight(self, *args, **kwargs): pass
	def setSlopeCostFunctorWeight(self, *args, **kwargs): pass
	def setTacticalCostFunctoWeight(self, *args, **kwargs): pass


class PathQueryContext(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathQueryContext'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	agent = property(lambda self: None)
	agentGirth = property(lambda self: None)
	agentRadius = property(lambda self: None)
	aiData = property(lambda self: None)
	coversPathfindingQueryBuffer = property(lambda self: None)
	enemyInfluenceMap = property(lambda self: None)
	enemyTeamID = property(lambda self: None)
	def getAliveEnemyPositions(self, *args, **kwargs): pass
	def getDeadObstaclesWeights(self, *args, **kwargs): pass
	def getNavmesh(self, *args, **kwargs): pass
	def getSpaceID(self, *args, **kwargs): pass
	def isPushableVehicle(self, *args, **kwargs): pass
	navMeshCheckQueryBuffer = property(lambda self: None)
	ownID = property(lambda self: None)
	ownInfluenceMap = property(lambda self: None)
	ownTeam = property(lambda self: None)
	ownWeight = property(lambda self: None)
	pathfindingQueryBuffer = property(lambda self: None)
	def setAgent(self, *args, **kwargs): pass
	def setMovementAgentGirth(self, *args, **kwargs): pass
	def setNavmesh(self, *args, **kwargs): pass
	threatInfluenceScale = property(lambda self: None)


class PathThreatEvaluationParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PathThreatEvaluationParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	currentOrientationFactorScale = property(lambda self: None)
	distantThreatDistanceFactor = property(lambda self: None)
	distantThreatIgnoreThreshold = property(lambda self: None)
	firstThreatPointBaseWeight = property(lambda self: None)
	fullVisibilityThreshold = property(lambda self: None)
	lastThreatPointBaseWeight = property(lambda self: None)
	lookAheadNumPoints = property(lambda self: None)
	maxThreatDistance = property(lambda self: None)
	minThreatDistance = property(lambda self: None)
	nearbyCoverDistanceLimit = property(lambda self: None)
	safeThreatRatioThreshold = property(lambda self: None)
	scoreDiffThresholds = property(lambda self: None)
	threatCheckCooldown = property(lambda self: None)
	threatCosThresholdFront = property(lambda self: None)
	threatCosThresholdRear = property(lambda self: None)
	threatOrientationDistanceEps = property(lambda self: None)
	threatPointsWeightsSum = property(lambda self: None)


class PenetrationEstimationParams(pybind11_object):
	PENETRATION_CHANCE_THRESHOLD_MAX = property(lambda self: None)
	PENETRATION_CHANCE_THRESHOLD_MIN = property(lambda self: None)
	PENETRATION_CHANCE_THRESHOLD_REDUCTION = property(lambda self: None)
	PENETRATION_CHANCE_THRESHOLD_SENSORS = property(lambda self: None)
	SKIP_ARMOR_PENETRATION_CHECK = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PenetrationEstimationParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class PointCheckResult(pybind11_object):
	ARMORED = PointCheckResult.ARMORED
	BEHIND_ANOTHER_VEHICLE = PointCheckResult.BEHIND_ANOTHER_VEHICLE
	BEHIND_OBSTACLE = PointCheckResult.BEHIND_OBSTACLE
	EXPOSED = PointCheckResult.EXPOSED
	OUT_OF_GUN_ANGLE_LIMITS = PointCheckResult.OUT_OF_GUN_ANGLE_LIMITS
	OUT_OF_SILHOUETTE = PointCheckResult.OUT_OF_SILHOUETTE
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  OUT_OF_SILHOUETTE\n\n  BEHIND_ANOTHER_VEHICLE\n\n  BEHIND_OBSTACLE\n\n  ARMORED\n\n  EXPOSED\n\n  OUT_OF_GUN_ANGLE_LIMITS'
	__entries = {u'OUT_OF_SILHOUETTE': (PointCheckResult.OUT_OF_SILHOUETTE, None), u'BEHIND_ANOTHER_VEHICLE': (PointCheckResult.BEHIND_ANOTHER_VEHICLE, None), u'BEHIND_OBSTACLE': (PointCheckResult.BEHIND_OBSTACLE, None), u'ARMORED': (PointCheckResult.ARMORED, None), u'EXPOSED': (PointCheckResult.EXPOSED, None), u'OUT_OF_GUN_ANGLE_LIMITS': (PointCheckResult.OUT_OF_GUN_ANGLE_LIMITS, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'OUT_OF_GUN_ANGLE_LIMITS': PointCheckResult.OUT_OF_GUN_ANGLE_LIMITS, u'BEHIND_ANOTHER_VEHICLE': PointCheckResult.BEHIND_ANOTHER_VEHICLE, u'OUT_OF_SILHOUETTE': PointCheckResult.OUT_OF_SILHOUETTE, u'ARMORED': PointCheckResult.ARMORED, u'EXPOSED': PointCheckResult.EXPOSED, u'BEHIND_OBSTACLE': PointCheckResult.BEHIND_OBSTACLE}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PointCheckResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class PositionType(pybind11_object):
	CirclingTarget = PositionType.CirclingTarget
	ClosestDetectedEnemy = PositionType.ClosestDetectedEnemy
	ClosestDetectedEnemyInZone = PositionType.ClosestDetectedEnemyInZone
	ClosestUndetectedEnemy = PositionType.ClosestUndetectedEnemy
	ClosestUndetectedEnemyInZone = PositionType.ClosestUndetectedEnemyInZone
	CoverPoint = PositionType.CoverPoint
	CurrentTarget = PositionType.CurrentTarget
	Enemies = PositionType.Enemies
	EnemyBase = PositionType.EnemyBase
	EnemyZoneEntryPoints = PositionType.EnemyZoneEntryPoints
	FarthestUndetectedEnemyInZone = PositionType.FarthestUndetectedEnemyInZone
	MoveLinkInZoneToEnemyBase = PositionType.MoveLinkInZoneToEnemyBase
	MoveLinksToContestedZones = PositionType.MoveLinksToContestedZones
	MoveLinksToHostileZones = PositionType.MoveLinksToHostileZones
	NearestFriend = PositionType.NearestFriend
	NearestPlayerFriend = PositionType.NearestPlayerFriend
	OwnBase = PositionType.OwnBase
	PassiveReconCoversPoint = PositionType.PassiveReconCoversPoint
	PositionForCircling = PositionType.PositionForCircling
	PositionForCirclingRoleTarget = PositionType.PositionForCirclingRoleTarget
	RoleTarget = PositionType.RoleTarget
	SavedPosition = PositionType.SavedPosition
	Self = PositionType.Self
	ShootLinkInZoneToEnemyBase = PositionType.ShootLinkInZoneToEnemyBase
	ShootLinksFromContestedZones = PositionType.ShootLinksFromContestedZones
	ShootLinksFromHostileZones = PositionType.ShootLinksFromHostileZones
	ShootingPoint = PositionType.ShootingPoint
	SnipePoint = PositionType.SnipePoint
	SpawnPosition = PositionType.SpawnPosition
	ZoneEntryPoint = PositionType.ZoneEntryPoint
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  PositionForCircling\n\n  PositionForCirclingRoleTarget\n\n  PassiveReconCoversPoint\n\n  Self\n\n  CoverPoint\n\n  ClosestDetectedEnemy\n\n  ZoneEntryPoint\n\n  OwnBase\n\n  ShootLinksFromContestedZones\n\n  CurrentTarget\n\n  NearestPlayerFriend\n\n  SpawnPosition\n\n  EnemyBase\n\n  MoveLinkInZoneToEnemyBase\n\n  ShootLinkInZoneToEnemyBase\n\n  SavedPosition\n\n  ClosestDetectedEnemyInZone\n\n  FarthestUndetectedEnemyInZone\n\n  SnipePoint\n\n  ClosestUndetectedEnemy\n\n  MoveLinksToHostileZones\n\n  ShootingPoint\n\n  MoveLinksToContestedZones\n\n  ClosestUndetectedEnemyInZone\n\n  CirclingTarget\n\n  ShootLinksFromHostileZones\n\n  EnemyZoneEntryPoints\n\n  NearestFriend\n\n  RoleTarget\n\n  Enemies'
	__entries = {u'PositionForCircling': (PositionType.PositionForCircling, None), u'PositionForCirclingRoleTarget': (PositionType.PositionForCirclingRoleTarget, None), u'PassiveReconCoversPoint': (PositionType.PassiveReconCoversPoint, None), u'Self': (PositionType.Self, None), u'CoverPoint': (PositionType.CoverPoint, None), u'ClosestDetectedEnemy': (PositionType.ClosestDetectedEnemy, None), u'ZoneEntryPoint': (PositionType.ZoneEntryPoint, None), u'OwnBase': (PositionType.OwnBase, None), u'ShootLinksFromContestedZones': (PositionType.ShootLinksFromContestedZones, None), u'CurrentTarget': (PositionType.CurrentTarget, None), u'NearestPlayerFriend': (PositionType.NearestPlayerFriend, None), u'SpawnPosition': (PositionType.SpawnPosition, None), u'EnemyBase': (PositionType.EnemyBase, None), u'MoveLinkInZoneToEnemyBase': (PositionType.MoveLinkInZoneToEnemyBase, None), u'ShootLinkInZoneToEnemyBase': (PositionType.ShootLinkInZoneToEnemyBase, None), u'SavedPosition': (PositionType.SavedPosition, None), u'ClosestDetectedEnemyInZone': (PositionType.ClosestDetectedEnemyInZone, None), u'FarthestUndetectedEnemyInZone': (PositionType.FarthestUndetectedEnemyInZone, None), u'SnipePoint': (PositionType.SnipePoint, None), u'ClosestUndetectedEnemy': (PositionType.ClosestUndetectedEnemy, None), u'MoveLinksToHostileZones': (PositionType.MoveLinksToHostileZones, None), u'ShootingPoint': (PositionType.ShootingPoint, None), u'MoveLinksToContestedZones': (PositionType.MoveLinksToContestedZones, None), u'ClosestUndetectedEnemyInZone': (PositionType.ClosestUndetectedEnemyInZone, None), u'CirclingTarget': (PositionType.CirclingTarget, None), u'ShootLinksFromHostileZones': (PositionType.ShootLinksFromHostileZones, None), u'EnemyZoneEntryPoints': (PositionType.EnemyZoneEntryPoints, None), u'NearestFriend': (PositionType.NearestFriend, None), u'RoleTarget': (PositionType.RoleTarget, None), u'Enemies': (PositionType.Enemies, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'PositionForCircling': PositionType.PositionForCircling, u'PositionForCirclingRoleTarget': PositionType.PositionForCirclingRoleTarget, u'PassiveReconCoversPoint': PositionType.PassiveReconCoversPoint, u'Self': PositionType.Self, u'CoverPoint': PositionType.CoverPoint, u'ClosestDetectedEnemy': PositionType.ClosestDetectedEnemy, u'ZoneEntryPoint': PositionType.ZoneEntryPoint, u'OwnBase': PositionType.OwnBase, u'ShootLinksFromContestedZones': PositionType.ShootLinksFromContestedZones, u'CurrentTarget': PositionType.CurrentTarget, u'NearestPlayerFriend': PositionType.NearestPlayerFriend, u'RoleTarget': PositionType.RoleTarget, u'EnemyBase': PositionType.EnemyBase, u'SnipePoint': PositionType.SnipePoint, u'ShootLinkInZoneToEnemyBase': PositionType.ShootLinkInZoneToEnemyBase, u'SavedPosition': PositionType.SavedPosition, u'ClosestDetectedEnemyInZone': PositionType.ClosestDetectedEnemyInZone, u'FarthestUndetectedEnemyInZone': PositionType.FarthestUndetectedEnemyInZone, u'MoveLinkInZoneToEnemyBase': PositionType.MoveLinkInZoneToEnemyBase, u'ClosestUndetectedEnemy': PositionType.ClosestUndetectedEnemy, u'MoveLinksToHostileZones': PositionType.MoveLinksToHostileZones, u'ShootingPoint': PositionType.ShootingPoint, u'MoveLinksToContestedZones': PositionType.MoveLinksToContestedZones, u'ClosestUndetectedEnemyInZone': PositionType.ClosestUndetectedEnemyInZone, u'CirclingTarget': PositionType.CirclingTarget, u'ShootLinksFromHostileZones': PositionType.ShootLinksFromHostileZones, u'EnemyZoneEntryPoints': PositionType.EnemyZoneEntryPoints, u'NearestFriend': PositionType.NearestFriend, u'SpawnPosition': PositionType.SpawnPosition, u'Enemies': PositionType.Enemies}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PositionType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class PyAITargeting(AITargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyAITargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def _applyExtraScore(self, *args, **kwargs): pass
	def _computeAimingTimeAfterChassisTurning(self, *args, **kwargs): pass
	def _computeBaseScore(self, *args, **kwargs): pass
	def _computeBonusScore(self, *args, **kwargs): pass
	def _computeDistanceScore(self, *args, **kwargs): pass
	def _computeDistractionScore(self, *args, **kwargs): pass
	def _computeEnemyAlphaScore(self, *args, **kwargs): pass
	def _computeEnemyAutoLoaderScore(self, *args, **kwargs): pass
	def _computeEnemyCurrentSpeedScore(self, *args, **kwargs): pass
	def _computeEnemyDetectionScore(self, *args, **kwargs): pass
	def _computeEnemyExposureScore(self, *args, **kwargs): pass
	def _computeEnemyPenetrationScore(self, *args, **kwargs): pass
	def _computeEnemyRemainingHPScore(self, *args, **kwargs): pass
	def _computeFocusFireScore(self, *args, **kwargs): pass
	def _computeHitChanceScore(self, *args, **kwargs): pass
	def _computeInvaderScore(self, *args, **kwargs): pass
	def _computeOutOfYawLimitsScore(self, *args, **kwargs): pass
	def _computePenetrationScore(self, *args, **kwargs): pass
	def _computePersonalThreatScore(self, *args, **kwargs): pass
	def _computePlayerVehicleScore(self, *args, **kwargs): pass
	def _computePriorityAreaScore(self, *args, **kwargs): pass
	def _computeSecondaryScores(self, *args, **kwargs): pass
	def _computeStickOnTargetScore(self, *args, **kwargs): pass
	def _computeTankTypeScore(self, *args, **kwargs): pass
	def _computeTimeToAimScore(self, *args, **kwargs): pass
	def _enemyExposureScoreVisibilityGridCheck(self, *args, **kwargs): pass
	def _getScoreBase(self, *args, **kwargs): pass
	def _selectTarget(self, *args, **kwargs): pass
	def _setTarget(self, *args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class uai.Agent(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'uai.Agent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addCombatant(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def clearCombatants(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	entity = property(lambda self: None)
	def getAliveThreats(self, *args, **kwargs): pass
	def getAliveValidAllies(self, *args, **kwargs): pass
	def getAliveValidThreats(self, *args, **kwargs): pass
	def getAllCombatants(self, *args, **kwargs): pass
	def getDeadCombatants(self, *args, **kwargs): pass
	def getEntity(self, *args, **kwargs): pass
	def getObstacleIds(self, *args, **kwargs): pass
	id = property(lambda self: None)
	def markObstacle(self, *args, **kwargs): pass
	def onCombatantStatusChange(self, *args, **kwargs): pass
	position = property(lambda self: None)
	def removeCombatant(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def unmarkObstacle(self, *args, **kwargs): pass


class PyAgent(uai.Agent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyAgent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addCombatant(self, *args, **kwargs): pass
	aimingMode = property(lambda self: None)
	def clear(self, *args, **kwargs): pass
	def clearCombatants(self, *args, **kwargs): pass
	coversParams = property(lambda self: None)
	coversState = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	entity = property(lambda self: None)
	def getAliveThreats(self, *args, **kwargs): pass
	def getAliveValidAllies(self, *args, **kwargs): pass
	def getAliveValidThreats(self, *args, **kwargs): pass
	def getAllCombatants(self, *args, **kwargs): pass
	def getDeadCombatants(self, *args, **kwargs): pass
	def getEntity(self, *args, **kwargs): pass
	def getNotActiveInCombatTime(self, *args, **kwargs): pass
	def getObstacleIds(self, *args, **kwargs): pass
	def getThreatsOnCurrentRoute(self, *args, **kwargs): pass
	id = property(lambda self: None)
	def initCovers(self, *args, **kwargs): pass
	def markObstacle(self, *args, **kwargs): pass
	def onCombatantStatusChange(self, *args, **kwargs): pass
	position = property(lambda self: None)
	def removeCombatant(self, *args, **kwargs): pass
	def setCircling(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setFireController(self, *args, **kwargs): pass
	def setGetMovementTargetFunc(self, *args, **kwargs): pass
	def setGetTimeSinceLastRoleTargetReachedFunc(self, *args, **kwargs): pass
	def setLogger(self, *args, **kwargs): pass
	def setMovementLogger(self, *args, **kwargs): pass
	def setSensor(self, *args, **kwargs): pass
	def setService(self, *args, **kwargs): pass
	def setSpotTargeting(self, *args, **kwargs): pass
	def setStats(self, *args, **kwargs): pass
	def setTacticalLogger(self, *args, **kwargs): pass
	def setTargeting(self, *args, **kwargs): pass
	def shutdownCovers(self, *args, **kwargs): pass
	def unmarkObstacle(self, *args, **kwargs): pass


class PyBTThreadDecorator(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTThreadDecorator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyBTDebugThreadDecorator(PyBTThreadDecorator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTDebugThreadDecorator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def fetchDebugStates(self, *args, **kwargs): pass


class PyBTNode(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTDecoratorFail(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTDecoratorFail'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTDecoratorNot(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTDecoratorNot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTDecoratorRunning(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTDecoratorRunning'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTDecoratorSuccess(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTDecoratorSuccess'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTNodeDecorator(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTNodeDecorator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyBTFunctionContainer(PyBTNodeDecorator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTFunctionContainer'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	function = property(lambda self: None)
	functionParams = property(lambda self: None)
	resetFunction = property(lambda self: None)
	resetFunctionParams = property(lambda self: None)


class PyBTGoalEnterSlot(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTGoalEnterSlot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTGoalExitSlot(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTGoalExitSlot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTGoalUpdateSlot(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTGoalUpdateSlot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTIntervalUpdateDecorator(PyBTNodeDecorator):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTIntervalUpdateDecorator'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyBTLeaf(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTLeaf'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	function = property(lambda self: None)
	def getFunctionName(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	parameters = property(lambda self: None)
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTParallelAllSucceed(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTParallelAllSucceed'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTParallelOneSucceed(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTParallelOneSucceed'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTRandomChoice(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTRandomChoice'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def addProbability(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class uai.BTRuntime(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'uai.BTRuntime'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyBTRuntime(uai.BTRuntime):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTRuntime'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addThreadDecorator(self, *args, **kwargs): pass
	def canChangeGoal(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def getGoalBT(self, *args, **kwargs): pass
	def getSlotBt(self, *args, **kwargs): pass
	def getUniqueCallID(self, *args, **kwargs): pass
	def removeThreadDecorator(self, *args, **kwargs): pass
	def requestGoalChange(self, *args, **kwargs): pass
	def reset(self, *args, **kwargs): pass
	def setGoalBT(self, *args, **kwargs): pass
	def setResetCallback(self, *args, **kwargs): pass
	def setSlotBT(self, *args, **kwargs): pass
	state = property(lambda self: None)
	tree = property(lambda self: None)


class PyBTSelector(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTSelector'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTSequence(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTSequence'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class PyBTSlot(PyBTNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyBTSlot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def addDecorator(self, *args, **kwargs): pass
	def getInterruptionFlag(self, *args, **kwargs): pass
	def setInterruptionFlag(self, *args, **kwargs): pass


class UAIEntity(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdatable(self, *args, **kwargs): pass
	direction = property(lambda self: None)
	entityId = property(lambda self: None)
	def getObstacleCreationTick(self, *args, **kwargs): pass
	id = property(lambda self: None)
	isAlive = property(lambda self: None)
	obstacle = property(lambda self: None)
	obstacleAreaId = property(lambda self: None)
	position = property(lambda self: None)
	def removeUpdatable(self, *args, **kwargs): pass
	scene = property(lambda self: None)
	type = property(lambda self: None)
	yaw = property(lambda self: None)


class PyEntity(UAIEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdatable(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	direction = property(lambda self: None)
	entityId = property(lambda self: None)
	def getObstacleCreationTick(self, *args, **kwargs): pass
	id = property(lambda self: None)
	isAlive = property(lambda self: None)
	obstacle = property(lambda self: None)
	obstacleAreaId = property(lambda self: None)
	position = property(lambda self: None)
	def removeUpdatable(self, *args, **kwargs): pass
	scene = property(lambda self: None)
	type = property(lambda self: None)
	yaw = property(lambda self: None)


class PyMovingTracker(IUpdatable):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyMovingTracker'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	distanceThreshold = property(lambda self: None)
	onStartMoving = property(lambda self: None)
	onStopMoving = property(lambda self: None)
	def setPhysicalEntity(self, *args, **kwargs): pass
	speedThreshold = property(lambda self: None)


class PyPVECircling(PVECircling):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyPVECircling'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def _applyExtraScore(self, *args, **kwargs): pass
	def _computeAlliesFlankScore(self, *args, **kwargs): pass
	def _computeBaseScore(self, *args, **kwargs): pass
	def _computeCirclingRadiusScore(self, *args, **kwargs): pass
	def _computeEnemyDetectionScore(self, *args, **kwargs): pass
	def _computeHullDirectionScore(self, *args, **kwargs): pass
	def _computeMovementDirectionScore(self, *args, **kwargs): pass
	def _computePathLengthScore(self, *args, **kwargs): pass
	def _computeStickOnTargetScore(self, *args, **kwargs): pass
	def _computeTargetTurretDirectionScore(self, *args, **kwargs): pass
	def _computeVisibilityScore(self, *args, **kwargs): pass
	def _getScoreBase(self, *args, **kwargs): pass
	def _skipOutMaxDrawRadius(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getCirclingPosition(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	onDebugPoints = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def selectTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass


class PyPVETargeting(PVETargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyPVETargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def _applyExtraScore(self, *args, **kwargs): pass
	def _computeAimingTimeAfterChassisTurning(self, *args, **kwargs): pass
	def _computeBaseScore(self, *args, **kwargs): pass
	def _computeBonusScore(self, *args, **kwargs): pass
	def _computeDistanceScore(self, *args, **kwargs): pass
	def _computeDistractionScore(self, *args, **kwargs): pass
	def _computeEnemyAlphaScore(self, *args, **kwargs): pass
	def _computeEnemyAutoLoaderScore(self, *args, **kwargs): pass
	def _computeEnemyCurrentSpeedScore(self, *args, **kwargs): pass
	def _computeEnemyDetectionScore(self, *args, **kwargs): pass
	def _computeEnemyExposureScore(self, *args, **kwargs): pass
	def _computeEnemyPenetrationScore(self, *args, **kwargs): pass
	def _computeEnemyRemainingHPScore(self, *args, **kwargs): pass
	def _computeFocusFireScore(self, *args, **kwargs): pass
	def _computeHitChanceScore(self, *args, **kwargs): pass
	def _computeInvaderScore(self, *args, **kwargs): pass
	def _computeOutOfYawLimitsScore(self, *args, **kwargs): pass
	def _computePenetrationScore(self, *args, **kwargs): pass
	def _computePersonalThreatScore(self, *args, **kwargs): pass
	def _computePlayerVehicleScore(self, *args, **kwargs): pass
	def _computePriorityAreaScore(self, *args, **kwargs): pass
	def _computeSecondaryScores(self, *args, **kwargs): pass
	def _computeStickOnTargetScore(self, *args, **kwargs): pass
	def _computeTankTypeScore(self, *args, **kwargs): pass
	def _computeTimeToAimScore(self, *args, **kwargs): pass
	def _enemyExposureScoreVisibilityGridCheck(self, *args, **kwargs): pass
	def _getScoreBase(self, *args, **kwargs): pass
	def _selectTarget(self, *args, **kwargs): pass
	def _setTarget(self, *args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class PyPhysicsEntity(PyEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyPhysicsEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdatable(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	direction = property(lambda self: None)
	entityId = property(lambda self: None)
	def getObstacleCreationTick(self, *args, **kwargs): pass
	id = property(lambda self: None)
	isAlive = property(lambda self: None)
	obstacle = property(lambda self: None)
	obstacleAreaId = property(lambda self: None)
	physics = property(lambda self: None)
	physicsBody = property(lambda self: None)
	position = property(lambda self: None)
	def removeUpdatable(self, *args, **kwargs): pass
	rspeed = property(lambda self: None)
	scene = property(lambda self: None)
	speed = property(lambda self: None)
	type = property(lambda self: None)
	velocity = property(lambda self: None)
	weight = property(lambda self: None)
	yaw = property(lambda self: None)


class SceneProcessor(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SceneProcessor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyPhysicsEntitySyncProcessor(SceneProcessor):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyPhysicsEntitySyncProcessor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyRangeReconParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyRangeReconParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	debugMode = property(lambda self: None)
	excludedPoints = property(lambda self: None)
	maxDistance = property(lambda self: None)
	maxPointsToCheck = property(lambda self: None)
	penalty = property(lambda self: None)
	searchVisibleEnemies = property(lambda self: None)


class PyShootingTest(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyShootingTest'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	curTrajectoryMode = property(lambda self: None)
	destructibleHealthCb = property(lambda self: None)
	entitiesToAvoid = property(lambda self: None)
	entityCollisionCb = property(lambda self: None)
	epsilon = property(lambda self: None)
	gravityScalar = property(lambda self: None)
	gravityVector = property(lambda self: None)
	gunPositionLocal = property(lambda self: None)
	maxGunPitchLimits = property(lambda self: None)
	minGunPitchLimits = property(lambda self: None)
	def setGravity(self, *args, **kwargs): pass
	spaceID = property(lambda self: None)
	speed = property(lambda self: None)
	targetEntity = property(lambda self: None)
	timePeriod = property(lambda self: None)
	trajectoryMode = property(lambda self: None)
	turretPositionLocal = property(lambda self: None)
	turretYawLimits = property(lambda self: None)
	useDistanceLimit = property(lambda self: None)
	vehicleMatrix = property(lambda self: None)


class PyTankEntity(PyPhysicsEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyTankEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdatable(self, *args, **kwargs): pass
	aiMover = property(lambda self: None)
	attrs = property(lambda self: None)
	botSkill = property(lambda self: None)
	circularVisionRadius = property(lambda self: None)
	def collideSegment(self, *args, **kwargs): pass
	descriptor = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	direction = property(lambda self: None)
	entityId = property(lambda self: None)
	def getAllTankComponents(self, *args, **kwargs): pass
	def getFrontArmorInDefaultTurretPos(self, *args, **kwargs): pass
	def getHullFlatDir(self, *args, **kwargs): pass
	def getInvisibility(self, *args, **kwargs): pass
	def getObstacleCreationTick(self, *args, **kwargs): pass
	def getReloadTimeLeft(self, *args, **kwargs): pass
	def getShotDispersionExt(self, *args, **kwargs): pass
	def getShotDispersionFactors(self, *args, **kwargs): pass
	def getTankComponent(self, *args, **kwargs): pass
	def getTurretFlatDir(self, *args, **kwargs): pass
	def getTurretYaw(self, *args, **kwargs): pass
	gunAngles = property(lambda self: None)
	gunRotator = property(lambda self: None)
	hasRearGunPosition = property(lambda self: None)
	hasTurret = property(lambda self: None)
	health = property(lambda self: None)
	hullMainArmor = property(lambda self: None)
	hullWeakArmor = property(lambda self: None)
	id = property(lambda self: None)
	def initTankComponents(self, *args, **kwargs): pass
	isAlive = property(lambda self: None)
	isArty = property(lambda self: None)
	isBot = property(lambda self: None)
	def isDirectlyVisible(self, *args, **kwargs): pass
	def isIndirectlyVisible(self, *args, **kwargs): pass
	isObservedByEnemy = property(lambda self: None)
	isShooting = property(lambda self: None)
	isSpg = property(lambda self: None)
	isStationary = property(lambda self: None)
	def isVisible(self, *args, **kwargs): pass
	maxSpeed = property(lambda self: None)
	name = property(lambda self: None)
	obstacle = property(lambda self: None)
	obstacleAreaId = property(lambda self: None)
	def onDescriptorUpdated(self, *args, **kwargs): pass
	physics = property(lambda self: None)
	physicsBody = property(lambda self: None)
	position = property(lambda self: None)
	def receiveVisibilityUpdate(self, *args, **kwargs): pass
	def removeUpdatable(self, *args, **kwargs): pass
	rspeed = property(lambda self: None)
	scene = property(lambda self: None)
	def setLogger(self, *args, **kwargs): pass
	def setShotDispersionFactors(self, *args, **kwargs): pass
	def setVisibleEntities(self, *args, **kwargs): pass
	def setWeakSpots(self, *args, **kwargs): pass
	speed = property(lambda self: None)
	tankType = property(lambda self: None)
	teamID = property(lambda self: None)
	turretMainArmor = property(lambda self: None)
	turretWeakArmor = property(lambda self: None)
	turretYawLimit = property(lambda self: None)
	type = property(lambda self: None)
	velocity = property(lambda self: None)
	weight = property(lambda self: None)
	yaw = property(lambda self: None)


class PyTankEntityPhysicsSyncProcessor(SceneProcessor):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyTankEntityPhysicsSyncProcessor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class PyWorld(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PyWorld'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addScene(self, *args, **kwargs): pass
	debugParams = property(lambda self: None)
	def getScene(self, *args, **kwargs): pass
	def removeScene(self, *args, **kwargs): pass
	def update(self, *args, **kwargs): pass


class PythonConvertNode(PyUtilityNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PythonConvertNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass


class PythonFunctionNode(PyUtilityNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PythonFunctionNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass


class UtilityWeightedAggreagationNode(PyUtilityNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UtilityWeightedAggreagationNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass
	def setStopOnOne(self, *args, **kwargs): pass
	def setStopOnZero(self, *args, **kwargs): pass


class PythonWeightedAggregationNode(UtilityWeightedAggreagationNode):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'PythonWeightedAggregationNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addChild(self, *args, **kwargs): pass
	def getCached(self, *args, **kwargs): pass
	def getValue(self, *args, **kwargs): pass
	def resetCache(self, *args, **kwargs): pass
	def setStopOnOne(self, *args, **kwargs): pass
	def setStopOnZero(self, *args, **kwargs): pass


class QueryCoversPerfDiag(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'QueryCoversPerfDiag'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	msBuildPyResult = property(lambda self: None)
	msFillShootingPointNearPoint = property(lambda self: None)
	msFindCandidateCovers = property(lambda self: None)
	msRangeCandidateCovers = property(lambda self: None)
	msTestDefensiveCoverProtection = property(lambda self: None)
	msTestDefensiveShootingPoint = property(lambda self: None)
	msTotal = property(lambda self: None)
	msValidateShootingPoints = property(lambda self: None)
	numCandidates = property(lambda self: None)
	numDefensiveCoverTests = property(lambda self: None)
	numDefensiveSpTests = property(lambda self: None)
	numNavmeshNodesMax = property(lambda self: None)
	numNavmeshNodesTraversed = property(lambda self: None)
	rayCastsCount = property(lambda self: None)


class QueryCoversResult(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'QueryCoversResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	coverMode = property(lambda self: None)
	covers = property(lambda self: None)
	perfDiag = property(lambda self: None)


class QueryCoversResultEntry(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'QueryCoversResultEntry'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	arcs = property(lambda self: None)
	coverPoint = property(lambda self: None)
	enemyPosition = property(lambda self: None)
	hasPeekingLine = property(lambda self: None)
	id = property(lambda self: None)
	mode = property(lambda self: None)
	moveCost = property(lambda self: None)
	path = property(lambda self: None)
	peekingDirection = property(lambda self: None)
	shootingDirection = property(lambda self: None)
	shootingPointGun = property(lambda self: None)
	shootingPointVehicle = property(lambda self: None)
	type = property(lambda self: None)


class QueryVisibilityRegionResult(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'QueryVisibilityRegionResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	center = property(lambda self: None)
	radius = property(lambda self: None)
	visibilityValue = property(lambda self: None)


class ReconCoverMode(pybind11_object):
	Aggressive = ReconCoverMode.Aggressive
	Defensive = ReconCoverMode.Defensive
	Normal = ReconCoverMode.Normal
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Aggressive\n\n  Defensive\n\n  Normal'
	__entries = {u'Aggressive': (ReconCoverMode.Aggressive, None), u'Defensive': (ReconCoverMode.Defensive, None), u'Normal': (ReconCoverMode.Normal, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Defensive': ReconCoverMode.Defensive, u'Aggressive': ReconCoverMode.Aggressive, u'Normal': ReconCoverMode.Normal}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReconCoverMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ReconSpaceData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReconSpaceData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def empty(self, *args, **kwargs): pass
	def findRangeReconPoint(self, *args, **kwargs): pass
	def queryActiveReconCoverPairs(self, *args, **kwargs): pass


class ReconTarget(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ReconTarget'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	flags = property(lambda self: None)
	invisibility = property(lambda self: None)
	position = property(lambda self: None)


class Ricochet(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Ricochet'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	angle_mp = 0.05235987901687622
	angle_sub = 1.0
	def shouldRicochet(*args, **kwargs): pass
	thresholdCaliber = 1.0


class RoleAgent(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleAgent'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	active = property(lambda self: None)
	agent = property(lambda self: None)
	assignedRole = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	entityID = property(lambda self: None)
	id = property(lambda self: None)
	lastAssignmentUpdateTime = property(lambda self: None)


class RoleCreationConditions(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleCreationConditions'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	active = property(lambda self: None)
	def canActivate(self, *args, **kwargs): pass
	def canActivateDebugInfo(self, *args, **kwargs): pass
	def canDeactivate(self, *args, **kwargs): pass
	def canDeactivateDebugInfo(self, *args, **kwargs): pass
	context = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	identifier = property(lambda self: None)


class RoleDebugLogInterface(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleDebugLogInterface'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class RoleGameModeSubType(pybind11_object):
	Any = RoleGameModeSubType.Any
	Attack = RoleGameModeSubType.Attack
	Defend = RoleGameModeSubType.Defend
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Defend\n\n  Any\n\n  Attack'
	__entries = {u'Defend': (RoleGameModeSubType.Defend, None), u'Any': (RoleGameModeSubType.Any, None), u'Attack': (RoleGameModeSubType.Attack, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Attack': RoleGameModeSubType.Attack, u'Any': RoleGameModeSubType.Any, u'Defend': RoleGameModeSubType.Defend}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleGameModeSubType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class RoleInstance(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleInstance'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	context = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getAssignmentRawValue(self, *args, **kwargs): pass
	def getId(self, *args, **kwargs): pass
	id = property(lambda self: None)
	insistence = property(lambda self: None)
	priority = property(lambda self: None)
	roleIdentifier = property(lambda self: None)
	runtime = property(lambda self: None)


class RoleRuntime(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleRuntime'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	assignmentConditionNode = property(lambda self: None)
	assignmentFactors = property(lambda self: None)
	assignmentGlobalFactors = property(lambda self: None)
	def canActivate(self, *args, **kwargs): pass
	def canActivateDebugInfo(self, *args, **kwargs): pass
	def canDeactivate(self, *args, **kwargs): pass
	def canDeactivateDebugInfo(self, *args, **kwargs): pass
	def getAssignmentDebugInfo(self, *args, **kwargs): pass
	def getAssignmentValue(self, *args, **kwargs): pass
	def getPriorityDebugInfo(self, *args, **kwargs): pass
	def getPriorityValue(self, *args, **kwargs): pass
	identifier = property(lambda self: None)
	priority = property(lambda self: None)
	priorityConditionNode = property(lambda self: None)
	settings = property(lambda self: None)


class RoleSettings(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleSettings'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	gameModeSubTypes = property(lambda self: None)
	gameModes = property(lambda self: None)
	stickToRoleModifier = property(lambda self: None)
	targetTeam = property(lambda self: None)
	targetType = property(lambda self: None)


class RoleSystem(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleSystem'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addAgent(self, *args, **kwargs): pass
	def assignRole(self, *args, **kwargs): pass
	def createRole(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def destroyRole(self, *args, **kwargs): pass
	def doAssignment(self, *args, **kwargs): pass
	def getAssignedRole(self, *args, **kwargs): pass
	def getRoles(self, *args, **kwargs): pass
	def removeAgent(self, *args, **kwargs): pass
	def setTraceInterface(self, *args, **kwargs): pass
	def startLogging(self, *args, **kwargs): pass
	def stopLogging(self, *args, **kwargs): pass
	def unassignRole(self, *args, **kwargs): pass
	def updateRolesPriority(self, *args, **kwargs): pass


class RoleTargetTeam(pybind11_object):
	Any = RoleTargetTeam.Any
	Enemy = RoleTargetTeam.Enemy
	Own = RoleTargetTeam.Own
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Any\n\n  Enemy\n\n  Own'
	__entries = {u'Any': (RoleTargetTeam.Any, None), u'Enemy': (RoleTargetTeam.Enemy, None), u'Own': (RoleTargetTeam.Own, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Enemy': RoleTargetTeam.Enemy, u'Own': RoleTargetTeam.Own, u'Any': RoleTargetTeam.Any}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleTargetTeam'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class RoleTargetType(pybind11_object):
	NoneType = RoleTargetType.NoneType
	Tank_Any = RoleTargetType.Tank_Any
	Tank_Bot = RoleTargetType.Tank_Bot
	Tank_Player = RoleTargetType.Tank_Player
	Tank_SPG = RoleTargetType.Tank_SPG
	TeamBase = RoleTargetType.TeamBase
	Zone = RoleTargetType.Zone
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Tank_SPG\n\n  Tank_Player\n\n  TeamBase\n\n  Zone\n\n  Tank_Bot\n\n  NoneType\n\n  Tank_Any'
	__entries = {u'Tank_SPG': (RoleTargetType.Tank_SPG, None), u'Tank_Player': (RoleTargetType.Tank_Player, None), u'TeamBase': (RoleTargetType.TeamBase, None), u'Zone': (RoleTargetType.Zone, None), u'Tank_Bot': (RoleTargetType.Tank_Bot, None), u'NoneType': (RoleTargetType.NoneType, None), u'Tank_Any': (RoleTargetType.Tank_Any, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Tank_SPG': RoleTargetType.Tank_SPG, u'Tank_Player': RoleTargetType.Tank_Player, u'TeamBase': RoleTargetType.TeamBase, u'Zone': RoleTargetType.Zone, u'Tank_Bot': RoleTargetType.Tank_Bot, u'NoneType': RoleTargetType.NoneType, u'Tank_Any': RoleTargetType.Tank_Any}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleTargetType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class RoleTraceCollectInterface(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'RoleTraceCollectInterface'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass

Roles = <module 'AI_Common.Roles' (built-in)>

class SensorDetection(pybind11_object):
	Direct = 2
	DirectAndIndirect = 3
	Indirect = 1
	Lost = 4
	Undetected = 0
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SensorDetection'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class SensorExposure(pybind11_object):
	Armored = 2
	Exposed = 3
	Hidden = 0
	Undefined = 1
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SensorExposure'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class SensorTeamBaseData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SensorTeamBaseData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	captureProgress = property(lambda self: None)
	captureStopped = property(lambda self: None)
	id = property(lambda self: None)
	invaders = property(lambda self: None)
	isActive = property(lambda self: None)
	pointsPerSecond = property(lambda self: None)
	position = property(lambda self: None)
	radius = property(lambda self: None)
	teamID = property(lambda self: None)


class ShootingTestEntityData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ShootingTestEntityData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	boundingRadiusSquared = property(lambda self: None)
	entityID = property(lambda self: None)
	def isValid(self, *args, **kwargs): pass
	position = property(lambda self: None)
	preciseMode = property(lambda self: None)


class SpotCheckingResults(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SpotCheckingResults'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	chance = property(lambda self: None)
	position = property(lambda self: None)
	potentiallyTargetable = property(lambda self: None)
	resultExternal = property(lambda self: None)
	resultInternal = property(lambda self: None)


class SpotHitCheckersParams(pybind11_object):
	DISPERSION_CIRCLE_SAFETY_AREA = property(lambda self: None)
	DISPERSION_CIRCLE_TESSELLATION_MULT = property(lambda self: None)
	SPG_MAX_OBSTACLE_HEIGHT = property(lambda self: None)
	SPG_MAX_PLAYABLE_HEIGHT = property(lambda self: None)
	SPG_RANGE_SQR_TO_USE_LOW_TRAJECTORY_ACCURACY = property(lambda self: None)
	SPG_RANGE_SQR_TO_USE_MAX_TRAJECTORY_ACCURACY = property(lambda self: None)
	SPG_RANGE_TO_USE_LOW_TRAJECTORY_ACCURACY = property(lambda self: None)
	SPG_RANGE_TO_USE_MAX_TRAJECTORY_ACCURACY = property(lambda self: None)
	TRACE_EXTRA_LENGTH = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SpotHitCheckersParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class SpotSelectorParams(pybind11_object):
	BASE_UPDATE_TICKS_RECENTLY_DETECTED = property(lambda self: None)
	BASE_UPDATE_TICKS_UNDETECTED = property(lambda self: None)
	CHASSIS_TRACK_WIDTH = property(lambda self: None)
	DRAFT_CENTER_HEIGHT = property(lambda self: None)
	LEADING_FIRE_ENEMY_SPEED_ERROR_MAX = property(lambda self: None)
	LEADING_FIRE_ENEMY_SPEED_ERROR_RESET_TIME = property(lambda self: None)
	LEADING_FIRE_RECALCULATION_TICKS = property(lambda self: None)
	LEADING_FIRE_UNDETECTED_ENEMY_TIMEOUT = property(lambda self: None)
	MAX_DIST_TO_USE_LAST_EXPOSED_POSITION = property(lambda self: None)
	MAX_DIST_TO_USE_LAST_EXPOSED_POSITION_SQR = property(lambda self: None)
	NO_LEADING_FIRE_RANGE = property(lambda self: None)
	RANDOM_POINT_CHECK_INTERVAL_TICKS = property(lambda self: None)
	RECENTLY_DETECTED_TIME_THRESHOLD = property(lambda self: None)
	REFINE_POINT_CHECK_INTERVAL_TICKS = property(lambda self: None)
	REFINE_POINT_TEST_MAX = property(lambda self: None)
	TARGET_POINT_TEST_MAX = property(lambda self: None)
	TIME_PREDICTION_FOR_ENEMY_POSITION = property(lambda self: None)
	UNDETECTION_TIME_TO_USE_LOW_FIDELITY = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SpotSelectorParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class SpotTargetingParams(pybind11_object):
	MAX_ARMORED_TARGET_POINTS_COUNT = property(lambda self: None)
	MAX_DIST_SQR_TO_AIM = property(lambda self: None)
	MIN_DIST_FIND_SPOT = property(lambda self: None)
	MIN_DIST_FIND_SPOT_SQR = property(lambda self: None)
	TARGETPOINT_FAILS_TO_SET_INVISIBLE = property(lambda self: None)
	TARGETPOINT_FAILS_TO_SET_INVISIBLE_MAX = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'SpotTargetingParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class StealthGridPack(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'StealthGridPack'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def bothStates(self, *args, **kwargs): pass
	def isPositionHiddenFromDetection(self, *args, **kwargs): pass
	def minCellSize(self, *args, **kwargs): pass
	def oneState(self, *args, **kwargs): pass


class StealthGridType(pybind11_object):
	Average = StealthGridType.Average
	Max = StealthGridType.Max
	Min = StealthGridType.Min
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Max\n\n  Average\n\n  Min'
	__entries = {u'Max': (StealthGridType.Max, None), u'Average': (StealthGridType.Average, None), u'Min': (StealthGridType.Min, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Max': StealthGridType.Max, u'Average': StealthGridType.Average, u'Min': StealthGridType.Min}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'StealthGridType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)

TANK_TYPE_MAPPING = {u'heavyTank': TankType.TankType_HeavyTank, u'SPG': TankType.TankType_SPG, u'AT-SPG': TankType.TankType_AT_SPG, u'mediumTank': TankType.TankType_MediumTank, u'lightTank': TankType.TankType_LightTank, u'<any>': TankType.TankType_Any}

class TankAtPosition(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAtPosition'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	isDetected = property(lambda self: None)
	position = property(lambda self: None)
	tank = property(lambda self: None)


class TankAttributes(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	ammoLeft = property(lambda self: None)
	chassis = property(lambda self: None)
	clipSizeLeft = property(lambda self: None)
	currentAmmoLeft = property(lambda self: None)
	currentShellIndexInAmmo = property(lambda self: None)
	damageFactor = property(lambda self: None)
	demaskFoliageFactor = property(lambda self: None)
	engine = property(lambda self: None)
	gun = property(lambda self: None)
	gunHeight = property(lambda self: None)
	height = property(lambda self: None)
	invisibility = property(lambda self: None)
	minVehicleSize = property(lambda self: None)
	reloadFinish = property(lambda self: None)
	turret = property(lambda self: None)


class TankAttributes__Chassis(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes::Chassis'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	shotDispersionFactors = property(lambda self: None)


class TankAttributes__Engine(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes::Engine'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	powerFactor = property(lambda self: None)


class TankAttributes__Gun(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes::Gun'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	canShoot = property(lambda self: None)


class TankAttributes__Invisibility(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes::Invisibility'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	current = property(lambda self: None)
	move = property(lambda self: None)
	shootFactor = property(lambda self: None)
	stay = property(lambda self: None)


class TankAttributes__Turret(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankAttributes::Turret'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	detached = property(lambda self: None)
	rotationSpeed = property(lambda self: None)


class TankComponentBase(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankComponentBase'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	descriptorComponent = property(lambda self: None)
	detached = property(lambda self: None)
	localTransform = property(lambda self: None)
	type = property(lambda self: None)
	def update(self, *args, **kwargs): pass
	worldTransform = property(lambda self: None)


class TankComponentType(pybind11_object):
	Chassis = TankComponentType.Chassis
	Gun = TankComponentType.Gun
	Hull = TankComponentType.Hull
	TrackPair = TankComponentType.TrackPair
	Turret = TankComponentType.Turret
	Wheel = TankComponentType.Wheel
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Turret\n\n  Hull\n\n  Chassis\n\n  TrackPair\n\n  Gun\n\n  Wheel'
	__entries = {u'Turret': (TankComponentType.Turret, None), u'Hull': (TankComponentType.Hull, None), u'Chassis': (TankComponentType.Chassis, None), u'TrackPair': (TankComponentType.TrackPair, None), u'Gun': (TankComponentType.Gun, None), u'Wheel': (TankComponentType.Wheel, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Turret': TankComponentType.Turret, u'Hull': TankComponentType.Hull, u'Chassis': TankComponentType.Chassis, u'TrackPair': TankComponentType.TrackPair, u'Gun': TankComponentType.Gun, u'Wheel': TankComponentType.Wheel}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankComponentType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class TankDefaultMaterials(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDefaultMaterials'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addDefaultMaterial(*args, **kwargs): pass
	def getDefault(*args, **kwargs): pass


class TankDescriptor(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	activeTurretIndex = property(lambda self: None)
	bestShot = property(lambda self: None)
	boundingRadius = property(lambda self: None)
	chassis = property(lambda self: None)
	defaultShot = property(lambda self: None)
	def getLocalAimPoint(self, *args, **kwargs): pass
	gun = property(lambda self: None)
	hull = property(lambda self: None)
	maxHealth = property(lambda self: None)
	miscAttrs = property(lambda self: None)
	name = property(lambda self: None)
	physics = property(lambda self: None)
	def setTurretCount(self, *args, **kwargs): pass
	shot = property(lambda self: None)
	turret = property(lambda self: None)
	turrets = property(lambda self: None)
	type = property(lambda self: None)
	typeLevel = property(lambda self: None)
	typeName = property(lambda self: None)
	typeTags = property(lambda self: None)
	typeTurrets = property(lambda self: None)
	def update(self, *args, **kwargs): pass
	visibilityCheckPoints = property(lambda self: None)


class TankDescriptor__Chassis(BaseTankDescriptorComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Chassis'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armorHomogenization = property(lambda self: None)
	drivingWheelsSizes = property(lambda self: None)
	hitTester = property(lambda self: None)
	materials = property(lambda self: None)
	name = property(lambda self: None)
	rotationSpeed = property(lambda self: None)


class TankDescriptor__Gun(BaseTankDescriptorComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Gun'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	absolutePitchLimits = property(lambda self: None)
	aimingTime = property(lambda self: None)
	armorHomogenization = property(lambda self: None)
	clip = property(lambda self: None)
	hitTester = property(lambda self: None)
	materials = property(lambda self: None)
	maxPitchLimits = property(lambda self: None)
	minPitchLimits = property(lambda self: None)
	name = property(lambda self: None)
	position = property(lambda self: None)
	reloadTime = property(lambda self: None)
	rotationSpeed = property(lambda self: None)
	shotDispersionAngle = property(lambda self: None)
	shotOffset = property(lambda self: None)
	shotPosition = property(lambda self: None)
	yawLimits = property(lambda self: None)


class TankDescriptor__Hull(BaseTankDescriptorComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Hull'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armorHomogenization = property(lambda self: None)
	hitTester = property(lambda self: None)
	materials = property(lambda self: None)
	name = property(lambda self: None)
	position = property(lambda self: None)
	primaryArmor = property(lambda self: None)


class TankDescriptor__Physics(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Physics'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	enginePower = property(lambda self: None)
	rotationSpeedLimit = property(lambda self: None)
	speedLimits = property(lambda self: None)
	weight = property(lambda self: None)


class TankDescriptor__Shot(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Shot'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	bwShot = property(lambda self: None)
	gravity = property(lambda self: None)
	maxDistance = property(lambda self: None)
	maxHeight = property(lambda self: None)
	piercingPower = property(lambda self: None)
	shell = property(lambda self: None)
	speed = property(lambda self: None)
	def update(self, *args, **kwargs): pass


class TankDescriptor__Shot__Shell(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Shot::Shell'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	caliber = property(lambda self: None)
	damage = property(lambda self: None)
	damageRandomization = property(lambda self: None)
	hitCrewChanceMultiplier = property(lambda self: None)
	hitDeviceChanceMultiplier = property(lambda self: None)
	piercingPowerRandomization = property(lambda self: None)
	type = property(lambda self: None)
	useAltDamageRandomization = property(lambda self: None)


class TankDescriptor__Shot__Shell__Type(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Shot::Shell::Type'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armorSpalls = property(lambda self: None)
	blastWave = property(lambda self: None)
	explosionDamageAbsorptionFactor = property(lambda self: None)
	explosionDamageFactor = property(lambda self: None)
	explosionEdgeDamageFactor = property(lambda self: None)
	explosionRadius = property(lambda self: None)
	maxDamage = property(lambda self: None)
	normalizationAngle = property(lambda self: None)
	ricochetAngleCos = property(lambda self: None)
	shellFragments = property(lambda self: None)
	shellFragmentsDamageAbsorptionFactor = property(lambda self: None)
	shieldPenetration = property(lambda self: None)


class TankDescriptor__Shot__Shell__Type__ImpactParams(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Shot::Shell::Type::ImpactParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	damageAbsorptionType = property(lambda self: None)
	damages = property(lambda self: None)
	isActive = property(lambda self: None)
	radius = property(lambda self: None)


class TankDescriptor__Shot__Shell__Type__ArmorSpalls(TankDescriptor__Shot__Shell__Type__ImpactParams):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Shot::Shell::Type::ArmorSpalls'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	coneAngleCos = property(lambda self: None)
	damageAbsorptionType = property(lambda self: None)
	damages = property(lambda self: None)
	isActive = property(lambda self: None)
	piercingSpalls = property(lambda self: None)
	radius = property(lambda self: None)


class TankDescriptor__Turret(BaseTankDescriptorComponent):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Turret'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armorHomogenization = property(lambda self: None)
	gun = property(lambda self: None)
	gunJointPitch = property(lambda self: None)
	hitTester = property(lambda self: None)
	materials = property(lambda self: None)
	name = property(lambda self: None)
	pitch = property(lambda self: None)
	position = property(lambda self: None)
	primaryArmor = property(lambda self: None)
	rotationSpeed = property(lambda self: None)


class TankDescriptor__Type(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankDescriptor::Type'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	overmatchMechanicsVer = property(lambda self: None)


class TankMaterialContainer(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankMaterialContainer'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addMaterialInfo(self, *args, **kwargs): pass
	def get(self, *args, **kwargs): pass


class TankMaterialInfo(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankMaterialInfo'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	armor = property(lambda self: None)
	chanceToHitByExplosion = property(lambda self: None)
	chanceToHitByProjectile = property(lambda self: None)
	checkCaliberForHitAngleNorm = property(lambda self: None)
	checkCaliberForRichet = property(lambda self: None)
	collideOnceOnly = property(lambda self: None)
	continueTraceIfNoHit = property(lambda self: None)
	damageKind = property(lambda self: None)
	extra = property(lambda self: None)
	isTankman = property(lambda self: None)
	isTrack = property(lambda self: None)
	kind = property(lambda self: None)
	mayRicochet = property(lambda self: None)
	useAntifragmentationLining = property(lambda self: None)
	useArmorHomogenization = property(lambda self: None)
	useHitAngle = property(lambda self: None)
	vehicleDamageFactor = property(lambda self: None)


class TankService(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankService'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getDamageAlongPath(self, *args, **kwargs): pass
	def getDamageAtPositionByTime(self, *args, **kwargs): pass
	def getGunDirectionDeviations(self, *args, **kwargs): pass
	def getOwnDamageForTimePeriod(self, *args, **kwargs): pass
	def getWGunPoint(self, *args, **kwargs): pass
	def isPathToPointHiddenFromEnemyDetection(self, *args, **kwargs): pass
	def isPositionHiddenFromEnemiesDetection(self, *args, **kwargs): pass


class TankServiceParams(pybind11_object):
	BOT_MAX_SPEED_FACTOR = property(lambda self: None)
	DAMAGE_ESTIMATION_PATH_SEGMENT_LENGTH = property(lambda self: None)
	WEAKSPOT_DAMAGE_ESTIMATION_SEQUENCE = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankServiceParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class TankType(pybind11_object):
	TankType_AT_SPG = TankType.TankType_AT_SPG
	TankType_Any = TankType.TankType_Any
	TankType_HeavyTank = TankType.TankType_HeavyTank
	TankType_LightTank = TankType.TankType_LightTank
	TankType_MediumTank = TankType.TankType_MediumTank
	TankType_SPG = TankType.TankType_SPG
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  TankType_MediumTank\n\n  TankType_HeavyTank\n\n  TankType_Any\n\n  TankType_LightTank\n\n  TankType_SPG\n\n  TankType_AT_SPG'
	__entries = {u'TankType_MediumTank': (TankType.TankType_MediumTank, None), u'TankType_HeavyTank': (TankType.TankType_HeavyTank, None), u'TankType_Any': (TankType.TankType_Any, None), u'TankType_LightTank': (TankType.TankType_LightTank, None), u'TankType_SPG': (TankType.TankType_SPG, None), u'TankType_AT_SPG': (TankType.TankType_AT_SPG, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'TankType_Any': TankType.TankType_Any, u'TankType_MediumTank': TankType.TankType_MediumTank, u'TankType_HeavyTank': TankType.TankType_HeavyTank, u'TankType_LightTank': TankType.TankType_LightTank, u'TankType_SPG': TankType.TankType_SPG, u'TankType_AT_SPG': TankType.TankType_AT_SPG}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TankType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class TargetDetectionType(pybind11_object):
	Direct = TargetDetectionType.Direct
	Indirect = TargetDetectionType.Indirect
	NotDetected = TargetDetectionType.NotDetected
	Undetected = TargetDetectionType.Undetected
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Indirect\n\n  Direct\n\n  NotDetected\n\n  Undetected'
	__entries = {u'Indirect': (TargetDetectionType.Indirect, None), u'Direct': (TargetDetectionType.Direct, None), u'NotDetected': (TargetDetectionType.NotDetected, None), u'Undetected': (TargetDetectionType.Undetected, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Indirect': TargetDetectionType.Indirect, u'Direct': TargetDetectionType.Direct, u'NotDetected': TargetDetectionType.NotDetected, u'Undetected': TargetDetectionType.Undetected}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TargetDetectionType'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class TargetingMode(pybind11_object):
	Chassis = TargetingMode.Chassis
	DoDamage = TargetingMode.DoDamage
	Hull = TargetingMode.Hull
	Turret = TargetingMode.Turret
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Turret\n\n  Hull\n\n  Chassis\n\n  DoDamage'
	__entries = {u'Turret': (TargetingMode.Turret, None), u'Hull': (TargetingMode.Hull, None), u'Chassis': (TargetingMode.Chassis, None), u'DoDamage': (TargetingMode.DoDamage, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Turret': TargetingMode.Turret, u'Hull': TargetingMode.Hull, u'Chassis': TargetingMode.Chassis, u'DoDamage': TargetingMode.DoDamage}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TargetingMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class Team(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Team'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addEntityData(self, *args, **kwargs): pass
	def addTankEntity(self, *args, **kwargs): pass
	def addUpdates(self, *args, **kwargs): pass
	battleLevel = property(lambda self: None)
	def clearRouteCostCache(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def deoccupyCirclingPoint(self, *args, **kwargs): pass
	def destroy(self, *args, **kwargs): pass
	def getArena(self, *args, **kwargs): pass
	def getBestRouteFromZoneToZone(self, *args, **kwargs): pass
	def getCirclingPointOccupant(self, *args, **kwargs): pass
	def getEntitiesInGroup(self, *args, **kwargs): pass
	def getEntitiesInRadius(self, *args, **kwargs): pass
	def getEntityData(self, *args, **kwargs): pass
	def getEntityDataGroup(self, *args, **kwargs): pass
	def hasEntityData(self, *args, **kwargs): pass
	def hasOccupiedCirclingPoint(self, *args, **kwargs): pass
	influenceMaps = property(lambda self: None)
	def isCirclingPointOccupiedBy(self, *args, **kwargs): pass
	def isEntityInRadius(self, *args, **kwargs): pass
	def occupyCirclingPoint(self, *args, **kwargs): pass
	def onAgentAdded(self, *args, **kwargs): pass
	def onAgentRemoved(self, *args, **kwargs): pass
	positionsPredicted = property(lambda self: None)
	def removeEntityData(self, *args, **kwargs): pass
	def removeUpdates(self, *args, **kwargs): pass
	def setArena(self, *args, **kwargs): pass
	def setLogger(self, *args, **kwargs): pass
	teamID = property(lambda self: None)
	zones = property(lambda self: None)


class TeamEntity(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TeamEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	entityId = property(lambda self: None)
	position = property(lambda self: None)
	team = property(lambda self: None)


class TeamBaseTeamEntity(TeamEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TeamBaseTeamEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	captureVehicles = property(lambda self: None)
	capturingRadius = property(lambda self: None)
	currentCapturePoints = property(lambda self: None)
	entityId = property(lambda self: None)
	health = property(lambda self: None)
	lastAttackedTime = property(lambda self: None)
	maxHealth = property(lambda self: None)
	pointsPerSecond = property(lambda self: None)
	position = property(lambda self: None)
	structureType = property(lambda self: None)
	team = property(lambda self: None)
	wasSpotted = property(lambda self: None)


class TeamParams(pybind11_object):
	DISABLE_BATTLEFRONT_MAP = property(lambda self: None)
	DISABLE_INFLUENCE_MAP = property(lambda self: None)
	UPDATE_RATE_COVERS_TEAM_CONTROLLER = property(lambda self: None)
	UPDATE_RATE_INFLUENCE_MAP = property(lambda self: None)
	UPDATE_RATE_RECONS_TEAM_CONTROLLER = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TeamParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class Threat(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'Threat'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def calculateVehicleThreat(*args, **kwargs): pass
	def getEntityThreatLevelInZone(*args, **kwargs): pass
	def getGlobalThreatLevels(*args, **kwargs): pass
	def getThreatLevelsAdvanced(*args, **kwargs): pass
	def getThreatLevelsInRadius(*args, **kwargs): pass
	def getThreatLevelsInZone(*args, **kwargs): pass
	def getThreatLevelsInZones(*args, **kwargs): pass
	def getThreatRatio(*args, **kwargs): pass


class TrajectoryMode(pybind11_object):
	FLAT_AIMING = TrajectoryMode.FLAT_AIMING
	MIXED_AIMING = TrajectoryMode.MIXED_AIMING
	STEEP_AIMING = TrajectoryMode.STEEP_AIMING
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  STEEP_AIMING\n\n  FLAT_AIMING\n\n  MIXED_AIMING'
	__entries = {u'STEEP_AIMING': (TrajectoryMode.STEEP_AIMING, None), u'FLAT_AIMING': (TrajectoryMode.FLAT_AIMING, None), u'MIXED_AIMING': (TrajectoryMode.MIXED_AIMING, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'STEEP_AIMING': TrajectoryMode.STEEP_AIMING, u'FLAT_AIMING': TrajectoryMode.FLAT_AIMING, u'MIXED_AIMING': TrajectoryMode.MIXED_AIMING}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'TrajectoryMode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class UAIAgentConfig(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIAgentConfig'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	halfWidth = property(lambda self: None)
	name = property(lambda self: None)
	radius = property(lambda self: None)


class UAICylinderRemovableObstacle(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAICylinderRemovableObstacle'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class UAILoggingHandlerVerbosity(pybind11_object):
	ERRORS = UAILoggingHandlerVerbosity.ERRORS
	INFOS = UAILoggingHandlerVerbosity.INFOS
	MAX_VERBOSITY = UAILoggingHandlerVerbosity.MAX_VERBOSITY
	WARNINGS = UAILoggingHandlerVerbosity.WARNINGS
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  INFOS\n\n  ERRORS\n\n  MAX_VERBOSITY\n\n  WARNINGS'
	__entries = {u'INFOS': (UAILoggingHandlerVerbosity.INFOS, None), u'ERRORS': (UAILoggingHandlerVerbosity.ERRORS, None), u'MAX_VERBOSITY': (UAILoggingHandlerVerbosity.MAX_VERBOSITY, None), u'WARNINGS': (UAILoggingHandlerVerbosity.WARNINGS, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'INFOS': UAILoggingHandlerVerbosity.INFOS, u'ERRORS': UAILoggingHandlerVerbosity.ERRORS, u'MAX_VERBOSITY': UAILoggingHandlerVerbosity.MAX_VERBOSITY, u'WARNINGS': UAILoggingHandlerVerbosity.WARNINGS}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAILoggingHandlerVerbosity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class UAIMesh(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIMesh'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	agent = property(lambda self: None)
	def getName(self, *args, **kwargs): pass


class UAIMeshCollectionBase(pybind11_object):
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
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
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
	__qualname__ = 'UAIMeshCollectionBase'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
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


class UAIMeshCollection(UAIMeshCollectionBase):
	def __contains__(self, *args, **kwargs): pass
	def __delattr__(*args, **kwargs): pass
	def __delitem__(self, *args, **kwargs): pass
	__doc__ = None
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getitem__(self, *args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	def __iter__(self, *args, **kwargs): pass
	def __len__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	def __nonzero__(self, *args, **kwargs): pass
	__pybind11_module_local_v5_msvc__ = PyCapsule()
	__qualname__ = 'UAIMeshCollection'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setitem__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addObstacle(self, *args, **kwargs): pass
	def append(self, *args, **kwargs): pass
	def clear(self, *args, **kwargs): pass
	def count(self, *args, **kwargs): pass
	def extend(self, *args, **kwargs): pass
	def findNavMesh(self, *args, **kwargs): pass
	def getMaxGirthNavmesh(self, *args, **kwargs): pass
	def getMinGirthNavmesh(self, *args, **kwargs): pass
	def getNavmeshByGirth(self, *args, **kwargs): pass
	def insert(self, *args, **kwargs): pass
	def pop(self, *args, **kwargs): pass
	def remove(self, *args, **kwargs): pass
	def removeObstacle(self, *args, **kwargs): pass
	def updateObstacles(self, *args, **kwargs): pass


class UAIQueryBuffer(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIQueryBuffer'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class UAIVector3(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UAIVector3'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	x = property(lambda self: None)
	y = property(lambda self: None)
	z = property(lambda self: None)


class UDOAIScenarioSpawnPoint(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOAIScenarioSpawnPoint'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	assignment = property(lambda self: None)
	btMain = property(lambda self: None)
	decissionTree = property(lambda self: None)
	guid = property(lambda self: None)
	maxSpawnOffsetDown = property(lambda self: None)
	maxSpawnOffsetUp = property(lambda self: None)
	name = property(lambda self: None)
	playerSpawn = property(lambda self: None)
	spawnTypes = property(lambda self: None)
	team = property(lambda self: None)
	tier = property(lambda self: None)
	transform = property(lambda self: None)
	userData = property(lambda self: None)


class UDOBadNavmeshZone(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOBadNavmeshZone'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	matKind = property(lambda self: None)
	model = property(lambda self: None)
	transform = property(lambda self: None)


class UDONotAIZone(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDONotAIZone'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	points = property(lambda self: None)
	transform = property(lambda self: None)


class UDOPatrolNode(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOPatrolNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	backtrackChance = property(lambda self: None)
	departureSpeed = property(lambda self: None)
	guid = property(lambda self: None)
	importance = property(lambda self: None)
	name = property(lambda self: None)
	patrolLinks = property(lambda self: None)
	radius = property(lambda self: None)
	tolAngle = property(lambda self: None)
	transform = property(lambda self: None)
	waitSecs = property(lambda self: None)


class UDOZoneCenter(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOZoneCenter'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	brawlSafetyFactor = property(lambda self: None)
	desirability = property(lambda self: None)
	guid = property(lambda self: None)
	position = property(lambda self: None)
	preferableTankType = property(lambda self: None)
	preferenceHeavyTank = property(lambda self: None)
	preferenceLightTank = property(lambda self: None)
	preferenceMediumTank = property(lambda self: None)
	preferenceSPG = property(lambda self: None)
	preferenceTankDestroyer = property(lambda self: None)


class UDOZoneEntryPoint(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOZoneEntryPoint'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	guid = property(lambda self: None)
	position = property(lambda self: None)
	preferableTankType = property(lambda self: None)
	preferenceHeavyTank = property(lambda self: None)
	preferenceLightTank = property(lambda self: None)
	preferenceMediumTank = property(lambda self: None)
	preferenceSPG = property(lambda self: None)
	preferenceTankDestroyer = property(lambda self: None)
	team = property(lambda self: None)


class UDOZoneNode(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UDOZoneNode'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	desirability = property(lambda self: None)
	guid = property(lambda self: None)
	nodes = property(lambda self: None)
	position = property(lambda self: None)
	scale = property(lambda self: None)
	type = property(lambda self: None)
	zone = property(lambda self: None)


class UserDataObjects(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UserDataObjects'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	aiScenarioSpawnPoints = property(lambda self: None)
	badNavmeshZone = property(lambda self: None)
	notAIZone = property(lambda self: None)
	patrolNodes = property(lambda self: None)
	zoneCenters = property(lambda self: None)
	zoneEntryPoints = property(lambda self: None)
	zoneNodes = property(lambda self: None)

UtilityCommon = <module 'AI_Common.UtilityCommon' (built-in)>

class UtilityContext(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'UtilityContext'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	agent = property(lambda self: None)
	aiTeam = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	identifier = property(lambda self: None)
	roleId = property(lambda self: None)
	roleTargetId = property(lambda self: None)


class VehicleAIMover(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleAIMover'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def abortMovement(self, *args, **kwargs): pass
	def buildPath(self, *args, **kwargs): pass
	currentFacingStatus = property(lambda self: None)
	currentMovementStatus = property(lambda self: None)
	def findRandomNeighbourPointWithRange(self, *args, **kwargs): pass
	def getClosestNavmeshPoint(self, *args, **kwargs): pass
	def getCurrentPath(self, *args, **kwargs): pass
	def getCurrentTickIndex(self, *args, **kwargs): pass
	def getDebugInfo(self, *args, **kwargs): pass
	def getMoveParameters(self, *args, **kwargs): pass
	def getMovementOutput(self, *args, **kwargs): pass
	def getRandomPointOnNavmesh(self, *args, **kwargs): pass
	def getTweakParameters(self, *args, **kwargs): pass
	moveParameters = property(lambda self: None)
	def navmeshRaycast(self, *args, **kwargs): pass
	pathQueryContext = property(lambda self: None)
	def setMovementSpeedFlags(self, *args, **kwargs): pass
	def setTweakParameters(self, *args, **kwargs): pass
	def startFacing(self, *args, **kwargs): pass
	def startMovement(self, *args, **kwargs): pass
	def tick(self, *args, **kwargs): pass
	tweakParameters = property(lambda self: None)


class VehicleBotSpotSelector(AISpotSelector):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleBotSpotSelector'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def checkCurrentGunDirection(self, *args, **kwargs): pass
	def checkVehicleVisibility(self, *args, **kwargs): pass
	def computeTargetPoint(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getNoneResult(*args, **kwargs): pass
	isCurrentSpotPotentiallyTargetable = property(lambda self: None)
	def resetData(self, *args, **kwargs): pass


class VehicleBotTargeting(AITargeting):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleBotTargeting'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addBonusScore(self, *args, **kwargs): pass
	def checkDataUpdate(self, *args, **kwargs): pass
	def clearBonusScore(self, *args, **kwargs): pass
	def clearPriorityArea(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def enableTargeting(self, *args, **kwargs): pass
	def getTarget(self, *args, **kwargs): pass
	def getTargetId(self, *args, **kwargs): pass
	def hasAnyTarget(self, *args, **kwargs): pass
	def hasDirectTarget(self, *args, **kwargs): pass
	def hasIndirectTarget(self, *args, **kwargs): pass
	def hasNonDirectTarget(self, *args, **kwargs): pass
	def hasUndetectedTarget(self, *args, **kwargs): pass
	def hasVisibleTarget(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	isTargetingEnabled = property(lambda self: None)
	def onTankEntityDestroyed(self, *args, **kwargs): pass
	def requestAssist(self, *args, **kwargs): pass
	def resetTarget(self, *args, **kwargs): pass
	def setEntity(self, *args, **kwargs): pass
	def setPriorityArea(self, *args, **kwargs): pass
	def tryToSelectTarget(self, *args, **kwargs): pass
	vehicle = property(lambda self: None)


class VehicleBotTargetingParams(AITargetingParams):
	BONUS_AUTOLOADER_ENEMY = property(lambda self: None)
	BONUS_CURRENT_TARGET = property(lambda self: None)
	BONUS_IN_PRIORITY_AREA = property(lambda self: None)
	BONUS_ONE_SHOT_ENEMY = property(lambda self: None)
	ENEMY_EXPOSURE_SELF_RADIUS = property(lambda self: None)
	MAX_TIME_FOCUS_TARGET = property(lambda self: None)
	PENALTY_CANT_TURN = property(lambda self: None)
	PENALTY_ENEMY_SPEED = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_ARMORED_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MAX_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MAX = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_MIN_MIN = property(lambda self: None)
	PENALTY_EXPOSURE_HIDDEN_RADIUS = property(lambda self: None)
	PENALTY_EXPOSURE_THRESHOLD = property(lambda self: None)
	PENALTY_FORBID_SELECTION = property(lambda self: None)
	PENALTY_LONG_TURN = property(lambda self: None)
	PENALTY_LOW_HIT_CHANCE = property(lambda self: None)
	PENALTY_OUT_OF_YAW_SCOPE = property(lambda self: None)
	PENALTY_SLIGHTLY_OUT_OF_DRAW_RADIUS = property(lambda self: None)
	PENALTY_TARGET_FOCUS_EXCEEDED = property(lambda self: None)
	PENALTY_UNDETECTED_MAX = property(lambda self: None)
	PENALTY_UNDETECTED_MIN = property(lambda self: None)
	SCORE_BASE = property(lambda self: None)
	SCORE_FORBIDDEN_TO_SELECT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_HT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_LT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_MT_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_SPG_TO_TD = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_HT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_LT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_MT = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_SPG = property(lambda self: None)
	SCORE_TANK_CLASS_TD_TO_TD = property(lambda self: None)
	SCORE_TANK_TYPE = property(lambda self: None)
	SCORING_AIMING_TIME_MULTIPLIER = property(lambda self: None)
	SCORING_ASSIST_DURATION = property(lambda self: None)
	SCORING_ASSIST_RADIUS = property(lambda self: None)
	SCORING_ASSIST_REDUCE_DURATION = property(lambda self: None)
	SCORING_DIST_TO_MOVE_TARGET = property(lambda self: None)
	SCORING_EXPOSURE_ARMOR_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_FADEOFF_TIME = property(lambda self: None)
	SCORING_EXPOSURE_UNDEFINED_PENALTY_MULTIPLIER = property(lambda self: None)
	SCORING_MAX_DIST_TO_ADD_TO_SCORE = property(lambda self: None)
	SCORING_MAX_GLASS_CANNON = property(lambda self: None)
	SCORING_MAX_MOVE_BEFORE_SHOT = property(lambda self: None)
	SCORING_MAX_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MAX_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MAX_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME = property(lambda self: None)
	SCORING_MAX_TURN_TIME_NO_PENALTY = property(lambda self: None)
	SCORING_MIN_GLASS_CANNON = property(lambda self: None)
	SCORING_MIN_HIT_CHANCE = property(lambda self: None)
	SCORING_MIN_PP_ADVANTAGE = property(lambda self: None)
	SCORING_MIN_RELATIVE_RETICLE_TO_ADD_AIM_TIME = property(lambda self: None)
	SCORING_MIN_TAKE_DAMAGE_TIME = property(lambda self: None)
	SCORING_OUT_OF_DRAW_RADIUS_EXTRA = property(lambda self: None)
	SCORING_TARGET_HEIGHT = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MAX = property(lambda self: None)
	SCORING_THREAT_FADEOFF_TIME_MIN = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MAXSPEED = property(lambda self: None)
	SCORING_UNDETECTED_FADEOFF_TIME_MINSPEED = property(lambda self: None)
	SCORING_UNDETECTED_MAX_SPEED = property(lambda self: None)
	SCORING_UNDETECTED_TIME_TO_IGNORE_TARGET = property(lambda self: None)
	SELECT_TARGET_MAX_DISTANCE = property(lambda self: None)
	TARGET_SELECTION_THRESHOLD = property(lambda self: None)
	UPDATE_RATE = property(lambda self: None)
	WEIGHT_ASSIST_BONUS = property(lambda self: None)
	WEIGHT_CLOSE_DISTANCE = property(lambda self: None)
	WEIGHT_DAMAGING_VEHICLE = property(lambda self: None)
	WEIGHT_DIRECTION = property(lambda self: None)
	WEIGHT_GLASS_CANNON = property(lambda self: None)
	WEIGHT_HIT_CHANCE = property(lambda self: None)
	WEIGHT_INVADER = property(lambda self: None)
	WEIGHT_PENETRATION = property(lambda self: None)
	WEIGHT_PENETRATION_HE = property(lambda self: None)
	WEIGHT_PIERCING_POWER = property(lambda self: None)
	WEIGHT_PLAYER_VEHICLE = property(lambda self: None)
	WEIGH_ENEMY_DISTRACTION = property(lambda self: None)
	WEIGH_ENEMY_HP = property(lambda self: None)
	WEIGH_TAKE_DAMAGE_RECENTLY = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleBotTargetingParams'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	_paramsSectionName = property(lambda self: None)
	def updateCalculatedParams(self, *args, **kwargs): pass


class VehicleTeamEntity(TeamEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VehicleTeamEntity'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	baseInfluence = property(lambda self: None)
	currentInfluence = property(lambda self: None)
	detected = property(lambda self: None)
	direction_debugOnly = property(lambda self: None)
	entityId = property(lambda self: None)
	health = property(lambda self: None)
	isBot = property(lambda self: None)
	lostTime = property(lambda self: None)
	maxHealth = property(lambda self: None)
	position = property(lambda self: None)
	def setCurrentHealth(self, *args, **kwargs): pass
	tankEntity = property(lambda self: None)
	tankLevel = property(lambda self: None)
	tankType = property(lambda self: None)
	team = property(lambda self: None)
	turretDirection_debugOnly = property(lambda self: None)
	undetectedTime = property(lambda self: None)
	def updateInfluence(self, *args, **kwargs): pass


class VisibilityGrid(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'VisibilityGrid'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def empty(self, *args, **kwargs): pass
	def minCellSize(self, *args, **kwargs): pass
	def point2Point(self, *args, **kwargs): pass
	def point2Region(self, *args, **kwargs): pass
	def region2Region(self, *args, **kwargs): pass


class WaitForAccuracyEnum(pybind11_object):
	Aim = WaitForAccuracyEnum.Aim
	DontWait = WaitForAccuracyEnum.DontWait
	Stand = WaitForAccuracyEnum.Stand
	StandAndHeal = WaitForAccuracyEnum.StandAndHeal
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Aim\n\n  StandAndHeal\n\n  Stand\n\n  DontWait'
	__entries = {u'Aim': (WaitForAccuracyEnum.Aim, None), u'StandAndHeal': (WaitForAccuracyEnum.StandAndHeal, None), u'Stand': (WaitForAccuracyEnum.Stand, None), u'DontWait': (WaitForAccuracyEnum.DontWait, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Aim': WaitForAccuracyEnum.Aim, u'StandAndHeal': WaitForAccuracyEnum.StandAndHeal, u'Stand': WaitForAccuracyEnum.Stand, u'DontWait': WaitForAccuracyEnum.DontWait}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'WaitForAccuracyEnum'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class WithinTurretLimitsResult(pybind11_object):
	AboveUpperLimit = WithinTurretLimitsResult.AboveUpperLimit
	BelowLowerLimit = WithinTurretLimitsResult.BelowLowerLimit
	WithinLimits = WithinTurretLimitsResult.WithinLimits
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  BelowLowerLimit\n\n  AboveUpperLimit\n\n  WithinLimits'
	__entries = {u'BelowLowerLimit': (WithinTurretLimitsResult.BelowLowerLimit, None), u'AboveUpperLimit': (WithinTurretLimitsResult.AboveUpperLimit, None), u'WithinLimits': (WithinTurretLimitsResult.WithinLimits, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'BelowLowerLimit': WithinTurretLimitsResult.BelowLowerLimit, u'AboveUpperLimit': WithinTurretLimitsResult.AboveUpperLimit, u'WithinLimits': WithinTurretLimitsResult.WithinLimits}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'WithinTurretLimitsResult'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ZoneArenaModule(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneArenaModule'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	aiData = property(lambda self: None)
	def getAllZonesEntryPointsByTeam(self, *args, **kwargs): pass
	def getDistanceToZoneCore(self, *args, **kwargs): pass
	def getMaxMoveLinkDesirability(self, *args, **kwargs): pass
	def getMaxShootLinkDesirability(self, *args, **kwargs): pass
	def getMoveLinks(self, *args, **kwargs): pass
	def getNeighborZones(self, *args, **kwargs): pass
	def getNeighborZonesByTypes(self, *args, **kwargs): pass
	def getShootLinks(self, *args, **kwargs): pass
	def getZone(self, *args, **kwargs): pass
	def getZoneEntryPoints(self, *args, **kwargs): pass
	def getZoneEntryPointsByTeam(self, *args, **kwargs): pass
	def getZoneEntryRouteNodeGUID(self, *args, **kwargs): pass
	def getZoneMoveLinksPaths(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	valid = property(lambda self: None)


class ZoneData(TeamEntity):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	brawlSafetyFactor = property(lambda self: None)
	desirability = property(lambda self: None)
	entityId = property(lambda self: None)
	lastUpdateTime = property(lambda self: None)
	position = property(lambda self: None)
	preferableTankType = property(lambda self: None)
	primaryEntities = property(lambda self: None)
	primaryThreats = property(lambda self: None)
	revertState = property(lambda self: None)
	secondaryEntities = property(lambda self: None)
	secondaryThreats = property(lambda self: None)
	state = property(lambda self: None)
	tankClassPreferences = property(lambda self: None)
	tankClassPreferencesAtStart = property(lambda self: None)
	team = property(lambda self: None)


class ZonePath(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonePath'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	totalDistance = property(lambda self: None)
	totalHeight = property(lambda self: None)


class ZonePathHop(pybind11_object):
	In = property(lambda self: None)
	Out = property(lambda self: None)
	Zone = property(lambda self: None)
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonePathHop'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass


class ZonePathMap(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonePathMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getMoveLinks(self, *args, **kwargs): pass
	def getZonePathHops(self, *args, **kwargs): pass


class ZonePathSimple(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonePathSimple'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	route = property(lambda self: None)
	totalDistance = property(lambda self: None)
	totalHeight = property(lambda self: None)


class ZonePredictedPlayerData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonePredictedPlayerData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	lastPosition = property(lambda self: None)
	lastTime = property(lambda self: None)
	zoneId = property(lambda self: None)


class ZoneState(pybind11_object):
	Contested = ZoneState.Contested
	Friendly = ZoneState.Friendly
	Hostile = ZoneState.Hostile
	Neutral = ZoneState.Neutral
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Contested\n\n  Neutral\n\n  Hostile\n\n  Friendly'
	__entries = {u'Contested': (ZoneState.Contested, None), u'Neutral': (ZoneState.Neutral, None), u'Hostile': (ZoneState.Hostile, None), u'Friendly': (ZoneState.Friendly, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Neutral': ZoneState.Neutral, u'Friendly': ZoneState.Friendly, u'Contested': ZoneState.Contested, u'Hostile': ZoneState.Hostile}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneState'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ZoneTeamModule(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneTeamModule'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def addUpdates(self, *args, **kwargs): pass
	def calculateRouteDistanceCost(self, *args, **kwargs): pass
	config = property(lambda self: None)
	def destroy(self, *args, **kwargs): pass
	def getAllZonesEntryPointsByTeam(self, *args, **kwargs): pass
	def getDistanceToZoneCore(self, *args, **kwargs): pass
	def getEntitiesIdsInZone(self, *args, **kwargs): pass
	def getEntitiesInZone(self, *args, **kwargs): pass
	def getEntitiesInZoneAdvanced(self, *args, **kwargs): pass
	def getGlobalThreatLevel(self, *args, **kwargs): pass
	def getMaxMoveLinkDesirability(self, *args, **kwargs): pass
	def getMaxShootLinkDesirability(self, *args, **kwargs): pass
	def getMoveLinks(self, *args, **kwargs): pass
	def getNeighborZones(self, *args, **kwargs): pass
	def getNeighborZonesByTypes(self, *args, **kwargs): pass
	def getPredictedPlayersZone(self, *args, **kwargs): pass
	def getRouteBotPositionFactor(self, *args, **kwargs): pass
	def getRouteEndPositionFactor(self, *args, **kwargs): pass
	def getShootLinks(self, *args, **kwargs): pass
	def getZone(self, *args, **kwargs): pass
	def getZoneEntryPoints(self, *args, **kwargs): pass
	def getZoneEntryPointsByTeam(self, *args, **kwargs): pass
	def getZoneEntryRouteNodeGUID(self, *args, **kwargs): pass
	def getZoneMoveLinksPaths(self, *args, **kwargs): pass
	def getZoneState(self, *args, **kwargs): pass
	def getZoneThreatLevel(self, *args, **kwargs): pass
	def init(self, *args, **kwargs): pass
	def isZoneId(self, *args, **kwargs): pass
	def removeUpdates(self, *args, **kwargs): pass
	def setZoneEntitiesUpdateCallback(self, *args, **kwargs): pass
	def setZoneStateChangeCallback(self, *args, **kwargs): pass
	def startArena(self, *args, **kwargs): pass
	staticDataOverridden = property(lambda self: None)
	def updatePlayersPrediction(self, *args, **kwargs): pass
	def updateZoneEntities(self, *args, **kwargs): pass
	def updateZones(self, *args, **kwargs): pass


class ZoneToZonePathData(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneToZonePathData'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	endZoneID = property(lambda self: None)
	initialLink = property(lambda self: None)
	path = property(lambda self: None)
	startZoneID = property(lambda self: None)


class ZoneTypeQuery(pybind11_object):
	Primary = ZoneTypeQuery.Primary
	PrimaryAndSecondary = ZoneTypeQuery.PrimaryAndSecondary
	Secondary = ZoneTypeQuery.Secondary
	def __delattr__(*args, **kwargs): pass
	__doc__ = u'Members:\n\n  Primary\n\n  PrimaryAndSecondary\n\n  Secondary'
	__entries = {u'Primary': (ZoneTypeQuery.Primary, None), u'PrimaryAndSecondary': (ZoneTypeQuery.PrimaryAndSecondary, None), u'Secondary': (ZoneTypeQuery.Secondary, None)}
	def __eq__(self, *args, **kwargs): pass
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __getstate__(self, *args, **kwargs): pass
	def __hash__(self, *args, **kwargs): pass
	def __init__(self, *args, **kwargs): pass
	def __int__(self, *args, **kwargs): pass
	def __long__(self, *args, **kwargs): pass
	__members__ = {u'Primary': ZoneTypeQuery.Primary, u'PrimaryAndSecondary': ZoneTypeQuery.PrimaryAndSecondary, u'Secondary': ZoneTypeQuery.Secondary}
	__module__ = 'AI_Common'
	def __ne__(self, *args, **kwargs): pass
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZoneTypeQuery'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(self, *args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __setstate__(self, *args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	name = property(lambda self: None)


class ZonesTextureMap(pybind11_object):
	def __delattr__(*args, **kwargs): pass
	__doc__ = None
	def __format__(*args, **kwargs): pass
	def __getattribute__(*args, **kwargs): pass
	def __hash__(*args, **kwargs): pass
	def __init__(*args, **kwargs): pass
	__module__ = 'AI_Common'
	def __new__(*args, **kwargs): pass
	__qualname__ = 'ZonesTextureMap'
	def __reduce__(*args, **kwargs): pass
	def __reduce_ex__(*args, **kwargs): pass
	def __repr__(*args, **kwargs): pass
	def __setattr__(*args, **kwargs): pass
	def __sizeof__(*args, **kwargs): pass
	def __str__(*args, **kwargs): pass
	def __subclasshook__(*args, **kwargs): pass
	def getAllZones(self, *args, **kwargs): pass
	def getDistanceToZoneCore(self, *args, **kwargs): pass
	def getSourcePath(self, *args, **kwargs): pass
	def getZone(self, *args, **kwargs): pass
	def getZoneIdWorld(self, *args, **kwargs): pass

__BtReturn_Failed__ = 0L
__BtReturn_Interruption__ = 3L
__BtReturn_Reset__ = 4L
__BtReturn_Running__ = 2L
__BtReturn_Success__ = 1L
__doc__ = None
__name__ = 'AI_Common'
__package__ = None
def addUAILoggingHandler(*args, **kwargs): pass
def calcMinMaxGridCellsDistance(*args, **kwargs): pass
def calcVehiclePresenceProbability(*args, **kwargs): pass
def canPenetrate(*args, **kwargs): pass
def canPenetrateFrontArmor(*args, **kwargs): pass
def canShootAtPoint(*args, **kwargs): pass
def canShootAtPointFixedAngles(*args, **kwargs): pass
def checkRayTraceDestructible(*args, **kwargs): pass
def computeMoveLinkToEnemyBasePosition(*args, **kwargs): pass
def computePiercingPowerAtDist(*args, **kwargs): pass
def computeSPGShootingPitch(*args, **kwargs): pass
def computeShootLinkToEnemyBasePosition(*args, **kwargs): pass
def describePointCheckResult(*args, **kwargs): pass
def doTrace(*args, **kwargs): pass
def estimateChanceForDamageByProjectile(*args, **kwargs): pass
def estimateVehicleArmor(*args, **kwargs): pass
def executeBTTree(*args, **kwargs): pass
def findDistancesFromPathEnds(*args, **kwargs): pass
def findMostArmoredClosestAlly(*args, **kwargs): pass
def generateUID(*args, **kwargs): pass
def getBTInterruptionNode(*args, **kwargs): pass
def getBTInterruptionStack(*args, **kwargs): pass
def getGunCurrentTrajectory(*args, **kwargs): pass
def getGunDirectionDeviations(*args, **kwargs): pass
def getGunWorldMatrix(*args, **kwargs): pass
def getMoverDebugInfoVersion(*args, **kwargs): pass
def getObjectsCount(*args, **kwargs): pass
def getShotAngles(*args, **kwargs): pass
def getShotConeSegmentsThatMayHitVehicle(*args, **kwargs): pass
def getTraceEventID(*args, **kwargs): pass
def getTurretWorldMatrix(*args, **kwargs): pass
def getVehicleSpecificPower(*args, **kwargs): pass
def getWGunPointForVehicle(*args, **kwargs): pass
def getWGunPointForVehicleWhenTargeting(*args, **kwargs): pass
def hasListeners(*args, **kwargs): pass
def isEnemyTargetableByGun(*args, **kwargs): pass
def isPositionHiddenFromDetection(*args, **kwargs): pass
def isTargetingModeDoAnyDamage(*args, **kwargs): pass
def lcm(*args, **kwargs): pass
def rangeMap(*args, **kwargs): pass
def selectEntryPoint(*args, **kwargs): pass
def setCollideCallbackFunction(*args, **kwargs): pass
def setEstimateModernHEDamageFunction(*args, **kwargs): pass
def setWeakspotsLogger(*args, **kwargs): pass
def shotConeSegmentMayHitVehicle(*args, **kwargs): pass
def splitPathIntoSegments(*args, **kwargs): pass
def splitPathIntoSegmentsUAI(*args, **kwargs): pass
def splitSegment(*args, **kwargs): pass
def splitSegmentUAI(*args, **kwargs): pass
def startExecuteBTTree(*args, **kwargs): pass
def subscribeTraceEvent(*args, **kwargs): pass
def unsubscribeTraceEvent(*args, **kwargs): pass