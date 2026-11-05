from __future__ import absolute_import
import CGF
from cgf_script.registration import registerComponent, ComponentProperty

@registerComponent
class ProBoostEffectsConfigComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Pro Boost Effects Config'
    category = 'Hangar'
    vseVisible = False
    activationPrefab = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='Activation prefab', annotations={'path': '*.prefab'})
    deactivationPrefab = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='Deactivation prefab', annotations={'path': '*.prefab'})