from collections import namedtuple
import BigWorld, CGF
from Math import Matrix, Vector3
import AnimationSequence
from cgf_components.capture_base_anim_component import CaptureBaseAnimationComponent
from GenericComponents import TransformComponent
FlagSettings = namedtuple('FlagSettings', ('flagCompounModel', 'flagAlias', 'flagAnim',
                                           'flagBackgroundTex', 'spaceID', 'flagEffectPrefab',
                                           'teamId', 'baseId'))

class FlagModel(object):
    model = property(lambda self: self.__flagCompoundModel)

    def __init__(self):
        self.__flagCompoundModel = None
        self.__flagStaffFashion = None
        self.__flagFashion = None
        self.__flagAnimator = None
        self.__spaceID = None
        self.__teamId = 0
        self.__baseId = 0
        return

    def setupFlag(self, position, flagSettings, color):
        self.__spaceID = flagSettings.spaceID
        self.__flagCompoundModel = flagSettings.flagCompounModel
        self.__flagCompoundModel.position = position
        self.__teamId = flagSettings.teamId
        self.__baseId = flagSettings.baseId
        self.__flagStaffFashion = BigWorld.AlphaFadeCompoundFashion()
        self.__flagFashion = BigWorld.FlagAlphaFadeFashion()
        self.__flagFashion.setColor(color)
        if flagSettings.flagEffectPrefab:
            go = CGF.GameObject(flagSettings.spaceID)
            go.createComponent(TransformComponent, position)
            go.activate()
            go.transferOwnershipToWorld()
            CGF.loadGameObjectIntoHierarchy(flagSettings.flagEffectPrefab, go, Vector3(), hierarchyLoadedCallback=self.__onEffectPrefabLoaded)
        translationMatrix = Matrix()
        translationMatrix.setTranslate(position)
        self.__flagFashion.overridePosition(translationMatrix)
        self.__flagCompoundModel.setupFashions((self.__flagStaffFashion, self.__flagFashion))
        self.__flagAnimator = flagSettings.flagAnim
        if self.__flagAnimator is not None:
            self.__flagAnimator.bindTo(AnimationSequence.PartWrapperContainer(self.__flagCompoundModel, self.__spaceID, flagSettings.flagAlias))
        return

    def changeFlagColor(self, color):
        if self.__flagFashion:
            self.__flagFashion.setColor(color)

    def startFlagAnimation(self):
        if self.__flagAnimator:
            self.__flagAnimator.start()

    def __onEffectPrefabLoaded(self, gameObject):
        hierarchyManager = CGF.HierarchyManager(gameObject.spaceID)
        if hierarchyManager:
            components = hierarchyManager.findComponentsInHierarchy(gameObject, CaptureBaseAnimationComponent)
            if components:
                for _, component in components:
                    component.teamId = self.__teamId
                    component.baseId = self.__baseId