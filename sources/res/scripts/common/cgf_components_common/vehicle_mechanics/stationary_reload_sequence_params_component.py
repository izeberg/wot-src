import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class StationaryReloadSequenceParamsComponent(object):
    category = 'Sequence'
    editorTitle = 'Stationary reload sequence params'
    domain = CGF.DomainOption.DomainAll
    sequencePreparingLayer = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sequence preparing layer', value='')
    sequenceFinishingLayer = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sequence finishing layer', value='')