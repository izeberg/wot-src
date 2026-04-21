package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_HOTKEY_CONST;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HotkeyFilledBgPlain extends MovieClip implements IDisposable
   {
       
      
      private var _isDisposed:Boolean = false;
      
      private var _width:int = 0;
      
      public function HotkeyFilledBgPlain()
      {
         super();
      }
      
      protected function onDispose() : void
      {
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setState(param1:String) : void
      {
         if(MECHANIC_WIDGET_HOTKEY_CONST.HOT_KEY_STATES.indexOf(param1) != -1)
         {
            gotoAndStop(param1);
            this.updateSize(this._width);
         }
      }
      
      public final function setWidth(param1:int) : void
      {
         if(this._width != param1)
         {
            this._width = param1;
            this.updateSize(param1);
         }
      }
      
      protected function updateSize(param1:int) : void
      {
         this.width = param1;
      }
   }
}
