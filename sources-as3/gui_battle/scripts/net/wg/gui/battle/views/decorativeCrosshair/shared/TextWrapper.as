package net.wg.gui.battle.views.decorativeCrosshair.shared
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class TextWrapper extends Sprite implements IDisposable
   {
       
      
      public var textField:TextField = null;
      
      private var _isDisposed:Boolean = false;
      
      public function TextWrapper()
      {
         super();
      }
      
      public function setText(param1:String) : void
      {
         this.textField.text = param1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.textField = null;
         this._isDisposed = true;
      }
   }
}
