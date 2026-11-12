package net.wg.gui.components.common.lobbyVehicleMarkers
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class NewYearObjectMarker extends UIComponentEx
   {
       
      
      public var tf:TextField;
      
      public var icon:MovieClip;
      
      private var _label:String = "";
      
      private var _type:String = "";
      
      public function NewYearObjectMarker()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.tf.autoSize = TextFieldAutoSize.CENTER;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.tf.text = this._label;
            this.icon.gotoAndStop(this._type);
         }
      }
      
      override protected function onDispose() : void
      {
         this.tf = null;
         this.icon = null;
         super.onDispose();
      }
      
      public function setLabel(param1:String) : void
      {
         this._label = param1;
         invalidateData();
      }
      
      public function setType(param1:String) : void
      {
         this._type = param1;
         invalidateData();
      }
   }
}
