package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BitmapData;
   import flash.geom.Point;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_HOTKEY_CONST;
   import net.wg.data.constants.generated.PROPELLANT_GUN_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.propellantGun.PropellantGunDamageIndicator;
   import net.wg.gui.battle.views.widgetsPanel.propellantGun.PropellantGunScaleCursor;
   import net.wg.gui.battle.views.widgetsPanel.propellantGun.PropellantGunScaleSector;
   import net.wg.infrastructure.base.meta.IPropellantGunWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.PropellantGunWidgetMeta;
   import net.wg.utils.IClassFactory;
   
   public class PropellantGunWidget extends PropellantGunWidgetMeta implements IPropellantGunWidgetMeta
   {
      
      private static const PATH_SECTOR_MARKER_LENGTH:Number = 1 / 51;
      
      private static const HALF_PATH_SECTOR_MARKER_LENGTH:Number = PATH_SECTOR_MARKER_LENGTH / 2;
      
      private static const CHARGE_PATH_READY_BMP_LINKAGE:String = "PropellantGunChargePathReadyUI";
      
      private static const CHARGE_PATH_READY_ALT_BMP_LINKAGE:String = "PropellantGunChargePathReadyAltUI";
      
      private static const CHARGE_PATH_ACTIVE_BMP_LINKAGE:String = "PropellantGunChargePathActiveUI";
      
      private static const CHARGE_PATH_ACTIVE_ALT_BMP_LINKAGE:String = "PropellantGunChargePathActiveAltUI";
      
      private static const CHARGE_PROGRESS_BMP_LINKAGE:String = "PropellantGunChargeProgressUI";
      
      private static const CHARGE_PROGRESS_ALT_BMP_LINKAGE:String = "PropellantGunChargeProgressAltUI";
      
      private static const OVERCHARGE_PATH_READY_BMP_LINKAGE:String = "PropellantGunOverchargePathReadyUI";
      
      private static const OVERCHARGE_PATH_READY_ALT_BMP_LINKAGE:String = "PropellantGunOverchargePathReadyAltUI";
      
      private static const OVERCHARGE_PATH_ACTIVE_BMP_LINKAGE:String = "PropellantGunOverchargePathActiveUI";
      
      private static const OVERCHARGE_PATH_ACTIVE_ALT_BMP_LINKAGE:String = "PropellantGunOverchargePathActiveAltUI";
      
      private static const OVERCHARGE_PROGRESS_BMP_LINKAGE:String = "PropellantGunOverchargeProgressUI";
      
      private static const OVERCHARGE_PROGRESS_ALT_BMP_LINKAGE:String = "PropellantGunOverchargeProgressAltUI";
      
      private static const OVERCHARGE_WARNING_BMP_LINKAGE:String = "PropellantGunOverchargeWarningUI";
      
      private static const WIDGET_SCALE_ARCADE:Number = 0.86;
      
      private static const WIDGET_SCALE_SNIPER:Number = 1;
      
      private static const CHARGE_CURSOR_TYPE:String = "charge";
      
      private static const OVERCHARGE_CURSOR_TYPE:String = "overcharge";
      
      private static const CHARGE_DAMAGE_INDICATOR_STATE:String = "charge";
      
      private static const OVERCHARGE_DAMAGE_INDICATOR_STATE:String = "overcharge";
      
      private static const OVERCHARGE_WARNING_SHOW_STATE:String = "show";
      
      private static const OVERCHARGE_WARNING_HIDE_STATE:String = "hide";
      
      private static const OVERCHARGE_WARNING_SECTOR_MAX_THRESHOLD:Number = 1.1;
      
      private static const OVERCHARGE_WARNING_SECTOR_MIN_THRESHOLD_OFFSET:Number = -0.008;
      
      private static const ACTIVE_STATES:Array = [PROPELLANT_GUN_WIDGET_CONST.ACTIVE_ENABLED,PROPELLANT_GUN_WIDGET_CONST.ACTIVE_DISABLED];
      
      private static const DISABLED_STATES:Array = [PROPELLANT_GUN_WIDGET_CONST.READY_DISABLED,PROPELLANT_GUN_WIDGET_CONST.ACTIVE_DISABLED];
      
      private static const THRESHOLD_INVALID:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const CHARGE_INVALID:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 3;
      
      private static const HOT_KEY_START_POS_X:int = 306;
      
      private static const HOT_KEY_START_POS_Y:int = 107;
      
      private static const HOT_KEY_SHOW_DURATION:Number = 200;
      
      private static const HOT_KEY_ACTIVATE_DURATION:Number = 200;
       
      
      public var scaleCursor:PropellantGunScaleCursor;
      
      public var chargePathReadySector:PropellantGunScaleSector;
      
      public var chargePathActiveSector:PropellantGunScaleSector;
      
      public var chargeProgressSector:PropellantGunScaleSector;
      
      public var overchargePathReadySector:PropellantGunScaleSector;
      
      public var overchargePathActiveSector:PropellantGunScaleSector;
      
      public var overchargeProgressSector:PropellantGunScaleSector;
      
      public var overchargeWarningSector:PropellantGunScaleSector;
      
      public var damageIndicator:PropellantGunDamageIndicator;
      
      private var _showTransition:Boolean = false;
      
      private var _chargeDamage:Number = 0;
      
      private var _chargeProgress:Number = 0;
      
      private var _chargeThreshold:Number = 1;
      
      private var _chargePathReadyBitmap:BitmapData = null;
      
      private var _chargePathReadyAltBitmap:BitmapData = null;
      
      private var _chargePathActiveBitmap:BitmapData = null;
      
      private var _chargePathActiveAltBitmap:BitmapData = null;
      
      private var _chargeProgressBitmap:BitmapData = null;
      
      private var _chargeProgressAltBitmap:BitmapData = null;
      
      private var _overchargePathReadyBitmap:BitmapData = null;
      
      private var _overchargePathReadyAltBitmap:BitmapData = null;
      
      private var _overchargePathActiveBitmap:BitmapData = null;
      
      private var _overchargePathActiveAltBitmap:BitmapData = null;
      
      private var _overchargeProgressBitmap:BitmapData = null;
      
      private var _overchargeProgressAltBitmap:BitmapData = null;
      
      private var _overchargeWarningBitmap:BitmapData = null;
      
      public function PropellantGunWidget()
      {
         super();
         var _loc1_:IClassFactory = App.utils.classFactory;
         this._chargePathReadyBitmap = _loc1_.getObject(CHARGE_PATH_READY_BMP_LINKAGE) as BitmapData;
         this._chargePathReadyAltBitmap = _loc1_.getObject(CHARGE_PATH_READY_ALT_BMP_LINKAGE) as BitmapData;
         this._chargePathActiveBitmap = _loc1_.getObject(CHARGE_PATH_ACTIVE_BMP_LINKAGE) as BitmapData;
         this._chargePathActiveAltBitmap = _loc1_.getObject(CHARGE_PATH_ACTIVE_ALT_BMP_LINKAGE) as BitmapData;
         this._chargeProgressBitmap = _loc1_.getObject(CHARGE_PROGRESS_BMP_LINKAGE) as BitmapData;
         this._chargeProgressAltBitmap = _loc1_.getObject(CHARGE_PROGRESS_ALT_BMP_LINKAGE) as BitmapData;
         this._overchargePathReadyBitmap = _loc1_.getObject(OVERCHARGE_PATH_READY_BMP_LINKAGE) as BitmapData;
         this._overchargePathReadyAltBitmap = _loc1_.getObject(OVERCHARGE_PATH_READY_ALT_BMP_LINKAGE) as BitmapData;
         this._overchargePathActiveBitmap = _loc1_.getObject(OVERCHARGE_PATH_ACTIVE_BMP_LINKAGE) as BitmapData;
         this._overchargePathActiveAltBitmap = _loc1_.getObject(OVERCHARGE_PATH_ACTIVE_ALT_BMP_LINKAGE) as BitmapData;
         this._overchargeProgressBitmap = _loc1_.getObject(OVERCHARGE_PROGRESS_BMP_LINKAGE) as BitmapData;
         this._overchargeProgressAltBitmap = _loc1_.getObject(OVERCHARGE_PROGRESS_ALT_BMP_LINKAGE) as BitmapData;
         this._overchargeWarningBitmap = _loc1_.getObject(OVERCHARGE_WARNING_BMP_LINKAGE) as BitmapData;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.chargePathReadySector.bitmapAlign = PropellantGunScaleSector.BITMAP_ALIGN_TO_MAX;
         this.overchargePathReadySector.bitmapAlign = PropellantGunScaleSector.BITMAP_ALIGN_TO_MAX;
         this.chargePathActiveSector.bitmapAlign = PropellantGunScaleSector.BITMAP_ALIGN_TO_MIN;
         this.overchargePathActiveSector.bitmapAlign = PropellantGunScaleSector.BITMAP_ALIGN_TO_MIN;
         this.overchargeWarningSector.snapValues = false;
         this.overchargeWarningSector.maxThreshold = OVERCHARGE_WARNING_SECTOR_MAX_THRESHOLD;
         this.overchargeWarningSector.currProgress = OVERCHARGE_WARNING_SECTOR_MAX_THRESHOLD;
         this.overchargeWarningSector.bitmapData = this._overchargeWarningBitmap;
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.scaleX = this.scaleY = crosshairType == CROSSHAIR_VIEW_ID.ARCADE ? Number(WIDGET_SCALE_ARCADE) : Number(WIDGET_SCALE_SNIPER);
         }
         if(isInvalid(InvalidationType.STATE))
         {
            super.applyState(state,!this._showTransition);
            this._showTransition = false;
            if(DISABLED_STATES.indexOf(state) < 0)
            {
               setKeysState(MECHANIC_WIDGET_HOTKEY_CONST.NORMAL);
               this.chargePathReadySector.bitmapData = this._chargePathReadyBitmap;
               this.chargePathActiveSector.bitmapData = this._chargePathActiveBitmap;
               this.chargeProgressSector.bitmapData = this._chargeProgressBitmap;
               this.overchargePathReadySector.bitmapData = this._overchargePathReadyBitmap;
               this.overchargePathActiveSector.bitmapData = this._overchargePathActiveBitmap;
               this.overchargeProgressSector.bitmapData = this._overchargeProgressBitmap;
            }
            else
            {
               setKeysState(MECHANIC_WIDGET_HOTKEY_CONST.INACTIVE);
               this.chargePathReadySector.bitmapData = this._chargePathReadyAltBitmap;
               this.chargePathActiveSector.bitmapData = this._chargePathActiveAltBitmap;
               this.chargeProgressSector.bitmapData = this._chargeProgressAltBitmap;
               this.overchargePathReadySector.bitmapData = this._overchargePathReadyAltBitmap;
               this.overchargePathActiveSector.bitmapData = this._overchargePathActiveAltBitmap;
               this.overchargeProgressSector.bitmapData = this._overchargeProgressAltBitmap;
            }
         }
         if(isInvalid(CHARGE_INVALID))
         {
            this.scaleCursor.progress = this._chargeProgress;
            this.chargeProgressSector.currProgress = this._chargeProgress;
            this.overchargeProgressSector.currProgress = this._chargeProgress;
            this.damageIndicator.damage = this._chargeDamage;
         }
         if(isInvalid(THRESHOLD_INVALID))
         {
            this.chargeProgressSector.maxThreshold = this._chargeThreshold;
            this.overchargeProgressSector.minThreshold = this._chargeThreshold + PATH_SECTOR_MARKER_LENGTH;
            this.chargePathReadySector.maxThreshold = this.chargeProgressSector.maxThreshold + HALF_PATH_SECTOR_MARKER_LENGTH;
            this.chargePathReadySector.minThreshold = this.chargePathReadySector.maxThreshold % PATH_SECTOR_MARKER_LENGTH;
            this.overchargePathReadySector.minThreshold = this.chargePathReadySector.maxThreshold != 1 ? Number(this.chargePathReadySector.maxThreshold + (1 - this.chargePathReadySector.maxThreshold) % PATH_SECTOR_MARKER_LENGTH) : Number(1);
            this.overchargePathActiveSector.minThreshold = this.overchargeProgressSector.minThreshold - HALF_PATH_SECTOR_MARKER_LENGTH;
            this.overchargePathActiveSector.maxThreshold = 1 - (1 - this.overchargePathActiveSector.minThreshold) % PATH_SECTOR_MARKER_LENGTH;
            this.chargePathActiveSector.maxThreshold = this.overchargePathActiveSector.minThreshold != 0 ? Number(this.overchargePathActiveSector.minThreshold - this.overchargePathActiveSector.minThreshold % PATH_SECTOR_MARKER_LENGTH) : Number(0);
            this.overchargeWarningSector.minThreshold = this.overchargeProgressSector.minThreshold + OVERCHARGE_WARNING_SECTOR_MIN_THRESHOLD_OFFSET;
         }
         if(isInvalid(CHARGE_INVALID | THRESHOLD_INVALID))
         {
            this.scaleCursor.cursorType = this._chargeProgress > this._chargeThreshold + HALF_PATH_SECTOR_MARKER_LENGTH ? OVERCHARGE_CURSOR_TYPE : CHARGE_CURSOR_TYPE;
            _loc1_ = this._chargeProgress > this._chargeThreshold;
            this.damageIndicator.state = !!_loc1_ ? OVERCHARGE_DAMAGE_INDICATOR_STATE : CHARGE_DAMAGE_INDICATOR_STATE;
            this.overchargeWarningSector.state = !!_loc1_ ? OVERCHARGE_WARNING_SHOW_STATE : OVERCHARGE_WARNING_HIDE_STATE;
         }
      }
      
      override protected function onDispose() : void
      {
         this.damageIndicator.dispose();
         this.damageIndicator = null;
         this.overchargeWarningSector.dispose();
         this.overchargeWarningSector = null;
         this.overchargeProgressSector.dispose();
         this.overchargeProgressSector = null;
         this.overchargePathActiveSector.dispose();
         this.overchargePathActiveSector = null;
         this.overchargePathReadySector.dispose();
         this.overchargePathReadySector = null;
         this.chargeProgressSector.dispose();
         this.chargeProgressSector = null;
         this.chargePathActiveSector.dispose();
         this.chargePathActiveSector = null;
         this.chargePathReadySector.dispose();
         this.chargePathReadySector = null;
         this.scaleCursor.dispose();
         this.scaleCursor = null;
         this._overchargeWarningBitmap.dispose();
         this._overchargeWarningBitmap = null;
         this._overchargeProgressAltBitmap.dispose();
         this._overchargeProgressAltBitmap = null;
         this._overchargeProgressBitmap.dispose();
         this._overchargeProgressBitmap = null;
         this._overchargePathActiveAltBitmap.dispose();
         this._overchargePathActiveAltBitmap = null;
         this._overchargePathActiveBitmap.dispose();
         this._overchargePathActiveBitmap = null;
         this._overchargePathReadyAltBitmap.dispose();
         this._overchargePathReadyAltBitmap = null;
         this._overchargePathReadyBitmap.dispose();
         this._overchargePathReadyBitmap = null;
         this._chargeProgressAltBitmap.dispose();
         this._chargeProgressAltBitmap = null;
         this._chargeProgressBitmap.dispose();
         this._chargeProgressBitmap = null;
         this._chargePathActiveAltBitmap.dispose();
         this._chargePathActiveAltBitmap = null;
         this._chargePathActiveBitmap.dispose();
         this._chargePathActiveBitmap = null;
         this._chargePathReadyAltBitmap.dispose();
         this._chargePathReadyAltBitmap = null;
         this._chargePathReadyBitmap.dispose();
         this._chargePathReadyBitmap = null;
         super.onDispose();
      }
      
      public function as_setChargeValues(param1:Number, param2:Number) : void
      {
         if(param1 == this._chargeProgress && param2 == this._chargeDamage)
         {
            return;
         }
         this._chargeProgress = param1;
         this._chargeDamage = param2;
         invalidate(CHARGE_INVALID);
      }
      
      public function as_setupThreshold(param1:Number) : void
      {
         if(param1 == this._chargeThreshold)
         {
            return;
         }
         this._chargeThreshold = param1;
         invalidate(THRESHOLD_INVALID);
      }
      
      public function as_activateHotKey(param1:String) : void
      {
         onActivateKey(param1,HOT_KEY_ACTIVATE_DURATION);
      }
      
      public function as_showHotKeys(param1:Boolean) : void
      {
         if(param1)
         {
            showKeys(HOT_KEY_SHOW_DURATION);
         }
         else
         {
            hideKeys();
         }
      }
      
      override protected function getInitialState() : String
      {
         return PROPELLANT_GUN_WIDGET_CONST.READY_ENABLED;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return [];
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),false,HotkeySettings.DIRECTION_FORWARD,0,0);
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         this._showTransition = !param2 && ACTIVE_STATES.indexOf(this.state) < 0;
      }
   }
}
