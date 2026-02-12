from gui.impl.gen import R
from wg_async import wg_await, wg_async
from BWUtil import AsyncReturn
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showResDialogWindow

@wg_async
def showLunarPossesionLeaverAliveWindow():
    quitBattleResRoot = R.strings.dialogs.lunarQuitBattle
    title = quitBattleResRoot.leaver.title()
    confirm = quitBattleResRoot.leaver.submit()
    cancel = quitBattleResRoot.leaver.cancel()
    description = quitBattleResRoot.leaver.descriptionAlive()
    icon = R.images.lunar_possession.gui.maps.icons.battle.deserterLeaveBattle()
    result = yield wg_await(showResDialogWindow(title, confirm=confirm, cancel=cancel, description=description, icon=icon))
    raise AsyncReturn(result)