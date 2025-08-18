package net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers
{
   import flash.text.TextField;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class WTUnionStrengthCounter extends SimpleDisposable
   {
       
      
      public var textField:TextField = null;
      
      private var _count:uint = 0;
      
      public function WTUnionStrengthCounter()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.textField = null;
         super.onDispose();
      }
      
      public function set count(param1:uint) : void
      {
         if(this._count != param1)
         {
            this._count = param1;
            this.textField.text = this._count.toString();
         }
      }
   }
}
