from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel
from white_tiger.gui.Scaleform.daapi.view.lobby.hangar.carousel.data_provider import WhiteTigerCarouselDataProvider
from white_tiger.gui.Scaleform.daapi.view.lobby.hangar.carousel.filter import WhiteTigerCarouselFilter

class WhiteTigerTankCarousel(TankCarousel):

    def __init__(self):
        super(WhiteTigerTankCarousel, self).__init__()
        self._carouselDPCls = WhiteTigerCarouselDataProvider
        self._carouselFilterCls = WhiteTigerCarouselFilter

    def hasRoles(self):
        return False

    def hasCustomization(self):
        return False

    def _getFiltersVisible(self):
        return False