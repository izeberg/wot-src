from enum import IntEnum
import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes

class StagedJetBoostersControllerDescriptor(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Staged Jet Boosters Controller'
    domain = CGF.DomainOption.DomainAll
    left = ComponentProperty(CGFMetaTypes.LINK, editorName='Left Rocket', value=CGF.GameObject)
    right = ComponentProperty(CGFMetaTypes.LINK, editorName='Right Rocket', value=CGF.GameObject)
    stateController = ComponentProperty(CGFMetaTypes.LINK, editorName='State Controller', value=CGF.GameObject)