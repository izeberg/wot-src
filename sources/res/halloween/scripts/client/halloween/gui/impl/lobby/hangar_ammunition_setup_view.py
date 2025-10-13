from frameworks.wulf import ViewFlags
from gui.impl.backport import TooltipData
from gui.impl.gen import R
from gui.impl.lobby.tank_setup.ammunition_setup.base_hangar import BaseHangarAmmunitionSetupView
from gui.impl.lobby.tank_setup.main_tank_setup.hangar import HangarMainTankSetupView
from gui.impl.lobby.tank_setup.tank_setup_builder import HangarTankSetupBuilder
from halloween.gui.impl.gen.view_models.views.lobby.ext_ammo_setup_view import ExtAmmoSetupView
from halloween.gui.impl.lobby.tooltips.ability_tooltip import AbilityTooltipView
from halloween.gui.sounds import playSound
from halloween.gui.sounds.sound_constants import CONSUMABLES_VIEW_EXIT, CONSUMABLES_VIEW_ENTER
from halloween.gui.impl.lobby.tank_setup.sub_view import HalloweenSetupSubView
from halloween.gui.impl.lobby.tank_setup.interactor import HalloweenInteractor
from halloween.gui.impl.lobby.hw_ammunition_panel_view import HWAmmunitionPanel, _CMD_ACCELERATION_ABILITY_KEY
from halloween.gui.halloween_gui_constants import HALLOWEEN_ABILITY_TOOLTIP, HALLOWEEN_MAIN_SHELL
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from account_helpers.settings_core.options import KeyboardSetting
from account_helpers.settings_core.settings_constants import CONTROLS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class HWHangarAmmunitionSetupView(BaseHangarAmmunitionSetupView):
    _VIEW_FLAG = ViewFlags.LOBBY_TOP_SUB_VIEW
    _VIEW_MODEL = ExtAmmoSetupView
    __settingsCore = dependency.descriptor(ISettingsCore)

    def changeGroupsPreset(self):
        self._ammunitionPanel.switchToNextPreset()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.halloween.mono.lobby.tooltips.ability_tooltip():
            abilityName = event.getArgument('abilityName')
            return AbilityTooltipView(abilityName=abilityName)
        return super(HWHangarAmmunitionSetupView, self).createToolTipContent(event, contentID)

    def _createBlur(self):
        return

    def _initialize(self, *args, **kwargs):
        self._ammunitionPanel.initialize()
        self._tankSetup.initialize()
        self.viewModel.setAccelerationKeyName(KeyboardSetting(_CMD_ACCELERATION_ABILITY_KEY).getKeyName())
        self._addListeners()
        playSound(CONSUMABLES_VIEW_ENTER)

    def _finalize(self):
        playSound(CONSUMABLES_VIEW_EXIT)
        super(HWHangarAmmunitionSetupView, self)._finalize()

    def _addListeners(self):
        super(HWHangarAmmunitionSetupView, self)._addListeners()
        self.viewModel.onSwitch += self.changeGroupsPreset
        self.__settingsCore.onSettingsApplied += self.__onSettingsApplied

    def _removeListeners(self):
        self.viewModel.onSwitch -= self.changeGroupsPreset
        self.__settingsCore.onSettingsApplied -= self.__onSettingsApplied
        super(HWHangarAmmunitionSetupView, self)._removeListeners()

    def _createMainTankSetup(self):
        return HangarMainTankSetupView(self.viewModel.tankSetup, self.__getTankSetupBuilder()(self._vehItem))

    def _createAmmunitionPanel(self):
        ctx = {'specializationClickable': True}
        return HWAmmunitionPanel(self.viewModel.ammunitionPanel, self._vehItem.getItem(), ctx=ctx)

    def _closeWindow(self):
        self._isClosed = True
        self.viewModel.setShow(False)
        self.destroyWindow()

    def _getBackportTooltipData(self, event):
        data = super(HWHangarAmmunitionSetupView, self)._getBackportTooltipData(event)
        if data.specialAlias in (TOOLTIPS_CONSTANTS.HANGAR_MODULE, TOOLTIPS_CONSTANTS.HANGAR_CARD_MODULE):
            return TooltipData(data.tooltip, data.isSpecial, HALLOWEEN_ABILITY_TOOLTIP, data.specialArgs, data.isWulfTooltip)
        if data.specialAlias == TOOLTIPS_CONSTANTS.TECH_MAIN_SHELL:
            return TooltipData(data.tooltip, data.isSpecial, HALLOWEEN_MAIN_SHELL, data.specialArgs, data.isWulfTooltip)
        return data

    def __getTankSetupBuilder(self):
        return HWTankSetupBuilder

    def __onSettingsApplied(self, diff):
        if CONTROLS.KEYBOARD in diff:
            with self.viewModel.transaction() as (model):
                model.setAccelerationKeyName(KeyboardSetting(_CMD_ACCELERATION_ABILITY_KEY).getKeyName())


class HWTankSetupBuilder(HangarTankSetupBuilder):
    __slots__ = ()

    def configureComponents(self, viewModel):
        components = []
        self.addComponent(components, viewModel.consumablesSetup, HalloweenSetupSubView, HalloweenInteractor(self._vehItem))
        return components