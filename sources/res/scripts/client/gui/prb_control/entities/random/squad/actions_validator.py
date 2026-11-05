from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_REGULAR
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION

class BalancedSquadVehiclesValidator(BaseActionsValidator):

    def _validate(self):
        levelsRange = self._entity.getRosterSettings().getLevelsRange()
        pInfo = self._entity.getPlayerInfo()
        if not pInfo.isReady and g_currentVehicle.isPresent() and g_currentVehicle.item.level not in levelsRange:
            return ValidationResult(False, UNIT_RESTRICTION.VEHICLE_INVALID_LEVEL)
        return super(BalancedSquadVehiclesValidator, self)._validate()


class BalancedSquadSlotsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        pInfo = self._entity.getPlayerInfo()
        if stats.occupiedSlotsCount > 1 and not pInfo.isReady:
            return ValidationResult(False, UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED)
        else:
            return


class SquadRestrictionsVehiclesValidator(BaseActionsValidator):

    def _validate(self):
        pInfo = self._entity.getPlayerInfo()
        result = super(SquadRestrictionsVehiclesValidator, self)._validate()
        if pInfo.isReady or not g_currentVehicle.isPresent():
            return result
        hasSlot, tagsWithoutSlot = self._entity.hasSlotForVehicle(g_currentVehicle.item)
        if not hasSlot:
            result = ValidationResult(False, UNIT_RESTRICTION.VEHICLES_GROUP_IS_FULL, ctx={'tags': tagsWithoutSlot})
        return result


class RandomSquadVehiclesValidator(SquadVehiclesValidator):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_REGULAR


class RandomSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        return RandomSquadVehiclesValidator(entity)


class BalancedSquadActionsValidator(RandomSquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        baseValidator = super(BalancedSquadActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         BalancedSquadVehiclesValidator(entity),
         baseValidator])

    def _createSlotsValidator(self, entity):
        baseValidator = super(BalancedSquadActionsValidator, self)._createSlotsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         BalancedSquadSlotsValidator(entity)])


class VehTypeForbiddenSquadActionsValidator(RandomSquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        baseValidator = super(VehTypeForbiddenSquadActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         SquadRestrictionsVehiclesValidator(entity),
         baseValidator])


class VehTypeForbiddenBalancedSquadActionsValidator(BalancedSquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        baseValidator = super(VehTypeForbiddenBalancedSquadActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         SquadRestrictionsVehiclesValidator(entity)])