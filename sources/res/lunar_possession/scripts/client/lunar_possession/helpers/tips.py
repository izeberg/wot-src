import random
from helpers.tips import TipsCriteria, TipData
from gui.impl.gen import R

class LunarTipsCriteria(TipsCriteria):

    def find(self):
        localsRoot = R.strings.lunar_battle.tips
        iconsRoot = R.images.lunar_possession.gui.maps.icons.battleLoading.tips
        items = localsRoot.items()
        candidates = []
        for tipID, tipRes in items:
            status = tipRes.title()
            body = tipRes.description()
            iconDyn = iconsRoot.dyn(tipID)
            icon = iconDyn() if iconDyn.isValid() else R.invalid()
            candidates.append(TipData(status, body, icon))

        if candidates:
            return random.choice(candidates)
        return TipData(R.invalid(), R.invalid(), R.invalid())

    def _getTipsValidator(self):
        return