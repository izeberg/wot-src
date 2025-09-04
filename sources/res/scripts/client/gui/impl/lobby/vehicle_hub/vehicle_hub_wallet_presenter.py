from __future__ import absolute_import
from gui.impl.lobby.page.wallet_presenter import WalletPresenter, GoldProvider, CreditsProvider, CrystalProvider, FreeXpProvider

class VehicleHubWalletPresenter(WalletPresenter):

    def __init__(self):
        super(VehicleHubWalletPresenter, self).__init__((
         CrystalProvider(),
         GoldProvider(),
         CreditsProvider(),
         FreeXpProvider()))