import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from gui.pet_system.constants import StorageStateKey

@registerComponent
class StorageStateComponent(object):
    group = 'Pet system'
    editorTitle = 'Pet Storage State Component'
    domain = CGF.Domain.Client
    names = {name:name for name in StorageStateKey.ALL}
    storageObjectKey = ComponentProperty(type=CGF.PropertyType.String, editorName='storage object key', value='active', annotations={'comboBox': names})