from helpers import dependency
from one_time_gift.gui.impl.gen.view_models.views.lobby.one_time_gift_view_model import MainViews
from one_time_gift.gui.impl.lobby.meta_view.sub_view_base import SubViewBase
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
_START_SOUND_EVENT = 'gui_reward_screen_general'

class WDRCompensationView(SubViewBase):
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)

    @property
    def viewId(self):
        return MainViews.WDR_REWARD_COMPENSATION

    def initialize(self, onConfirmCallback=None, onCloseCallback=None, onErrorCallback=None):
        super(WDRCompensationView, self).initialize(onConfirmCallback, onCloseCallback, onErrorCallback)
        self.parentView.soundManager.playSound(_START_SOUND_EVENT)

    def _getEvents(self):
        return super(WDRCompensationView, self)._getEvents() + (
         (
          self.getViewModel().onClose, self._onClose),)