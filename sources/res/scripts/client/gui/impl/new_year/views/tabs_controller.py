from account_helpers.AccountSettings import AccountSettings, NY_DOG_PAGE_VISITED, NY_NARKET_PLACE_PAGE_VISITED, NY_CAT_PAGE_VISITED, NY_CELEBRITY_DAY_QUESTS_VISITED_MASK, NY_CELEBRITY_ADV_QUESTS_VISITED_MASK, NY_NO_FRIENDS_PAGE_RESET_TIME
from gui.impl.common.tabs_controller import TabsController, tabUpdateFunc
from gui.impl.gen.view_models.views.lobby.new_year.components.new_year_tab_model import NewYearTabModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_main_menu_tab_model import NyMainMenuTabModel
from gui.shared.utils import decorators
from helpers import dependency, time_utils
from items.components.ny_constants import NyATMReward
from new_year.celebrity.celebrity_quests_helpers import hasCelebrityBubble, isDogPageVisited, isUnseenCelebrityQuestsAvailable, getTotalDogSacksCount, checkIsAllAvailableDiscountApplied
from new_year.ny_constants import NyWidgetTopMenu, NyTabBarMainView, NyTabBarFriendGladeView, NyTabBarChallengeView, NyTabBarMarketplaceView, DAYS_BETWEEN_FRIEND_TAB_REMINDER
from new_year.ny_marketplace_helper import isCollectionReceived
from new_year.ny_piggy_bank_helper import getPiggyBankStatus
from new_year.ny_resource_collecting_helper import isCollectingAvailable
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import INewYearController, IGiftMachineController, IFriendServiceController, INewYearTriggerHintsController

class NyTabsController(TabsController):
    __slots__ = ('_iconNamePostfix', '_selectedTabIdx')

    def __init__(self, autoCreating=True, iconNamePostfix=''):
        super(NyTabsController, self).__init__(autoCreating)
        self._iconNamePostfix = iconNamePostfix
        self._selectedTabIdx = 0

    @property
    def tabs(self):
        return self._getTabs()

    def getSelectedTabIdx(self):
        return self._selectedTabIdx

    def setSelectedTabIdx(self, idx):
        if 0 <= idx < len(self._getTabs()):
            self._selectedTabIdx = idx

    def selectTab(self, tabName):
        tabs = self._getTabs()
        self._selectedTabIdx = tabs.index(tabName) if tabName in tabs else 0

    def getSelectedName(self, tabsArray):
        if self._selectedTabIdx < len(tabsArray):
            return tabsArray[self._selectedTabIdx].getName()
        else:
            return

    def getCurrentTabName(self):
        tabsArray = self._getTabs()
        if self._selectedTabIdx < len(tabsArray):
            return tabsArray[self._selectedTabIdx]
        else:
            return

    def isTabActive(self, tabName):
        return tabName in self._getTabs()

    def updateTabModels(self, tabsArray):
        self._autoCreating = len(tabsArray) != len(self._getTabs())
        super(NyTabsController, self).updateTabModels(tabsArray)

    def getDefaultTab(self):
        tabs = self._getTabs()
        if tabs:
            return tabs[0]
        return super(NyTabsController, self).getDefaultTab()

    def getSettingKeysForUpdate(self):
        return set()

    def clearData(self):
        pass

    def _createViewModel(self, name):
        modelCls = self._getModelCls()
        viewModel = modelCls()
        viewModel.setIconName(name + self._iconNamePostfix)
        return viewModel

    def _getModelCls(self):
        return NewYearTabModel

    def _getTabs(self, **kwargs):
        tabs = super(NyTabsController, self)._getTabs(**kwargs)
        return [ tab for tab in tabs if self._tabActive(tab) ]

    @staticmethod
    def _tabActive(_):
        return True


class NewYearMainTabsController(NyTabsController):
    __nyController = dependency.descriptor(INewYearController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    __nyGiftMachineCtrl = dependency.descriptor(IGiftMachineController)
    __friendsService = dependency.descriptor(IFriendServiceController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, autoCreating=True):
        super(NewYearMainTabsController, self).__init__(autoCreating)
        self.__isFriendHangar = False

    def getIsFriendHangar(self):
        return self.__isFriendHangar

    def updateIsFriendHangar(self, isFriendHangar):
        self.__isFriendHangar = isFriendHangar

    def selectTab(self, tabName):
        super(NewYearMainTabsController, self).selectTab(tabName)
        if tabName == NyATMReward.ShortName.MARKETPLACE:
            if AccountSettings.getUIFlag(NY_NARKET_PLACE_PAGE_VISITED) is False:
                AccountSettings.setUIFlag(NY_NARKET_PLACE_PAGE_VISITED, True)

    def _getModelCls(self):
        return NyMainMenuTabModel

    @tabUpdateFunc(NyWidgetTopMenu.GLADE)
    def _updateGlade(self, viewModel, _=False):
        viewModel.setUnseenCount(self.__nyController.checkForNewToys())

    @tabUpdateFunc(NyWidgetTopMenu.REWARDS)
    def _updateRewards(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyWidgetTopMenu.MARKETPLACE)
    def _updateMarketplace(self, viewModel, _=False):
        flag = AccountSettings.getUIFlag(NY_NARKET_PLACE_PAGE_VISITED)
        if flag is not None:
            if flag is False and self._getTabs()[self.getSelectedTabIdx()] == NyATMReward.ShortName.MARKETPLACE:
                AccountSettings.setUIFlag(NY_NARKET_PLACE_PAGE_VISITED, True)
                flag = True
            viewModel.setUnseenCount(not flag)
        return

    @tabUpdateFunc(NyWidgetTopMenu.FRIENDS)
    @decorators.adisp_process()
    def _updateFriends(self, viewModel, _=False):
        isFriendServiceEnabled = self.__friendsService.isServiceEnabled
        viewModel.setIsEnabled(isFriendServiceEnabled)
        if not isFriendServiceEnabled:
            return
        currentTime = time_utils.getServerUTCTime()
        lastSeenTime = AccountSettings.getUIFlag(NY_NO_FRIENDS_PAGE_RESET_TIME)
        resetTimeDelta = DAYS_BETWEEN_FRIEND_TAB_REMINDER * time_utils.ONE_DAY
        friendsListUpdated = self.__friendsService.hasBeenUpdatedOnce
        if not friendsListUpdated:
            friendsListUpdated = yield self.__friendsService.updateFriendList()
        if friendsListUpdated:
            friendList = self.__friendsService.friendList
            if not friendList and (lastSeenTime == 0 or currentTime >= lastSeenTime + resetTimeDelta):
                viewModel.setUnseenCount(True)
                return
        _, completedQuestsCount, receivedRewardsCount, _ = getPiggyBankStatus()
        if receivedRewardsCount < completedQuestsCount:
            viewModel.setUnseenCount(True)
            return
        viewModel.setUnseenCount(False)

    @tabUpdateFunc(NyWidgetTopMenu.CHALLENGE)
    def _updateChallenge(self, viewModel, _=False):
        viewModel.setUnseenCount(hasCelebrityBubble())

    @tabUpdateFunc(NyWidgetTopMenu.GIFT_MACHINE)
    def _updateGiftMachine(self, viewModel, _=False):
        viewModel.setInfoCount(self.__nyController.currencies.getCoinsCount())
        viewModel.setUnseenCount(not self.__nyGiftMachineCtrl.isBuyCoinVisited)

    @tabUpdateFunc(NyWidgetTopMenu.FRIEND_GLADE)
    def _updateFriendGlade(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyWidgetTopMenu.FRIEND_CHALLENGE)
    def _updateFriendChallenge(self, viewModel, _=False):
        pass

    def tabOrderKey(self, tabName):
        return self._getTabs().index(tabName)

    def _getTabs(self, **kwargs):
        if self.__isFriendHangar:
            return NyWidgetTopMenu.ALL_FRIEND_HANGAR
        return NyWidgetTopMenu.ALL_PLAYER_HANGAR


class GladeTabsController(NyTabsController):
    __nyController = dependency.descriptor(INewYearController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)

    @tabUpdateFunc(NyTabBarMainView.TOWN)
    def _updateTown(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarMainView.FIR)
    def _updateFir(self, viewModel, _=False):
        viewModel.setUnseenCount(self.__nyController.checkForNewToysByType(NyTabBarMainView.FIR))

    @tabUpdateFunc(NyTabBarMainView.FAIR)
    def _updateFair(self, viewModel, _=False):
        viewModel.setUnseenCount(self.__nyController.checkForNewToysByType(NyTabBarMainView.FAIR))

    @tabUpdateFunc(NyTabBarMainView.INSTALLATION)
    def _updateInstallation(self, viewModel, _=False):
        viewModel.setUnseenCount(self.__nyController.checkForNewToysByType(NyTabBarMainView.INSTALLATION))

    @tabUpdateFunc(NyTabBarMainView.RESOURCES)
    def _updateResources(self, viewModel, _=False):
        collectingAvailable = isCollectingAvailable()
        __wallet = dependency.instance(IWalletController)
        viewModel.setUnseenCount(collectingAvailable and __wallet.isAvailable)
        viewModel.setIsCompleted(not collectingAvailable and __wallet.isAvailable)

    def tabOrderKey(self, tabName):
        return NyTabBarMainView.ALL.index(tabName)


class FriendGladeTabsController(NyTabsController):
    __nyController = dependency.descriptor(INewYearController)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def clearData(self):
        self._selectedTabIdx = 0

    @tabUpdateFunc(NyTabBarFriendGladeView.TOWN)
    def _updateTown(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarFriendGladeView.FIR)
    def _updateFir(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarFriendGladeView.FAIR)
    def _updateFair(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarFriendGladeView.INSTALLATION)
    def _updateInstallation(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarFriendGladeView.RESOURCES)
    def _updateResources(self, viewModel, _=False):
        hasCooldown = bool(self.__friendsService.getFriendCollectingCooldownTime())
        isBestFriend = self.__friendsService.friendHangarSpaId in self.__friendsService.bestFriendList
        viewModel.setUnseenCount(isBestFriend and not hasCooldown)
        viewModel.setIsCompleted(hasCooldown)

    def tabOrderKey(self, tabName):
        return NyTabBarFriendGladeView.ALL.index(tabName)


class ChallengeTabsController(NyTabsController):
    __nyController = dependency.descriptor(INewYearController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)

    def __init__(self, autoCreating=True):
        super(ChallengeTabsController, self).__init__(autoCreating, iconNamePostfix='Challenge')

    def getSettingKeysForUpdate(self):
        return {
         NY_DOG_PAGE_VISITED,
         NY_CELEBRITY_DAY_QUESTS_VISITED_MASK,
         NY_CELEBRITY_ADV_QUESTS_VISITED_MASK}

    def getCustomTabsKeyUpdate(self):
        return {NY_CAT_PAGE_VISITED: NyTabBarChallengeView.GUEST_CAT}

    @tabUpdateFunc(NyTabBarChallengeView.TOURNAMENT)
    def _updateTournament(self, viewModel, _=False):
        viewModel.setUnseenCount(isUnseenCelebrityQuestsAvailable() or not checkIsAllAvailableDiscountApplied())

    @tabUpdateFunc(NyTabBarChallengeView.GUEST_A)
    def _updateCelebrityA(self, viewModel, _=False):
        pass

    @tabUpdateFunc(NyTabBarChallengeView.GUEST_CAT)
    def _updateCat(self, viewModel, _=False):
        if self.__nyController.isCatTokenReceived():
            flag = AccountSettings.getUIFlag(NY_CAT_PAGE_VISITED)
            viewModel.setUnseenCount(not flag)

    @tabUpdateFunc(NyTabBarChallengeView.GUEST_D)
    def _updateCelebrityD(self, viewModel, _=False):
        if self.__nyController.isDogTokenReceived():
            sacksCount = getTotalDogSacksCount()
            viewModel.setUnseenCount(not isDogPageVisited() or sacksCount > 0)

    @tabUpdateFunc(NyTabBarChallengeView.HEADQUARTERS)
    def _updateStaff(self, viewModel, _=False):
        pass

    def tabOrderKey(self, tabName):
        return NyTabBarChallengeView.ALL.index(tabName)


class MarketplaceTabsController(NyTabsController):

    def __init__(self, autoCreating=True):
        super(MarketplaceTabsController, self).__init__(autoCreating, iconNamePostfix='Reward')

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[0])
    def _updateCategory1(self, viewModel, _=False):
        viewModel.setIsCompleted(isCollectionReceived(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[0]))

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[1])
    def _updateCategory2(self, viewModel, _=False):
        viewModel.setIsCompleted(isCollectionReceived(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[1]))

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[2])
    def _updateCategory3(self, viewModel, _=False):
        viewModel.setIsCompleted(isCollectionReceived(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[2]))

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[3])
    def _updateCategory4(self, viewModel, _=False):
        viewModel.setIsCompleted(isCollectionReceived(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[3]))

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[4])
    def _updateCategory5(self, viewModel, _=False):
        viewModel.setIsCompleted(isCollectionReceived(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[4]))

    @tabUpdateFunc(NyTabBarMarketplaceView.VISIBLE_CATEGORIES[5])
    def _updatePreviousCategory(self, viewModel, _=False):
        isReceived = all(isCollectionReceived(category) for category in NyTabBarMarketplaceView.PREVIOUS_CATEGORIES)
        viewModel.setIsCompleted(isReceived)

    def tabOrderKey(self, tabName):
        return NyTabBarMarketplaceView.VISIBLE_CATEGORIES.index(tabName)