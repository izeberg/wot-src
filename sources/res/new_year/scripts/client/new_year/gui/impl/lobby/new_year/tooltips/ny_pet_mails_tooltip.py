from frameworks.wulf import ViewSettings
from helpers import dependency
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_pet_mails_tooltip_model import NyPetMailsTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from new_year.skeletons.new_year import ITamagotchiDataProvider

class NyPetMailsTooltip(ViewImpl):
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)

    def __init__(self):
        settings = ViewSettings(R.views.new_year.lobby.new_year.tooltips.NyPetMailsTooltip())
        settings.model = NyPetMailsTooltipModel()
        super(NyPetMailsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyPetMailsTooltip, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self._dataProvider.onGiftCountUpdated, self.__onGiftCountUpdated),)

    def _onLoading(self, *args, **kwargs):
        self.__onGiftCountUpdated()
        super(NyPetMailsTooltip, self)._onLoading(*args, **kwargs)

    def __onGiftCountUpdated(self):
        with self.getViewModel().transaction() as (tx):
            tx.setMailsAmount(self._dataProvider.playerInfo.giftCount)
            tx.setNextMailTime(self._dataProvider.getGiftDelay())