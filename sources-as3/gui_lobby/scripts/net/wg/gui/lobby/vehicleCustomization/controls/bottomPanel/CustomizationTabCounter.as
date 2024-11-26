package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.infrastructure.base.UIComponentEx;
   
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
      
      public function set text(param1:String) : void
      {
         this.label.text = param1;
         this.background.width = this.label.textWidth + this.BACKGROUND_OFFSET;
         this.background.x = -this.background.width >> 1;
         this.label.x = -(this.label.width >> 1) - this.TEXT_OFFSET;
      }
   }
}
