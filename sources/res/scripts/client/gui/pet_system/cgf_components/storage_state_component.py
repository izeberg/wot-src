import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from gui.pet_system.constants import StorageStateKey

@registerComponent
class StorageStateComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'Pet Storage State Component'
    category = 'Pet system'
    names = {name:name for name in StorageStateKey.ALL}
    storageObjectKey = ComponentProperty(type=CGFMetaTypes.STRING, editorName='storage object key', value='active', annotations={'comboBox': names})