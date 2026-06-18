from __future__ import absolute_import
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import HasVehiclesList, Deprecated

class HistoricalAchievement(Deprecated, HasVehiclesList, RegularAchievement):
    _LIST_NAME = 'vehiclesTakePart'

    def _getVehiclesDescrsList(self):
        return []