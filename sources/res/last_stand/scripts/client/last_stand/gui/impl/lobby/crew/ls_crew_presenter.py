from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from gui.shared.gui_items import checkForTags
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter
from items.tankmen import MAX_SKILL_LEVEL

class LSCrewPresenter(CrewPresenter):

    def _createTankmanModel(self, tman, battleBoosterBonus, isQuickTrainingEnabled, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses):
        model = super(LSCrewPresenter, self)._createTankmanModel(tman, battleBoosterBonus, isQuickTrainingEnabled, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses)
        if g_currentVehicle.isPresent() and checkForTags(g_currentVehicle.item.tags, 'lockCrewSkills'):
            model.setNewPerksCount(0)
            model.setNewBonusPerksCount(0)
            model.setTrainingProgress(MAX_SKILL_LEVEL)
        return model