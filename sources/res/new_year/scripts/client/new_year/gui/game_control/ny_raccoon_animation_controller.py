import CGF, Event
from new_year.gui.impl.gen.view_models.views.lobby.new_year.ny_pet_tv_screen_view_model import PetTvAnimation
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_model import State
from new_year_account_settings import getNYSetting, setNYSettings
from new_year.ny_constants import NY_HAS_PET_ANIMATION
from new_year.skeletons.new_year import IRaccoonAnimationController
from new_year.cgf.raccoon_customization_components import RaccoonManager, RaccoonMoodStates, RaccoonCommands
from skeletons.gui.shared.utils import IHangarSpace
from helpers.CallbackDelayer import CallbackDelayer
from helpers import dependency
_STATE_TO_MOOD = {State.FUN: RaccoonMoodStates.HAPPY, 
   State.NORMAL: RaccoonMoodStates.NEUTRAL, 
   State.SAD: RaccoonMoodStates.SAD}
_INDICATOR_TO_TV_ANIMATION = {RaccoonCommands.FOOD: PetTvAnimation.FOOD, 
   RaccoonCommands.FUN: PetTvAnimation.CARE, 
   RaccoonCommands.ACTIVITY: PetTvAnimation.ACTIVITY}

class RaccoonAnimationController(IRaccoonAnimationController):
    __slots__ = ('__animationsEnabled', '__isRaidStarted', '__isTvRaidActive', '__tvAnimation',
                 '__em', '__tvPresentationDelayer', 'onRaidStateChanged', 'onTvRaidPresentationChanged',
                 'onTvAnimationChanged')
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        super(RaccoonAnimationController, self).__init__()
        self.__animationsEnabled = False
        self.__isRaidStarted = False
        self.__isTvRaidActive = False
        self.__tvAnimation = PetTvAnimation.OFF
        self.__tvPresentationDelayer = CallbackDelayer()
        self.__em = Event.EventManager()
        self.onRaidStateChanged = Event.Event(self.__em)
        self.onTvRaidPresentationChanged = Event.Event(self.__em)
        self.onTvAnimationChanged = Event.Event(self.__em)

    def onConnected(self):
        self.__animationsEnabled = getNYSetting(NY_HAS_PET_ANIMATION)

    def fini(self):
        self.__tvPresentationDelayer.clearCallbacks()
        self.__em.clear()

    def onDisconnected(self):
        self.__tvPresentationDelayer.clearCallbacks()
        self.__isRaidStarted = False
        self.__isTvRaidActive = False
        self.__tvAnimation = PetTvAnimation.OFF

    @property
    def __raccoonManager(self):
        if self.__hangarSpace.spaceID:
            return CGF.getManager(self.__hangarSpace.spaceID, RaccoonManager)
        else:
            return

    @property
    def isRaidStarted(self):
        return self.__isRaidStarted

    @property
    def isRaidActive(self):
        return self.__isTvRaidActive

    @property
    def tvAnimation(self):
        return self.__tvAnimation

    @property
    def raidAnimationDuration(self):
        if self.__raccoonManager:
            return self.__raccoonManager.raidAnimationDuration
        return 0.0

    def setRaidActive(self, isActive):
        if isActive:
            if self.__isTvRaidActive:
                return
            manager = self.__raccoonManager
            alreadyInRaidVisual = bool(manager and manager.isRaidVisualActive())
            raidExitAtEnd = bool(alreadyInRaidVisual and manager.isRaidExitAtEnd())
            if self.__isRaidStarted:
                if raidExitAtEnd:
                    self.beginTvRaidPresentation()
                return
            self.__isRaidStarted = True
            if manager and not alreadyInRaidVisual:
                manager.doRaidAction()
            self.onRaidStateChanged(True)
            if raidExitAtEnd:
                self.beginTvRaidPresentation()
            else:
                self.__scheduleTvPresentation()
            return
        self.__resetRaidPresentation()

    def beginTvRaidPresentation(self):
        self.__tvPresentationDelayer.clearCallbacks()
        if not self.__isRaidStarted or self.__isTvRaidActive:
            return
        self.__isTvRaidActive = True
        self.setTvAnimation(PetTvAnimation.WALK)
        self.onTvRaidPresentationChanged(True)

    def endRaidTvPresentation(self):
        if not self.__isTvRaidActive:
            if self.__isRaidStarted:
                self.__resetRaidPresentation()
            return
        if self.__tvAnimation == PetTvAnimation.OFF and not self.__isRaidStarted:
            return
        self.__isRaidStarted = False
        self.setTvAnimation(PetTvAnimation.OFF)

    def onTvPresentationFinished(self):
        if self.__tvAnimation == PetTvAnimation.OFF:
            self.__resetRaidPresentation()
        elif self.__isRaidStarted:
            self.setTvAnimation(PetTvAnimation.WALK)

    def setTvAnimation(self, animation):
        if self.__tvAnimation == animation:
            return
        self.__tvAnimation = animation
        self.onTvAnimationChanged(animation)

    def setAnimationsEnabled(self, enabled):
        setNYSettings(NY_HAS_PET_ANIMATION, enabled)
        self.__animationsEnabled = enabled
        if not self.__animationsEnabled:
            manager = self.__raccoonManager
            if manager:
                manager.clearQueue()

    def activateItem(self, name):
        if self.__isTvRaidActive:
            if self.__isRaidStarted:
                animation = _INDICATOR_TO_TV_ANIMATION.get(name)
                if animation is not None:
                    self.setTvAnimation(animation)
            return
        if self.__isRaidStarted:
            return
        else:
            if self.__animationsEnabled:
                manager = self.__raccoonManager
                if manager:
                    manager.addCommand(name)
            return

    def updateMoodState(self, state):
        mood = _STATE_TO_MOOD.get(state)
        if mood is None:
            return
        else:
            manager = self.__raccoonManager
            if manager:
                manager.setMoodState(mood)
            return

    def __scheduleTvPresentation(self):
        self.__tvPresentationDelayer.clearCallbacks()
        self.__tvPresentationDelayer.delayCallback(self.raidAnimationDuration, self.beginTvRaidPresentation)

    def __resetRaidPresentation(self):
        self.__tvPresentationDelayer.clearCallbacks()
        wasRaidStarted = self.__isRaidStarted or self.__isTvRaidActive
        wasTvActive = self.__isTvRaidActive
        self.__isRaidStarted = False
        self.__isTvRaidActive = False
        manager = self.__raccoonManager
        if manager:
            manager.releaseRaidAction()
        if wasTvActive:
            self.onTvRaidPresentationChanged(False)
        self.setTvAnimation(PetTvAnimation.OFF)
        if wasRaidStarted:
            self.onRaidStateChanged(False)