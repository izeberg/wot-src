from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from constants import PlayerSatisfactionRating as Rating
BATTLE_RESULTS = [
 (
  'avatarPlayerSatisfactionRating', tuple, (int(Rating.NONE), 0.0), None, 'skip', ENTRY_TYPE.ACCOUNT_SELF)]