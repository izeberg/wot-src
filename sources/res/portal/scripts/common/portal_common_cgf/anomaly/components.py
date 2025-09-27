import CGF, Triggers
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class AnomalySystemComponent(object):
    category = 'Portal'
    editorTitle = 'Anomaly System'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor


@registerComponent
class AnomalyTriggerZoneComponent(object):
    category = 'Portal'
    editorTitle = 'Anomaly trigger zone component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Area trigger link', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return