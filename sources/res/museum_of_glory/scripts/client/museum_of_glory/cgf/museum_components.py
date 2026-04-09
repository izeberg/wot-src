import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class MuseumTankBack(object):
    domain = CGF.DomainOption.DomainClient


@registerComponent
class TankObjectSoundComponent(object):
    domain = CGF.DomainOption.DomainClient


@registerComponent
class MuseumTankLightFade(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    isFadeIn = ComponentProperty(type=CGFMetaTypes.BOOL, editorName='is FadeIn', value=True)