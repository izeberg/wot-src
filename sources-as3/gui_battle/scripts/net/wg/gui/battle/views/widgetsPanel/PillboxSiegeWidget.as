package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_HOTKEY_CONST;
   import net.wg.data.constants.generated.PILLBOX_SIEGE_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.DevicesHolder;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.pillbox.PillboxAnim;
   import net.wg.gui.battle.views.widgetsPanel.pillbox.PillboxAnimMgr;
   import net.wg.gui.battle.views.widgetsPanel.vo.DeviceStateInfo;
   import net.wg.infrastructure.base.meta.IPillboxSiegeWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.PillboxSiegeWidgetMeta;
   
   public class PillboxSiegeWidget extends PillboxSiegeWidgetMeta implements IPillboxSiegeWidgetMeta
   {
      
      private static const HOT_KEY_START_POS_X:int = 36;
      
      private static const HOT_KEY_START_POS_Y:int = 0;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
      
      private static const HOT_KEY_ACTIVATE_DURATION:Number = 1000;
      
      private static const SEC_TO_MILLISECONDS_MULTIPLIER:int = 1000;
       
      
      public var animNormal:PillboxAnim = null;
      
      public var animOrange:PillboxAnim = null;
      
      public var animRed:PillboxAnim = null;
      
      public var devices:DevicesHolder = null;
      
      private var _animMgr:PillboxAnimMgr = null;
      
      private var _condition:String = "";
      
      private var _isUpdatable:Boolean = true;
      
      private var _lastAffectCommand:String = "";
      
      private var _conditionToKeyStateMap:Object = null;
      
      private var _isProgressActive:Boolean = false;
      
      private var _isAnimUpdatable:Boolean = true;
      
      private var _keysAvailability:Boolean = true;
      
      private var _readyToActivate:String = "";
      
      public function PillboxSiegeWidget()
      {
         super();
         this.animNormal.blendMode = BlendMode.SCREEN;
         this.animOrange.blendMode = BlendMode.SCREEN;
         this.animRed.blendMode = BlendMode.SCREEN;
         this._animMgr = new PillboxAnimMgr(this.animNormal,this.animOrange,this.animRed);
         this._conditionToKeyStateMap = {};
         this._conditionToKeyStateMap[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_NORMAL] = MECHANIC_WIDGET_HOTKEY_CONST.NORMAL;
         this._conditionToKeyStateMap[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_WARNING] = MECHANIC_WIDGET_HOTKEY_CONST.WARNING;
         this._conditionToKeyStateMap[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL] = MECHANIC_WIDGET_HOTKEY_CONST.ALERT;
      }
      
      override protected function onDispose() : void
      {
         App.utils.data.cleanupDynamicObject(this._conditionToKeyStateMap);
         this._conditionToKeyStateMap = null;
         this.devices.dispose();
         this.devices = null;
         this._animMgr.dispose();
         this._animMgr = null;
         this.animNormal.dispose();
         this.animNormal = null;
         this.animOrange.dispose();
         this.animOrange = null;
         this.animRed.dispose();
         this.animRed = null;
         super.onDispose();
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         var _loc3_:Boolean = PILLBOX_SIEGE_WIDGET_CONST.PILLBOX_SIEGE_TRANSITIONS_STATE.indexOf(param1) != -1;
         if(this._readyToActivate && _loc3_)
         {
            onActivateKey(this._readyToActivate,HOT_KEY_ACTIVATE_DURATION);
            this._readyToActivate = Values.EMPTY_STR;
         }
         this._animMgr.setState(param1,param2);
         if(!_loc3_)
         {
            showKeys();
         }
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return [];
      }
      
      override protected function getInitialState() : String
      {
         return PILLBOX_SIEGE_WIDGET_CONST.IDLE;
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),true,HotkeySettings.DIRECTION_DOWN,Values.ZERO,HOT_KEY_GAP_Y);
      }
      
      override protected function setDeviceStates(param1:Vector.<DeviceStateInfo>) : void
      {
         this.devices.setDevices(param1);
      }
      
      public function as_setCommand(param1:String, param2:String, param3:Number) : void
      {
         param3 *= SEC_TO_MILLISECONDS_MULTIPLIER;
         this._readyToActivate = Values.EMPTY_STR;
         switch(param1)
         {
            case MECHANIC_WIDGET_HOTKEY_CONST.CANCELLED:
               if(this._lastAffectCommand == param2)
               {
                  onKeyRelease(param2);
               }
               break;
            case MECHANIC_WIDGET_HOTKEY_CONST.PREPARING:
               onKeyPress(param2,param3);
               break;
            case MECHANIC_WIDGET_HOTKEY_CONST.COMMAND_ACTIVATE:
               shakeKey(param2);
            case MECHANIC_WIDGET_HOTKEY_CONST.ALTERNATIVE_ACTIVATE:
               this._readyToActivate = param2;
         }
         this._lastAffectCommand = param2;
      }
      
      public function as_setCondition(param1:String, param2:Boolean) : void
      {
         if(this._condition == param1 && this._isUpdatable == param2)
         {
            return;
         }
         if(this._readyToActivate && param1 == PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL)
         {
            onKeyRelease(this._readyToActivate);
         }
         if(this._conditionToKeyStateMap.hasOwnProperty(param1))
         {
            setKeysState(this._conditionToKeyStateMap[param1]);
         }
         this._condition = param1;
         this._isUpdatable = param2;
         this.updateAvailability();
         this._animMgr.setCondition(param1);
      }
      
      public function as_setProgress(param1:Number, param2:Number) : void
      {
         this._isProgressActive = param2 > 0;
         this.updateAvailability();
         this._animMgr.setProgress(param1,param2);
      }
      
      private function updateAvailability() : void
      {
         var _loc1_:Boolean = this._isProgressActive || this._isUpdatable;
         if(this._isAnimUpdatable != _loc1_)
         {
            this._animMgr.setUpdatable(_loc1_);
            this._isAnimUpdatable = _loc1_;
         }
         var _loc2_:Boolean = this._condition != PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL || this._isProgressActive;
         if(this._keysAvailability != _loc2_)
         {
            setKeyAvailability(_loc2_);
            this._keysAvailability = _loc2_;
         }
      }
      
      override public function set visible(param1:Boolean) : void
      {
         super.visible = param1;
         this.animNormal.setWidgetVisible(param1);
         this.animOrange.setWidgetVisible(param1);
         this.animRed.setWidgetVisible(param1);
      }
   }
}
