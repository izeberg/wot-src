package net.wg.gui.lobby.vehicleCustomization
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.utils.ICommons;
   
   public class CustomizationHelpMessage extends UIComponentEx
   {
      
      private static const ICON_OFFSET_X:Number = 10;
      
      private static const BUTTON_OFFSET_X:Number = 30;
      
      private static const PADDING:Number = 30;
       
      
      public var labelLeft:TextField = null;
      
      public var labelRight:TextField = null;
      
      public var escIcon:Sprite = null;
      
      public var background:Sprite = null;
      
      public var closeBtn:SoundButtonEx = null;
      
      private var _commons:ICommons;
      
      public function CustomizationHelpMessage()
      {
         this._commons = App.utils.commons;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.labelLeft.text = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_ESCHELP_LEFT;
         this.labelRight.text = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_ESCHELP_RIGHT;
         this._commons.updateTextFieldSize(this.labelLeft,true,false);
         this._commons.updateTextFieldSize(this.labelRight,true,false);
         var _loc1_:Number = this.labelLeft.textWidth + ICON_OFFSET_X;
         _loc1_ += this.escIcon.width + ICON_OFFSET_X + this.labelRight.textWidth;
         _loc1_ += BUTTON_OFFSET_X + this.closeBtn.width;
         this.background.width = PADDING * 2 + _loc1_;
         this.labelLeft.x = PADDING;
         this.escIcon.x = this.labelLeft.x + this.labelLeft.textWidth + ICON_OFFSET_X;
         this.labelRight.x = this.escIcon.x + this.escIcon.width + ICON_OFFSET_X;
         this.closeBtn.x = this.labelRight.x + this.labelRight.textWidth + BUTTON_OFFSET_X;
         this.closeBtn.addEventListener(MouseEvent.CLICK,this.onCloseBtnClockHandler);
      }
      
      override protected function onDispose() : void
      {
         this.closeBtn.removeEventListener(MouseEvent.CLICK,this.onCloseBtnClockHandler);
         this.closeBtn.dispose();
         this.closeBtn = null;
         this._commons = null;
         this.labelLeft = null;
         this.labelRight = null;
         this.escIcon = null;
         this.background = null;
         super.onDispose();
      }
      
      private function onCloseBtnClockHandler(param1:Event) : void
      {
         visible = false;
      }
   }
}
