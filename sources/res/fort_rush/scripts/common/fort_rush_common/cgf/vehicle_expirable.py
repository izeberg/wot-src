from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class VehicleExpirableComponentDescriptor(object):
    category = 'Expirable'
    editorTitle = 'Vehicle Expirable Component'
    domain = CGF.Domain.All
    duration = ComponentProperty(CGF.PropertyType.Float, editorName='Duration', value=0.0)