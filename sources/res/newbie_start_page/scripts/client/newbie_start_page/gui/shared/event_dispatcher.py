import typing

def showNewbieStartPage(guiCtx):
    from newbie_start_page.gui.impl.lobby.newbie_start_page.newbie_start_page_view import NewbieStartPageViewWindow
    window = NewbieStartPageViewWindow(guiCtx)
    window.load()