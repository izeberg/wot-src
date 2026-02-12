from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import RibbonsAggregator, _FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY as _DEFAULT_RIBBON_FACTORIES, _SingleVehicleDamageRibbon, _RibbonClassFactory
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import _singleVehRibbonFormatter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID
from lunar_constants import ATTACK_REASON
from lunar_possession.gui.Scaleform.genConsts.LUNAR_BATTLE_EFFICIENCY_TYPES import LUNAR_BATTLE_EFFICIENCY_TYPES
_LUNAR_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = {}
_LUNAR_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY.update(_DEFAULT_RIBBON_FACTORIES)

class LunarPossessionRibbonsAggregator(RibbonsAggregator):
    FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = _LUNAR_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY


def createRibbonsAggregator():
    return LunarPossessionRibbonsAggregator()


def registerRibbonsFactory(eventID):

    def decorator(cls):
        _LUNAR_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY[eventID] = cls()
        return cls

    return decorator


class _AbstractLunarRibbonsFactory(_RibbonClassFactory):
    ATTACK_REASONS = None

    def getRibbonClass(self, event):
        result = self._getRibbonClass(event.getExtra().getAttackReasonID(), event.getExtra().getSecondaryAttackReasonID())
        return result or self._DEFAULT_FACTORY.getRibbonClass(event)

    @classmethod
    def registerAttackReasonRibbon(cls, reason, secondaryReason=None):

        def decorator(ribbonCls):
            key = (ATTACK_REASON.getIndex(reason), ATTACK_REASON.getIndex(secondaryReason)) if secondaryReason else ATTACK_REASON.getIndex(reason)
            cls.ATTACK_REASONS[key] = ribbonCls
            return ribbonCls

        return decorator

    @classmethod
    def _getRibbonClass(cls, reasonID, secondaryReasonID):
        registry = cls.ATTACK_REASONS
        return registry.get((reasonID, secondaryReasonID), None) or registry.get(reasonID, None)


@registerRibbonsFactory(FEEDBACK_EVENT_ID.ENEMY_DAMAGED_HP_PLAYER)
class LunarDamageRibbonsFactory(_AbstractLunarRibbonsFactory):
    ATTACK_REASONS = {}
    _DEFAULT_FACTORY = _DEFAULT_RIBBON_FACTORIES[FEEDBACK_EVENT_ID.ENEMY_DAMAGED_HP_PLAYER]


@LunarDamageRibbonsFactory.registerAttackReasonRibbon(ATTACK_REASON.SPIRIT_CARRIER_DOT)
class _SpiritCarrierDotDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__ = ()

    def getType(self):
        return LUNAR_BATTLE_EFFICIENCY_TYPES.SPIRIT_CARRIER_DOT

    def getFormatter(self):
        return _singleVehRibbonFormatter