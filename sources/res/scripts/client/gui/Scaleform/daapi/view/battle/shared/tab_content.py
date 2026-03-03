from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.TabContentMeta import TabContentMeta
from gui.impl.battle.battle_page.tab_view import TabView
from gui.impl.gen import R

class TabContent(TabContentMeta):

    def _onPopulate(self):
        self._createInjectView()

    def _makeInjectView(self):
        self.__view = TabView(R.views.battle.battle_page.TabView())
        return self.__view

    def onTabChanged(self, tabAlias):
        self.__view.handleTabChange(tabAlias)