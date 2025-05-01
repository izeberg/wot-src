from gui.Scaleform.daapi.view.meta.MissionsPremiumViewMeta import MissionsPremiumViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.daily.daily_quests_view import DailyQuestsView

class DailyQuestsInjectorView(InjectComponentAdaptor, MissionsPremiumViewMeta):
    __slots__ = ()

    def setDefaultTab(self, tabIdx):
        if self._injectView is not None:
            self._injectView.setDefaultTab(tabIdx)
        return

    def changeTab(self, tabIdx):
        if self._injectView is not None:
            self._injectView.changeTab(tabIdx)
        return

    def markVisited(self):
        pass

    def setProxy(self, proxy):
        if self._injectView is not None:
            self._injectView.setProxy(proxy)
        return

    def _makeInjectView(self):
        return DailyQuestsView()