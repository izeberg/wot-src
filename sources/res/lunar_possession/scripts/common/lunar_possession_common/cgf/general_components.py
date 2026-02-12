import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class TeamIDComponent(object):
    domain = CGF.DomainOption.DomainAll
    editorTitle = 'Lunar team ID component'
    category = 'Lunar'
    teamID = ComponentProperty(type=CGFMetaTypes.INT, editorName='teamID', value=1)


@registerComponent
class SpiritComponent(object):
    domain = CGF.DomainOption.DomainAll
    editorTitle = 'Lunar spirit component'
    category = 'Lunar'