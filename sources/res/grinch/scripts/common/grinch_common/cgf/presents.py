import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes

@registerComponent
class PresentSunflowerHolder(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    count = ComponentProperty(type=CGFMetaTypes.INT, editorName='count', value=50)
    radius = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='radius', value=40)

    def __init__(self):
        self.__positions = []

    def release(self, pos):
        self.__positions.append(pos)

    def acquire(self, root):
        positions = self.__positions
        if not positions:
            return None
        else:
            pos = min(positions, key=root.flatDistSqrTo)
            positions.remove(pos)
            return pos


@registerComponent
class PresentSunflowerSeed(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class PresentPickupAreaTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionID = None
        return


@registerComponent
class PresentDeliveryAreaTriggerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return


class DeliverableComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    amount = None

    def __init__(self):
        self.beingPickedUp = False


@registerComponent
class PresentDeliverableComponent(DeliverableComponent):
    amount = 1


@registerComponent
class BigPresentDeliverableComponent(DeliverableComponent):
    amount = 7


@registerComponent
class HomebaseComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    team = ComponentProperty(type=CGFMetaTypes.INT, editorName='Team', value=1)


@registerComponent
class IsAtHomebaseComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    base = ComponentProperty(type=CGFMetaTypes.LINK, value=CGF.GameObject)

    def __init__(self, base):
        self.base = base


@registerComponent
class DeliveredPresentComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    base = ComponentProperty(type=CGFMetaTypes.LINK, value=CGF.GameObject)
    amount = 1

    def __init__(self, base, amount):
        self.base = base
        self.amount = amount


@registerComponent
class StolenPresentsComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll
    amount = ComponentProperty(type=CGFMetaTypes.INT, value=0)
    amountBig = ComponentProperty(type=CGFMetaTypes.INT, value=0)

    def increment(self):
        self.amount += 1

    def incrementBig(self):
        self.amountBig += 1


@registerComponent
class GrinchPresentCoreSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentEarlygameSpawnTargetA(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentEarlygameSpawnTargetB(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentEarlygameSpawnTargetC(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentEarlygameSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentMidgameSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentLategameSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentIslandSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchCaptureRewardSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentCenterSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchPresentOutskirtSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchBigPresentSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchBotSpawnTarget(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class GrinchNavmeshPositionTrackerComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainServer
    lastNavmeshValidPosition = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName='Last Navmesh Valid Position', value=(0,
                                                                                                                             0,
                                                                                                                             0))
    girth = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Girth value for the navmesh', value='')


@registerComponent
class GrinchNavmeshPositionHolderComponent(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainServer
    lastNavmeshValidPosition = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName='The last Vehicle valid position on Navmesh', value=(0,
                                                                                                                                            0,
                                                                                                                                            0))
    girth = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Girth value for the Navmesh', value='')
    holderVehicleID = ComponentProperty(type=CGFMetaTypes.INT, editorName='The ID of a vehicle that has been carrier of the present', value=0)
    lastActualPosition = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName='The last actual position of the vehicle before destruction', value=(0,
                                                                                                                                                      0,
                                                                                                                                                      0))


@registerComponent
class GrinchPresentInAbyss(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainServer