from items.attributes_helpers import CommonFactorsHelper
AUTOSHOOT_DYNAMIC_ATTRS = [
 'rate/multiplier',
 'shotDispersionPerSecFactor',
 'maxShotDispersionFactor']

class AutoshootFactorsHelper(CommonFactorsHelper):
    ALLOWED_ATTRS = AUTOSHOOT_DYNAMIC_ATTRS
    PREFIX = 'autoShootAttrs/'


attributes_autoshoot_factory = AutoshootFactorsHelper()