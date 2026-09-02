import Math, CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class AnomalyZoneComponent(object):
    category = 'White Tiger'
    editorTitle = 'Anomaly zone component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


@registerComponent
class AnomalyPathComponent(object):
    category = 'White Tiger'
    editorTitle = 'Anomaly path component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    anomalyPrefabOffset = ComponentProperty(type=CGFMetaTypes.VECTOR3, value=Math.Vector3(0, -20, 0), editorName='Anomaly prefab offset')