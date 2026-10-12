from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class RespawnPolicyVehicleLinkComponentDescr(object):
    category = 'Respawns'
    editorTitle = 'RespawnPolicyVehicleLinkComponent'
    domain = CGF.Domain.All
    vehicleId = ComponentProperty(type=CGF.PropertyType.Int, editorName='vehicleId', value=0)