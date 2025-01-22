package net.wg.gui.notification.custom
{
   import flash.events.Event;
   import flash.geom.Rectangle;
   import net.wg.gui.notification.ServiceMessageContent;
   
   public class SMParagonsMessageContent extends ServiceMessageContent
   {
      
      private static const TF_PADDING_TOP:int = -45;
      
      private static const BUTTONS_GROUP_PADDING_TOP:int = 16;
      
      private static const MESSAGE_PADDING_BOTTOM:int = 15;
      
      private static const WIDTH:int = 288;
      
      private static const BG_ICON_SCALE_GRID:Rectangle = new Rectangle(0,230,349,2);
      
      private static const BG_ICON_OFFSET_X:int = -30;
      
      private static const BG_ICON_OFFSET_Y:int = 80;
      
      private static const BG_ICON_MARGIN_BOTTOM:int = 35;
       
      
      public function SMParagonsMessageContent()
      {
         super();
         background.alpha = 0;
         bgIcon.scale9Grid = BG_ICON_SCALE_GRID;
      }
      
      override public function get width() : Number
      {
         return WIDTH;
      }
      
      override protected function updateData() : void
      {
         super.updateData();
         bgIcon.source = RES_ICONS.MAPS_ICONS_PARAGONS_MESSENGER_NOTIFICATION_BG;
         icon.source = messageInfo.icon || RES_ICONS.MAPS_ICONS_PARAGONS_MESSENGER_NOTIFICATION_ICON;
      }
      
      override protected function updateLayout() : void
      {
         var _loc1_:uint = 0;
         if(timeComponent != null)
         {
            timeComponent.visible = false;
         }
         App.utils.commons.updateTextFieldSize(textField,false,true);
         icon.y = 0;
         icon.x = this.width - icon.width >> 1;
         textField.x = this.width - textField.width >> 1;
         textField.y = icon.y + icon.height + TF_PADDING_TOP | 0;
         _loc1_ = textField.y + textField.height;
         if(buttonsGroup != null)
         {
            buttonsGroup.x = this.width - buttonsGroup.width >> 1;
            buttonsGroup.y = _loc1_ + BUTTONS_GROUP_PADDING_TOP ^ 0;
            _loc1_ = buttonsGroup.y + buttonsGroup.height;
         }
         _loc1_ += MESSAGE_PADDING_BOTTOM;
         bgIcon.x = BG_ICON_OFFSET_X;
         bgIcon.y = BG_ICON_OFFSET_Y;
         if(_loc1_ != background.height)
         {
            background.height = _loc1_;
            bgIcon.height = _loc1_ - BG_ICON_OFFSET_Y + BG_ICON_MARGIN_BOTTOM;
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
   }
}
