package net.wg.gui.battle.views.decorativeCrosshair.accuracy
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.decorativeCrosshair.shared.TextWrapper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class SpeedLimitMark extends MovieClip implements IDisposable
   {
      
      private static const ANIM_SHOW:String = "show";
      
      private static const ANIM_HIDE:String = "hide";
       
      
      public var textWrapper:TextWrapper = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _shown:Boolean = false;
      
      public function SpeedLimitMark()
      {
         super();
      }
      
      public function show(param1:Boolean) : void
      {
         if(this._shown != param1)
         {
            gotoAndPlay(!!param1 ? ANIM_SHOW : ANIM_HIDE);
         }
         this._shown = param1;
      }
      
      public function setSpeed(param1:int) : void
      {
         this.textWrapper.setText(param1.toString());
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.textWrapper.dispose();
         this.textWrapper = null;
         this._isDisposed = true;
      }
   }
}
