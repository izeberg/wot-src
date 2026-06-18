from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from material_kinds import EFFECT_MATERIALS

@registerComponent
class MaterialComponent(object):
    category = 'Material'
    editorTitle = 'Material'
    domain = CGF.Domain.All
    materials = {m:m for m in EFFECT_MATERIALS}
    kind = ComponentProperty(type=CGF.PropertyType.String, editorName='Kind', value='', annotations={'comboBox': materials})