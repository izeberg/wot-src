import CGF
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty

@registerComponent
class WTDomeClientComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = 'White Tiger'

    def __init__(self):
        self.enterReactionID = 0
        self.exitReactionID = 0


@registerComponent
class WTDomeClientInDomeHoundEffectComponent(object):
    category = 'White Tiger'
    editorTitle = 'In Dome Hound Effect'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPrefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect prefab path', value='')