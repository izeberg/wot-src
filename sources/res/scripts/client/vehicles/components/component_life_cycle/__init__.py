from vehicles.components.component_life_cycle.custom_integrations import ComponentLifeCycleLogger
from vehicles.components.component_life_cycle.life_cycle_events import ComponentLifeCycleEvents
from vehicles.components.component_life_cycle.life_cycle_interfaces import ILifeCycleComponent, IComponentLifeCycleEvents, IComponentLifeCycleListener, IComponentLifeCycleListenerLogic
__all__ = ('ILifeCycleComponent', 'IComponentLifeCycleEvents', 'IComponentLifeCycleListener',
           'IComponentLifeCycleListenerLogic', 'ComponentLifeCycleEvents', 'ComponentLifeCycleLogger',
           'createComponentLifeCycleEvents')

def createComponentLifeCycleEvents(component):
    componentLifeCycleEvents = ComponentLifeCycleEvents(component)
    ComponentLifeCycleLogger().subscribeTo(componentLifeCycleEvents)
    return componentLifeCycleEvents