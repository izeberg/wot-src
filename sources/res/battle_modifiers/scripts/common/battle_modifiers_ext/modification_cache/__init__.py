from __future__ import absolute_import
from battle_modifiers_ext.modification_cache import constants_modifications, vehicle_modifications

def init():
    vehicle_modifications.init()
    constants_modifications.init()