package net.wg.historical_battles.gui.battle.views.respawn.components
{
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HBTextBase extends SimpleDisposable
   {
       
      
      public var textField:TextField = null;
      
      private var _tf:TextFormat = null;
      
      public function HBTextBase()
      {
         super();
         this.textField.cacheAsBitmap = true;
         this._tf = this.textField.getTextFormat();
      }
      
      override protected function onDispose() : void
      {
         this._tf = null;
         this.textField.filters = null;
         this.textField = null;
         super.onDispose();
      }
      
      public function set label(param1:String) : void
      {
         this.textField.text = param1;
      }
      
      protected function set fontSize(param1:int) : void
      {
         this._tf.size = param1;
         this.textField.setTextFormat(this._tf);
         App.utils.commons.updateTextFieldSize(this.textField);
      }
   }
}
