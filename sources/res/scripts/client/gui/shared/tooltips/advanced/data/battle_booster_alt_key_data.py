import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips.advanced.data.advanced_constants import SKILL_MOVIES
from gui.shared.tooltips.advanced.data.default_alt_key_data import DefaultAltKeyData
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.artefacts import BattleBooster

class BattleBoosterKeyData(DefaultAltKeyData):

    @classmethod
    def _getSwfName(cls, item, mechanicName):
        return SKILL_MOVIES.get(cls._getMechanicKeys(item))

    @staticmethod
    def _getHeader(item, mechanicName):
        return item.userName

    @classmethod
    def _getDescriptionKey(cls, item, mechanicName):
        if item.isCrewBooster():
            affectedSkillName = item.getAffectedSkillName()
            skillLocales = R.strings.crew_perks.dyn(affectedSkillName)
            if skillLocales.isValid():
                return backport.text(skillLocales.shortDescription())
            return affectedSkillName
        if item.isEconomicBooster():
            return item.descriptor.shortDescriptionSpecial
        return super(BattleBoosterKeyData, cls)._getDescriptionKey(item, mechanicName)