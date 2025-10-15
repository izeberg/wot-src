from gui.impl.pub.view_component import ViewComponent
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController
from helpers import dependency
from halloween.gui.impl.gen.view_models.views.lobby.widgets.reward_path_card_view_model import RewardPathCardViewModel
from halloween.gui.shared.event_dispatcher import showRewardPathView
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController

class RewardPathCardPresenter(ViewComponent[RewardPathCardViewModel]):
    _hwArtefactsCtrl = dependency.descriptor(IHalloweenArtefactsController)
    _hwTwitchCtrl = dependency.descriptor(IHalloweenTwitchConController)

    def __init__(self):
        super(RewardPathCardPresenter, self).__init__(model=RewardPathCardViewModel)

    def _onLoading(self, *args, **kwargs):
        super(RewardPathCardPresenter, self)._onLoading()
        self.__fillMetaWidget()

    def _getEvents(self):
        return (
         (
          self._hwArtefactsCtrl.onArtefactStatusUpdated, self.__onArtefactStatusUpdated),
         (
          self.getViewModel().onClick, self.__onClick),
         (
          self._hwTwitchCtrl.onCertificateCountUpdated, self.__cerfCountUpdate))

    def __onClick(self):
        showRewardPathView()

    def __fillMetaWidget(self):
        with self.getViewModel().transaction() as (tx):
            maxProgress = self._hwArtefactsCtrl.getMaxArtefactsProgress()
            currentProgress = self._hwArtefactsCtrl.getCurrentArtefactProgress()
            tx.setMaxProgress(maxProgress)
            tx.setCurrentProgress(min(currentProgress, maxProgress))
            tx.setIsCompleted(currentProgress >= maxProgress)
            tx.setCertificates(self._hwTwitchCtrl.getCertificateCount())

    def __onArtefactStatusUpdated(self, _):
        self.__fillMetaWidget()

    def __cerfCountUpdate(self):
        self.getViewModel().setCertificates(self._hwTwitchCtrl.getCertificateCount())