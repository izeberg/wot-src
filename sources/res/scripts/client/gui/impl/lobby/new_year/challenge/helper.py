import typing, logging
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.mastery_progression_reward_level_model import MasteryProgressionRewardLevelModel
from gui.impl.new_year.new_year_bonus_packer import packBonusModelAndTooltipData, getMasteryProgressionBonusPacker
from helpers import dependency
from items.components.ny_constants import CelebrityQuestTokenParts
from new_year.celebrity.celebrity_quests_helpers import getCelebrityMasteryQuests, getFullSealTokensCount, masteryProgressionTokenCountExtractor
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.ho_mastery_progression_model import RewardState
from skeletons.new_year import INewYearController
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.ho_mastery_progression_model import HoMasteryProgressionModel

def fillMasteryProgression(masteryProgression):
    quests = getCelebrityMasteryQuests()
    if not quests:
        _logger.warning('Can not find mastery progression quests')
        return
    sortedQIDs = sorted(quests.keys(), key=lambda qID: int(qID.split(CelebrityQuestTokenParts.SEPARATOR)[(-1)]))
    masteryProgression.setCurrentProgress(getFullSealTokensCount())
    setMasteryProgressionRewardState(masteryProgression)
    levelsModel = masteryProgression.getRewardsLevels()
    levelsModel.clear()
    for qID in sortedQIDs:
        quest = quests[qID]
        progressModel = MasteryProgressionRewardLevelModel()
        progressModel.setProgress(masteryProgressionTokenCountExtractor(quest))
        packBonusModelAndTooltipData(quest.getBonuses(), progressModel.getRewards(), getMasteryProgressionBonusPacker())
        levelsModel.addViewModel(progressModel)

    levelsModel.invalidate()


def setMasteryProgressionRewardState(masteryProgressionModel):
    masteryProgressionModel.setRewardState(getMasteryProgressionRewardState())


@dependency.replace_none_kwargs(nyController=INewYearController)
def getMasteryProgressionRewardState(nyController=None):
    if not nyController.isDogTokenReceived():
        return RewardState.LOCKED
    if nyController.isDogObtainTokenReceived():
        return RewardState.OBTAINED
    return RewardState.AVAILABLE