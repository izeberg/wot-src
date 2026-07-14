from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from last_stand.cgf_components.show_event_component import LSShowEventSystem, LSShowEventComponent

@registerModule
class LastStandModeModule(object):
    name = 'Last Stand Mode Module'
    desc = 'Last Stand Core'
    group = 'Store Mode'
    systems = [
     CGF.RegisterSystem(LSShowEventSystem, domain=CGF.Domain.Client)]
    components = [
     LSShowEventComponent]