from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BobBattleLoadingMeta(BaseDAAPIComponent):

    def as_setBloggerIdsS(self, bloggerLeftId, bloggerRightId):
        if self._isDAAPIInited():
            return self.flashObject.as_setBloggerIds(bloggerLeftId, bloggerRightId)