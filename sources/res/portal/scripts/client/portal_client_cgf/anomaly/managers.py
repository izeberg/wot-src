import CGF
from portal_common_cgf.portal_helpers import registerPortalManager

@registerPortalManager(CGF.DomainOption.DomainClient)
class AnomalyManager(CGF.ComponentManager):
    pass