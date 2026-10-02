import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class PortalOutlineGoComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Portal Outline Game object'
    category = 'Portal'