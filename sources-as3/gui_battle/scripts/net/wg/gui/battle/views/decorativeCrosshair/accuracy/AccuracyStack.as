package net.wg.gui.battle.views.decorativeCrosshair.accuracy
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class AccuracyStack extends MovieClip implements IDisposable
   {
       
      
      public var asset:MovieClip = null;
      
      private var _isDisposed:Boolean = false;
      
      public function AccuracyStack()
      {
         super();
      }
      
      public function switchState(param1:uint) : void
      {
         this.asset.gotoAndStop(param1);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.asset = null;
         this._isDisposed = true;
      }
   }
}
