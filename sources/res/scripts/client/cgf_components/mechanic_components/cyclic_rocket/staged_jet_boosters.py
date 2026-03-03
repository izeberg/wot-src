import CGF
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery
from StagedJetBoostersController import StagedJetBoostersController

@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class StagedJetBoostersComponentManager(CGF.ComponentManager):

    @onAddedQuery(StagedJetBoostersController)
    def onAdded(self, ctrl):
        ctrl.attachInput()
        ctrl.createInputLogger()

    @onRemovedQuery(StagedJetBoostersController)
    def onRemoved(self, ctrl):
        if ctrl.isValid and not ctrl.isComponentDestroyed():
            ctrl.detachInput()