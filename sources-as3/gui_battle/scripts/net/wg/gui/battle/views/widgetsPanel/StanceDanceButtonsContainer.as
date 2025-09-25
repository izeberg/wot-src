package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class StanceDanceButtonsContainer extends MovieClip implements IDisposable
   {
       
      
      public var timer:Timer = null;
      
      public var hotkeyTarget:MovieClip = null;
      
      private var _isDisposed:Boolean = false;
      
      public function StanceDanceButtonsContainer()
      {
         super();
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.timer.dispose();
         this.timer = null;
         this.hotkeyTarget = null;
         this._isDisposed = true;
      }
      
      public function get container() : MovieClip
      {
         return this.hotkeyTarget;
      }
      
      public function set time(param1:Number) : void
      {
         this.timer.setLabel(param1);
      }
   }
}
