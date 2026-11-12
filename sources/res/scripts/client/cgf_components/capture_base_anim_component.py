import BigWorld, CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import autoregisterInBattle, onAddedQuery, onRemovedQuery
from PlayerEvents import g_playerEvents

@registerComponent
class CaptureBaseAnimationComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'Capture base component'
    category = 'Battle'
    baseCapturedAnim = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Base captured anim', value=CGF.GameObject)

    def __init__(self):
        super(CaptureBaseAnimationComponent, self).__init__()
        self.teamId = 0
        self.baseId = 0


@autoregisterInBattle(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class CaptureBaseManager(CGF.ComponentManager):
    _MAX_POINTS = 100

    def __init__(self):
        super(CaptureBaseManager, self).__init__()
        self._animComponents = {}

    def activate(self):
        g_playerEvents.onBaseCapture += self.__onBaseCapture

    def deactivate(self):
        g_playerEvents.onBaseCapture -= self.__onBaseCapture
        self._animComponents.clear()

    @onAddedQuery(CGF.GameObject, CaptureBaseAnimationComponent)
    def onListenerAdded(self, go, animComponent):
        key = self.__getAnimationKey(animComponent.teamId, animComponent.baseId)
        self._animComponents[key] = animComponent

    @onRemovedQuery(CaptureBaseAnimationComponent)
    def onListenerRemoved(self, animComponent):
        key = self.__getAnimationKey(animComponent.teamId, animComponent.baseId)
        self._animComponents.pop(key, None)
        return

    @staticmethod
    def __getAnimationKey(teamId, baseId):
        return teamId << 8 | baseId

    def __onBaseCapture(self, baseTeam, baseID, points, timeLeft, invadersCnt, capturingStopped):
        key = self.__getAnimationKey(baseTeam, baseID)
        if key in self._animComponents:
            if points >= self._MAX_POINTS and BigWorld.player().team != baseTeam:
                self.__playBaseCapturedAnimation(self._animComponents[key])

    def __playBaseCapturedAnimation(self, animComponent):
        if animComponent.baseCapturedAnim:
            animComponent.baseCapturedAnim.activate()