from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
from helpers import dependency
from portal.skeletons.portal_event_controller import IPortalEventController

class _PortalVehiclesValidator(SquadVehiclesValidator):

    def _isValidMode(self, vehicle):
        return VEHICLE_TAGS.PORTAL in vehicle.tags


class _PortalSquadSlotsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        roster = self._entity.getRoster()
        pInfo = self._entity.getPlayerInfo()
        hasEmptySlots = roster.MAX_SLOTS > stats.readyCount + roster.MAX_EMPTY_SLOTS
        if hasEmptySlots or not pInfo.isReady:
            return ValidationResult(False, UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED)


class _PortalValidator(CommanderValidator):

    def _validate(self):
        portalController = dependency.instance(IPortalEventController)
        if not portalController.isAvailable():
            return ValidationResult(False, UNIT_RESTRICTION.CURFEW)
        return super(_PortalValidator, self)._validate()


class PortalSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        validators = [
         _PortalVehiclesValidator(entity),
         _PortalValidator(entity)]
        return ActionsValidatorComposite(entity, validators=validators)

    def _createSlotsValidator(self, entity):
        baseValidator = super(PortalSquadActionsValidator, self)._createSlotsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         _PortalSquadSlotsValidator(entity)])