package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class CustomizationTabCounter extends UIComponentEx
   {
       
      
      public var background:Sprite = null;
      
      public var label:TextField = null;
      
      private const BACKGROUND_OFFSET:int = 35;
      
      private const TEXT_OFFSET:int = 1;
      
      public function CustomizationTabCounter()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.label.autoSize = TextFieldAutoSize.LEFT;
      }
      
      public function set text(param1:String) : void
      {
         this.label.text = param1;
         invalidateSize();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.background.width = this.label.textWidth + this.BACKGROUND_OFFSET;
            this.background.x = -this.background.width >> 1;
            this.label.width = this.label.textWidth;
            this.label.x = -(this.label.width >> 1) - this.TEXT_OFFSET;
         }
      }
      
      override protected function onDispose() : void
      {
         this.background = null;
         this.label = null;
         super.onDispose();
      }
   }
}
