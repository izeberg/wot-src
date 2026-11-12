import Event
from festivity.base import FestivityQuestsHangarFlag
from skeletons.gui.game_control import IFestivityController, IFestivityFirstEnterVideoController
_DEFAULT_QUESTS_FLAG = FestivityQuestsHangarFlag(None, None, None)

class DummyController(IFestivityController):

    def __init__(self):
        super(DummyController, self).__init__()
        self.__state = None
        self.__em = Event.EventManager()
        self.onStateChanged = Event.Event(self.__em)
        self.onUpdateSlot = Event.Event(self.__em)
        self.onSetHangToyEffectEnabled = Event.Event(self.__em)
        self.__firstEnterVideo = DummyFirstEnterVideoController()
        return

    def isEnabled(self):
        return False

    def getHangarQuestsFlagData(self):
        return _DEFAULT_QUESTS_FLAG

    def getHangarWidgetLinkage(self):
        return

    def getHangarEdgeColor(self):
        return

    def isInProgress(self):
        return False

    def isPostEvent(self):
        return False

    def isWidgetVisible(self, prbState):
        return False

    def isCreditBonusVisible(self, prbState):
        return False

    def isOnboardingFinished(self):
        return False

    @property
    def firstEnterVideo(self):
        return self.__firstEnterVideo


class DummyFirstEnterVideoController(IFestivityFirstEnterVideoController):

    def __init__(self):
        super(DummyFirstEnterVideoController, self).__init__()
        self.__em = Event.EventManager()
        self.onIntroComplete = Event.Event(self.__em)

    def shouldStartIntro(self):
        return False

    @property
    def isActive(self):
        return False

    def tryStartIntro(self):
        pass