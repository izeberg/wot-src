from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from messenger.formatters import TimeFormatter
from gui.shared.formatters import text_styles
from skeletons.gui.game_control import IWhiteTigerController
from white_tiger_common.wt_constants import WHITE_TIGER_GAME_PARAMS_KEY

class WTLobbyHeader(LobbyHeader):
    _wtController = dependency.descriptor(IWhiteTigerController)
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(WTLobbyHeader, self).__init__()
        self.__inEvent = False

    def onPrbEntitySwitched(self):
        self._populateButtons()
        super(WTLobbyHeader, self).onPrbEntitySwitched()

    def _addListeners(self):
        super(WTLobbyHeader, self)._addListeners()
        self._wtController.onLobbyHeaderUpdate += self.__onLobbyHeaderUpdate
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onSettingsChanged

    def _removeListeners(self):
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onSettingsChanged
        self._wtController.onLobbyHeaderUpdate -= self.__onLobbyHeaderUpdate
        super(WTLobbyHeader, self)._removeListeners()

    def __onLobbyHeaderUpdate(self):
        self._updatePrebattleControls()

    def _updatePrebattleControls(self, *_):
        super(WTLobbyHeader, self)._updatePrebattleControls(*_)
        if self._wtController.isWtMode():
            if self._wtController.isBanned:
                timeStr = text_styles.yellowText(TimeFormatter.getLongDatetimeFormat(self._wtController.banExpiryTime))
                r = R.strings.white_tiger.hangar.startBtn
                body = backport.text(r.banned.body(), time=timeStr)
                self.as_disableFightButtonS(True)
                self.as_setFightBtnTooltipS(makeTooltip(backport.text(r.banned.header()), body), False)

    def __onSettingsChanged(self, diff):
        if WHITE_TIGER_GAME_PARAMS_KEY not in diff:
            return
        self._updatePrebattleControls()