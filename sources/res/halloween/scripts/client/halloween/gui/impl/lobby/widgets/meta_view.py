import typing
from adisp import adisp_process
from frameworks.wulf import ViewEvent, View, WindowLayer
from gui.impl.backport import createTooltipData, BackportTooltipWindow
from gui.impl.common.fade_manager import UseFading
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.meta_view_model import MetaViewModel
from halloween.gui.impl.lobby.hw_helpers import getArtefactState, fillProminentBonus, PROMINENT_REWARD_TOOLTIP_ID
from halloween.gui.impl.lobby.tooltips.event_mission_tooltip import MissionsTooltip
from halloween.gui.shared.event_dispatcher import showDecryptWindowView, showBundleWindow
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from helpers import dependency
if typing.TYPE_CHECKING:
    from halloween.gui.game_control.halloween_artefacts_controller import Artefact
_R_BACKPORT_TOOLTIP = R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent()

class MetaWidgetView(ViewComponent[MetaViewModel]):
    _hwArtifactsCtrl = dependency.descriptor(IHalloweenArtefactsController)

    def __init__(self, parent=None):
        super(MetaWidgetView, self).__init__(R.aliases.halloween.shared.Meta(), MetaViewModel)
        self.__artefactID = None
        self.__parent = parent
        self.__prominentBonus = None
        return

    def createToolTip(self, event):
        if event.contentID == _R_BACKPORT_TOOLTIP:
            tooltipId = event.getArgument('tooltipId')
            if tooltipId == PROMINENT_REWARD_TOOLTIP_ID and self.__prominentBonus is not None:
                window = BackportTooltipWindow(createTooltipData(tooltip=self.__prominentBonus.tooltip, isSpecial=self.__prominentBonus.isSpecial, specialAlias=self.__prominentBonus.specialAlias, specialArgs=self.__prominentBonus.specialArgs, isWulfTooltip=self.__prominentBonus.isWulfTooltip), self.getParentWindow(), event=event)
                window.load()
                return window
        return super(MetaWidgetView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.halloween.mono.lobby.tooltips.mission_tooltip():
            return MissionsTooltip(selectedArtefactID=self.__artefactID, isHangar=True)
        return super(MetaWidgetView, self).createToolTipContent(event, contentID)

    @property
    def viewModel(self):
        return super(MetaWidgetView, self).getViewModel()

    def updateData(self, selectedArtefactIndex):
        with self.viewModel.transaction() as (tx):
            artefactID = self._hwArtifactsCtrl.getArtefactIDByIndex(selectedArtefactIndex)
            self.__artefactID = artefactID
            artefact = self._hwArtifactsCtrl.getArtefact(artefactID)
            if artefact is None:
                return
            tx.setKeys(self._hwArtifactsCtrl.getArtefactKeyQuantity())
            tx.setId(artefactID)
            tx.setIndex(selectedArtefactIndex)
            tx.setName(artefact.questConditions.name)
            tx.setDescription(artefact.questConditions.description.replace('\\n', '\n'))
            tx.setDecodePrice(artefact.decodePrice.amount)
            tx.setSkipPrice(artefact.skipPrice.amount)
            tx.setState(getArtefactState(artefactID))
            tx.getTypes().clear()
            for type in artefact.artefactTypes:
                tx.getTypes().addString(type)

            tx.getTypes().invalidate()
            self.__prominentBonus = fillProminentBonus(artefactID, artefact.bonusRewards, tx.bonus)
            tx.setHasProminentReward(self.__prominentBonus is not None)
        return

    def _finalize(self):
        self.__parent = None
        super(MetaWidgetView, self)._finalize()
        return

    def _getEvents(self):
        return [
         (
          self.viewModel.onView, self.__onView),
         (
          self.viewModel.onSkip, self.__onSkip),
         (
          self.viewModel.onDecrypt, self.__onDecrypt),
         (
          self.viewModel.onSlideToNext, self.__onSlideToNext),
         (
          self._hwArtifactsCtrl.onArtefactKeyUpdated, self.__onKeyUpdated)]

    def __onKeyUpdated(self):
        self.viewModel.setKeys(self._hwArtifactsCtrl.getArtefactKeyQuantity())

    def __onSlideToNext(self):
        if self.__parent is not None:
            self.__parent.updateSlide()
        return

    @UseFading(layer=WindowLayer.OVERLAY, waitForLayoutReady=R.views.halloween.mono.lobby.decrypt())
    def __onView(self):
        showDecryptWindowView(self.__artefactID)

    def __onSkip(self):
        artefact = self._hwArtifactsCtrl.getArtefact(self.__artefactID)
        if artefact.skipPrice.amount > self._hwArtifactsCtrl.getArtefactKeyQuantity():
            showBundleWindow(artefactID=self.__artefactID)
            return
        self.__skipArtefact()

    @adisp_process
    def __skipArtefact(self):
        yield self._hwArtifactsCtrl.openArtefact(self.__artefactID, True)

    def __onDecrypt(self):
        artefact = self._hwArtifactsCtrl.getArtefact(self.__artefactID)
        if artefact.decodePrice.amount > self._hwArtifactsCtrl.getArtefactKeyQuantity():
            showBundleWindow(artefactID=self.__artefactID)
            return
        self.__decryptArtefact()

    @adisp_process
    def __decryptArtefact(self):
        yield self._hwArtifactsCtrl.openArtefact(self.__artefactID, False)