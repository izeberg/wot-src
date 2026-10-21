from constants import PREMIUM_ENTITLEMENTS
from gui.shared.money import Currency
from gui.server_events.bonuses import VehiclesBonus
_REWARDS_ORDER = (
 VehiclesBonus.VEHICLES_BONUS, 'customizations', Currency.CRYSTAL, Currency.GOLD, PREMIUM_ENTITLEMENTS.PLUS,
 PREMIUM_ENTITLEMENTS.BASIC, 'goodies', 'crewBooks', 'freeXP', Currency.CREDITS, 'items',
 'slots', 'berths')

def bonusSortKeyFunc(bonus):
    return _REWARDS_ORDER.index(bonus.getName())