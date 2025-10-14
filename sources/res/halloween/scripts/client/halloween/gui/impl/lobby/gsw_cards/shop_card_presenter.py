from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.shop_card_view_model import ShopCardViewModel
from halloween.gui.shared.event_dispatcher import showHalloweenShopAll

class ShopCardPresenter(ViewComponent[ShopCardViewModel]):

    def __init__(self):
        super(ShopCardPresenter, self).__init__(model=ShopCardViewModel)

    def _getEvents(self):
        return (
         (
          self.getViewModel().onClick, self.__onClick),)

    def __onClick(self):
        showHalloweenShopAll()