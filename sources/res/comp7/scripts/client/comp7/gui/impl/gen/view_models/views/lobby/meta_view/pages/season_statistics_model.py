from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.statistics_model import StatisticsModel

class SeasonStatisticsModel(StatisticsModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(SeasonStatisticsModel, self).__init__(properties=properties, commands=commands)

    def getDayOfMaxRatingIndex(self):
        return self._getNumber(14)

    def setDayOfMaxRatingIndex(self, value):
        self._setNumber(14, value)

    def _initialize(self):
        super(SeasonStatisticsModel, self)._initialize()
        self._addNumberProperty('dayOfMaxRatingIndex', 0)