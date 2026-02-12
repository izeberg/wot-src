import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class SpiritSpawn(object):
    category = 'Lunar'
    editorTitle = 'Lunar Spirit Spawn'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor