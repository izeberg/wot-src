from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from collections import OrderedDict
    from Event import Event
    from typing import List, Optional
    from halloween.gui.game_control.halloween_anomalies_controller import AnomalyData, RecipeData

class IHalloweenAnomaliesController(IGameController):
    onRefreshData = None
    onChangeSystemAnomaliesUnlock = None

    @property
    def anomalies(self):
        raise NotImplementedError

    @property
    def lootAnomalies(self):
        raise NotImplementedError

    @property
    def recipes(self):
        raise NotImplementedError

    def getAnomalyByID(self, anomalyID):
        raise NotImplementedError