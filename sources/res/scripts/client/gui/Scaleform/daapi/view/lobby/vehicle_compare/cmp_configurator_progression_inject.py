from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.vehicle_compare.modifications_panel import CompareModificationsPanelView
from gui.impl.lobby.vehicle_compare.upgrades_panel import CompareUpgradesPanelView

class VehicleCompareConfiguratorProgressionInject(InjectComponentAdaptor):

    def update(self):
        self.getInjectView().update()

    def _makeInjectView(self):
        vehicle = cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicleItem()
        if vehicle.getItem().postProgression.isVehSkillTree():
            return CompareUpgradesPanelView()
        return CompareModificationsPanelView()