from __future__ import absolute_import
import extension_rules, battle_modifiers_ext

def preInit():
    extension_rules.init()
    battle_modifiers_ext.init()