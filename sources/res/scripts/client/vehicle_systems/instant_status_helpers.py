import CGF, InstantStatuses

def invokeInstantStatusForVehicle(vehicle, instantStatusType):
    gameObject = vehicle.appearance.gameObject
    instantStatus = gameObject.findWrite(instantStatusType)
    if not instantStatus:
        queue = CGF.CommandQueue(gameObject.spaceID)
        queue.createComponent(gameObject, instantStatusType)
    else:
        instantStatus.addNextDone()


def invokeShotsDoneStatus(vehicle):
    invokeInstantStatusForVehicle(vehicle, InstantStatuses.ShotsDoneComponent)