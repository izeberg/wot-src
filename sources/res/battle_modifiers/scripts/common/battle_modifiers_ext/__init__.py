from __future__ import absolute_import
from battle_modifiers_ext import battle_params, modification_cache, remappings_cache

def init():
    battle_params.init()
    remappings_cache.init()
    modification_cache.init()