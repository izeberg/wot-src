from constants import EVENT_TYPE, INVOICE_ASSET, CUSTOMIZATION_PROGRESS_PREFIX
from chat_shared import SYS_MESSAGE_TYPE
from frameworks.wulf import WindowLayer
from gui.server_events.bonuses import mergeBonuses, getMergedBonusesFromDicts
from gui.impl.lobby.awards import SupportedTokenTypes
from gui.impl.gen import R
from gui.impl import backport
from gui.SystemMessages import SM_TYPE
from gui.game_control.AwardController import ServiceChannelHandler, MultiTypeServiceChannelHandler
from gui.server_events.bonuses import getAllNonQuestBonuses
from gui.shared.event_dispatcher import getParentWindow
from gui.shared.system_factory import registerAwardControllerHandlers
from helpers import dependency
from new_year.messenger.sys_messages import showMachineNotification, pushNewYearEventButtonMessage
from skeletons.gui.game_control import IBootcampController
from shared_utils import findFirst
from debug_utils import LOG_ERROR
from new_year.ny_constants import NY_LEVEL_PREFIX, NY_MARKETPLACE_UNLOCK_ENTITLEMENT, NY_INVOICE_LEADERBOARD_REWARD_PREFIX, NY_LEADERBOARD_CUMULATIVE_TAG_SUFFIXES, NY_CUMULATIVE_LEADERBOARD_SEASON_ID, NY_PREORDER_REWARDS_QUEST_ID, NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY
from new_year.gui.shared.ny_level_helper import parseNYLevelToken
from new_year.gui.shared.event_dispatcher import showNYLevelUpWindow, showNYQuestsRewardWindow, showNYLeaderboardRewardWindow, showNYPreorderRewardWindow
from new_year.gui.shared.ny_machine_helper import getMachineLootboxToken
from new_year.gui.impl.new_year.sounds import NewYearCelebVoiceOvers
from new_year.helpers.ny_helpers import showEmbeddedAudioVideoView, lockNyNotifications
from new_year.helpers.ny_leaderboard_tank_reward import registerLeaderboardTankReward
from new_year_common.items import new_year
from new_year_common.items.components.ny_constants import CurrentNYConstants, YEARS_INFO, MAX_ATMOSPHERE_LVL
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year.skeletons.new_year import INewYearController
from skeletons.gui.impl import INotificationWindowController

class NewYearAtmosphereHandler(ServiceChannelHandler):
    _bootcampController = dependency.descriptor(IBootcampController)
    __notificationMgr = dependency.descriptor(INotificationWindowController)
    _FIRST_LEVEL = 1

    def __init__(self, awardCtrl):
        super(NewYearAtmosphereHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        self.__alreadyGotForBootcamp = set()
        self.__pendingMaxLevelSequence = None
        return

    def stop(self):
        self.__discardMaxLevelSequence()
        super(NewYearAtmosphereHandler, self).stop()

    def onAvatarBecomePlayer(self):
        self.__discardMaxLevelSequence()
        super(NewYearAtmosphereHandler, self).onAvatarBecomePlayer()

    def _needToShowAward(self, ctx):
        if not super(NewYearAtmosphereHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        completedQuestIDs = message.data.get('completedQuestIDs', set())
        return self.__hasNewYearAward(completedQuestIDs)

    def _showAward(self, ctx):
        data = ctx[1].data
        completedQuestIDs = data.get('completedQuestIDs', set())
        levelRewards = {}
        collectionRewards = {}
        detailedRewards = data.get('detailedRewards', {})
        shouldPushMarketplaceMessage = False
        collectionRewardIDs = new_year.g_cache.collectionIDByCollectionRewards
        for questID in completedQuestIDs:
            rewards = detailedRewards.get(questID, {})
            level = parseNYLevelToken(questID) if questID.startswith(NY_LEVEL_PREFIX) else None
            if level is not None and level != self._FIRST_LEVEL:
                levelRewards[level] = getAllNonQuestBonuses(rewards)
            elif questID in collectionRewardIDs:
                collectionStrId = collectionRewardIDs[questID]
                collectionRewards[collectionStrId] = getAllNonQuestBonuses(rewards)
            shouldPushMarketplaceMessage = shouldPushMarketplaceMessage or NY_MARKETPLACE_UNLOCK_ENTITLEMENT in rewards.get('entitlements', {})

        if shouldPushMarketplaceMessage:
            self.__pushMessage()
        if levelRewards and MAX_ATMOSPHERE_LVL in levelRewards:
            self.__pendingMaxLevelSequence = {'levelRewards': levelRewards, 'collectionRewards': collectionRewards, 
               'completedQuestIDs': completedQuestIDs}
            self.__showMaxLevelGreetingsVideo()
            return
        else:
            self.__showRewardWindows(levelRewards, collectionRewards)
            return

    def __showRewardWindows(self, levelRewards, collectionRewards):
        if levelRewards:
            self.__showWindow({'levelRewards': levelRewards})
        if collectionRewards:
            self.__showWindow({'collectionRewards': collectionRewards})

    def __hasNewYearAward(self, completedQuestIDs):
        awardTokens = set()
        collectionRewardIDs = new_year.g_cache.collectionIDByCollectionRewards
        for token in completedQuestIDs:
            level = parseNYLevelToken(token)
            if level == self._FIRST_LEVEL:
                continue
            if level or token in collectionRewardIDs:
                awardTokens.add(token)

        if not awardTokens:
            return False
        if self._bootcampController.isInBootcampAccount():
            self.__alreadyGotForBootcamp.update(awardTokens)
            return True
        return bool(awardTokens.difference(self.__alreadyGotForBootcamp))

    def __showMaxLevelGreetingsVideo(self):
        showEmbeddedAudioVideoView(videoSource=R.videos.new_year.greetings.lvl_greetings(), parent=getParentWindow(), onVideoClosed=self.__onMaxLevelGreetingsClosed, isControlsVisible=False, releaseNotificationsLockOnClose=False)

    def __onMaxLevelGreetingsClosed(self):
        pending = self.__pendingMaxLevelSequence
        self.__pendingMaxLevelSequence = None
        self.__notificationMgr.postponeActive()
        try:
            if pending is not None:
                self.__showRewardWindows(pending['levelRewards'], pending['collectionRewards'])
        finally:
            lockNyNotifications(NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY, lock=False)

        return

    def __discardMaxLevelSequence(self):
        if self.__pendingMaxLevelSequence is None:
            return
        else:
            self.__pendingMaxLevelSequence = None
            self.__notificationMgr.postponeActive()
            lockNyNotifications(NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY, lock=False)
            return

    @classmethod
    def __showWindow(cls, ctx):
        showNYLevelUpWindow(layer=WindowLayer.TOP_WINDOW, **ctx)

    def __pushMessage(self):
        pushNewYearEventButtonMessage(text=backport.text(R.strings.ny.notification.previousStyles.text()), msgType=SM_TYPE.NewYearPreviousStyleShop, messageData={'header': backport.text(R.strings.ny.notification.header(), year=YEARS_INFO.CURRENT_YEAR_FULL)})


class NewYearQuestHandler(MultiTypeServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(NewYearQuestHandler, self).__init__((
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.battleResults.index(),
         SYS_MESSAGE_TYPE.versusAIBattleResults.index()), awardCtrl)

    @staticmethod
    def __showWindow(rewards, voiceoverEvent=None):
        showNYQuestsRewardWindow(data=rewards, voiceoverEvent=voiceoverEvent)

    @staticmethod
    def _isAppropriate(quest):
        return quest.getType() == EVENT_TYPE.BATTLE_QUEST

    def _showAward(self, ctx):
        data = ctx[1].data
        if data is None:
            return
        else:
            detailedRewards = data.get('detailedRewards') or {}
            completedQuestIDs = data.get('completedQuestIDs') or ()
            questRewards = []
            machineRewards = []
            machineLootboxToken = getMachineLootboxToken()
            voiceoverEvent = None
            for questId in completedQuestIDs:
                if questId.startswith(CurrentNYConstants.NY_WEEKLY_COMMON_QUESTS_PREFIX):
                    voiceoverEvent = NewYearCelebVoiceOvers.REWARD_EPIC
                else:
                    if questId.startswith(CurrentNYConstants.NY_WEEKLY_QUESTS_PREFIX):
                        if voiceoverEvent is None:
                            voiceoverEvent = NewYearCelebVoiceOvers.REWARD_WEEKLY
                    elif not questId.startswith(CurrentNYConstants.NY_DAILY_QUESTS_PREFIX):
                        continue
                    for reward in getAllNonQuestBonuses(detailedRewards.get(questId) or {}):
                        if reward.getName() == SupportedTokenTypes.LOOTBOX_TOKEN:
                            rewardTokens = reward.getTokens() or {}
                            if machineLootboxToken in rewardTokens:
                                machineRewards.append(reward)
                                continue
                        questRewards.append(reward)

            if questRewards or machineRewards:
                self.__showWindow(mergeBonuses(questRewards) + mergeBonuses(machineRewards), voiceoverEvent)
            if machineRewards:
                showMachineNotification()
            return


class NewYearWeeklyRewardHandler(ServiceChannelHandler):
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, awardCtrl):
        super(NewYearWeeklyRewardHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        self.__leaderboardSeasonToRewards = {}

    def _needToShowAward(self, ctx):
        if not super(NewYearWeeklyRewardHandler, self)._needToShowAward(ctx):
            return False
        else:
            seasonId = self.__getRewardsSeasonID(ctx)
            if seasonId is None:
                return False
            self.__appendRewards(ctx, seasonId)
            return self.__canShow(seasonId)

    def __appendRewards(self, ctx, seasonId):
        invoiceData = self.__getProductInvoiceData(ctx)
        if invoiceData is None:
            return
        else:
            rewardsDict = invoiceData.get('data', {})
            for key, value in rewardsDict.iteritems():
                self.__leaderboardSeasonToRewards.setdefault(seasonId, []).append({key: value})

            return

    def _showAward(self, ctx):
        seasonId = self.__getRewardsSeasonID(ctx)
        if seasonId is not None:
            self.__processLeaderboardRewards(seasonId)
        return

    def __processLeaderboardRewards(self, seasonId):
        seasonRewards = self.__leaderboardSeasonToRewards.get(seasonId, [])
        rewards = getMergedBonusesFromDicts(seasonRewards)
        isFinalSeason = seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID
        self.__leaderboardSeasonToRewards.pop(seasonId, None)
        if not rewards:
            return
        else:
            rewards = self.__filterDuplicateStyles(rewards)
            rewards = self.__filterZeroTokens(rewards)
            if isFinalSeason:
                self.__presentCumulativeRewards(seasonId, rewards)
            else:
                showNYLeaderboardRewardWindow(rewards, seasonId)
            TamagotchiSysMsgHandler.sendRewardNotification(rewards, seasonId, isFinalSeason)
            return

    def __filterDuplicateStyles(self, rewards):
        styleIDs = {int(tokenID.split('_')[2]) for tokenID in rewards.get('tokens', {}).iterkeys() if tokenID.startswith(CUSTOMIZATION_PROGRESS_PREFIX) if tokenID.startswith(CUSTOMIZATION_PROGRESS_PREFIX)}
        if styleIDs:
            rewards['customizations'] = [ item for item in rewards.get('customizations', []) if not (item.get('custType') == 'style' and item.get('id') in styleIDs)
                                        ]
        return rewards

    def __filterZeroTokens(self, rewards):
        tokens = rewards.get('tokens', {})
        tokensToRemove = {tokenID for tokenID, data in tokens.iteritems() if tokenID.startswith(CUSTOMIZATION_PROGRESS_PREFIX) and data['count'] == 0 if tokenID.startswith(CUSTOMIZATION_PROGRESS_PREFIX) and data['count'] == 0}
        for token in tokensToRemove:
            tokens.pop(token)

        return rewards

    def __presentCumulativeRewards(self, seasonId, rewards):
        if registerLeaderboardTankReward(seasonId, rewards):
            self.__nyController.leaderboardTankReward.requestPresent()
            return
        LOG_ERROR('[NewYearWeeklyRewardHandler]: cumulative invoice without vehicle', seasonId)
        showNYLeaderboardRewardWindow(rewards, seasonId)

    def __canShow(self, seasonID):
        if seasonID == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            return True
        seasonRewards = self.__leaderboardSeasonToRewards.get(seasonID)
        if not seasonRewards:
            return True
        dogTagComponents = [ item for item in seasonRewards if 'dogTagComponents' in item ]
        if not dogTagComponents:
            return True
        if len(dogTagComponents) < 2:
            return False
        return True

    def __getRewardsSeasonID(self, ctx):
        invoiceData = self.__getProductInvoiceData(ctx)
        if invoiceData is None:
            return
        else:
            nyLeaderboardTag = self.__extractLeaderboardTag(invoiceData)
            if nyLeaderboardTag is None:
                return
            return self.__parseLeaderboardTag(nyLeaderboardTag)

    def __getProductInvoiceData(self, ctx):
        invoiceData = ctx[1].data
        if invoiceData and isinstance(invoiceData, dict) and invoiceData.get('assetType') == INVOICE_ASSET.PURCHASE:
            return invoiceData
        else:
            return

    def __extractLeaderboardTag(self, invoiceData):
        tags = invoiceData.get('tags', [])
        return findFirst(lambda tag: tag.startswith(NY_INVOICE_LEADERBOARD_REWARD_PREFIX), tags)

    def __parseLeaderboardTag(self, tag):
        if not tag.startswith(NY_INVOICE_LEADERBOARD_REWARD_PREFIX):
            LOG_ERROR('[NewYearWeeklyRewardHandler]: incorrect leaderboard tag format')
            return
        else:
            seasonKey = tag[len(NY_INVOICE_LEADERBOARD_REWARD_PREFIX):]
            if seasonKey.isdigit():
                return int(seasonKey)
            if seasonKey in NY_LEADERBOARD_CUMULATIVE_TAG_SUFFIXES:
                return NY_CUMULATIVE_LEADERBOARD_SEASON_ID
            LOG_ERROR('[NewYearWeeklyRewardHandler]: incorrect leaderboard tag format', tag)
            return


class NewYearPreorderRewardHandler(MultiTypeServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(NewYearPreorderRewardHandler, self).__init__((
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.battleResults.index()), awardCtrl)

    def _needToShowAward(self, ctx):
        if not super(NewYearPreorderRewardHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        completedQuestIDs = message.data.get('completedQuestIDs', set())
        return NY_PREORDER_REWARDS_QUEST_ID in completedQuestIDs

    def _showAward(self, ctx):
        _, message = ctx
        rewards = message.data.get('detailedRewards', {}).get(NY_PREORDER_REWARDS_QUEST_ID)
        if not rewards:
            return
        showNYPreorderRewardWindow(rewards)


def registerNewYearAwardControllerHandlers():
    registerAwardControllerHandlers((
     NewYearAtmosphereHandler,
     NewYearQuestHandler,
     NewYearWeeklyRewardHandler,
     NewYearPreorderRewardHandler))