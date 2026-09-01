package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_HOTKEY_CONST;
   import net.wg.gui.battle.views.widgetsPanel.bustleFeed.BustleFeedProgress;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.infrastructure.base.meta.IBustleFeedWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.BustleFeedWidgetMeta;
   
   public class BustleFeedWidget extends BustleFeedWidgetMeta implements IBustleFeedWidgetMeta
   {
      
      private static const HOT_KEY_START_POS_X:int = 27;
      
      private static const HOT_KEY_START_POS_Y:int = 13;
      
      private static const HOT_KEY_SHOW_DURATION:int = 200;
      
      private static const INACTIVE_ALPHA:Number = 0.5;
      
      private static const TRANSITION_STATES:Vector.<String> = Vector.<String>([MECHANICS_WIDGET_CONST.PREPARING,MECHANICS_WIDGET_CONST.TRANSITION]);
       
      
      public var progressMc:BustleFeedProgress = null;
      
      private var _isDisable:Boolean = false;
      
      private var _isLocked:Boolean = false;
      
      public function BustleFeedWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),false,HotkeySettings.DIRECTION_FORWARD,Values.ZERO,Values.ZERO);
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         super.applyState(param1,param2);
         var _loc3_:Boolean = TRANSITION_STATES.indexOf(param1) >= 0;
         this.progressMc.isInProgress = _loc3_;
         this.progressMc.setAlpha(param1 == MECHANICS_WIDGET_CONST.PREPARING ? Number(Values.DEFAULT_ALPHA) : Number(INACTIVE_ALPHA));
         if(_loc3_)
         {
            hideKeys();
         }
         else
         {
            showKeys(HOT_KEY_SHOW_DURATION);
         }
      }
      
      override protected function onDispose() : void
      {
         this.progressMc.dispose();
         this.progressMc = null;
         super.onDispose();
      }
      
      public function as_setProgress(param1:Number, param2:Number) : void
      {
         as_setTime(param2);
         this.progressMc.setProgress(param1);
      }
      
      public function as_setLock(param1:Boolean) : void
      {
         if(this._isLocked == param1)
         {
            return;
         }
         this._isLocked = param1;
         this.updateKeyStatus();
      }
      
      public function as_setAvailability(param1:Boolean) : void
      {
         if(this._isDisable == param1)
         {
            return;
         }
         this._isDisable = param1;
         this.updateKeyStatus();
         shakeKey(MECHANIC_WIDGET_HOTKEY_CONST.SWITCH);
      }
      
      private function updateKeyStatus() : void
      {
         setKeysState(this.getKeyState());
         setKeyAvailability(!this._isDisable && !this._isLocked);
      }
      
      private function getKeyState() : String
      {
         if(this._isDisable)
         {
            return MECHANIC_WIDGET_HOTKEY_CONST.ALERT;
         }
         if(this._isLocked)
         {
            return MECHANIC_WIDGET_HOTKEY_CONST.INACTIVE;
         }
         return MECHANIC_WIDGET_HOTKEY_CONST.NORMAL;
      }
      
      public function as_setCommand(param1:String) : void
      {
         if(param1 != MECHANIC_WIDGET_HOTKEY_CONST.SWITCH)
         {
            return;
         }
         shakeKey(param1);
      }
   }
}
