import BigWorld, Event

class PortalBattleFeedbackComponent(BigWorld.DynamicScriptComponent):
    onVehicleHeal = Event.Event()

    @classmethod
    def unpackPortalActionApplied(cls, packedEffect):
        return (packedEffect >> 24 & 65535, packedEffect >> 12 & 4095, packedEffect & 255)