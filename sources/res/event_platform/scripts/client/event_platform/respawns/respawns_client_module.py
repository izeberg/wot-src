from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from event_platform.respawns.respawns import RespawnPolicySystem
from DisconnectRespawnValidatorComponent import DisconnectRespawnValidatorComponent
from IndividualRespawnTimerComponent import IndividualRespawnTimerComponent
from RespawnPolicyVehicleLinkComponent import RespawnPolicyVehicleLinkComponent

@registerModule
class ClientRespawnsModule(object):
    name = 'ClientRespawnsModule'
    group = 'Battle'
    systems = [
     CGF.RegisterSystem(RespawnPolicySystem, domain=CGF.Domain.Client)]
    components = [
     RespawnPolicyVehicleLinkComponent,
     DisconnectRespawnValidatorComponent,
     IndividualRespawnTimerComponent]