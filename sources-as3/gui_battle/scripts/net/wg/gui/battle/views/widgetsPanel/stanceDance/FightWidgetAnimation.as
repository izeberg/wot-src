package net.wg.gui.battle.views.widgetsPanel.stanceDance
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class FightWidgetAnimation extends MovieClip implements IDisposable
   {
       
      
      public var transitionAnimation:MovieClip = null;
      
      public var textfield:Timer = null;
      
      private var _disposed:Boolean = false;
      
      public function FightWidgetAnimation()
      {
         super();
      }
      
      public function setText(param1:Number) : void
      {
         this.textfield.setLabel(param1);
      }
      
      public function setPause(param1:Boolean) : void
      {
         if(param1)
         {
            this.transitionAnimation.stop();
         }
         else
         {
            this.transitionAnimation.play();
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function dispose() : void
      {
         this._disposed = true;
         this.textfield = null;
      }
   }
}
