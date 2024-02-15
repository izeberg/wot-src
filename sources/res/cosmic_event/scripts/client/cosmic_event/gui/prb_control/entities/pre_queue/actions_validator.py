from typing import TYPE_CHECKING
from cosmic_event.skeletons.battle_controller import ICosmicEventBattleController
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.settings import PREBATTLE_RESTRICTION
from helpers import dependency
if TYPE_CHECKING:
    from gui.prb_control.entities.base.entity import BasePrbEntity

class CosmicEventBattleVehicleValidator(BaseActionsValidator):
    __cosmicEventController = dependency.descriptor(ICosmicEventBattleController)

    def _validate(self):
        vehicle = self.__cosmicEventController.getEventVehicle()
        if vehicle is None or not vehicle.isInInventory:
            return ValidationResult(False, PREBATTLE_RESTRICTION.VEHICLE_NOT_SUPPORTED)
        else:
            if vehicle.isInBattle or vehicle.isDisabled:
                return ValidationResult(False, PREBATTLE_RESTRICTION.VEHICLE_IN_BATTLE)
            return ValidationResult(True, '')


class CosmicEventValidator(BaseActionsValidator):
    __cosmicEventController = dependency.descriptor(ICosmicEventBattleController)

    def _validate(self):
        if not self.__cosmicEventController.isEnabled or self.__cosmicEventController.isFrozen() or not self.__cosmicEventController.isBattleAvailable():
            return ValidationResult(False, PREBATTLE_RESTRICTION.UNDEFINED)
        return super(CosmicEventValidator, self)._validate()


class CosmicEventBattleActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(CosmicEventBattleActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         CosmicEventValidator(entity)])

    def _createVehiclesValidator(self, entity):
        return CosmicEventBattleVehicleValidator(entity)