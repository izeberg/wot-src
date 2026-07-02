import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class EventStateEnabledComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Event State Enabled'
    category = 'Event State'