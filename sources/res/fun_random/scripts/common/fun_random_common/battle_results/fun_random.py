from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
BATTLE_RESULTS = [
 (
  'funEventID', int, UNKNOWN_EVENT_ID, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'fallTanksCheckpointsPassed', int, 0, None, 'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  'fallTanksPosition', int, 0, None, 'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  'fallTanksUsedSkillsN', int, 0, None, 'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  'fallTanksFinishTime', float, 0.0, None, 'any', ENTRY_TYPE.VEHICLE_ALL)]