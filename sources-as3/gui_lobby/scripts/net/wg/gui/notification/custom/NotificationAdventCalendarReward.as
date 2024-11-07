package net.wg.gui.notification.custom
{
   import flash.display.DisplayObject;
   import flash.text.TextFormatAlign;
   import net.wg.gui.notification.ServiceMessageContent;
   
   public class NotificationAdventCalendarReward extends ServiceMessageContent
   {
      
      private static const MESSAGE_BOTTOM_OFFSET:int = 14;
      
      private static const BUTTONS_GROUP_PADDING_BOTTOM:int = 56;
       
      
      public function NotificationAdventCalendarReward()
      {
         super();
         messageTopOffset = 0;
         messageBottomOffset = MESSAGE_BOTTOM_OFFSET;
         buttonsAlign = TextFormatAlign.CENTER;
         textField.defaultTextFormat.bold = true;
      }
      
      override protected function updateData() : void
      {
         super.updateData();
         if(!bgIcon.source)
         {
            bgIcon.source = RES_ICONS.MAPS_ICONS_ADVENT_CALENDAR_MESSENGER_NOTIFICATION_BG_232X174;
         }
         textField.text = messageInfo.message;
         textField.setTextFormat(textField.defaultTextFormat);
      }
      
      override public function get height() : Number
      {
         return background.y + background.height;
      }
      
      override protected function get buttonsAnchorVertical() : DisplayObject
      {
         return background;
      }
      
      override protected function get buttonsGroupPaddingTop() : int
      {
         return -BUTTONS_GROUP_PADDING_BOTTOM;
      }
   }
}
