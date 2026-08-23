from __future__ import absolute_import
import typing
from PlayerEvents import g_playerEvents
from helpers.dependency import descriptor
from journey_marathon.jm_constants import JmTokensUpdType
from journey_marathon.jm_helpers import jmCtrl
from journey_marathon_common.journey_marathon_constants import JM_COIN_TOKEN_FMT, QUEST_ISSUED_POSTFIX, SEPARATOR, JM_SHOP_BUNDLE_ACCRUING_TOKEN_FMT
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Dict, Tuple
    from journey_marathon.jm_constants import JmTokensUpdTypes
    Tokens = Dict[(str, Tuple[(long, int)])]
    Token = Tuple[(str, long, int)]
_QUEST_TOKEN_SUFFIX = SEPARATOR + QUEST_ISSUED_POSTFIX

class JmTokens(object):
    __itemsCache = descriptor(IItemsCache)

    def __init__(self):
        self.__questTokens = {}
        self.__lockTokens = {}
        self.__coinToken = ('', 0, 0)
        self.__shopBundleToken = ('', 0, 0)

    def init(self):
        g_playerEvents.onClientSynchronize += self.__onClientSynchronize

    def fini(self):
        g_playerEvents.onClientSynchronize -= self.__onClientSynchronize
        self.__questTokens.clear()
        self.__lockTokens.clear()
        self.__coinToken = ('', 0, 0)
        self.__shopBundleToken = ('', 0, 0)

    def getJmLockTokens(self):
        return self.__lockTokens

    def getJmCoinToken(self):
        return self.__coinToken

    def getJmQuestTokens(self):
        return self.__questTokens

    def getJmShopBundleToken(self):
        return self.__shopBundleToken

    def buildJmTokensFromConfig(self, journeyIdDiff, nodesDiff):
        ctrl = jmCtrl()
        allTokens = self.__itemsCache.items.tokens.getTokens()
        updTypes = set()
        if journeyIdDiff:
            journeyId = ctrl.jmConfig.getJmJourneyId()
            newCoinToken = JM_COIN_TOKEN_FMT.format(journeyId=journeyId)
            oldCoinToken, _, __ = self.__coinToken
            self.__coinToken = (newCoinToken, 0, 0)
            if newCoinToken != oldCoinToken:
                updTypes.add(JmTokensUpdType.COINS)
            self.__updateCoinToken(allTokens, updTypes)
            newShopBundleToken = JM_SHOP_BUNDLE_ACCRUING_TOKEN_FMT.format(journeyId=journeyId)
            oldShopBundleToken, _, __ = self.__shopBundleToken
            if oldShopBundleToken != newShopBundleToken:
                self.__shopBundleToken = (
                 newShopBundleToken, 0, 0)
                updTypes.add(JmTokensUpdType.SHOP_BUNDLE)
            self.__updateShopBundleToken(allTokens, updTypes)
            self.__questTokens.clear()
            self.__updateQuestTokens(allTokens, updTypes)
        if nodesDiff:
            oldLockTokens = self.__lockTokens
            self.__lockTokens = newLockTokens = {token:(0, 0) for nodeInfo in ctrl.jmConfig.getJmNodesConfig().values() for token in nodeInfo.get('lockedBy', ())}
            if set(oldLockTokens) != set(newLockTokens):
                updTypes.add(JmTokensUpdType.LOCK)
            self.__updateLockTokens(allTokens, updTypes)
        if updTypes:
            ctrl.onJmTokensChange(updTypes, True)

    def __updateCoinToken(self, tokensDiff, updTypes):
        token, oldExp, oldCnt = self.__coinToken
        if token in tokensDiff:
            newExp, newCnt = tokensDiff[token] or (0, 0)
            if oldExp != newExp or oldCnt != newCnt:
                self.__coinToken = (
                 token, newExp, newCnt)
                updTypes.add(JmTokensUpdType.COINS)

    def __updateShopBundleToken(self, tokensDiff, updTypes):
        token, oldExp, oldCnt = self.__shopBundleToken
        if token in tokensDiff:
            newExp, newCnt = tokensDiff[token] or (0, 0)
            if oldExp != newExp or oldCnt != newCnt:
                self.__shopBundleToken = (
                 token, newExp, newCnt)
                updTypes.add(JmTokensUpdType.SHOP_BUNDLE)

    def __updateLockTokens(self, tokensDiff, updTypes):
        lockTokens = self.__lockTokens
        for token in lockTokens:
            if token in tokensDiff:
                oldInfo = lockTokens[token]
                newInfo = tokensDiff[token] or (0, 0)
                if oldInfo != newInfo:
                    lockTokens[token] = newInfo
                    updTypes.add(JmTokensUpdType.LOCK)

    def __updateQuestTokens(self, tokensDiff, updTypes):
        prefix = jmCtrl().jmConfig.getJmQuestTokenPrefix()
        questTokens = self.__questTokens
        for token in tokensDiff:
            if not (token.startswith(prefix) and token.endswith(_QUEST_TOKEN_SUFFIX)):
                continue
            newTokenInfo = tokensDiff[token]
            if token in questTokens and newTokenInfo is None:
                del questTokens[token]
                continue
            if questTokens.get(token, (0, 0)) != newTokenInfo:
                questTokens[token] = newTokenInfo
                updTypes.add(JmTokensUpdType.QUEST)

        return

    def __onClientSynchronize(self, isFullSync, diff):
        if 'tokens' not in diff:
            return
        updTypes = set()
        tokensDiff = diff['tokens']
        self.__updateLockTokens(tokensDiff, updTypes)
        self.__updateCoinToken(tokensDiff, updTypes)
        self.__updateQuestTokens(tokensDiff, updTypes)
        self.__updateShopBundleToken(tokensDiff, updTypes)
        if updTypes:
            jmCtrl().onJmTokensChange(updTypes, isFullSync)