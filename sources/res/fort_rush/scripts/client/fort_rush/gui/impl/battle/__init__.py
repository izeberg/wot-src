from __future__ import absolute_import
from fort_rush.gui.impl.battle.fort_rush_hud import FortRushHudWindow, FortRushHudView
from helpers import dependency
from skeletons.gui.impl import IGuiLoader

def showFortRushHud():
    window = FortRushHudWindow()
    window.load()


def destroyFortRushHud():
    guiLoader = dependency.instance(IGuiLoader)
    view = guiLoader.windowsManager.getViewByLayoutID(FortRushHudView.LAYOUT_ID)
    if view is not None:
        view.destroyWindow()
    return