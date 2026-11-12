from constants_utils import ConstInjector
from gui.Scaleform.daapi.settings import views

class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type = str
    NY_SELECT_VEHICLE_FOR_DISCOUNT_POPOVER = 'NYSelectVehicleForDiscountPopover'
    NY_BROWSER_VIEW = 'NyBrowserView'
    NY_VEHICLE_PREVIEW = 'NyVehiclePreview'