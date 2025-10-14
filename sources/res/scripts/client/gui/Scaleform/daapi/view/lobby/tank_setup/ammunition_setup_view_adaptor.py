from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView
from gui.shared.system_factory import collectAmmunitionSetupView
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

class AmmunitionSetupViewAdaptor(InjectComponentAdaptor):
    __hangarGuiCtrl = dependency.descriptor(IHangarGuiController)

    def __init__(self, ctx):
        super(AmmunitionSetupViewAdaptor, self).__init__()
        self.__ctx = ctx

    def _makeInjectView(self):
        currentPresetGetter = self.__hangarGuiCtrl.sfController.currentPresetGetter
        ammunitionPanelSetupCls = collectAmmunitionSetupView(currentPresetGetter.getAmmoSetupViewAlias())
        injectViewCls = ammunitionPanelSetupCls if ammunitionPanelSetupCls else HangarAmmunitionSetupView
        injectView = injectViewCls(**self.__ctx)
        self.__ctx = None
        return injectView