package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.DisplayObjectContainer;
   import flash.geom.Point;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeyManager;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.gui.battle.views.widgetsPanel.vo.HotKeyVo;
   import net.wg.infrastructure.base.meta.IBaseVehicleMechanicsWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.BaseVehicleMechanicsWidgetMeta;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class BaseVehicleMechanicsWidget extends BaseVehicleMechanicsWidgetMeta implements IBaseVehicleMechanicsWidgetMeta
   {
      
      protected static const INSTANTLY_POSTFIX:String = "_instantly";
      
      private static const INVALID_KEY:int = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const HOT_KEY_START_POS_X:int = 28;
      
      private static const HOT_KEY_START_POS_Y:int = 18;
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.DISABLE];
       
      
      public var timer:Timer;
      
      private var _state:String = null;
      
      private var _targetLabel:String = null;
      
      private var _crosshairType:int = 1;
      
      private var _time:Number = -1;
      
      private var _isPlayer:Boolean = true;
      
      private var _isReplay:Boolean = false;
      
      private var _hotKeyMgr:HotkeyManager = null;
      
      private var _isColorBlind:Boolean = false;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      public function BaseVehicleMechanicsWidget()
      {
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
         this._state = this.getInitialState();
         var _loc1_:HotkeySettings = this.getHotkeySettings();
         this._hotKeyMgr = new HotkeyManager(this.getHotKeysTarget(),_loc1_);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = mouseChildren = false;
         this.onColorSchemeUpdateHandler();
         this._colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemeUpdateHandler);
      }
      
      override protected function onDispose() : void
      {
         this._colorSchemeMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemeUpdateHandler);
         this._colorSchemeMgr = null;
         if(this.timer)
         {
            this.timer.dispose();
            this.timer = null;
         }
         this._hotKeyMgr.dispose();
         this._hotKeyMgr = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.STATE) || isInvalid(InvalidationType.DATA))
         {
            this._hotKeyMgr.setVisibility(this.getHotKeyVisibility());
         }
         if(isInvalid(INVALID_KEY))
         {
            this._hotKeyMgr.invalidate();
         }
      }
      
      override protected function setHotKeys(param1:Vector.<HotKeyVo>) : void
      {
         this._hotKeyMgr.setData(param1);
         invalidate(INVALID_KEY);
      }
      
      public function as_setCrosshairType(param1:int) : void
      {
         this.crosshairType = param1;
      }
      
      public function as_setState(param1:String, param2:Boolean) : void
      {
         if(this._state == param1 && this._targetLabel != null)
         {
            return;
         }
         this.applyState(param1,param2);
         this._state = param1;
         invalidateState();
      }
      
      public function as_setTime(param1:Number) : void
      {
         if(this._time == param1)
         {
            return;
         }
         this._time = param1;
         this.setTimer(param1);
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         setCompVisible(param1);
      }
      
      protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return this;
      }
      
      protected function applyState(param1:String, param2:Boolean) : void
      {
         this._targetLabel = param1;
         if(param2 || this.getInstantTransitionStates().indexOf(this._state) > -1)
         {
            this._targetLabel += INSTANTLY_POSTFIX;
            gotoAndStop(this._targetLabel);
         }
         else
         {
            gotoAndPlay(this._targetLabel);
         }
      }
      
      protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.PREPARING;
      }
      
      protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      protected function setTimer(param1:Number) : void
      {
         if(this.timer)
         {
            this.timer.setLabel(param1);
         }
      }
      
      protected final function onKeyPress(param1:String, param2:Number) : void
      {
         this._hotKeyMgr.onKeyPress(param1,param2);
      }
      
      protected final function onActivateKey(param1:String, param2:Number) : void
      {
         this._hotKeyMgr.activateKey(param1,param2);
      }
      
      protected final function onKeyRelease(param1:String) : void
      {
         this._hotKeyMgr.onKeyRelease(param1);
      }
      
      protected final function showKeys(param1:Number = 0) : void
      {
         this._hotKeyMgr.showKeys(param1);
      }
      
      protected final function hideKeys(param1:Number = 0) : void
      {
         this._hotKeyMgr.hideKeys(param1);
      }
      
      protected final function setKeysState(param1:String) : void
      {
         this._hotKeyMgr.setState(param1);
      }
      
      protected final function setKeyAvailability(param1:Boolean) : void
      {
         this._hotKeyMgr.setAvailability(param1);
      }
      
      protected final function shakeKey(param1:String) : void
      {
         this._hotKeyMgr.shakeKey(param1);
      }
      
      protected function getHotKeyVisibility() : Boolean
      {
         return this._isPlayer && !this._isReplay;
      }
      
      protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),false,HotkeySettings.DIRECTION_FORWARD,Values.ZERO,Values.ZERO);
      }
      
      public function set isPlayer(param1:Boolean) : void
      {
         if(param1 == this._isPlayer)
         {
            return;
         }
         this._isPlayer = param1;
         invalidateData();
      }
      
      public function set isReplay(param1:Boolean) : void
      {
         if(param1 == this._isReplay)
         {
            return;
         }
         this._isReplay = param1;
         invalidateData();
      }
      
      public function set crosshairType(param1:int) : void
      {
         if(param1 == this._crosshairType)
         {
            return;
         }
         this._crosshairType = param1;
         invalidateSize();
      }
      
      public function get crosshairType() : int
      {
         return this._crosshairType;
      }
      
      public function get targetLabel() : String
      {
         return this._targetLabel;
      }
      
      protected function get state() : String
      {
         return this._state;
      }
      
      protected function set isColorBlind(param1:Boolean) : void
      {
         if(param1 == this._isColorBlind)
         {
            return;
         }
         this._isColorBlind = param1;
         invalidateData();
      }
      
      protected function get isColorBlind() : Boolean
      {
         return this._isColorBlind;
      }
      
      private function onColorSchemeUpdateHandler(param1:ColorSchemeEvent = null) : void
      {
         this.isColorBlind = this._colorSchemeMgr.getIsColorBlindS();
      }
   }
}
