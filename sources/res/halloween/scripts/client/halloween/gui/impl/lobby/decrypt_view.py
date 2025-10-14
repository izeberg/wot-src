import typing
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.backport import createTooltipData, BackportTooltipWindow
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.shared import g_eventBus, events
from halloween.gui import halloween_account_settings
from halloween.gui.halloween_account_settings import AccountSettingsKeys
from halloween.gui.impl.gen.view_models.views.lobby.decrypt_view_model import DecryptViewModel
from halloween.gui.impl.lobby.hw_helpers import fillRewards
from halloween.gui.sounds import playSound
from halloween.gui.sounds.sound_constants import META_QUANTUM_VO_ON, META_QUANTUM_VO_OFF, META_QUANTUM_SCREEN_ENTER, META_QUANTUM_SCREEN_EXIT
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency
from ids_generators import SequenceIDGenerator
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from halloween.gui.game_control.halloween_artefacts_controller import Artefact
_R_BACKPORT_TOOLTIP = R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent()
_SOUND_TAG = 'sound'

class DecryptView(ViewImpl):
    _guiLoader = dependency.descriptor(IGuiLoader)
    _hwArtefactsCtrl = dependency.descriptor(IHalloweenArtefactsController)
    _hwController = dependency.descriptor(IHalloweenController)
    _MAX_BONUSES_IN_VIEW = 5

    def __init__(self, artefactID, isRewardScreen=False):
        settings = ViewSettings(R.views.halloween.mono.lobby.decrypt())
        settings.model = DecryptViewModel()
        super(DecryptView, self).__init__(settings)
        self.__artefactID = artefactID
        self.__isRewardScreen = isRewardScreen
        self.__bonusCache = {}
        self.__idGen = SequenceIDGenerator()

    def createToolTip(self, event):
        if event.contentID == _R_BACKPORT_TOOLTIP:
            tooltipId = event.getArgument('tooltipId')
            bonus = self.__bonusCache.get(tooltipId)
            if bonus:
                window = BackportTooltipWindow(createTooltipData(tooltip=bonus.tooltip, isSpecial=bonus.isSpecial, specialAlias=bonus.specialAlias, specialArgs=bonus.specialArgs, isWulfTooltip=bonus.isWulfTooltip), self.getParentWindow(), event=event)
                window.load()
                return window
        return super(DecryptView, self).createToolTip(event)

    @property
    def viewModel(self):
        return super(DecryptView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(DecryptView, self)._onLoading()
        artefactIndex = self._hwArtefactsCtrl.getIndex(self.__artefactID)
        playSound(META_QUANTUM_SCREEN_ENTER.format(artefactIndex))
        self.__fillViewModel()

    def _onShown(self):
        g_eventBus.handleEvent(events.ViewReadyEvent(self.layoutID))

    def _finalize(self):
        artefactIndex = self._hwArtefactsCtrl.getIndex(self.__artefactID)
        playSound(META_QUANTUM_SCREEN_EXIT.format(artefactIndex))
        if self.__isRewardScreen:
            hangarView = self._guiLoader.windowsManager.getViewByLayoutID(R.views.halloween.mono.lobby.hangar())
            if hangarView is not None:
                hangarView.selectNextSlide()
        super(DecryptView, self)._finalize()
        return

    def _getEvents(self):
        return [
         (
          self.viewModel.onAffirmation, self.__onClose),
         (
          self.viewModel.onMuted, self.__onMuted)]

    def __onClose(self):
        self.destroyWindow()

    def __onMuted(self):
        isMuted = halloween_account_settings.getSettings(AccountSettingsKeys.ARTEFACT_VOICEOVER_MUTED)
        newStateMute = not isMuted
        halloween_account_settings.setSettings(AccountSettingsKeys.ARTEFACT_VOICEOVER_MUTED, newStateMute)
        self.viewModel.setIsMuted(newStateMute)
        artefactIndex = self._hwArtefactsCtrl.getIndex(self.__artefactID)
        if newStateMute:
            playSound(META_QUANTUM_VO_OFF.format(artefactIndex))
        else:
            playSound(META_QUANTUM_VO_ON.format(artefactIndex))

    def __fillViewModel(self):
        artefact = self._hwArtefactsCtrl.getArtefact(self.__artefactID)
        if artefact is None:
            return
        else:
            with self.viewModel.transaction() as (tx):
                tx.setId(self.__artefactID)
                tx.setName(artefact.questConditions.name)
                artefactIndex = self._hwArtefactsCtrl.getIndex(self.__artefactID)
                tx.setIndex(artefactIndex)
                isMuted = halloween_account_settings.getSettings(AccountSettingsKeys.ARTEFACT_VOICEOVER_MUTED)
                tx.setIsMuted(isMuted)
                if self._isArtefactSoundEnabled() and not isMuted:
                    playSound(META_QUANTUM_VO_ON.format(artefactIndex))
                tx.setIsTransition(self.__isRewardScreen and (self._hwArtefactsCtrl.isArtefactHasTwitchConCertificate(self.__artefactID) or len(self._hwArtefactsCtrl.getRareAttachmentsFromArtefact(self.__artefactID)) > 0 or self._hwArtefactsCtrl.isProgressCompleted() or self._hwArtefactsCtrl.isFinalArtefact(artefact)))
                self.__bonusCache = fillRewards(artefact, tx.getRewards(), self._MAX_BONUSES_IN_VIEW, self.__idGen)
                for type in artefact.artefactTypes:
                    tx.getTypes().addString(type)

                tx.getTypes().invalidate()
            return

    def _isArtefactSoundEnabled(self):
        artefact = self._hwArtefactsCtrl.getArtefact(self.__artefactID)
        if artefact is None:
            return False
        else:
            return _SOUND_TAG in artefact.artefactTypes


class DecryptWindow(LobbyNotificationWindow):

    def __init__(self, artefactID, isRewardScreen=None, parent=None):
        super(DecryptWindow, self).__init__(wndFlags=WindowFlags.WINDOW_FULLSCREEN | WindowFlags.WINDOW, content=DecryptView(artefactID, isRewardScreen), parent=parent)
        self._args = (
         artefactID, isRewardScreen)

    def isParamsEqual(self, *args):
        return self._args == args