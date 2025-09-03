package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.decorativeCrosshair.OverheatDecorativeCrosshair;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatIcon extends MovieClip implements IDisposable
   {
      
      public static const STATE_EMPTY:String = "empty";
      
      public static const STATE_ON:String = "on";
      
      public static const STATE_OFF:String = "off";
      
      public static const STATE_HEAT_ON:String = "heat";
      
      public static const STATE_HEAT_OFF:String = "hide";
       
      
      private var _isHeated:Boolean = false;
      
      private var _isDisposed:Boolean = false;
      
      private var _currentUIState:String = "empty";
      
      public function OverheatIcon()
      {
         super();
      }
      
      public function setState(param1:uint, param2:uint) : void
      {
         var _loc3_:String = STATE_EMPTY;
         if(param2 == OverheatDecorativeCrosshair.STATE_CHARGE_MAX)
         {
            _loc3_ = STATE_HEAT_ON;
         }
         else if(param1 == OverheatDecorativeCrosshair.STATE_CHARGE_MAX)
         {
            _loc3_ = STATE_HEAT_OFF;
            this._isHeated = false;
         }
         else if(param2 == OverheatDecorativeCrosshair.STATE_STACK_GAIN)
         {
            _loc3_ = STATE_ON;
            this._isHeated = true;
         }
         else if(this._isHeated)
         {
            this._isHeated = false;
            _loc3_ = STATE_OFF;
         }
         if(_loc3_ != this._currentUIState)
         {
            this._currentUIState = _loc3_;
            gotoAndPlay(this._currentUIState);
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this._isDisposed = true;
      }
   }
}
