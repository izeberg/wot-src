package net.wg.gui.components.common.lobbyVehicleMarkers
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.base.UIComponentEx;
   
   public class RaccoonMarker extends UIComponentEx
   {
       
      
      public var tf:TextField;
      
      private var _label:String = "";
      
      public function RaccoonMarker()
      {
         super();
      }
      
      override protected function draw() : void
      {
         super.draw();
         this.tf.text = this._label;
         this.tf.autoSize = TextFieldAutoSize.CENTER;
      }
      
      override protected function onDispose() : void
      {
         this.tf = null;
         super.onDispose();
      }
      
      public function setLabel(param1:String) : void
      {
         this._label = param1;
         invalidateData();
      }
   }
}
