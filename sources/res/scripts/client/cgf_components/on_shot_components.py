import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class EffectOnShotComponent(object):
    category = 'Shooting'
    editorTitle = 'Effect On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect Prefab', annotations={'path': '*.prefab'})


@registerComponent
class SoundOnShotComponent(object):
    category = 'Shooting'
    editorTitle = 'Sound On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sound Prefab', annotations={'path': '*.prefab'})