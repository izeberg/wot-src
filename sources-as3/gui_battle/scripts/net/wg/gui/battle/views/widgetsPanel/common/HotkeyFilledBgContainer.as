package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HotkeyFilledBgContainer extends Sprite implements IDisposable
   {
       
      
      public var defBg:HotkeyFilledBgPlain = null;
      
      public var longBg:HotkeyFilledBgLong = null;
      
      private var _disposed:Boolean = false;
      
      private var _isLong:Boolean = false;
      
      private var _width:int = 0;
      
      private var _state:String = "normal";
      
      public function HotkeyFilledBgContainer()
      {
         super();
         this.defBg.visible = false;
         this.longBg.visible = false;
      }
      
      public final function dispose() : void
      {
         this.defBg.dispose();
         this.defBg = null;
         this.longBg.dispose();
         this.longBg = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setState(param1:String) : void
      {
         this._state = param1;
         this.updateState();
      }
      
      public function setWidth(param1:Number) : void
      {
         this._width = param1;
         this.updateSize();
      }
      
      private function updateSize() : void
      {
         if(this._isLong)
         {
            this.longBg.setWidth(this._width);
         }
         else
         {
            this.defBg.setWidth(this._width);
         }
      }
      
      private function invalidateAll() : void
      {
         this.updateState();
         this.updateSize();
      }
      
      private function updateState() : void
      {
         if(this._isLong)
         {
            this.longBg.setState(this._state);
         }
         else
         {
            this.defBg.setState(this._state);
         }
      }
      
      public function set isLong(param1:Boolean) : void
      {
         this.defBg.visible = !param1;
         this.longBg.visible = param1;
         this._isLong = param1;
         this.invalidateAll();
      }
   }
}
