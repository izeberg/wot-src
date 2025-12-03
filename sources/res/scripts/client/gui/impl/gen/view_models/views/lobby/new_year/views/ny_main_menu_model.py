from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_main_menu_tab_model import NyMainMenuTabModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_trigger_hint_tabs_model import NyTriggerHintTabsModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_widget_friend_info_model import NyWidgetFriendInfoModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_widget_level_progress_model import NyWidgetLevelProgressModel

class NyMainMenuModel(ViewModel):
    __slots__ = ('onGoToFriendsList', )

    def __init__(self, properties=8, commands=1):
        super(NyMainMenuModel, self).__init__(properties=properties, commands=commands)

    @property
    def widgetLevelProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getWidgetLevelProgressType():
        return NyWidgetLevelProgressModel

    @property
    def widgetFriendStatus(self):
        return self._getViewModel(1)

    @staticmethod
    def getWidgetFriendStatusType():
        return NyWidgetFriendInfoModel

    @property
    def triggerHintTabs(self):
        return self._getViewModel(2)

    @staticmethod
    def getTriggerHintTabsType():
        return NyTriggerHintTabsModel

    def getItemsMenu(self):
        return self._getArray(3)

    def setItemsMenu(self, value):
        self._setArray(3, value)

    @staticmethod
    def getItemsMenuType():
        return NyMainMenuTabModel

    def getStartIndexMenu(self):
        return self._getNumber(4)

    def setStartIndexMenu(self, value):
        self._setNumber(4, value)

    def getCurrentView(self):
        return self._getString(5)

    def setCurrentView(self, value):
        self._setString(5, value)

    def getIsAnimationLevelUp(self):
        return self._getBool(6)

    def setIsAnimationLevelUp(self, value):
        self._setBool(6, value)

    def getHasChangedViewAnimation(self):
        return self._getBool(7)

    def setHasChangedViewAnimation(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(NyMainMenuModel, self)._initialize()
        self._addViewModelProperty('widgetLevelProgress', NyWidgetLevelProgressModel())
        self._addViewModelProperty('widgetFriendStatus', NyWidgetFriendInfoModel())
        self._addViewModelProperty('triggerHintTabs', NyTriggerHintTabsModel())
        self._addArrayProperty('itemsMenu', Array())
        self._addNumberProperty('startIndexMenu', 0)
        self._addStringProperty('currentView', '')
        self._addBoolProperty('isAnimationLevelUp', False)
        self._addBoolProperty('hasChangedViewAnimation', False)
        self.onGoToFriendsList = self._addCommand('onGoToFriendsList')