import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes

@registerComponent
class GrinchSnowstormTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionId = None
        self.exitReactionId = None
        return


@registerComponent
class GrinchSnowstormTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll