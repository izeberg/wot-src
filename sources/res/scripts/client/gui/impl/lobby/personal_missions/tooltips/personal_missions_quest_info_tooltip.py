from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.personal_missions.tooltips.personal_missions_quest_info_tooltip_model import PersonalMissionsQuestInfoTooltipModel, HelpTooltipType
from gui.impl.pub import ViewImpl
from gui.server_events.event_items import PersonalMission
import personal_missions_constants as PMConstants
from shared_utils import first
from helpers import dependency
from skeletons.gui.game_control import IPersonalMissionsController

class PersonalMissionsQuestInfoTooltip(ViewImpl):
    __slots__ = ('__questId', )
    __personalMissionsCtrl = dependency.descriptor(IPersonalMissionsController)

    def __init__(self, questId):
        settings = ViewSettings(R.views.lobby.personal_missions.tooltips.PersonalMissionsQuestInfoTooltip())
        settings.model = PersonalMissionsQuestInfoTooltipModel()
        self.__questId = int(questId)
        super(PersonalMissionsQuestInfoTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(PersonalMissionsQuestInfoTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(PersonalMissionsQuestInfoTooltip, self)._onLoading()
        with self.viewModel.transaction() as (vm):
            vm.setType(self.__getQuestHelpTooltipType(self.__personalMissionsCtrl.getQuest(self.__questId)))

    def __getQuestHelpTooltipType(self, quest):
        if quest is None:
            return HelpTooltipType.TYPE1
        else:
            questConfig = quest.getConditionsConfig()
            isFinal = quest.isFinal()
            mainQuestsDict = {}
            addQuestsDict = {}
            for key, val in questConfig.iteritems():
                quest = val.get('config')
                if quest['isMain']:
                    mainQuestsDict[key] = val
                else:
                    addQuestsDict[key] = val

            if isFinal:
                return self.__getFinalQuestType(mainQuestsDict, addQuestsDict)
            return self.__getMainQuestType(mainQuestsDict)

    @staticmethod
    def __getMainQuestType(mainQuestsDict):
        mainQuestsCount = len(mainQuestsDict)
        if mainQuestsCount == 1:
            questItem = first(mainQuestsDict.itervalues())
            if questItem['config'].get('isCumulative', False):
                return HelpTooltipType.TYPE1
            questItemName = first(mainQuestsDict)
            if 'Diversity' in questItemName or 'targetClasses' in mainQuestsDict[questItemName].get('params', {}):
                return HelpTooltipType.TYPE8
        if mainQuestsCount > 1 and 'battlesSeries' not in mainQuestsDict:
            if all(questItem['config'].get('isCumulative', False) for questItem in mainQuestsDict.itervalues()):
                return HelpTooltipType.TYPE2
        if all('groupID' in questItem['config'] for questItem in mainQuestsDict.itervalues()):
            if 'battlesSeries' in mainQuestsDict:
                return HelpTooltipType.TYPE5
            return HelpTooltipType.TYPE7
        if mainQuestsCount == 2 and 'battlesSeries' in mainQuestsDict:
            return HelpTooltipType.TYPE3
        if mainQuestsCount > 2 and 'battlesSeries' in mainQuestsDict:
            return HelpTooltipType.TYPE4
        if 'battlesSeries1' in mainQuestsDict and 'battlesSeries2' in mainQuestsDict:
            return HelpTooltipType.TYPE6
        if mainQuestsCount == 2:
            for questItemName, questItem in mainQuestsDict.iteritems():
                if 'Diversity' in questItemName or 'targetClasses' in mainQuestsDict[questItemName].get('params', {}):
                    return HelpTooltipType.TYPE9

            firstQuestInfo, secondQuestInfo = mainQuestsDict.itervalues()
            if firstQuestInfo['config'].get('isCumulative', False) != secondQuestInfo['config'].get('isCumulative', False):
                return HelpTooltipType.TYPE10
        return HelpTooltipType.TYPE11

    @staticmethod
    def __getFinalQuestType(mainQuestsDict, addQuestsDict):
        isHasTypeSeriesInMain = False
        isHasTypeSeriesInAdd = False
        for questInfo in mainQuestsDict.itervalues():
            description = questInfo.get('description', None)
            if isinstance(description, PMConstants.HeaderDescription) and description.displayType == PMConstants.DISPLAY_TYPE.SERIES:
                isHasTypeSeriesInMain = True
                break

        for questInfo in addQuestsDict.itervalues():
            description = questInfo.get('description', None)
            if isinstance(description, PMConstants.HeaderDescription) and description.displayType == PMConstants.DISPLAY_TYPE.SERIES:
                isHasTypeSeriesInAdd = True
                break

        if isHasTypeSeriesInMain and isHasTypeSeriesInAdd:
            return HelpTooltipType.TYPE20
        else:
            isHasDescriptionWithCounterIdMain = any(isinstance(questItem.get('description', None), PMConstants.AverageDescription) for questItem in mainQuestsDict.itervalues())
            isHasDescriptionWithCounterIdAdd = any(isinstance(questItem.get('description', None), PMConstants.AverageDescription) for questItem in addQuestsDict.itervalues())
            if isHasDescriptionWithCounterIdMain and isHasDescriptionWithCounterIdAdd:
                return HelpTooltipType.TYPE24
            hasSeriesInNameMain = any('Series' in questItem for questItem in mainQuestsDict)
            hasSeriesInNameAdd = any('Series' in questItem for questItem in addQuestsDict)
            hasAddIsCumulative = any(questItem['config'].get('isCumulative', False) for questItem in addQuestsDict.itervalues())
            hasMainIsCumulative = any(questItem['config'].get('isCumulative', False) for questItem in mainQuestsDict.itervalues())
            if not hasSeriesInNameMain and not hasMainIsCumulative and not hasSeriesInNameAdd and not hasAddIsCumulative:
                return HelpTooltipType.TYPE21
            isHasBattleSeriesWithLimitMain = False
            isHasBattleSeriesWithLimitAdd = False
            for questName, questInfo in addQuestsDict.iteritems():
                if 'Series' in questName and 'battlesLimit' in questInfo['config']:
                    isHasBattleSeriesWithLimitAdd = True
                    break

            for questName, questInfo in mainQuestsDict.iteritems():
                if 'Series' in questName and 'battlesLimit' in questInfo['config']:
                    isHasBattleSeriesWithLimitMain = True
                    break

            if not isHasBattleSeriesWithLimitMain and not isHasBattleSeriesWithLimitAdd:
                return HelpTooltipType.TYPE22
            if not hasSeriesInNameMain and not hasMainIsCumulative and isHasBattleSeriesWithLimitAdd:
                return HelpTooltipType.TYPE23
            if hasSeriesInNameMain and hasSeriesInNameAdd:
                return HelpTooltipType.TYPE25
            return HelpTooltipType.TYPE20