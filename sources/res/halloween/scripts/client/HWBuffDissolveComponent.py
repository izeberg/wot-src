from __future__ import absolute_import, division
import weakref, BigWorld
from dyn_components_groups import groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from xml_config_specs import FloatParam
from functools import partial
from math_utils import clamp, clamp01

class DissolveUpdater(object):
    __slots__ = ('dissolveHandler', 'componentRef', 'entityRef', 'appearanceRef', 'dissolveFactor',
                 'fadeInTime', 'fadeOutTime', 'maxDissolveFactor', 'dissolveFashions',
                 'compoundModel')
    UPDATE_RATE = 0.05

    def __init__(self, componentRef, entityRef, appearanceRef, dissolveFactor, fadeInTime, fadeOutTime, maxDissolveFactor):
        super(DissolveUpdater, self).__init__()
        self.dissolveHandler = BigWorld.PyDissolveHandler()
        self.componentRef = componentRef
        self.entityRef = entityRef
        self.appearanceRef = appearanceRef
        self.dissolveFactor = clamp01(dissolveFactor)
        self.fadeInTime = max(0.0001, fadeInTime)
        self.fadeOutTime = max(0.0001, fadeOutTime)
        self.maxDissolveFactor = clamp01(maxDissolveFactor)
        self.dissolveFashions = None
        self.compoundModel = None
        return

    def start(self):
        appearance = self.appearanceRef()
        self.compoundModel = appearance.compoundModel
        self.dissolveFashions = tuple(f for f in appearance.fashions if f)
        for fashion in self.dissolveFashions:
            fashion.addMaterialHandler(self.dissolveHandler)
            fashion.addTrackMaterialHandler(self.dissolveHandler)

        self.dissolveHandler.setEnabled(True)
        DissolveUpdater._updateDissolve(self)

    def stop(self):
        if self.dissolveHandler is not None and self._isTargetValid():
            self.dissolveHandler.setEnabled(False)
            if self.dissolveFashions is not None:
                for fashion in self.dissolveFashions:
                    fashion.removeMaterialHandler(self.dissolveHandler)

        self.dissolveFashions = None
        self.dissolveHandler = None
        self.compoundModel = None
        return

    def _isTargetValid(self):
        entity = self.entityRef()
        appearance = self.appearanceRef()
        if entity is None or entity.isDestroyed or not entity.isStarted:
            return False
        if appearance is None or entity.appearance is not appearance:
            return False
        if appearance.compoundModel is not self.compoundModel:
            return False
        else:
            fashions = appearance.fashions
            return all(f in fashions for f in self.dissolveFashions or ())

    @classmethod
    def _updateDissolve(cls, updater):
        if not cls._isTargetValid(updater) or updater.entityRef().health <= 0:
            updater.stop()
            return
        prevFactor = updater.dissolveFactor
        velocity = updater.maxDissolveFactor / updater.fadeInTime if updater.componentRef() else -updater.maxDissolveFactor / updater.fadeOutTime
        updater.dissolveFactor = clamp(0.0, updater.maxDissolveFactor, updater.dissolveFactor + cls.UPDATE_RATE * velocity)
        if prevFactor != updater.dissolveFactor:
            updater.dissolveHandler.setDissolveFactor(updater.dissolveFactor)
        if not updater.componentRef() and updater.dissolveFactor <= 0.0:
            updater.stop()
            return
        BigWorld.callback(cls.UPDATE_RATE, partial(cls._updateDissolve, updater))


@groupComponent(fadeInTime=FloatParam(1.0), fadeOutTime=FloatParam(1.0), maxDissolveFactor=FloatParam(1.0))
class HWBuffDissolveComponent(DynamicScriptComponent):

    def _onAvatarReady(self):
        super(HWBuffDissolveComponent, self)._onAvatarReady()
        appearance = self.entity.appearance
        if appearance is None or not appearance.isConstructed:
            self.entity.events.onAppearanceReady += self._onAppearanceReady
        elif not appearance.damageState.isCurrentModelDamaged:
            self._onAppearanceReady()
        return

    def onDestroy(self):
        self.entity.events.onAppearanceReady -= self._onAppearanceReady

    def _onAppearanceReady(self):
        appearance = self.entity.appearance
        self.entity.events.onAppearanceReady -= self._onAppearanceReady
        if appearance.damageState.isCurrentModelDamaged:
            return
        DissolveUpdater(componentRef=weakref.ref(self), entityRef=weakref.ref(self.entity), appearanceRef=weakref.ref(appearance), dissolveFactor=0.0, fadeInTime=self.groupComponentConfig.fadeInTime, fadeOutTime=self.groupComponentConfig.fadeOutTime, maxDissolveFactor=self.groupComponentConfig.maxDissolveFactor).start()