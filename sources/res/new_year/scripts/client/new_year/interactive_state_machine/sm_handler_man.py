from helpers import dependency
from new_year.helpers.server_settings import getNewYearMachineConfig
from new_year.interactive_state_machine.config import getSMSetting, setSMSetting
from new_year.interactive_state_machine.constants import COOL_REWARD_CYCLE, SIMPLE_REWARD_CYCLE, PersonaTypes, MANDARINS_THRESHOLD, GIFT_TOKEN_THRESHOLD
from new_year.interactive_state_machine.sm_handler import StateMachineHandler
from new_year.interactive_state_machine.sm_utils import isCoolRewards
from new_year.ny_constants import COOL_REWARD_COUNT, SIMPLE_REWARD_COUNT, NY_IS_MACHINE_CELEB_VOICEOVERS_ENABLED
from new_year.skeletons.i_sm_queue_context import IQueueContext
from new_year.skeletons.new_year import INewYearCurrencyController, INewYearSurpriseMachine
from new_year_account_settings import getNYSetting

class ManStateMachineHandler(StateMachineHandler):
    __slots__ = ('__machineConfig', )
    _TYPE = PersonaTypes.CELEB_MAN
    _CONDITION_S = 'condition'
    _REWARD_COOL_S = 'reward_cool'
    _REWARD_SIMPLE_S = 'reward_simple'
    _INTERRUPT_GROUP = StateMachineHandler._INTERRUPT_GROUP + (_CONDITION_S,)
    __context = dependency.descriptor(IQueueContext)
    __nyCurrencyController = dependency.descriptor(INewYearCurrencyController)
    __nyMachineController = dependency.descriptor(INewYearSurpriseMachine)

    def __init__(self, animator):
        super(ManStateMachineHandler, self).__init__(animator)
        self.__machineConfig = getNewYearMachineConfig()

    @property
    def isEnabled(self):
        return getNYSetting(NY_IS_MACHINE_CELEB_VOICEOVERS_ENABLED)

    def _handleNewWeek(self):
        return False

    def _handleNewDay(self):
        return False

    def handleRewards(self, rewards):
        if not self.isEnabled:
            return
        isCool = isCoolRewards(rewards)
        key = COOL_REWARD_COUNT if isCool else SIMPLE_REWARD_COUNT
        trigger = self._REWARD_COOL_S if isCool else self._REWARD_SIMPLE_S
        cycle = COOL_REWARD_CYCLE if isCool else SIMPLE_REWARD_CYCLE
        count = getSMSetting(key, self._TYPE) + 1
        setSMSetting(key, self._TYPE, count)
        if self.state in self._INTERRUPT_GROUP and count % cycle == 0:
            self.setTrigger(trigger)

    def handleLoaded(self):
        if not self.__context.wasInBattle or self.__context.isLocked or self.__context.firstBattleLatch or not self.isHangarViewLoaded:
            return False
        nyCtrl = self.__nyCurrencyController
        isMandarinsEnough = nyCtrl.getMandarinTokenCount >= self.__machineConfig.getCoinPrice() * MANDARINS_THRESHOLD
        isCoinEnough = self.__nyCurrencyController.getGiftMachineTokenCount >= GIFT_TOKEN_THRESHOLD
        if isMandarinsEnough and self.__nyMachineController.canBuyCoin or isCoinEnough:
            self.setTrigger(self._CONDITION_S)
            self.__context.firstBattleLatch = True
            return True
        return False