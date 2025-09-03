package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PM3VehicleIcon extends Sprite implements IDisposable
   {
       
      
      public var completeIco:Sprite = null;
      
      private var _isDisposed:Boolean = false;
      
      public function PM3VehicleIcon()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.completeIco = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      public function set isComplete(param1:Boolean) : void
      {
         this.completeIco.visible = param1;
      }
   }
}
