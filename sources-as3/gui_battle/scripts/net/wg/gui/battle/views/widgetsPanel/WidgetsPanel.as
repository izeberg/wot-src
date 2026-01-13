package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.Sprite;
   import flash.utils.Dictionary;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.BATTLE_WIDGETS_CONSTS;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.infrastructure.base.meta.IWidgetsPanelMeta;
   import net.wg.infrastructure.base.meta.impl.WidgetsPanelMeta;
   
   public class WidgetsPanel extends WidgetsPanelMeta implements IWidgetsPanelMeta
   {
      
      private static const MECHANICS_SNIPER_RIGHT_X:int = 190;
      
      private static const MECHANICS_SNIPER_RIGHT_Y:int = 190;
      
      private static const MECHANICS_ARCADE_RIGHT_X:int = 150;
      
      private static const MECHANICS_ARCADE_RIGHT_Y:int = 100;
      
      private static const MECHANICS_SNIPER_LEFT_X:int = -190;
      
      private static const MECHANICS_SNIPER_LEFT_Y:int = 190;
      
      private static const MECHANICS_ARCADE_LEFT_X:int = -150;
      
      private static const MECHANICS_ARCADE_LEFT_Y:int = 100;
      
      private static const INFO_OFFSET:int = 47;
       
      
      public var mechanicsSlotLeft:Sprite;
      
      public var mechanicsSlotRight:Sprite;
      
      public var infoSlot:Sprite;
      
      public var centralSlot:Sprite;
      
      private var _crosshairType:int = 1;
      
      private var _componentsStorage:Dictionary;
      
      private var _isPlayer:Boolean = true;
      
      private var _isReplay:Boolean = false;
      
      private var _isVisible:Boolean = true;
      
      public function WidgetsPanel()
      {
         this._componentsStorage = new Dictionary();
         super();
         this.mechanicsSlotLeft.visible = false;
         this.mechanicsSlotRight.visible = false;
         this.infoSlot.visible = false;
         this.centralSlot.visible = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            if(this._crosshairType == CROSSHAIR_VIEW_ID.ARCADE)
            {
               this.mechanicsSlotRight.x = MECHANICS_ARCADE_RIGHT_X;
               this.mechanicsSlotRight.y = MECHANICS_ARCADE_RIGHT_Y;
               this.mechanicsSlotLeft.x = MECHANICS_ARCADE_LEFT_X;
               this.mechanicsSlotLeft.y = MECHANICS_ARCADE_LEFT_Y;
            }
            else if(this._crosshairType == CROSSHAIR_VIEW_ID.SNIPER)
            {
               this.mechanicsSlotRight.x = MECHANICS_SNIPER_RIGHT_X;
               this.mechanicsSlotRight.y = MECHANICS_SNIPER_RIGHT_Y;
               this.mechanicsSlotLeft.x = MECHANICS_SNIPER_LEFT_X;
               this.mechanicsSlotLeft.y = MECHANICS_SNIPER_LEFT_Y;
            }
            this.infoSlot.x = INFO_OFFSET;
            this.infoSlot.y = INFO_OFFSET;
         }
         var _loc1_:BaseVehicleMechanicsWidget = null;
         if(isInvalid(InvalidationType.DATA))
         {
            for each(_loc1_ in this._componentsStorage)
            {
               _loc1_.isPlayer = this._isPlayer;
               _loc1_.isReplay = this._isReplay;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.mechanicsSlotRight = null;
         this.mechanicsSlotLeft = null;
         this.infoSlot = null;
         this.centralSlot = null;
         App.utils.data.cleanupDynamicObject(this._componentsStorage);
         this._componentsStorage = null;
         super.onDispose();
      }
      
      public function addWidget(param1:String) : void
      {
         var _loc2_:Sprite = null;
         var _loc3_:String = null;
         var _loc4_:Class = null;
         var _loc5_:String = null;
         var _loc6_:BaseVehicleMechanicsWidget = null;
         if(BATTLE_WIDGETS_CONSTS.MECHANICS_WIDGETS_RIGHT.indexOf(param1) > -1)
         {
            _loc2_ = this.mechanicsSlotRight;
         }
         else if(BATTLE_WIDGETS_CONSTS.MECHANICS_WIDGETS_LEFT.indexOf(param1) > -1)
         {
            _loc2_ = this.mechanicsSlotLeft;
         }
         else if(BATTLE_WIDGETS_CONSTS.INFO_WIDGETS.indexOf(param1) > -1)
         {
            _loc2_ = this.infoSlot;
         }
         else if(BATTLE_WIDGETS_CONSTS.CENTRAL_WIDGETS.indexOf(param1) > -1)
         {
            _loc2_ = this.centralSlot;
         }
         else
         {
            DebugUtils.LOG_ERROR("Incorrect type of slot for " + param1 + " widget!");
            _loc2_ = this.infoSlot;
         }
         switch(param1)
         {
            case BATTLE_WIDGETS_CONSTS.ROCKET_ACCELERATOR:
               _loc3_ = Linkages.ROCKET_ACCELERATOR;
               _loc4_ = RocketAcceleratorWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.ROCKET_ACCELERATOR_INDICATOR;
               break;
            case BATTLE_WIDGETS_CONSTS.RECHARGEABLE_NITRO:
               _loc3_ = Linkages.RECHARGEABLE_NITRO;
               _loc4_ = RechargeableNitroWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.RECHARGEABLE_NITRO_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.CONCENTRATION:
               _loc3_ = Linkages.CONCENTRATION;
               _loc4_ = ConcentrationWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.CONCENTRATION_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.POWER:
               _loc3_ = Linkages.POWER;
               _loc4_ = PowerWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.POWER_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.SUPPORT_WEAPON:
               _loc3_ = Linkages.SUPPORT_WEAPON;
               _loc4_ = SupportWeaponWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.SUPPORT_WEAPON;
               break;
            case BATTLE_WIDGETS_CONSTS.PILLBOX_SIEGE:
               _loc3_ = Linkages.PILLBOX_SIEGE;
               _loc4_ = PillboxSiegeWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.PILLBOX_SIEGE_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.CHARGE_SHOT:
               _loc3_ = Linkages.CHARGE_SHOT;
               _loc4_ = ChargeShotWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.CHARGE_SHOT_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.STANCE_DANCE_FIGHT:
               _loc3_ = Linkages.STANCE_DANCE_FIGHT;
               _loc4_ = StanceDanceFightWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.STANCE_DANCE_WIDGET_FIGHT;
               break;
            case BATTLE_WIDGETS_CONSTS.STANCE_DANCE_TURBO:
               _loc3_ = Linkages.STANCE_DANCE_TURBO;
               _loc4_ = StanceDanceTurboWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.STANCE_DANCE_WIDGET_TURBO;
               break;
            case BATTLE_WIDGETS_CONSTS.TARGET_DESIGNATOR_WIDGET:
               _loc3_ = Linkages.TARGET_DESIGNATOR_WIDGET;
               _loc4_ = TargetDesignatorWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.TARGET_DESIGNATOR_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.CHARGEABLE_BURST:
               _loc3_ = Linkages.CHARGEABLE_BURST;
               _loc4_ = ChargeableBurstWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.CHARGEABLE_BURST_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.STATIONARY_RELOAD:
               _loc3_ = Linkages.STATIONARY_RELOAD;
               _loc4_ = StationaryReloadWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.STATIONARY_RELOAD_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.TEMPERATURE_GUN_OVERHEAT:
               _loc3_ = Linkages.TEMPERATURE_GUN_OVERHEAT;
               _loc4_ = TemperatureGunOverheatWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.TEMPERATURE_GUN_OVERHEAT_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.TEMPERATURE_GUN_HEAT_ZONES:
               _loc3_ = Linkages.TEMPERATURE_GUN_HEAT_ZONES;
               _loc4_ = TemperatureGunHeatZonesWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.TEMPERATURE_GUN_HEAT_ZONES_WIDGET;
               break;
            case BATTLE_WIDGETS_CONSTS.STAGED_JET_BOOSTERS:
               _loc3_ = Linkages.STAGED_JET_BOOSTERS;
               _loc4_ = StagedJetBoostersWidget;
               _loc5_ = BATTLE_VIEW_ALIASES.STAGED_JET_BOOSTERS_WIDGET;
               break;
            default:
               return;
         }
         if(!this._componentsStorage[_loc5_])
         {
            _loc6_ = App.utils.classFactory.getComponent(_loc3_,_loc4_);
            _loc2_.addChild(_loc6_);
            _loc2_.visible = true;
            this.registerComponent(_loc6_,_loc5_);
            _loc6_.isReplay = this._isReplay;
            _loc6_.isPlayer = this._isPlayer;
         }
      }
      
      public function as_addWidget(param1:String) : void
      {
         this.addWidget(param1);
      }
      
      public function as_isPlayer(param1:Boolean) : void
      {
         this._isPlayer = param1;
         invalidateData();
      }
      
      public function as_isReplay(param1:Boolean) : void
      {
         this._isReplay = param1;
         invalidateData();
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         if(this._isVisible == param1)
         {
            return;
         }
         this._isVisible = param1;
         this.updateVisibility();
      }
      
      public function as_updateCrosshairType(param1:int) : void
      {
         this._crosshairType = param1;
         invalidateSize();
      }
      
      public function as_updateLayout(param1:int, param2:int) : void
      {
         this.x = param1;
         this.y = param2;
         invalidateSize();
      }
      
      override protected function updateVisibility() : void
      {
         this.visible = this._isVisible && _isCompVisible;
      }
      
      private function registerComponent(param1:BaseVehicleMechanicsWidget, param2:String) : void
      {
         this._componentsStorage[param2] = param1;
         registerFlashComponentS(param1,param2);
      }
   }
}
