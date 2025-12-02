import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class GrinchTeamComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    team = ComponentProperty(type=CGFMetaTypes.INT, editorName='team', value=0)


@registerComponent
class GrinchVulnerabilityConfigComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    team = ComponentProperty(type=CGFMetaTypes.INT, editorName='team', value=1)
    ownerId = ComponentProperty(type=CGFMetaTypes.INT, editorName='ownerId', value=1)
    debuffDuration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='debuffDuration', value=10.0)
    receivedDamageFactor = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='receivedDamageFactor', value=0.5)
    blockers = ComponentProperty(type=CGFMetaTypes.STRING_LIST, editorName='blockers', value=-1)
    activationDelay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='activationDelay', value=0.0)
    startingDamage = ComponentProperty(type=CGFMetaTypes.INT, editorName='startingDamage', value=0)


class OnLinkedDisappearPrefabSpawner(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    prefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName='prefab', value='', annotations={'path': '*.prefab'})
    useTransform = ComponentProperty(type=CGFMetaTypes.BOOL, editorName='Use Transform', value=True)
    linkedComponent = None