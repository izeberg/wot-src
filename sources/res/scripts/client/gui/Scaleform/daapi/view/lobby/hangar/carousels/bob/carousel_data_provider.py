from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider
from gui.shared.utils.requesters import REQ_CRITERIA

class BobCarouselDataProvider(HangarCarouselDataProvider):

    def __init__(self, carouselFilter, itemsCache):
        super(BobCarouselDataProvider, self).__init__(carouselFilter, itemsCache)
        self._baseCriteria = REQ_CRITERIA.INVENTORY