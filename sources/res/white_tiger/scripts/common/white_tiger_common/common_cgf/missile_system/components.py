import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty
from cgf_script.component_meta_class import registerComponent

@registerComponent
class WTSpawnerComponent(object):
    editorTitle = 'WT Missile Spawner'
    category = 'White Tiger'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    missileNumber = ComponentProperty(type=CGFMetaTypes.INT, editorName='Missile Number ', value=3)
    spawnDelay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Spawn Delay', value=1.0)

    def __init__(self):
        self.alive = True
        self.missilePrefabPath = None
        self.missiles = []
        self.deactivateCallback = None
        return