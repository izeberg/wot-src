import CGF
from BunkerLogicComponent import BunkerLogicComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, autoregister

@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class BunkersManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, BunkerLogicComponent)
    def onBunkerLogicComponentAdded(self, _, bunkerLogic):
        bunkerLogic.startLogic()

    @onRemovedQuery(CGF.GameObject, BunkerLogicComponent)
    def onBunkerLogicComponentRemoved(self, _, bunkerLogic):
        bunkerLogic.stopLogic()