import itertools
from collections import OrderedDict, namedtuple
from typing import TYPE_CHECKING
import SoundGroups
from account_helpers.AccountSettings import AccountSettings, PERSONAL_MISSION_3
from adisp import adisp_process
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.game_control.links import URLMacros
from gui.impl.gen.view_models.views.lobby.personal_missions_30.additional_mission_model import AdditionalMissionType
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import OperationState
from gui.impl.gen.view_models.views.lobby.personal_missions_30.main_view_reward_model import RewardsType
from gui.impl.lobby.personal_missions_30.personal_mission_constants import MISSIONS_ROLES_TO_CATEGORIES, STAGES_CONFIG, AssemblingType, MAX_NEWBIE_DAILY_QUESTS_PM_POINTS, MAX_DAILY_QUESTS_PM_POINTS
from gui.server_events.awards_formatters import PM_POINTS_TOKEN
from gui.server_events.bonuses import PersonalMissionsPointsTokensBonus
from gui.server_events.event_items import NEWBIES_QUESTS_PASS_TOKEN
from gui.server_events.finders import BRANCH_TO_OPERATION_IDS
from gui.server_events.personal_progress.formatters import PMCardConditionsFormatter
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showBrowserOverlayView
from gui.sounds.filters import StatesGroup, States
from helpers import dependency
from personal_missions import PM_BRANCH
from shared_utils import findFirst
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if TYPE_CHECKING:
    from gui.impl.lobby.personal_missions_30.personal_mission_constants import StageInfo
ConditionsConfig = namedtuple('ConditionsConfig', 'maxProgressValue, allQuestsRequired, questsDetails')

def isIntroShown(intro):
    serverSettings = dependency.instance(ISettingsCore).serverSettings
    return serverSettings.getPersonalMission3Data().get(intro, False)


def markIntroShown(introKey):
    serverSettings = dependency.instance(ISettingsCore).serverSettings
    defaults = AccountSettings.getSettingsDefault(PERSONAL_MISSION_3)
    settings = serverSettings.getPersonalMission3Data(defaults)
    if not settings.get(introKey):
        settings[introKey] = True
        serverSettings.setPersonalMission3Data(settings)


def isBannerAnimationShown(animationKey):
    serverSettings = dependency.instance(ISettingsCore).serverSettings
    return serverSettings.getPersonalMission3Data().get(animationKey, False)


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def markBannerAnimationShown(animationKey, reset=False, settingsCore=None):
    serverSettings = settingsCore.serverSettings
    defaults = AccountSettings.getSettingsDefault(PERSONAL_MISSION_3)
    settings = serverSettings.getPersonalMission3Data(defaults)
    settings[animationKey] = not reset
    serverSettings.setPersonalMission3Data(settings)


def isVehDetailInstalled(lastInstalledDetail, detail):
    return int(detail.rsplit(':')[(-1)]) <= lastInstalledDetail


def firstUnclaimedOperation(operation, operations):
    unclaimedOperation = None
    if operation.getBranch() == PM_BRANCH.PERSONAL_MISSION_3:
        unclaimedOperation = findFirst(lambda o: not o.isAwardAchieved(), operations)
    return unclaimedOperation


def getMissionConfigData(mission):
    maxProgressValue = 0
    allQuestsRequired = False
    missionQuests = OrderedDict()
    conditionConfig = PMCardConditionsFormatter(mission)
    for conditionsCfg in conditionConfig.bodyFormat():
        maxProgressValue = conditionsCfg.get('progressData', {}).get('uniqueVehicles', 1)
        initData = conditionsCfg.get('initData')
        if not allQuestsRequired:
            allQuestsRequired = not initData.get('isInOrGroup')
        questID = ('{}_{}').format(mission.getGeneralQuestID(), conditionsCfg.get('progressID'))
        missionQuests[questID] = {'title': initData.get('title'), 
           'description': initData.get('description'), 
           'icon': initData.get('iconID')}

    return ConditionsConfig(maxProgressValue, allQuestsRequired, missionQuests)


def getDetailNameByToken(token):
    return ('_').join(token.split(':')[2:])


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def getSortedPm3Operations(eventsCache=None):
    return OrderedDict(sorted(eventsCache.getPersonalMissions().getAllOperations(PM_BRANCH.V2_BRANCHES).items()))


def getOperationStatus(operation, allOperations):
    unclaimedOperation = firstUnclaimedOperation(operation, allOperations.values())
    state = OperationState.UNAVAILABLE
    if operation.isDisabled():
        state = OperationState.LOCKED
    elif operation.isFullCompleted():
        state = OperationState.COMPLETED_WITH_HONORS
    elif operation.isAwardAchieved():
        state = OperationState.COMPLETED
    elif operation.isInProgress() or wasOperationActivatedBefore(operation, unclaimedOperation):
        state = OperationState.ACTIVE
    elif not operation.isDisabled() and isOperationAvailableByVehicles(operation) and operation.isUnlocked() and (unclaimedOperation is None or unclaimedOperation.getID() == operation.getID()):
        state = OperationState.AVAILABLE
    return state


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def getQuestsByOperationsChains(eventsCache=None):
    operations = eventsCache.getPersonalMissions().getOperationsForBranch(PM_BRANCH.PERSONAL_MISSION_3)
    allMissions = OrderedDict()
    for operation in sorted(operations.values(), key=lambda o: o.getID()):
        allMissions[operation.getID()] = OrderedDict()
        for missionsType in operation.getIterationChain():
            missionsForChain = sorted(operation.getChainByClassifierAttr(missionsType)[1].values(), key=lambda q: q.getID())
            allMissions[operation.getID()][MISSIONS_ROLES_TO_CATEGORIES[missionsType].value] = OrderedDict([ (missionData.getID(), missionData) for missionData in missionsForChain ])

    return allMissions


def getMainRewardInfo(operation, allOperations, rewardType):
    completedTasks = 0
    tasksNumber = 0
    if rewardType == RewardsType.MAIN:
        tasksNumber = 1
        completedTasks = int(operation.isCompleted())
    elif rewardType == RewardsType.CAMPAIGN:
        completedTasks = len([ operation for operation in allOperations.values() if operation.isFullCompleted() ])
        tasksNumber = len(allOperations)
    elif rewardType == RewardsType.OPERATION:
        completedTasks = len(operation.getCompletedQuests())
        tasksNumber = len(list(itertools.chain.from_iterable(operation.getQuests().values())))
    return (
     completedTasks, tasksNumber)


def getNextNotStartedOperation(currentOperation, operations):
    notStartedOperation = None
    unclaimedOperation = firstUnclaimedOperation(currentOperation, operations)
    for operation in operations:
        if not operation.isStarted() and operation.getID() > currentOperation.getID() and unclaimedOperation is not None and unclaimedOperation.getID() == operation.getID():
            notStartedOperation = operation
            break

    return notStartedOperation


def setForceLeavePM3State():
    from gui.Scaleform.lobby_entry import getLobbyStateMachine
    from gui.impl.lobby.personal_missions_30.state import PersonalMissions3State
    lsm = getLobbyStateMachine()
    lsm.getStateByCls(PersonalMissions3State).setForceLeave()


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def showRewardVehicleInHangar(operation, itemsCache=None):
    vehicleBonus = operation.getPM3VehicleBonus()
    if vehicleBonus:
        itemCD = vehicleBonus.compactDescr
        vehicle = itemsCache.items.getItemByCD(itemCD)
        if vehicle.isInInventory:
            shared_events.selectVehicleInHangar(itemCD)


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def isPMCampaignsStarted(branches=PM_BRANCH.V1_BRANCHES, eventsCache=None):
    return any(operation for operation in eventsCache.getPersonalMissions().getAllOperations(branches=branches).values() if operation.isStarted())


def setVideoOverlayOn():
    SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_ON)


def setVideoOverlayOff():
    SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_OFF)


def isOperationAvailableByVehicles--- This code section failed: ---

 L. 210         0  LOAD_FAST             0  'operation'
                3  LOAD_ATTR             0  'getBranch'
                6  CALL_FUNCTION_0       0  None
                9  LOAD_GLOBAL           1  'PM_BRANCH'
               12  LOAD_ATTR             2  'PERSONAL_MISSION_3'
               15  COMPARE_OP            2  ==
               18  POP_JUMP_IF_FALSE    49  'to 49'
               21  LOAD_GLOBAL           3  'isPMCampaignsStarted'
               24  LOAD_CONST               'branches'
               27  LOAD_GLOBAL           1  'PM_BRANCH'
               30  LOAD_ATTR             4  'ALL'
               33  CALL_FUNCTION_256   256  None
               36  JUMP_IF_TRUE_OR_POP    58  'to 58'
               39  LOAD_FAST             0  'operation'
               42  LOAD_ATTR             5  'hasRequiredVehicles'
               45  CALL_FUNCTION_0       0  None
               48  RETURN_END_IF    
             49_0  COME_FROM            36  '36'
             49_1  COME_FROM            18  '18'

 L. 211        49  LOAD_FAST             0  'operation'
               52  LOAD_ATTR             5  'hasRequiredVehicles'
               55  CALL_FUNCTION_0       0  None
               58  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `None' instruction at offset -1


def getStageNumberByDetailId(detailId):
    return int(detailId.split('_')[(-1)])


def hasAssemblingVideo(operationID, stageNumber):
    stageInfo = STAGES_CONFIG[operationID][stageNumber]
    return stageInfo.assemblingType == AssemblingType.VIDEO


def getPersonalMissions3URL():
    return GUI_SETTINGS.personalMissions3.get('infoPage', {}).get('url')


@adisp_process
def openInfoPageScreen():
    urlParser = URLMacros()
    url = yield urlParser.parse(getPersonalMissions3URL())
    showBrowserOverlayView(url, VIEW_ALIAS.BROWSER_OVERLAY)


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def wasOperationActivatedBefore(operation, unclaimedOperation=None, settingsCore=None):
    if unclaimedOperation is None:
        unclaimedOperation = firstUnclaimedOperation(operation, getSortedPm3Operations().values())
    wasPM3OperationActivated = operation.getID() in BRANCH_TO_OPERATION_IDS[PM_BRANCH.PERSONAL_MISSION_3][1:] and (unclaimedOperation is None or unclaimedOperation.getID() == operation.getID()) and settingsCore.serverSettings.getPM3InstalledVehDetails() == 0
    return operation.isStarted() or wasPM3OperationActivated


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def getRegularQuestsPMPoints(missionType, eventsCache=None):
    earnedPoints = 0
    totalPoints = 0
    if missionType == AdditionalMissionType.DAILY:
        quests = eventsCache.getDailyQuests()
        totalPoints = MAX_NEWBIE_DAILY_QUESTS_PM_POINTS if eventsCache.questsProgress.getTokenCount(NEWBIES_QUESTS_PASS_TOKEN) else MAX_DAILY_QUESTS_PM_POINTS
    else:
        quests = eventsCache.getWeeklyQuests()
    for quest in quests.values():
        for bonus in quest.getBonuses():
            if isinstance(bonus, PersonalMissionsPointsTokensBonus):
                points = bonus.getValue().get(PM_POINTS_TOKEN).get('count')
                if missionType == AdditionalMissionType.WEEKLY:
                    totalPoints += points
                if quest.isCompleted():
                    earnedPoints += points

    return (
     earnedPoints, totalPoints)# Decompile failed :(