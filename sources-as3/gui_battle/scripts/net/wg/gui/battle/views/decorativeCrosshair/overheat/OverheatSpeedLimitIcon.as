package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.decorativeCrosshair.shared.TextWrapper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatSpeedLimitIcon extends MovieClip implements IDisposable
   {
       
      
      public var icon:MovieClip = null;
      
      public var textWrapper:TextWrapper = null;
      
      private var _isDisposed:Boolean = false;
      
      public function OverheatSpeedLimitIcon()
      {
         super();
      }
      
      public function setText(param1:String) : void
      {
         this.textWrapper.setText(param1);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.textWrapper.dispose();
         this.textWrapper = null;
         this.icon = null;
         this._isDisposed = true;
      }
   }
}
