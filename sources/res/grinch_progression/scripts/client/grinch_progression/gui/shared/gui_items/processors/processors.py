import BigWorld
from typing import Any, Dict
from account_helpers.settings_core.settings_constants import OnceOnlyHints
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.processors import Processor, makeError
from gui.shared.notifications import NotificationPriorityLevel
from messenger.formatters.service_channel import QuestAchievesFormatter
from grinch_progression.gui.shared.event_dispatcher import showGPStyleRewardNotification, showAttachmentRewardWindow
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.customization import ICustomizationService
from gui.shared.gui_items import getItemTypeID
from items.components.c11n_constants import Rarity
from grinch.gui.grinch_gui_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.system_messages import ISystemMessages
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN
NOTIFICATION_RARITY_RANGE = [
 Rarity.RARE]

class OpenStepForChapter(Processor):
    c11n = dependency.descriptor(ICustomizationService)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self, chapterID, stepID):
        super(OpenStepForChapter, self).__init__()
        self._chapterID = chapterID
        self._stepID = stepID

    def _request(self, callback):
        BigWorld.player().GrinchProgressionAccountComponent.openStep(self._chapterID, self._stepID, lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext))

    def _errorHandler(self, code, errStr='', ctx=None):
        SystemMessages.pushMessage(text=backport.text(R.strings.grinch_progression.notification.reward.error()), priority=NotificationPriorityLevel.MEDIUM, type=SystemMessages.SM_TYPE.Error)
        return makeError(errStr, SystemMessages.SM_TYPE.Error)

    def _getItemsForNotification(self, ctx=None):
        if ctx is None:
            return {}
        else:
            result = {key:value for key, value in ctx.iteritems() if key not in ('version',
                                                                                 'tokens') if key not in ('version',
                                                                                                          'tokens')}
            if BATTLE_BONUS_X5_TOKEN in ctx.get('tokens', {}):
                result['tokens'] = {BATTLE_BONUS_X5_TOKEN: ctx['tokens'][BATTLE_BONUS_X5_TOKEN]}
            return result

    def _successHandler(self, code, ctx=None):
        _ctx = self._getItemsForNotification(ctx)
        for customization in _ctx.get('customizations', []):
            custType = customization.get('custType')
            if custType == 'attachment':
                attachment = self.c11n.getItemByID(getItemTypeID(custType), customization.get('id'))
                if attachment.rarity in Rarity.FILTERABLE:
                    isFirstEntry = not self.__settingsCore.serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.NEW_C11N_SECTION_HINT)
                    showAttachmentRewardWindow(attachment, isFirstEntry)
            if custType == 'style':
                style = self.c11n.getItemByID(getItemTypeID(custType), customization.get('id'))
                if not style.is3D:
                    showGPStyleRewardNotification({'bonuses': {'customizations': [customization]}})

        for dossier in _ctx.get('dossier', {}).itervalues():
            for dossierRecord in dossier.iterkeys():
                self.__systemMessages.proto.serviceChannel.pushClientMessage({'medal': dossierRecord[1]}, SCH_CLIENT_MSG_TYPE.GRINCH_CONGRATULATIONS_MESSAGE)

        fmt = QuestAchievesFormatter.formatQuestAchieves(_ctx, False)
        if fmt is not None:
            header = backport.text(R.strings.grinch_progression.notification.board.rewardClaim.header())
            SystemMessages.pushMessage(fmt, type=SystemMessages.SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.MEDIUM, messageData={'header': header})
        return super(OpenStepForChapter, self)._successHandler(code, ctx)