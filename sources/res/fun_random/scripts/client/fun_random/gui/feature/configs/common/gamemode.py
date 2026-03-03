from __future__ import absolute_import
from dict2model import fields, models, schemas

class GameModeConfigurationModel(models.Model):
    __slots__ = ('regularDevices', 'regularBoosters', 'regularShells', 'regularConsumables')

    def __init__(self, regularDevices, regularBoosters, regularShells, regularConsumables):
        super(GameModeConfigurationModel, self).__init__()
        self.regularDevices = regularDevices
        self.regularBoosters = regularBoosters
        self.regularShells = regularShells
        self.regularConsumables = regularConsumables


gameModeConfigurationSchema = schemas.Schema[GameModeConfigurationModel](fields={'regularDevices': fields.Boolean(required=True), 
   'regularBoosters': fields.Boolean(required=True), 
   'regularShells': fields.Boolean(required=True), 
   'regularConsumables': fields.Boolean(required=True)}, modelClass=GameModeConfigurationModel)