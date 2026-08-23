from gui.impl.lobby.gf_notifications.notification_base import NotificationBase
from journey_marathon.gui.impl.gen.view_models.views.lobby.notifications.daily_reward_view_model import DailyRewardViewModel

class JMDailyRewardNotification(NotificationBase):

    def __init__(self, resId, *args, **kwargs):
        super(JMDailyRewardNotification, self).__init__(resId, DailyRewardViewModel(), *args, **kwargs)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _update(self):
        with self.viewModel.transaction() as (tx):
            tx.setAmount(self._getPayload()['count'])
            tx.setIsPopUp(self._isPopUp)