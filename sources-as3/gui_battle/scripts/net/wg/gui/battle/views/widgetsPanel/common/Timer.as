package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class Timer extends MovieClip implements IDisposable
   {
      
      public static var NORMAL:String = "normal";
      
      public static var WARNING:String = "warning";
      
      public static var CRITICAL:String = "critical";
      
      public static var COLOR_NORMAL:uint = 16771993;
      
      public static var COLOR_WARNING:uint = 16751872;
      
      public static var COLOR_CRITICAL:uint = 16711680;
      
      private static const STATES:Vector.<String> = Vector.<String>([NORMAL,WARNING,CRITICAL]);
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
       
      
      public var label:TextField;
      
      private var _isDisposed:Boolean = false;
      
      private var _state:String;
      
      private var _colors:Dictionary;
      
      public function Timer()
      {
         this._state = NORMAL;
         this._colors = new Dictionary();
         super();
         this._colors[NORMAL] = COLOR_NORMAL;
         this._colors[WARNING] = COLOR_WARNING;
         this._colors[CRITICAL] = COLOR_CRITICAL;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         App.instance.utils.data.cleanupDynamicObject(this._colors);
         this._colors = null;
         this.onDispose();
         this._isDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function set state(param1:String) : void
      {
         if(STATES.indexOf(param1) == -1 || this._state == param1)
         {
            return;
         }
         this.label.textColor = this._colors[param1];
         this._state = param1;
      }
      
      public function get timeWidth() : int
      {
         return this.label.textWidth >> 0;
      }
      
      public function setLabel(param1:Number) : void
      {
         var _loc2_:String = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param1]);
         this.label.text = _loc2_.slice(0,_loc2_.length - 1);
      }
      
      protected function onDispose() : void
      {
         this.label = null;
      }
   }
}
