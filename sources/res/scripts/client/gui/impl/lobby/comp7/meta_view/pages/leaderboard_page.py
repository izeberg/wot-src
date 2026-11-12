from gui.impl.gen.view_models.views.lobby.comp7.meta_view.tab_model import MetaRootViews
from gui.impl.lobby.comp7.meta_view.pages import PageSubModelPresenter

class LeaderboardPage(PageSubModelPresenter):
    __slots__ = ()

    @property
    def pageId(self):
        return MetaRootViews.LEADERBOARD

    def initialize(self, *args, **kwargs):
        super(LeaderboardPage, self).initialize(*args, **kwargs)
        browserView = self.parentView.getChildView(self.pageId)
        if browserView is not None and browserView.browser is not None:
            browserView.browser.navigate(browserView.url)
        return

    def finalize(self):
        browserView = self.parentView.getChildView(self.pageId)
        if browserView is not None and browserView.browser is not None:
            browserView.browser.unfocus()
            browserView.browser.navigate('about:blank')
        super(LeaderboardPage, self).finalize()
        return