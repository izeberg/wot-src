from __future__ import absolute_import
from future.utils import viewkeys, viewvalues
from typing import Dict, List, TYPE_CHECKING
from adisp import adisp_async, adisp_process
from constants import LOOTBOX_TOKEN_PREFIX
from helpers import dependency
from fun_random.gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import getFunAwardsPacker
from fun_random.gui.feature.fun_constants import FEP_MODE_ITEMS_QUEST_ID, FEP_PROGRESSION_EXECUTOR_QUEST_ID, FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID
from fun_random.gui.feature.util.fun_helpers import getProgressionInfoByExecutor
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression
from fun_random.gui.impl.lobby.common.lootboxes import FEP_CATEGORY, FunRandomLootBoxTypes
from fun_random.gui.impl.lobby.common.fun_view_helpers import getStageRarity, DEFAULT_NON_FEP_LB_RARITY, DEFAULT_FEP_PROGRESSION_STAGE_RARITY, sortFunProgressionBonuses
from fun_random.gui.shared.event_dispatcher import showFunRandomLootBoxAwardWindow
from fun_random.messenger.formatters.loot_box_auto_open_subformatters import FunRandomLootboxAutoOpenFormatter, FunRandomMessageAwardsComposer, MAX_AWARDS_COUNT
from fun_random.notification.decorators import FunRandomProgressionStageMessageDecorator
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.notifications import NotificationPriorityLevel
from gui.server_events.awards_formatters import AWARDS_SIZES
from gui.server_events.bonuses import LootBoxTokensBonus
from helpers.time_utils import ONE_DAY
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData, getRewardsForQuests
from messenger.formatters.token_quest_subformatters import TokenQuestsSubFormatter, AsyncTokenQuestsSubFormatter, SyncTokenQuestsSubFormatter
from skeletons.gui.server_events import IEventsCache
from shared_utils import first
if TYPE_CHECKING:
    from gui.server_events.event_items import Quest

class FunProgressionRewardsBaseFormatter(ServiceChannelFormatter, TokenQuestsSubFormatter, FunAssetPacksMixin, FunProgressionWatcher):
    __INFO_TEMPLATE = 'InformationHeaderSysMessage'
    __PROGRESSION_STAGE_TEMPLATE = 'FunRandomProgressionStage'
    __RES_SHORTCUT = R.strings.fun_random.notification
    __eventsCache = dependency.descriptor(IEventsCache)

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(FEP_PROGRESSION_EXECUTOR_QUEST_ID) or questID.startswith(FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID)

    def _getAchievesFormatter(self):
        raise NotImplementedError

    def _format(self, message, *_):
        messageData = message.data or {}
        completedQuestIDs = self.getQuestOfThisGroup(messageData.get('completedQuestIDs', set()))
        completedQuestsInfo = {qID:getProgressionInfoByExecutor(qID) for qID in completedQuestIDs}
        messageDataList = []
        for qID in sorted(completedQuestIDs, key=lambda qID: completedQuestsInfo[qID]):
            messageDataList.append(self._formatSingleQuestCompletion(completedQuestsInfo[qID], getRewardsForQuests(message, {qID}), qID))

        return messageDataList

    def _formatProgressionCompletion(self, progression, rewardsFmt):
        resetText = None
        if not progression.state.isLastProgression:
            resetDays = int(progression.resetTimer // ONE_DAY)
            if resetDays > 0:
                resetText = backport.text(self.__RES_SHORTCUT.progressionComplete.resetTimeLeft(), days=resetDays)
            else:
                resetText = backport.text(self.__RES_SHORTCUT.progressionComplete.resetLessDay())
        msgId = self.__RES_SHORTCUT.progressionComplete()
        if progression.hasUnlimitedProgression:
            msgId = self.__RES_SHORTCUT.progressionComplete.infiniteStarted()
        messageText = backport.text(msgId, modeName=self.getModeUserName())
        messageText = text_styles.concatStylesToMultiLine(messageText, rewardsFmt)
        if resetText:
            return text_styles.concatStylesToMultiLine(messageText, '', resetText)
        else:
            return messageText

    @hasActiveProgression(defReturn=MessageData(None, None))
    def _formatSingleQuestCompletion(self, qInfo, rewards, questID):
        pName, pCounter = qInfo
        currProgression = self.getActiveProgression()
        executors = currProgression.config.executors
        isActiveStage = pCounter in executors
        stageIndex = executors.index(pCounter) + 1 if isActiveStage else None
        maximumStage = currProgression.state.maximumStageIndex + 1
        rewardsFmt = self._getAchievesFormatter().formatQuestAchieves(rewards, asBattleFormatter=False)
        if not rewardsFmt or currProgression.config.name != pName:
            return MessageData(None, None)
        else:
            quest = self.__eventsCache.getHiddenQuests().get(questID)
            if quest is not None and isActiveStage:
                return self._getFancyMessageData(quest, rewards, stageIndex, maximumStage)
            messageHeader = backport.text(self.__RES_SHORTCUT.congratulation())
            messageText, priority = None, NotificationPriorityLevel.MEDIUM
            if currProgression.isInUnlimitedProgression and pCounter == currProgression.config.unlimitedExecutor:
                messageText = backport.text(self.__RES_SHORTCUT.progressionInfiniteStageComplete())
                messageText = text_styles.concatStylesToMultiLine(messageText, rewardsFmt)
            else:
                if isActiveStage:
                    if pCounter != executors[(-1)]:
                        messageText = backport.text(self.__RES_SHORTCUT.progressionStageComplete(), modeName=self.getModeUserName(), stage=stageIndex)
                        messageText = text_styles.concatStylesToMultiLine(messageText, rewardsFmt)
                    else:
                        messageText = self._formatProgressionCompletion(currProgression, rewardsFmt)
                        priority = NotificationPriorityLevel.HIGH
                template, decorator = self.__PROGRESSION_STAGE_TEMPLATE, FunRandomProgressionStageMessageDecorator
                if messageText:
                    return MessageData(g_settings.msgTemplates.format(template, {'header': messageHeader, 'text': messageText}), self._getGuiSettings(None, key=template, priorityLevel=priority, decorator=decorator))
            return MessageData(None, None)

    def _getFancyMessageData(self, quest, rewards, stageIndex, maximumStage):
        bonuses = sortFunProgressionBonuses(quest.getBonuses())
        stageRarity = getStageRarity(bonuses, DEFAULT_FEP_PROGRESSION_STAGE_RARITY)
        if stageRarity not in (DEFAULT_FEP_PROGRESSION_STAGE_RARITY, DEFAULT_NON_FEP_LB_RARITY):
            return MessageData(None, None)
        else:
            if stageRarity == DEFAULT_NON_FEP_LB_RARITY:
                self._showAwardWindow(rewards)
            mainRewards = []
            otherRewards = []
            for item in bonuses:
                if isinstance(item, LootBoxTokensBonus):
                    mainRewards.append(item)
                else:
                    otherRewards.append(item)

            if len(mainRewards) > 1:
                otherRewards = mainRewards[1:] + otherRewards
                mainRewards = [mainRewards[0]]
            composer = FunRandomMessageAwardsComposer(MAX_AWARDS_COUNT, getFunAwardsPacker())
            mainFormatted = None
            if mainRewards:
                mainFormatted = first(composer.getFormattedBonuses(mainRewards, AWARDS_SIZES.S232X174))
            otherFormatted = composer.getFormattedBonuses(otherRewards, AWARDS_SIZES.SMALL)
            bgIcon = backport.image(self.getModeIconsResRoot().library.notification_bg())
            rewardsData = {'linkageData': {'mainReward': mainFormatted, 
                               'rewards': otherFormatted, 
                               'bgIcon': bgIcon}}
            if stageIndex == maximumStage:
                rewardText = backport.text(self.__RES_SHORTCUT.progressionStageComplete.rewardReceivedLastStage())
            else:
                rewardText = backport.text(self.__RES_SHORTCUT.progressionStageComplete.rewardReceived(), stageIndex=stageIndex, maximumStage=maximumStage)
            context = {'header': self.getModeUserName(), 'rewardText': rewardText}
            template = FunRandomLootboxAutoOpenFormatter.get_template()
            decorator = FunRandomProgressionStageMessageDecorator
            return MessageData(g_settings.msgTemplates.format(template, ctx=context, data=rewardsData), self._getGuiSettings(None, key=template, decorator=decorator))

    def _showAwardWindow(self, rewards):
        mainRewards = {}
        otherRewards = {}
        for rewardKey, rewardValue in rewards.iteritems():
            if rewardKey == LootBoxTokensBonus.TOKENS:
                for tokenKey, tokenValue in rewardValue.items():
                    if tokenKey.startswith(LOOTBOX_TOKEN_PREFIX):
                        mainRewards.setdefault(rewardKey, {})[tokenKey] = tokenValue
                    else:
                        otherRewards.setdefault(rewardKey, {})[tokenKey] = tokenValue

            else:
                otherRewards[rewardKey] = rewardValue

        awardData = {'lootBoxType': FunRandomLootBoxTypes.LEGENDARY, 'mainRewards': mainRewards, 
           'addRewards': otherRewards}
        showFunRandomLootBoxAwardWindow(awardData)


class FunProgressionRewardsAsyncFormatter(AsyncTokenQuestsSubFormatter, FunProgressionRewardsBaseFormatter):

    def __init__(self):
        super(FunProgressionRewardsAsyncFormatter, self).__init__()
        self._achievesFormatter = FunRandomLootBoxFormatter()

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        messageDataList = self._format(message) if isSynced else []
        callback(messageDataList)

    def _getAchievesFormatter(self):
        return self._achievesFormatter


class FunProgressionRewardsSyncFormatter(SyncTokenQuestsSubFormatter, FunProgressionRewardsBaseFormatter):

    def __init__(self):
        super(FunProgressionRewardsSyncFormatter, self).__init__()
        self._achievesFormatter = FunRandomLootBoxFormatter()

    def format(self, message, *args):
        return self._format(message, *args)

    def _getAchievesFormatter(self):
        return self._achievesFormatter


class FunRandomLootBoxFormatter(QuestAchievesFormatter, FunAssetPacksMixin):

    @classmethod
    def getFormattedAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        result = super(FunRandomLootBoxFormatter, cls).getFormattedAchieves(data, asBattleFormatter, processCustomizations, processTokens)
        battlePassPoints = sum(viewvalues(data.get('battlePassPoints', {}).get('vehicles', {})))
        if battlePassPoints > 0:
            result.append(backport.text(R.strings.messenger.serviceChannelMessages.battleResults.quests.battlePassPoints(), value=text_styles.neutral(battlePassPoints)))
        return result

    @classmethod
    def _processTokens(cls, data):
        result = []
        tokensData = data.get('tokens', {})
        sortedTokens = sorted(viewkeys(tokensData), key=cls._sortTokenFunc)
        for token in sortedTokens:
            if token.startswith(LOOTBOX_TOKEN_PREFIX):
                lootBox = cls._itemsCache.items.tokens.getLootBoxByTokenID(token)
                if lootBox and lootBox.getCategory() == FEP_CATEGORY:
                    lbName = backport.text(cls.getModeLocalsResRoot().lootbox.dyn(lootBox.getType())())
                    result.append(g_settings.htmlTemplates.format('funRandomLootBox', {'text': lbName, 'count': tokensData[token].get('count', 1)}))

        return ('\n').join(result)

    @classmethod
    def _sortTokenFunc(cls, tokenId):
        if tokenId.startswith(LOOTBOX_TOKEN_PREFIX):
            lootBox = cls._itemsCache.items.tokens.getLootBoxByTokenID(tokenId)
            if lootBox and lootBox.getType() in FunRandomLootBoxTypes.ORDERED:
                return FunRandomLootBoxTypes.ORDERED.index(lootBox.getType())
        return -1


class FunModeItemsQuestAsyncFormatter(AsyncTokenQuestsSubFormatter, FunAssetPacksMixin):
    __INFO_TEMPLATE = 'InformationHeaderSysMessage'

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        isEnabledByLUI = self._itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount() > 0
        messageDataList = self._format(message) if isSynced and isEnabledByLUI else []
        callback(messageDataList)

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(FEP_MODE_ITEMS_QUEST_ID)

    def _format(self, message, *_):
        messageData = message.data or {}
        messageDataList = []
        for qID in self.getQuestOfThisGroup(messageData.get('completedQuestIDs', set())):
            messageDataList.append(self._formatModeItemsSingleQuest(getRewardsForQuests(message, {qID})))

        return messageDataList

    def _formatModeItemsSingleQuest(self, rewards):
        template = self.__INFO_TEMPLATE
        messageHeader = self.getModeUserName()
        messageText = self._achievesFormatter.formatQuestAchieves(rewards, asBattleFormatter=False)
        messageData = g_settings.msgTemplates.format(template, {'header': messageHeader, 'text': messageText})
        return MessageData(messageData, self._getGuiSettings(None, key=template))