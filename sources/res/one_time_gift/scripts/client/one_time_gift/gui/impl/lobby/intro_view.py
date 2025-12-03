import logging
from helpers import dependency
from shared_utils import safeCall
from one_time_gift.gui.impl.gen.view_models.views.lobby.intro_view_model import IntroViewModel
from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
from one_time_gift.gui.impl.lobby.meta_view.sub_view_base import SubViewBase
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
_logger = logging.getLogger(__name__)

class IntroView(SubViewBase):
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)

    def __init__(self, viewModel, parentView):
        super(IntroView, self).__init__(viewModel, parentView)
        self.__showAnimation = False

    @property
    def viewId(self):
        return MainViews.INTRO

    @property
    def viewModel(self):
        return super(IntroView, self).getViewModel()

    def initialize(self, onConfirmCallback=None, onCloseCallback=None, onErrorCallback=None, showAnimation=False):
        _logger.debug('IntroView::initialize')
        super(IntroView, self).initialize(onConfirmCallback, onCloseCallback, onErrorCallback)
        self.__showAnimation = showAnimation
        self.__updateViewModel()

    def _getEvents(self):
        return super(IntroView, self)._getEvents() + (
         (
          self.viewModel.onContinue, self.__onContinue),
         (
          self.viewModel.onClose, self._onClose),
         (
          self.__oneTimeGiftController.onSettingsChanged, self.__onSettingsChanged),
         (
          self.__oneTimeGiftController.onEntryPointUpdated, self.__onSettingsChanged))

    def __onContinue(self):
        _logger.debug('IntroView::__onContinue')
        safeCall(self._onConfirmCallback)

    def __onSettingsChanged(self, *_, **__):
        _logger.debug('IntroView::__onSettingsChanged')
        error = self.__oneTimeGiftController.getAvailabilityError()
        if error is not None:
            safeCall(self._onErrorCallback, error=error)
            return
        else:
            self.__updateViewModel()
            return

    def __updateViewModel(self):
        endTime = self.__oneTimeGiftController.getEndTime()
        self.viewModel.setEndTime(endTime)
        self.viewModel.setShowAnimation(self.__showAnimation)