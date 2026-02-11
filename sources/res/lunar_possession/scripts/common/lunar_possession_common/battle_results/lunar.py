from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from fun_random_common.battle_results.fun_random import BATTLE_RESULTS as FEP_BATTLE_RESULTS
LUNAR_BATTLE_RESULTS = [
 (
  'lunarSpiritDeliveries', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'lunarSpiritCarriersDestroyed', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'lunarSpiritCarriersDamaged', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'lunarSpiritScore', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL)]
BATTLE_RESULTS = FEP_BATTLE_RESULTS[:] + LUNAR_BATTLE_RESULTS