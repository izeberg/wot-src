from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.lobby.gsw_cards.key_card_presenter import KeyCardPresenter
from halloween.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestsCardPresenter
from halloween.gui.impl.lobby.gsw_cards.reward_path_presenter import RewardPathCardPresenter
from halloween.gui.impl.lobby.gsw_cards.shop_card_presenter import ShopCardPresenter

class GswPresenter(ViewComponent):

    def _getChildComponents(self):
        halloween = R.aliases.halloween.shared
        return {halloween.Shop(): ShopCardPresenter, 
           halloween.Keys(): KeyCardPresenter, 
           halloween.RewardPath(): RewardPathCardPresenter, 
           halloween.Quests(): lambda : QuestsCardPresenter(isGSW=True)}