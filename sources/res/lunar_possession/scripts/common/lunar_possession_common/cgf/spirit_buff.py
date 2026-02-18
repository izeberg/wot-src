import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes

class LunarSpiritBuffComponentDescr(object):
    category = 'Lunar'
    domain = CGF.DomainOption.DomainAll
    buffGameObject = ComponentProperty(type=CGFMetaTypes.LINK, value=CGF.GameObject, editorName='')