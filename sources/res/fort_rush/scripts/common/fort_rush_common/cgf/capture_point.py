from __future__ import absolute_import
import CGF, Triggers
from GenericComponents import Sequence
from cgf_script.registration import ComponentProperty

class FortRushCapturePointComponentDescr(object):
    category = 'CapturePoint'
    domain = CGF.Domain.All
    editorTitle = 'Capture Point Component'
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)
    sequence = ComponentProperty(type=CGF.PropertyType.Link, editorName='SequenceComponent', value=Sequence)
    capturablePointName = ComponentProperty(type=CGF.PropertyType.String, editorName='capturablePointName')