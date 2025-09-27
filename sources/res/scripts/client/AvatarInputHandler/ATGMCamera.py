from VideoCamera import VideoCamera
import Math, math_utils

class ATGMCamera(VideoCamera):
    camera = property(lambda self: self._cam)

    def __init__(self, configDataSec):
        super(ATGMCamera, self).__init__(configDataSec)
        self.position = None
        return

    def enable(self, **args):
        super(ATGMCamera, self).enable(**args)
        worldMat = Math.Matrix(self._cam.invViewMatrix)
        yawMatrix = math_utils.createRTMatrix((worldMat.yaw, worldMat.pitch, 0), worldMat.translation)
        yawMatrix.invert()
        self.setViewMatrix(yawMatrix)

    def _update(self):
        super(ATGMCamera, self)._update()
        self.__position = self.position
        self._cam.invViewProvider.a.translation = self.position
        return 0.0

    def handleKeyEvent(self, key, isDown):
        return False