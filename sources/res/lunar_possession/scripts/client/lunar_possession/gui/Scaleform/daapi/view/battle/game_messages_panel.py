from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel, PlayerMessageData
from gui.battle_control import avatar_getter
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.utils import toUpper
from constants import FINISH_REASON

class LunarPossessionGameMessagesPanel(GameMessagesPanel):

    def sendEndGameMessage(self, winningTeam, reason):
        playerTeam = avatar_getter.getPlayerTeam()
        reasonType = {FINISH_REASON.TECHNICAL: 'rivalAbandoned', 
           FINISH_REASON.WIN_POINTS_CAP: 'pointLimit', 
           FINISH_REASON.WIN_POINTS: 'timeLimit'}
        if winningTeam == 0:
            messageType = GAME_MESSAGES_CONSTS.DRAW
            subTitleString = R.strings.lunar_battle.postBattle.dyn('draw')()
        elif playerTeam == winningTeam:
            messageType = GAME_MESSAGES_CONSTS.WIN
            subTitleString = R.strings.lunar_battle.postBattle.dyn('win').dyn(reasonType.get(reason, ''))()
        else:
            messageType = GAME_MESSAGES_CONSTS.DEFEAT
            subTitleString = R.strings.lunar_battle.postBattle.dyn('lose').dyn(reasonType.get(reason, ''))()
        endGameMsgData = {'title': toUpper(backport.text(R.strings.menu.finalStatistic.commonStats.resultlabel.dyn(messageType)())), 
           'subTitle': backport.text(subTitleString)}
        msg = PlayerMessageData(messageType, GAME_MESSAGES_CONSTS.DEFAULT_MESSAGE_LENGTH, GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_END_GAME, endGameMsgData)
        self._addMessage(msg.getDict())