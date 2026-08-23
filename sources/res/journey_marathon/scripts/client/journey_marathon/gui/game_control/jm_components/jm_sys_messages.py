from __future__ import absolute_import
import logging, typing
from time import time
from ChatManager import chatManager
from PlayerEvents import g_playerEvents
from chat_shared import CHAT_ACTIONS, SYS_MESSAGE_TYPE
from gui.SystemMessages import SM_TYPE, pushMessage
from gui.impl.backport import ntext, text
from gui.impl.gen import R
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.notifications import NotificationPriorityLevel as Priority
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from journey_marathon.gui.shared.bonus_packers import getJmLockTokenUserName
from journey_marathon.jm_constants import JmFtState, JmTokensUpdType
from journey_marathon.jm_helpers import jmCtrl
from messenger import g_settings as messengerSettings
from messenger.formatters.service_channel import QuestAchievesFormatter, _getAchievementsFromQuestData
from shared_utils import first
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List, Optional, Tuple, Type, Sequence
_logger = logging.getLogger(__name__)
_RES = R.strings.journey_marathon.systemMessage
_COOLDOWN = 5.0
_BATTLE_RESULTS_INDEX = SYS_MESSAGE_TYPE.battleResults.index()

class JmSysMessages(object):

    def __init__(self):
        super(JmSysMessages, self).__init__()
        self.__isLobbyInited = False
        self.__lobbyPendingPushers = []
        self.__animPendingPushers = []
        self.__callTimes = {}
        self.__featureState = None
        self.__coinTokenCount = 0
        self.__coinTokensShown = 0
        return

    def init(self):
        ctrl = jmCtrl()
        ctrl.onJmTokensChange += self.__onTokensChange
        ctrl.onJmFeatureStateChange += self.__onJmFeatureStateChange
        g_playerEvents.onAccountBecomeNonPlayer += self.__onAccountBecomeNonPlayer
        chatManager.subscribeChatAction(self.__onChatAction, CHAT_ACTIONS.personalSysMessage)

    def fini(self):
        ctrl = jmCtrl()
        ctrl.onJmFeatureStateChange -= self.__onJmFeatureStateChange
        ctrl.onJmTokensChange -= self.__onTokensChange
        g_playerEvents.onAccountBecomeNonPlayer -= self.__onAccountBecomeNonPlayer
        chatManager.unsubscribeChatAction(self.__onChatAction, CHAT_ACTIONS.personalSysMessage)
        self.__isLobbyInited = False
        self.__lobbyPendingPushers = []
        self.__animPendingPushers = []
        self.__callTimes = {}
        self.__featureState = None
        self.__coinTokenCount = 0
        self.__coinTokensShown = 0
        return

    def onLobbyInited(self):
        self.__isLobbyInited = True
        self.__pushLobbyPending()

    def pushMessJmActionUnavailable(self):
        lastCallTime = self.__callTimes.get(_pushMessActionUnavailable, 0)
        nextCallTime = lastCallTime + _COOLDOWN
        now = time()
        if now > nextCallTime:
            _pushMessActionUnavailable()
            self.__callTimes[_pushMessActionUnavailable] = now

    def onJmNodesExplored(self, nodeIds, invoiceResp):
        self.__animPendingPushers.append(_KeysSpent(nodeIds))
        self.__animPendingPushers.append(_NodesExplored(nodeIds, invoiceResp))

    def pushJmAnimPending(self):
        for pusher in self.__animPendingPushers:
            pusher()

        self.__animPendingPushers = []

    def __onChatAction(self, data):
        data = data.data
        if data.get('type') != _BATTLE_RESULTS_INDEX:
            return
        ctrl = jmCtrl()
        prefix = ctrl.jmConfig.getJmQuestTokenPrefix()
        coinToken, _, __ = ctrl.jmTokens.getJmCoinToken()
        detailedRewards = data.get('data', {}).get('detailedRewards') or {}
        for qID in detailedRewards:
            if qID.startswith(prefix):
                coinCount = detailedRewards[qID].get('tokens', {}).get(coinToken, {}).get('count') or 0
                if coinCount > 0:
                    self.__addOrCallPusher(_MissionCompleted(coinCount))
                    self.__coinTokensShown += coinCount

    def __onTokensChange(self, updTypes, isFullSync):
        if JmTokensUpdType.COINS in updTypes:
            oldCount = self.__coinTokenCount
            self.__coinTokenCount = newCount = jmCtrl().jmTokens.getJmCoinToken()[(-1)]
            shown = self.__coinTokensShown
            self.__coinTokensShown = 0
            if not isFullSync:
                diff = newCount - oldCount - shown
                if diff != 0:
                    self.__addOrCallPusher(_CoinReceipt(diff))

    def __onAccountBecomeNonPlayer(self):
        self.__isLobbyInited = False

    def __onJmFeatureStateChange(self):
        oldState = self.__featureState
        newState = jmCtrl().jmSwitcher.getJmFtState()
        if newState == JmFtState.HIDDEN:
            return
        else:
            self.__featureState = newState
            if oldState is None or oldState == newState:
                return
            if newState == JmFtState.DISABLED:
                self.__addOrCallPusher(_FtDisabled())
            elif newState == JmFtState.PAUSED:
                self.__addOrCallPusher(_FtPaused())
            elif oldState != JmFtState.ACTIVE and newState == JmFtState.ACTIVE:
                self.__addOrCallPusher(_FtAvailable())
            return

    def __addOrCallPusher(self, pusher):
        if self.__isLobbyInited:
            pusher()
            return
        pendingPushers = self.__lobbyPendingPushers
        if pusher.isUnique and pusher in pendingPushers:
            return
        for pendingPusher in pendingPushers[:]:
            for pusherType in pusher.replaces:
                if isinstance(pendingPusher, pusherType):
                    pendingPushers.remove(pendingPusher)

        pendingPushers.append(pusher)

    def __pushLobbyPending(self):
        for pusher in self.__lobbyPendingPushers:
            pusher()

        self.__lobbyPendingPushers = []


class _Pusher(object):
    isUnique = True
    replaces = ()

    def __call__(self):
        raise NotImplementedError


class _FtAvailable(_Pusher):

    def __init__(self):
        self.replaces = (
         _FtDisabled, _FtPaused)

    def __call__(self):
        body = text(_RES.available.text())
        pushMessage('', SM_TYPE.InformationHeader, Priority.MEDIUM, {'header': _longName(), 'text': body})


class _FtDisabled(_Pusher):

    def __init__(self):
        self.replaces = (
         _FtAvailable, _FtPaused)

    def __call__(self):
        pushMessage(text(_RES.disabled.text(), longName=_longName()), SM_TYPE.Warning, Priority.MEDIUM)


class _FtPaused(_Pusher):

    def __init__(self):
        self.replaces = (
         _FtAvailable, _FtDisabled)

    def __call__(self):
        longName = _longName()
        body = text(_RES.paused.text(), longName=longName)
        pushMessage('', SM_TYPE.ErrorHeader, Priority.HIGH, {'header': longName, 'text': body})


class _MissionCompleted(_Pusher):
    isUnique = False

    def __init__(self, coinTokenCount):
        self.coinTokenCount = coinTokenCount

    def __call__(self):
        header = text(_RES.missionCompleted.header())
        body = text(_RES.missionCompleted.text())
        body = formatJmTokenMessage(body, self.coinTokenCount)
        pushMessage('', SM_TYPE.InformationHeader, Priority.MEDIUM, {'header': header, 'text': body})


class _CoinReceipt(_Pusher):
    isUnique = False

    def __init__(self, coinTokenDiff):
        self.coinTokenDiff = coinTokenDiff

    def __call__(self):
        header = text(_RES.coinReceipt.header())
        body = text(_RES.coinReceipt.text.dyn('add' if self.coinTokenDiff > 0 else 'draw')())
        body = formatJmTokenMessage(body, abs(self.coinTokenDiff))
        pushMessage('', SM_TYPE.InformationHeader, Priority.MEDIUM, {'header': header, 'text': body})


class _NodesExplored(_Pusher):

    def __init__(self, nodeIds, invoiceResp):
        self.nodeIds = nodeIds
        self.invoiceResp = invoiceResp

    def __call__(self):
        if not self.invoiceResp:
            return
        fmtBonuses = JmBonusFormatter.formatQuestAchieves(self.invoiceResp, False)
        if not fmtBonuses:
            return
        res = _RES.nodesExplored
        lenNodes = len(self.nodeIds)
        body = ntext(res.text(), lenNodes, nodesCount=lenNodes, bonuses=fmtBonuses)
        pushMessage('', SM_TYPE.InformationHeader, Priority.MEDIUM, {'header': text(res.header()), 'text': body})


class _KeysSpent(_Pusher):

    def __init__(self, nodeIds):
        self.nodeIds = nodeIds

    def __call__(self):
        ctrl = jmCtrl()
        nodes = ctrl.jmNodes.getJmNodes()
        keysCount = 0
        for nodeId in self.nodeIds:
            if nodeId not in nodes:
                _logger.error('Invalid node id when pushing notifications, nodeId=%s', nodeId)
                continue
            keysCount += len(nodes[nodeId].lockedBy)

        if keysCount <= 0:
            return
        res = _RES.nodeUnlocked
        if keysCount == 1:
            lockToken = first(jmCtrl().jmTokens.getJmLockTokens())
            keyName = getJmLockTokenUserName(lockToken) or ''
            if not keyName:
                _logger.error('Key name not found from token, token=%s, name=%s', lockToken, keyName)
                return
            body = ntext(res.text(), keysCount, keysCount=keysCount, keyName=keyName)
        else:
            body = ntext(res.text(), keysCount, keysCount=keysCount)
        pushMessage('', SM_TYPE.InformationHeader, Priority.MEDIUM, {'header': text(res.header()), 'text': body})


def _pushMessActionUnavailable():
    pushMessage(text(_RES.actionUnavailable.text()), SM_TYPE.ErrorSimple, Priority.MEDIUM)


class JmBonusFormatter(QuestAchievesFormatter):

    @classmethod
    def _processTokens(cls, tokens):
        if 'tokens' not in tokens:
            return ''
        else:
            result = []
            tokens = tokens['tokens']
            lockTokens = jmCtrl().jmTokens.getJmLockTokens()
            for token in tokens:
                if token.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                    info = getRecruitInfo(token)
                    if info is None:
                        _logger.error('Failed to find recruit info, token=%s', token)
                        continue
                    result.append(text(_RES.nodeUnlocked.tman.text(), name=info.getFullUserName()))
                if token in lockTokens:
                    count = tokens[token].get('count') or 0
                    if count <= 0:
                        _logger.error('Lock token count missing from invoice, token=%s', token)
                        continue
                    userName = getJmLockTokenUserName(token)
                    if userName is None:
                        _logger.error('Failed to find text for lock token, token=%s', token)
                        continue
                    result.append(formatJmTokenMessage(userName, count))

            return ('\n').join(result)

    @classmethod
    def _extractAchievements(cls, data):
        return _getAchievementsFromQuestData(data)


def formatJmTokenMessage(userName, count=None):
    return messengerSettings.htmlTemplates.format('platformCurrency', {'msg': userName, 'count': count or 1})


def _longName():
    return text(R.strings.journey_marathon.longName())