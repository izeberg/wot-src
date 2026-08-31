from __future__ import absolute_import
from vehicles.mechanics.mechanic_inputs.mechanic_base_input import BaseMechanicInput
from vehicles.mechanics.mechanic_inputs.mechanic_input_profile import MechanicInputProfile

class MechanicSingleInput(BaseMechanicInput):

    def __init__(self, component, profileName, actionName, inputCallback):
        super(MechanicSingleInput, self).__init__()
        self._register(MechanicInputProfile(component.entity, profileName, actionName, inputCallback))