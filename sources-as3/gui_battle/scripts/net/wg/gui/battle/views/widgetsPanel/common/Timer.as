package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class Timer extends MovieClip implements IDisposable
   {
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
       
      
      public var label:TextField;
      
      private var _disposed:Boolean = false;
      
      public function Timer()
      {
         super();
      }
      
      public function dispose() : void
      {
         this.label = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setLabel(param1:Number) : void
      {
         var _loc2_:String = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param1]);
         this.label.text = _loc2_.slice(0,_loc2_.length - 1);
      }
   }
}
