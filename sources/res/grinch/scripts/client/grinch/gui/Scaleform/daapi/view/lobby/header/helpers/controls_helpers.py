from __future__ import absolute_import
from typing import TYPE_CHECKING
from grinch.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getGrinchFightBtnTooltipData
from grinch.gui.impl.lobby.page.lobby_header import GrinchLobbyHeader
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper
from gui.impl.gen import R
if TYPE_CHECKING:
    from typing import Type
    from gui.impl.pub.view_component import ViewComponent

class GrinchLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__ = ()

    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        return (getGrinchFightBtnTooltipData(prbValidation, isInSquad), False)

    @classmethod
    def _getOutSquadTooltipData(cls, _):
        header = R.strings.platoon.headerButton.tooltips.grinchSquad.header()
        body = R.strings.platoon.headerButton.tooltips.grinchSquad.body()
        return (header, body, {})

    @classmethod
    def getHeaderType(cls):
        return GrinchLobbyHeader