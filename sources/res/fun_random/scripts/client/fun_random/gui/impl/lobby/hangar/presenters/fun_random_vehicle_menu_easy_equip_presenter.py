from __future__ import absolute_import
from gui.prb_control.entities.base.listener import IPrbListener
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel

class FunRandomEasyEquipMenuEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):

    def _getState(self):
        return VehicleMenuModel.UNAVAILABLE

    def onNavigate(self):
        pass