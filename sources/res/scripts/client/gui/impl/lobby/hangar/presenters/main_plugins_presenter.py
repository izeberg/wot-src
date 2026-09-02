from __future__ import absolute_import
import logging
from gui.impl.gen.view_models.views.lobby.hangar.main_plugins_model import MainPluginsModel
from gui.impl.pub.view_component import ViewComponent
_logger = logging.getLogger(__name__)

class MainPluginsPresenter(ViewComponent[MainPluginsModel]):

    def __init__(self):
        super(MainPluginsPresenter, self).__init__(model=MainPluginsModel)

    @property
    def viewModel(self):
        return super(MainPluginsPresenter, self).getViewModel()