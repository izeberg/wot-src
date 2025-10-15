from skeletons.gui.game_control import IGameController

class IHalloweenTwitchConController(IGameController):
    onLimitsUpdated = None
    onShopLimitsUpdated = None
    onCertificateCountUpdated = None
    onTwitchConSettingsUpdated = None

    def isEnabled(self):
        raise NotImplementedError

    def isPromoScreenEnabled(self):
        raise NotImplementedError

    def getFullCrewSound(self):
        raise NotImplementedError

    def commanders(self):
        raise NotImplementedError

    def getCommanderByID(self, commanderID):
        raise NotImplementedError

    def getCertificateTokenName(self):
        raise NotImplementedError

    def exchangeCommander(self, commandersData, callback):
        raise NotImplementedError

    def getCertificateCount(self):
        raise NotImplementedError

    def getExchangedCountByCommanderID(self, commanderID):
        raise NotImplementedError

    def getBlockCardCountByCommanderID(self, commanderID):
        raise NotImplementedError

    def canExchangeCertificateByCommanderID(self, commanderID):
        raise NotImplementedError

    def getRemainLimits(self, commanderID):
        raise NotImplementedError

    def getRemainShopLimits(self, commanderID):
        raise NotImplementedError