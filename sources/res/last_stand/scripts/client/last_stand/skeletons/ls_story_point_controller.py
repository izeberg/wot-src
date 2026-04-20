from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSStoryPointController(IGameController):
    FIRST_STORY_POINT_INDEX = None
    onStoryPointStatusUpdated = None

    @property
    def selectedStoryPointID(self):
        raise NotImplementedError

    @selectedStoryPointID.setter
    def selectedStoryPointID(self, artefactID):
        raise NotImplementedError

    @property
    def storyPoints(self):
        raise NotImplementedError

    def getIndex(self, storyPointID):
        raise NotImplementedError

    def getStoryPointIDByIndex(self, index):
        raise NotImplementedError

    def getStoryPointsCount(self):
        raise NotImplementedError

    def isStoryPointReceived(self, storyPointID):
        raise NotImplementedError