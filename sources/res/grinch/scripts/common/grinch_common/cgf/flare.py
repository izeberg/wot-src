import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes

@registerComponent
class GrinchFlareZoneTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionId = None
        return