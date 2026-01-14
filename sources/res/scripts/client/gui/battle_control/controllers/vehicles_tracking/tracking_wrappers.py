from __future__ import absolute_import
import operator, typing
from functools import wraps
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehiclesTrackingWatcher

def hasVehiclesTrackingCtrl(ctrlName='vehiclesTrackingCtrl', defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(vehiclesTrackingWatcher, *args, **kwargs):
            trackingCtrl = vehiclesTrackingWatcher.getVehiclesTrackingCtrl()
            if trackingCtrl is not None:
                kwargs[ctrlName] = trackingCtrl
                return method(vehiclesTrackingWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(vehiclesTrackingWatcher)
                return defReturn

        return wrapper

    return decorator