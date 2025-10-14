from itertools import cycle
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
from gui.impl.gen import R
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController, GroupData
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import BaseAmmunitionBlocksController
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import ConsumablesBlock, ShellsBlock
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_shells_section import AmmunitionShellsSection
from gui.impl.lobby.tank_setup.ammunition_panel.base_view import BaseAmmunitionPanelView
from halloween.gui.impl.gen.view_models.views.lobby.ext_ammo_panel_view import ExtAmmoPanelView
from halloween.gui.impl.lobby.tooltips.ability_tooltip import AbilityTooltipView
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants
from halloween.gui.halloween_gui_constants import HALLOWEEN_ABILITY_TOOLTIP, HALLOWEEN_MAIN_SHELL, AmmoPanelSwitchPreset
from halloween.gui.halloween_account_settings import getSettings, AccountSettingsKeys, setSettings
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport import TooltipData
AMMO_SECTIONS_DEFAULT = (
 TankSetupConstants.SHELLS, HWTankSetupConstants.HW_CONSUMABLES)
AMMO_SECTIONS_ALTERNATIVE = (HWTankSetupConstants.HW_CONSUMABLES, TankSetupConstants.SHELLS)
_PRESET_AMMO_SECTIONS = {AmmoPanelSwitchPreset.PRESET_1: AMMO_SECTIONS_DEFAULT, 
   AmmoPanelSwitchPreset.PRESET_2: AMMO_SECTIONS_ALTERNATIVE, 
   'default': AMMO_SECTIONS_DEFAULT}
_CMD_KEYS_123 = ('CMD_AMMO_CHOICE_1', 'CMD_AMMO_CHOICE_2', 'CMD_AMMO_CHOICE_3')
_CMD_KEYS_456 = ('CMD_AMMO_CHOICE_4', 'CMD_AMMO_CHOICE_5', 'CMD_AMMO_CHOICE_6')
_CMD_ACCELERATION_ABILITY_KEY = 'CMD_CM_VEHICLE_SWITCH_AUTOROTATION'
_PRESET_MAP_AMMO_KEYS = {AmmoPanelSwitchPreset.PRESET_1: (
                                  _CMD_KEYS_123, _CMD_KEYS_456), 
   AmmoPanelSwitchPreset.PRESET_2: (
                                  _CMD_KEYS_456, _CMD_KEYS_123), 
   'default': (
             _CMD_KEYS_123, _CMD_KEYS_456)}
_TOOLTIPS_OVERRIDES = {TOOLTIPS_CONSTANTS.HANGAR_MODULE: HALLOWEEN_ABILITY_TOOLTIP, 
   TOOLTIPS_CONSTANTS.TECH_MAIN_SHELL: HALLOWEEN_MAIN_SHELL}

class HWAmmunitionPanelView(BaseAmmunitionPanelView):
    _VIEW_MODEL = ExtAmmoPanelView

    def _addListeners(self):
        super(HWAmmunitionPanelView, self)._addListeners()
        self.viewModel.onSwitch += self.changeGroupsPreset

    def _removeListeners(self):
        super(HWAmmunitionPanelView, self)._removeListeners()
        self.viewModel.onSwitch -= self.changeGroupsPreset

    def changeGroupsPreset(self):
        self._ammunitionPanel.switchToNextPreset()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.halloween.mono.lobby.tooltips.ability_tooltip():
            abilityName = event.getArgument('abilityName')
            return AbilityTooltipView(abilityName=abilityName)
        return super(HWAmmunitionPanelView, self).createToolTipContent(event, contentID)

    def _createAmmunitionPanel(self):
        return HWAmmunitionPanel(self.viewModel.ammunitionPanel, self.vehItem)

    def _getBackportTooltipData(self, event):
        data = super(HWAmmunitionPanelView, self)._getBackportTooltipData(event)
        override = _TOOLTIPS_OVERRIDES.get(data.specialAlias, data.specialAlias)
        return TooltipData(data.tooltip, data.isSpecial, override, data.specialArgs, data.isWulfTooltip)


class HWAmmunitionPanel(BaseAmmunitionPanel):

    def switchToNextPreset(self):
        self._controller.setNextPreset()

    def fullUpdateGroups(self):
        with self.viewModel.transaction() as (model):
            self._controller.createGroupsModels(model.getSectionGroups())
            model.setSyncInitiator((model.getSyncInitiator() + 1) % 1000)

    def _createAmmunitionGroupsController(self, vehicle):
        return HWHangarAmmunitionGroupsController(vehicle, ctx=self._ctx)

    def updateSectionsWithKeySettings(self):
        super(HWAmmunitionPanel, self).updateSectionsWithKeySettings()
        with self.viewModel.transaction() as (model):
            self._controller.updateGroupSectionModel(HWTankSetupConstants.HW_CONSUMABLES, model.getSectionGroups())
            model.setSyncInitiator((model.getSyncInitiator() + 1) % 1000)


class HWConsumablesBlock(ConsumablesBlock):

    def _getSectionName(self):
        return HWTankSetupConstants.HW_CONSUMABLES

    def _getKeySettings(self):
        return _PRESET_MAP_AMMO_KEYS.get(getSettings(AccountSettingsKeys.AMMO_PANEL_PRESET), 'default')[1]


class HWShellsBlock(ShellsBlock):

    def _getKeySettings(self):
        return _PRESET_MAP_AMMO_KEYS.get(getSettings(AccountSettingsKeys.AMMO_PANEL_PRESET), 'default')[0]


class HWAmmunitionBlocksController(BaseAmmunitionBlocksController):

    @tabUpdateFunc(TankSetupConstants.SHELLS)
    def _updateShells(self, viewModel, isFirst=False):
        HWShellsBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    @tabUpdateFunc(HWTankSetupConstants.HW_CONSUMABLES)
    def _updateHWConsumables(self, viewModel, isFirst=False):
        HWConsumablesBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    def _createViewModel(self, name):
        if name == TankSetupConstants.SHELLS:
            return AmmunitionShellsSection()
        return AmmunitionItemsSection()


class HWHangarAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__ = ('_presetCycle', )
    _guiLoader = dependency.descriptor(IGuiLoader)

    def __init__(self, vehicle, autoCreating=True, ctx=None):
        super(HWHangarAmmunitionGroupsController, self).__init__(vehicle, autoCreating=autoCreating, ctx=ctx)
        self._presetCycle = cycle(AmmoPanelSwitchPreset.ALL)

    def finalize(self):
        super(HWHangarAmmunitionGroupsController, self).finalize()
        self._presetCycle = None
        return

    def setNextPreset(self):
        currentPreset = self._getPreset()
        nextPreset = next((preset for preset in self._presetCycle if preset != currentPreset), AmmoPanelSwitchPreset.PRESET_1)
        self._setPreset(nextPreset)
        ammoPanels = [
         R.views.halloween.mono.lobby.ammunition_setup(), R.views.lobby.tanksetup.AmmunitionPanel()]
        views = self._guiLoader.windowsManager.findViews(lambda view: view.layoutID in ammoPanels)
        for view in views:
            view._ammunitionPanel.fullUpdateGroups()

    def _getGroups(self):
        if self._vehicle is None:
            return []
        else:
            ammoSections = _PRESET_AMMO_SECTIONS.get(self._getPreset(), 'default')
            groups = (
             GroupData(AmmunitionPanelConstants.EQUIPMENT_AND_SHELLS, ammoSections),)
            return groups

    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        return HWAmmunitionBlocksController(vehicle, ctx=ctx)

    @staticmethod
    def _setPreset(presetNum):
        setSettings(AccountSettingsKeys.AMMO_PANEL_PRESET, presetNum)

    @staticmethod
    def _getPreset():
        return getSettings(AccountSettingsKeys.AMMO_PANEL_PRESET)