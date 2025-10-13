from account_helpers.AccountSettings import MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, MAPBOX_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter

class MapboxCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(MapboxCarouselFilter, self).__init__()
        self._serverSections = (MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         MAPBOX_CAROUSEL_FILTER_3)
        self._clientSections = (MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)