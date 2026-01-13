from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover

class FrontlineCarouselFilterPopoverMeta(TankCarouselFilterPopover):

    def onPlayListsChange(self, playListId):
        self._printOverrideError('onPlayListsChange')

    def as_updatePlayListsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayLists(dataProvider)