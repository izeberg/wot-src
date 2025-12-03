import CGF, Triggers
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class GrinchSonarComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll

    def __init__(self):
        self.vehiclesHit = set()


@registerComponent
class GrinchChainedActivationControllerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    duration = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0, editorName='duration')

    def __init__(self):
        self.delayedTimers = set()


@registerComponent
class GrinchChainedActivationComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    order = ComponentProperty(type=CGFMetaTypes.INT, value=0, editorName='order')


@registerComponent
class GrinchSonarTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionId = None
        return