from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel

class Comp7LightParamType(Enum):
    SHOTS = 'shots'
    HITS = 'hits'
    EXPLOSIONHITS = 'explosionHits'
    DAMAGEDEALT = 'damageDealt'
    SNIPERDAMAGEDEALT = 'sniperDamageDealt'
    DAMAGEDEALTBYSKILLS = 'damageDealtBySkills'
    ARTILLERYSTRIKE = 'artilleryStrike'
    DIRECTHITSRECEIVED = 'directHitsReceived'
    PIERCINGSRECEIVED = 'piercingsReceived'
    NODAMAGEDIRECTHITSRECEIVED = 'noDamageDirectHitsReceived'
    EXPLOSIONHITSRECEIVED = 'explosionHitsReceived'
    DAMAGEBLOCKEDBYARMOR = 'damageBlockedByArmor'
    TEAMHITSDAMAGE = 'teamHitsDamage'
    SPOTTED = 'spotted'
    DAMAGEDKILLED = 'damagedKilled'
    DAMAGEASSISTED = 'damageAssisted'
    DAMAGEASSISTEDSELF = 'damageAssistedSelf'
    STUNDURATION = 'stunDuration'
    DAMAGEASSISTEDSTUN = 'damageAssistedStun'
    DAMAGEASSISTEDSTUNSELF = 'damageAssistedStunSelf'
    STUNNUM = 'stunNum'
    CAPTUREPOINTSVAL = 'capturePointsVal'
    MILEAGE = 'mileage'
    HEALED = 'healed'
    CAPTUREDPOINTSOFINTEREST = 'capturedPointsOfInterest'
    ROLESKILLUSED = 'roleSkillUsed'


class Comp7LightDetailedStatsParameterModel(DetailedStatsParameterModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(Comp7LightDetailedStatsParameterModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Comp7LightDetailedStatsParameterModel, self)._initialize()