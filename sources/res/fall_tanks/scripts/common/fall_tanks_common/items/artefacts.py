from __future__ import absolute_import
import importlib
artefacts = importlib.import_module('items.artefacts')

class FallTanksAbilityDashEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = ('duration', 'cooldownSeconds')

    def _readConfig(self, xmlCtx, section):
        super(FallTanksAbilityDashEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat('duration')
        self.cooldownSeconds = section.readFloat('cooldownSeconds')
        self._exportSlotsToVSE()


class FallTanksAbilityShieldEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = ('duration', 'cooldownSeconds')

    def _readConfig(self, xmlCtx, section):
        super(FallTanksAbilityShieldEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat('duration')
        self.cooldownSeconds = section.readFloat('cooldownSeconds')
        self._exportSlotsToVSE()