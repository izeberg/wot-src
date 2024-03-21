from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  'comp7PrestigePoints', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'roleSkillUsed', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'healthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'alliedHealthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'comp7Rating', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7Rank', tuple, (0, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7RatingDelta', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7TeamStats', dict, {}, None, 'skip', ENTRY_TYPE.SERVER),
 (
  'fareTeamPrestigePointsPosition', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7QualActive', None, None, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7QualBattleIndex', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7QualRating', int, 0, None, 'skip', ENTRY_TYPE.SERVER),
 (
  'comp7QualRank', tuple, (0, 0), None, 'skip', ENTRY_TYPE.SERVER),
 (
  'isSuperSquad', bool, False, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL)]