import BigWorld
from gui.shared.gui_items.processors import Processor

class PlayerSatisfactionRatingProcessor(Processor):

    def __init__(self, arenaUniqueID, rating):
        super(PlayerSatisfactionRatingProcessor, self).__init__()
        self._arenaUniqueID = arenaUniqueID
        self._rating = rating

    def _request(self, callback):
        BigWorld.player().submitPlayerSatisfactionRating(self._arenaUniqueID, self._rating, lambda code, errStr: self._response(code, callback, errStr=errStr))