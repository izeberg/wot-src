from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from cgf_components.client_worlds_helpers import clientWorldsPredicate, ClientWorld
from halloween.cgf_components.hexapod_component import HWIsHexapod, HWHexapodSystem
from halloween.cgf_components.soul_collector_components import SoulCollectorProgressComponent, SoulCollectorComponent

@registerModule
class HalloweenClientBattleModule(object):
    name = 'Halloween Battle Client Module'
    group = 'Halloween'
    systems = [
     CGF.RegisterSystem(HWHexapodSystem, domain=CGF.Domain.Client, predicate=clientWorldsPredicate(ClientWorld.BATTLE | ClientWorld.EDITOR), perTickUpdate=True, updateAfter=(
      CGF.TransformUpdateSystem,))]
    components = [
     HWIsHexapod,
     SoulCollectorProgressComponent,
     SoulCollectorComponent]