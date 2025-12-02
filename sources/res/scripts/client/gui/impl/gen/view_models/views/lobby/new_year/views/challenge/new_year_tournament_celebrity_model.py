from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.ho_mastery_progression_model import HoMasteryProgressionModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_card_model import NewYearChallengeCardModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_progress_model import NewYearChallengeProgressModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_upcoming_card_model import NewYearChallengeUpcomingCardModel

class NewYearTournamentCelebrityModel(ViewModel):
    __slots__ = ('onStylePreviewShow', 'onUpdateTimeTill', 'onVisited', 'onOpenMasteryRewardInfo')

    def __init__(self, properties=9, commands=4):
        super(NewYearTournamentCelebrityModel, self).__init__(properties=properties, commands=commands)

    @property
    def masteryProgression(self):
        return self._getViewModel(0)

    @staticmethod
    def getMasteryProgressionType():
        return HoMasteryProgressionModel

    def getDiscountPopoverId(self):
        return self._getString(1)

    def setDiscountPopoverId(self, value):
        self._setString(1, value)

    def getCompletedQuestsQuantity(self):
        return self._getNumber(2)

    def setCompletedQuestsQuantity(self, value):
        self._setNumber(2, value)

    def getPreviousCompletedQuestsQuantity(self):
        return self._getNumber(3)

    def setPreviousCompletedQuestsQuantity(self, value):
        self._setNumber(3, value)

    def getQuestsQuantity(self):
        return self._getNumber(4)

    def setQuestsQuantity(self, value):
        self._setNumber(4, value)

    def getTimeTill(self):
        return self._getNumber(5)

    def setTimeTill(self, value):
        self._setNumber(5, value)

    def getChallengeCards(self):
        return self._getArray(6)

    def setChallengeCards(self, value):
        self._setArray(6, value)

    @staticmethod
    def getChallengeCardsType():
        return NewYearChallengeCardModel

    def getUpcomingCards(self):
        return self._getArray(7)

    def setUpcomingCards(self, value):
        self._setArray(7, value)

    @staticmethod
    def getUpcomingCardsType():
        return NewYearChallengeUpcomingCardModel

    def getProgressRewards(self):
        return self._getArray(8)

    def setProgressRewards(self, value):
        self._setArray(8, value)

    @staticmethod
    def getProgressRewardsType():
        return NewYearChallengeProgressModel

    def _initialize(self):
        super(NewYearTournamentCelebrityModel, self)._initialize()
        self._addViewModelProperty('masteryProgression', HoMasteryProgressionModel())
        self._addStringProperty('discountPopoverId', '')
        self._addNumberProperty('completedQuestsQuantity', 0)
        self._addNumberProperty('previousCompletedQuestsQuantity', 0)
        self._addNumberProperty('questsQuantity', 0)
        self._addNumberProperty('timeTill', 0)
        self._addArrayProperty('challengeCards', Array())
        self._addArrayProperty('upcomingCards', Array())
        self._addArrayProperty('progressRewards', Array())
        self.onStylePreviewShow = self._addCommand('onStylePreviewShow')
        self.onUpdateTimeTill = self._addCommand('onUpdateTimeTill')
        self.onVisited = self._addCommand('onVisited')
        self.onOpenMasteryRewardInfo = self._addCommand('onOpenMasteryRewardInfo')