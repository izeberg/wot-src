import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class ActiveGuidedMissileComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = 'Portal'
    editorTitle = 'Active Guided Missile'