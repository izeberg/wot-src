from gui.shared.events import HasCtxEvent

class DynamicFactorsEvent(HasCtxEvent):
    UPDATE_LEVEL = 'dynamicFactors/updateLevel'


class WTCrosshairVisibilityEvents(HasCtxEvent):
    SHOW_CROSSHAIR = 'WTCrosshairVisibility/showCrossHair'