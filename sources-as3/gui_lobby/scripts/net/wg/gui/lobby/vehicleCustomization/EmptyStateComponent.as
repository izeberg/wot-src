package net.wg.gui.lobby.vehicleCustomization
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.lobby.vehicleCustomization.data.FilterFallbackDataVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class EmptyStateComponent extends UIComponentEx
   {
      
      private static const BTN_OFFSET:int = 100;
      
      private static const BTN_OFFSET_SMALL:int = 40;
      
      private static const TEXT_POSITION:int = 70;
      
      private static const TEXT_POSITION_SMALL:int = 100;
      
      private static const LINK_OFFSET_X:int = 0;
      
      private static const LINK_OFFSET_Y:int = 7;
      
      private static const LBL_OFFSET_X:int = 20;
      
      private static const MIN_RESOLUTION:int = 1600;
       
      
      public var lblMessage:TextField = null;
      
      public var videoButton:SoundButtonEx = null;
      
      public var tanksPopoverButton:SoundButtonEx = null;
      
      private var _data:FilterFallbackDataVO = null;
      
      public function EmptyStateComponent()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.lblMessage.autoSize = TextFieldAutoSize.LEFT;
         this.tanksPopoverButton.label = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EMPTYSTATE_ATTACHMENTS;
         this.videoButton.addEventListener(MouseEvent.CLICK,this.onVideoButtonClickHandler);
         this.tanksPopoverButton.addEventListener(MouseEvent.CLICK,this.onTanksPopoverButtonClickHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data != null && isInvalid(InvalidationType.DATA))
         {
            this.setMessageText(this._data.message);
            this.videoButton.visible = this._data.hasVideo;
            this.tanksPopoverButton.visible = this._data.popoverBtnVisible;
            invalidateLayout();
         }
         if(InvalidationType.LAYOUT)
         {
            if(this._data.hasVideo)
            {
               this.lblMessage.x = App.appWidth < MIN_RESOLUTION ? Number(TEXT_POSITION_SMALL) : Number(TEXT_POSITION);
               this.videoButton.x = this.lblMessage.x + this.lblMessage.textWidth;
               this.videoButton.x += App.appWidth < MIN_RESOLUTION ? BTN_OFFSET_SMALL : BTN_OFFSET;
               this.lblMessage.width = this.videoButton.x - this.lblMessage.x - LBL_OFFSET_X;
            }
            else
            {
               this.lblMessage.x = width - this.lblMessage.textWidth >> 1;
            }
            this.tanksPopoverButton.x = this.lblMessage.x + LINK_OFFSET_X;
            this.tanksPopoverButton.y = this.lblMessage.y + this.lblMessage.textHeight + LINK_OFFSET_Y;
         }
      }
      
      public function setData(param1:FilterFallbackDataVO) : void
      {
         if(param1 != null && this._data != param1)
         {
            this._data = param1;
         }
         invalidateData();
      }
      
      private function onVideoButtonClickHandler(param1:Event) : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.SHOW_ATTACHMENTS_VIDEO));
      }
      
      private function onTanksPopoverButtonClickHandler(param1:Event) : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.SHOW_VEHICLES_SIDEBAR));
      }
      
      override protected function onDispose() : void
      {
         this.videoButton.addEventListener(MouseEvent.CLICK,this.onVideoButtonClickHandler);
         this.tanksPopoverButton.addEventListener(MouseEvent.CLICK,this.onTanksPopoverButtonClickHandler);
         this.tanksPopoverButton.dispose();
         this.tanksPopoverButton = null;
         this.videoButton.dispose();
         this.videoButton = null;
         this.lblMessage = null;
         super.onDispose();
      }
      
      private function setMessageText(param1:String) : void
      {
         this.lblMessage.htmlText = param1;
      }
   }
}
