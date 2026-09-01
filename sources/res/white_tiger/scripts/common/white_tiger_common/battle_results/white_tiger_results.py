from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  'wtBattleVSPriorityBoss', bool, False, None, 'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  'wtBossVulnerableDamage', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'maxWtPlasmaBonus', int, 0, None, 'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  'wtGeneratorsCaptured', int, 0, None, 'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  'wtDeathCount', int, 0, None, 'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  'wtMiniBossDestroyed', int, 0, None, 'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  'wtKilledByHyperionCount', int, 0, None, 'max', ENTRY_TYPE.VEHICLE_ALL)]