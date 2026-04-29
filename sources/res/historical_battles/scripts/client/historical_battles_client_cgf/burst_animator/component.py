import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class BurstAnimatorComponent(object):
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient