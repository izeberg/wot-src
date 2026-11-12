from new_year.interactive_state_machine.constants import PersonaTypes
from new_year.interactive_state_machine.sm_handler import StateMachineHandler
from new_year.ny_constants import NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED
from new_year_account_settings import getNYSetting

class WomanStateMachineHandler(StateMachineHandler):
    __slots__ = ()
    _TYPE = PersonaTypes.CELEB_WOMAN

    @property
    def isEnabled(self):
        return getNYSetting(NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED)

    def _handleNewDay(self):
        return False