from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSShopController(IGameController):
    onShopSettingsUpdated = None
    onBundlesUpdated = None

    def isEnabled(self):
        raise NotImplementedError

    def keyBundles(self):
        raise NotImplementedError

    def getBundleByID(self, bundleID):
        raise NotImplementedError

    def getProgressPointsInBundle(self, bundleID):
        raise NotImplementedError

    def purchaseBundle(self, bundleID, int):
        raise NotImplementedError

    def getPurchaseCount(self, bundleID):
        raise NotImplementedError

    def checkIsEnoughBundles(self):
        raise NotImplementedError