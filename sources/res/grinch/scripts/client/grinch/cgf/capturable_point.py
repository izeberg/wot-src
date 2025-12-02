import BigWorld, CGF
from GenericComponents import TransformComponent
from Math import Vector3, Matrix
from constants import IS_EDITOR
if IS_EDITOR:

    class GrinchCapturablePointComponent(object):
        pass


else:
    from GrinchCapturablePointComponent import GrinchCapturablePointComponent
Y_MARKER_OFFSET = 40

def getCapturablePointTransform(name):
    spaceID = BigWorld.player().spaceID
    query = CGF.Query(spaceID, (CGF.GameObject, GrinchCapturablePointComponent, TransformComponent))
    for _, baseComponent, transform in query:
        if name == baseComponent.capturablePointName:
            newMatrix = Matrix(transform.worldTransform)
            newMatrix.translation = transform.worldPosition + Vector3(0, Y_MARKER_OFFSET, 0)
            return newMatrix

    return Matrix()