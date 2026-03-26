package net.wg.gui.battle.views.widgetsPanel.settings
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.BATTLE_WIDGETS_CONSTS;
   import net.wg.gui.battle.views.widgetsPanel.ChargeShotWidget;
   import net.wg.gui.battle.views.widgetsPanel.ChargeableBurstWidget;
   import net.wg.gui.battle.views.widgetsPanel.ConcentrationWidget;
   import net.wg.gui.battle.views.widgetsPanel.LowChargeShotWidget;
   import net.wg.gui.battle.views.widgetsPanel.PillboxSiegeWidget;
   import net.wg.gui.battle.views.widgetsPanel.PowerWidget;
   import net.wg.gui.battle.views.widgetsPanel.PropellantGunWidget;
   import net.wg.gui.battle.views.widgetsPanel.RechargeableNitroWidget;
   import net.wg.gui.battle.views.widgetsPanel.RocketAcceleratorWidget;
   import net.wg.gui.battle.views.widgetsPanel.StagedJetBoostersWidget;
   import net.wg.gui.battle.views.widgetsPanel.StanceDanceFightWidget;
   import net.wg.gui.battle.views.widgetsPanel.StanceDanceTurboWidget;
   import net.wg.gui.battle.views.widgetsPanel.StationaryReloadWidget;
   import net.wg.gui.battle.views.widgetsPanel.SupportWeaponWidget;
   import net.wg.gui.battle.views.widgetsPanel.TargetDesignatorWidget;
   import net.wg.gui.battle.views.widgetsPanel.TemperatureGunHeatZonesWidget;
   import net.wg.gui.battle.views.widgetsPanel.TemperatureGunOverheatWidget;
   import net.wg.gui.battle.views.widgetsPanel.WheeledDashWidget;
   
   public class WidgetSettings
   {
      
      private static var _instance:WidgetSettings = null;
       
      
      private var _settingsList:Dictionary;
      
      public function WidgetSettings()
      {
         this._settingsList = new Dictionary();
         super();
         if(_instance != null)
         {
            throw new Error("Singleton WidgetSettings can only be accessed through WidgetSettings.instance");
         }
         this._settingsList[BATTLE_WIDGETS_CONSTS.ROCKET_ACCELERATOR] = new WidgetProperties(Linkages.ROCKET_ACCELERATOR,RocketAcceleratorWidget,BATTLE_VIEW_ALIASES.ROCKET_ACCELERATOR_INDICATOR);
         this._settingsList[BATTLE_WIDGETS_CONSTS.RECHARGEABLE_NITRO] = new WidgetProperties(Linkages.RECHARGEABLE_NITRO,RechargeableNitroWidget,BATTLE_VIEW_ALIASES.RECHARGEABLE_NITRO_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.CONCENTRATION] = new WidgetProperties(Linkages.CONCENTRATION,ConcentrationWidget,BATTLE_VIEW_ALIASES.CONCENTRATION_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.POWER] = new WidgetProperties(Linkages.POWER,PowerWidget,BATTLE_VIEW_ALIASES.POWER_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.SUPPORT_WEAPON] = new WidgetProperties(Linkages.SUPPORT_WEAPON,SupportWeaponWidget,BATTLE_VIEW_ALIASES.SUPPORT_WEAPON);
         this._settingsList[BATTLE_WIDGETS_CONSTS.PILLBOX_SIEGE] = new WidgetProperties(Linkages.PILLBOX_SIEGE,PillboxSiegeWidget,BATTLE_VIEW_ALIASES.PILLBOX_SIEGE_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.CHARGE_SHOT] = new WidgetProperties(Linkages.CHARGE_SHOT,ChargeShotWidget,BATTLE_VIEW_ALIASES.CHARGE_SHOT_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.STANCE_DANCE_FIGHT] = new WidgetProperties(Linkages.STANCE_DANCE_FIGHT,StanceDanceFightWidget,BATTLE_VIEW_ALIASES.STANCE_DANCE_WIDGET_FIGHT);
         this._settingsList[BATTLE_WIDGETS_CONSTS.STANCE_DANCE_TURBO] = new WidgetProperties(Linkages.STANCE_DANCE_TURBO,StanceDanceTurboWidget,BATTLE_VIEW_ALIASES.STANCE_DANCE_WIDGET_TURBO);
         this._settingsList[BATTLE_WIDGETS_CONSTS.TARGET_DESIGNATOR_WIDGET] = new WidgetProperties(Linkages.TARGET_DESIGNATOR_WIDGET,TargetDesignatorWidget,BATTLE_VIEW_ALIASES.TARGET_DESIGNATOR_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.CHARGEABLE_BURST] = new WidgetProperties(Linkages.CHARGEABLE_BURST,ChargeableBurstWidget,BATTLE_VIEW_ALIASES.CHARGEABLE_BURST_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.STATIONARY_RELOAD] = new WidgetProperties(Linkages.STATIONARY_RELOAD,StationaryReloadWidget,BATTLE_VIEW_ALIASES.STATIONARY_RELOAD_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.TEMPERATURE_GUN_OVERHEAT] = new WidgetProperties(Linkages.TEMPERATURE_GUN_OVERHEAT,TemperatureGunOverheatWidget,BATTLE_VIEW_ALIASES.TEMPERATURE_GUN_OVERHEAT_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.TEMPERATURE_GUN_HEAT_ZONES] = new WidgetProperties(Linkages.TEMPERATURE_GUN_HEAT_ZONES,TemperatureGunHeatZonesWidget,BATTLE_VIEW_ALIASES.TEMPERATURE_GUN_HEAT_ZONES_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.STAGED_JET_BOOSTERS] = new WidgetProperties(Linkages.STAGED_JET_BOOSTERS,StagedJetBoostersWidget,BATTLE_VIEW_ALIASES.STAGED_JET_BOOSTERS_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.WHEELED_DASH] = new WidgetProperties(Linkages.WHEELED_DASH,WheeledDashWidget,BATTLE_VIEW_ALIASES.WHEELED_DASH_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.PROPELLANT_GUN] = new WidgetProperties(Linkages.PROPELLANT_GUN,PropellantGunWidget,BATTLE_VIEW_ALIASES.PROPELLANT_GUN_WIDGET);
         this._settingsList[BATTLE_WIDGETS_CONSTS.LOW_CHARGE_SHOT] = new WidgetProperties(Linkages.LOW_CHARGE_SHOT,LowChargeShotWidget,BATTLE_VIEW_ALIASES.LOW_CHARGE_SHOT_WIDGET);
      }
      
      public static function get instance() : WidgetSettings
      {
         if(_instance == null)
         {
            _instance = new WidgetSettings();
         }
         return _instance;
      }
      
      public function getProperties(param1:String) : WidgetProperties
      {
         if(this._settingsList.hasOwnProperty(param1))
         {
            return this._settingsList[param1];
         }
         return null;
      }
   }
}
