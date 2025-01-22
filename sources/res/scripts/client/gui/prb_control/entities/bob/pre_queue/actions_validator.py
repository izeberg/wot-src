from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus
from helpers import dependency
from skeletons.gui.game_control import IBobController

class BobValidator(BaseActionsValidator):
    bobCtrl = dependency.descriptor(IBobController)

    def _validate(self):
        status, _, _ = self.bobCtrl.getPrimeTimeStatus()
        if status != PrimeTimeStatus.AVAILABLE:
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE)
        return super(BobValidator, self)._validate()


class BobVehicleValidator(BaseActionsValidator):
    bobCtrl = dependency.descriptor(IBobController)

    def _validate(self):
        levels = self.bobCtrl.getConfig().levels
        forbiddenClassTags = self.bobCtrl.getConfig().forbiddenClassTags
        forbiddenVehTypes = self.bobCtrl.getConfig().forbiddenVehTypes
        if not g_currentVehicle.isPresent():
            return ValidationResult(False, PREBATTLE_RESTRICTION.VEHICLE_NOT_PRESENT)
        vehicle = g_currentVehicle.item
        if vehicle.level not in levels:
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_LEVEL, {'levels': levels})
        if vehicle.type in forbiddenClassTags:
            return ValidationResult(False, PREBATTLE_RESTRICTION.LIMIT_VEHICLES, {})
        if vehicle.intCD in forbiddenVehTypes:
            return ValidationResult(False, PREBATTLE_RESTRICTION.LIMIT_VEHICLES, {})
        return super(BobVehicleValidator, self)._validate()


class BobActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(BobActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         BobValidator(entity)])

    def _createVehiclesValidator(self, entity):
        baseValidator = super(BobActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [
         BobVehicleValidator(entity),
         baseValidator])