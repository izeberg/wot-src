import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes

@registerComponent
class BossComponent(object):
    category = 'Portal'
    editorTitle = 'Boss'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class SyncActivationComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = 'Portal'
    editorTitle = 'Sync activation'


@registerComponent
class FrontierObserverComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = 'Portal'
    editorTitle = 'Frontier Observer'
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Trigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        return