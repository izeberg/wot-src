from __future__ import absolute_import
from HWBuffEffectsListPlayerComponent import HWBuffEffectsListPlayerComponent

class HWBuffFlashBangEffectComponent(HWBuffEffectsListPlayerComponent):

    def set_isActive(self, prev):
        self._updateEffectsStatus()

    @property
    def _isActive(self):
        if not self.isActive:
            return False
        return super(HWBuffFlashBangEffectComponent, self)._isActive