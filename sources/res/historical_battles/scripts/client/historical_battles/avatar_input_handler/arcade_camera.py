from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera

class ArcadeCameraAOE(ArcadeCamera):

    @staticmethod
    def _getConfigsKey():
        return ArcadeCameraAOE.__name__