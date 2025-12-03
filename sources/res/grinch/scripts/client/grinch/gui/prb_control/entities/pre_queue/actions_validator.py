from CurrentVehicle import g_currentVehicle
from gui.periodic_battles.prb_control.actions_validator import PrimeTimeValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from grinch.skeletons.battle_controller import IGrinchController
from helpers import dependency

class GrinchPrimeTimeValidator(PrimeTimeValidator):
    __grinchCtrl = dependency.descriptor(IGrinchController)

    def _getController(self):
        return self.__grinchCtrl


class GrinchVehicleValidator(BaseActionsValidator):

    def _validate(self):
        vehicle = g_currentVehicle.item
        if vehicle is None:
            return ValidationResult(False)
        else:
            return super(GrinchVehicleValidator, self)._validate()


class GrinchActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(GrinchActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         GrinchPrimeTimeValidator(entity)])

    def _createVehiclesValidator(self, entity):
        baseValidator = super(GrinchActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [
         GrinchVehicleValidator(entity),
         baseValidator])