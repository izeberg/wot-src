import typing
if typing.TYPE_CHECKING:
    from dependency_injection_container import DependencyManager

def registerSkeletons(manager):
    from new_year.skeletons.new_year import ITamagotchiDataProvider, ITamagotchiWebRequester, INewYearMetricsLogger
    from new_year.tamagotchi.data_provider import TamagotchiDataProvider
    from new_year.tamagotchi.requester import TamagotchiWebRequester
    from new_year.uilogging.loggers import NewYearMetricsLogger
    from new_year.interactive_state_machine.context import QueueContext
    from new_year.interactive_state_machine.sm_queue import StateMachineQueue
    from new_year.skeletons.i_sm_queue import IStateMachineQueue
    from new_year.skeletons.i_sm_queue_context import IQueueContext
    manager.addInstance(ITamagotchiWebRequester, TamagotchiWebRequester())
    manager.addInstance(ITamagotchiDataProvider, TamagotchiDataProvider())
    manager.addInstance(INewYearMetricsLogger, NewYearMetricsLogger())
    manager.addInstance(IQueueContext, QueueContext())
    manager.addInstance(IStateMachineQueue, StateMachineQueue())