import typing, weakref
from functools import partial
import BigWorld, CGF
from GenericComponents import AnimatorComponent
import Event
from cgf_script.managers_registrator import autoregisterInBattle, onAddedQuery, onRemovedQuery
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider
from constants import ARENA_PERIOD
if typing.TYPE_CHECKING:
    from typing import List

@registerComponent
class PrebattleAnimationComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'Prebattle animation'
    category = 'Battle'
    singleAnimation = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Prebattle singleAnim object', value=CGF.GameObject)
    timer = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='SingleAnim delay before start battle, sec')
    loopAnimation = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Prebattle loopAnim object', value=CGF.GameObject)


@autoregisterInBattle(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class PrebattleAnimManager(CGF.ComponentManager):

    def __init__(self):
        super(PrebattleAnimManager, self).__init__()
        self.__prebattleAnimComponents = {}
        self.__prebattleAnimTriggerHandler = PrebattleAnimTriggerHandler()
        self.__callbackDelayer = CallbackDelayer()

    def activate(self):
        self.__prebattleAnimTriggerHandler.onSingleAnimStart += self.__onSingleAnimStart
        self.__prebattleAnimTriggerHandler.onPrebaatleTimerStart += self.__onPrebattleAnimStart
        self.__prebattleAnimTriggerHandler.onBattleStart += self.__onBattleStartStart

    def deactivate(self):
        if self.__prebattleAnimTriggerHandler:
            self.__prebattleAnimTriggerHandler.onSingleAnimStart -= self.__onSingleAnimStart
            self.__prebattleAnimTriggerHandler.onPrebaatleTimerStart -= self.__onPrebattleAnimStart
            self.__prebattleAnimTriggerHandler.onBattleStart -= self.__onBattleStartStart
            self.__prebattleAnimTriggerHandler.clear()
        self.__prebattleAnimTriggerHandler = None
        self.__prebattleAnimComponents.clear()
        self.__callbackDelayer.clearCallbacks()
        return

    @onAddedQuery(CGF.GameObject, PrebattleAnimationComponent)
    def onListenerAdded(self, go, animComponent):
        if self.__prebattleAnimTriggerHandler and self.__prebattleAnimTriggerHandler.isValidPeriod():
            animId = id(animComponent)
            self.__prebattleAnimComponents[animId] = (weakref.proxy(go), weakref.proxy(animComponent))
            self.__prebattleAnimTriggerHandler.startListen(animId, animComponent.timer)
        else:
            self.__deactivateAnimObjects(animComponent)

    @onRemovedQuery(PrebattleAnimationComponent)
    def onListenerRemoved(self, animComponent):
        objId = id(animComponent)
        if objId in self.__prebattleAnimComponents:
            self.__prebattleAnimComponents.pop(objId)

    def __deactivateAnimObjects(self, prebattleComponent):
        singleAnimation = prebattleComponent.singleAnimation
        if singleAnimation:
            singleAnimation.deactivate()
        loopAnimation = prebattleComponent.loopAnimation
        if loopAnimation:
            loopAnimation.deactivate()
        self.__callbackDelayer.clearCallbacks()

    def __onSingleAnimStart(self, objId, timeAfterStart=0.0):
        if objId in self.__prebattleAnimComponents:
            _, anim = self.__prebattleAnimComponents[objId]
            singleAnimation = anim.singleAnimation
            if singleAnimation:
                if singleAnimation.isActive():
                    self.__playSingleAnim(singleAnimation, timeAfterStart)
                else:
                    singleAnimation.activate()
                    callback = partial(self.__playSingleAnim, singleAnimation, timeAfterStart)
                    self.__callbackDelayer.delayCallback(0, callback)

    def __playSingleAnim(self, singleAnimation, timeAfterStart):
        self.__singleAnimCallback = None
        result = self.__findAnimatorComponent(singleAnimation)
        if result:
            _, animComponent = result[0]
            animComponent.stop()
            animComponent.start(timeAfterStart * animComponent.getSpeed())
        return

    def __onPrebattleAnimStart(self, timeBeforeStartBattle):
        for go, anim in self.__prebattleAnimComponents.values():
            go.activate()
            loopAnimation = anim.loopAnimation
            if loopAnimation:
                if loopAnimation.isActive():
                    self.__playLoopAnim(loopAnimation, timeBeforeStartBattle)
                else:
                    loopAnimation.activate()
                    callback = partial(self.__playLoopAnim, loopAnimation, timeBeforeStartBattle)
                    self.__callbackDelayer.delayCallback(0, callback)

    def __playLoopAnim(self, loopAnimation, timeBeforeStartBattle):
        self.__loopAnimCallback = None
        animComponent = loopAnimation.findComponentByType(AnimatorComponent)
        animDuration = animComponent.getDuration() / animComponent.getSpeed()
        timeAfterStart = animDuration - (timeBeforeStartBattle % animDuration if animDuration else animDuration)
        self.__updateAnimatorComponentPosition(loopAnimation, timeAfterStart)
        return

    def __onBattleStartStart(self):
        for _, prebattleAnimComponent in self.__prebattleAnimComponents.values():
            self.__deactivateAnimObjects(prebattleAnimComponent)

    def __updateAnimatorComponentPosition(self, animation, timeAfterStart):
        if timeAfterStart >= 0:
            result = self.__findAnimatorComponent(animation)
            if result:
                for _, animComponent in result:
                    animComponent.reset()
                    animComponent.start(timeAfterStart * animComponent.getSpeed())

    @staticmethod
    def __findAnimatorComponent(gameObject):
        hierarchy = CGF.HierarchyManager(gameObject.spaceID)
        return hierarchy.findComponentsInHierarchy(gameObject, AnimatorComponent, includingRoot=True)


class PrebattleAnimTriggerHandler(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(PrebattleAnimTriggerHandler, self).__init__()
        self.__delayer = CallbackDelayer()
        self.__eManager = Event.EventManager()
        self.__animsReadyToPlay = {}
        self.onSingleAnimStart = Event.Event(self.__eManager)
        self.onPrebaatleTimerStart = Event.Event(self.__eManager)
        self.onBattleStart = Event.Event(self.__eManager)

    def startListen(self, objId, animDelayBeforeStartBattle):
        period = self.__getPeriod()
        if period == ARENA_PERIOD.PREBATTLE:
            self.__checkAnimStartTime(objId, animDelayBeforeStartBattle)
        elif period not in (ARENA_PERIOD.BATTLE, ARENA_PERIOD.AFTERBATTLE):
            self.__animsReadyToPlay[objId] = animDelayBeforeStartBattle
        else:
            self.onBattleStart()
        arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
        arena.onPeriodChange += self.__onArenaPeriodChange

    def clear(self):
        self.__eManager.clear()
        self.__clearArenaListeners()
        self.__delayer.clearCallbacks()
        self.__animsReadyToPlay.clear()

    def isValidPeriod(self):
        return self.__getPeriod() not in (ARENA_PERIOD.BATTLE, ARENA_PERIOD.AFTERBATTLE)

    def __clearArenaListeners(self):
        arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
        if arena:
            arena.onPeriodChange -= self.__onArenaPeriodChange

    def __checkAnimStartTime(self, objId, animDelayBeforeStartBattle):
        timeBeforeStartAnim = self.__getTimeBeforeStartBattle() - animDelayBeforeStartBattle
        if timeBeforeStartAnim > 0:
            self.__delayer.delayCallback(timeBeforeStartAnim, partial(self.__callbackOnAnimStart, objId))
        else:
            self.onSingleAnimStart(objId, abs(timeBeforeStartAnim))

    def __onArenaPeriodChange(self, arenaPeriod, endTime, *_):
        if arenaPeriod == ARENA_PERIOD.PREBATTLE:
            self.onPrebaatleTimerStart(self.__getTimeBeforeStartBattle())
            for objId, animDelayBeforeStartBattle in self.__animsReadyToPlay.iteritems():
                self.__checkAnimStartTime(objId, animDelayBeforeStartBattle)

        elif arenaPeriod == ARENA_PERIOD.BATTLE:
            self.onBattleStart()
            self.__clearArenaListeners()

    def __getPeriod(self):
        return self.__sessionProvider.shared.arenaPeriod.getPeriod()

    def __getTimeBeforeStartBattle(self):
        arenaPeriod = self.__sessionProvider.shared.arenaPeriod
        if arenaPeriod.getPeriod() == ARENA_PERIOD.PREBATTLE:
            return arenaPeriod.getEndTime() - BigWorld.serverTime()
        return 0

    def __callbackOnAnimStart(self, objId):
        self.onSingleAnimStart(objId)