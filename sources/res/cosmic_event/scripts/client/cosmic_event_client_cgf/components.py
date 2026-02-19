import CGF
from cgf_script.managers_registrator import registerComponent

@registerComponent
class UserGunShotEffectComponent(object):
    domain = CGF.DomainOption.DomainClient