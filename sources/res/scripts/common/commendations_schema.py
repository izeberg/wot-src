from game_params_common.base_manager import GameParamsSchema
from constants import Configs
from dict2model import models, fields as d2mfields

class CommendationsConfigModel(models.Model):
    __slots__ = ('isLiveTagsEnabled', 'isCommendationsEnabled')

    def __init__(self, isLiveTagsEnabled, isCommendationsEnabled):
        super(CommendationsConfigModel, self).__init__()
        self.isCommendationsEnabled = isCommendationsEnabled
        self.isLiveTagsEnabled = isLiveTagsEnabled


commendationsConfigSchema = GameParamsSchema[CommendationsConfigModel](gameParamsKey=Configs.COMMENDATIONS_CONFIG.value, fields={'isLiveTagsEnabled': d2mfields.Boolean(), 
   'isCommendationsEnabled': d2mfields.Boolean()}, modelClass=CommendationsConfigModel, checkUnknown=True, usedInReplay=True)