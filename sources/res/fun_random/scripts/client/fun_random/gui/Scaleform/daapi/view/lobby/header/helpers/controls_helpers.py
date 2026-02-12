from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from fun_random.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getFunRandomFightBtnTooltipData
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper

class FunRandomLobbyHeaderHelper(DefaultLobbyHeaderHelper, FunAssetPacksMixin):
    __slots__ = ()

    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        return (getFunRandomFightBtnTooltipData(prbValidation, isInSquad), False)

    @classmethod
    def _getOutSquadTooltipData(cls, _):
        return (R.strings.platoon.members.card.disabledVertical(), R.invalid(), {})