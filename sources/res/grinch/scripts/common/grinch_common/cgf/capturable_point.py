import CGF, Triggers
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class GrinchPointPenalty(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    points = ComponentProperty(type=CGFMetaTypes.INT, editorName='points')


@registerComponent
class GrinchDefenceTurretEmplacement(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchBaseTurretSpawnTarget(object):
    category = 'Grinch'
    editor = 'Base defence turret spawn'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchBaseTurretComponent(object):
    category = 'Grinch'
    editor = 'Base defence turret tag'
    domain = CGF.DomainOption.DomainAll
    pointName = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Base name')


@registerComponent
class GrinchAnnouncementCooldownComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


class GrinchCapturablePointComponentDescr(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)
    capturablePointName = ComponentProperty(type=CGFMetaTypes.STRING, editorName='capturablePointName')
    maxPoints = ComponentProperty(type=CGFMetaTypes.INT, editorName='Max points for capture')
    pointsForInvader = ComponentProperty(type=CGFMetaTypes.INT, editorName='Points for one invader')
    rollbackPoints = ComponentProperty(type=CGFMetaTypes.INT, editorName='Amount of rollback points in 1 second')