import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class WTMissileFlyEffectComponent(object):
    category = 'White Tiger'
    editorTitle = 'Missile Fly Effect'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPrefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect prefab path', value='')