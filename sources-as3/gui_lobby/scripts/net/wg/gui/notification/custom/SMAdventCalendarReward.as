package net.wg.gui.notification.custom
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.text.TextField;
   import flash.text.TextFormatAlign;
   import net.wg.gui.notification.ServiceMessageContent;
   import net.wg.gui.notification.custom.vo.SMAdventCalendarRewardVO;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class SMAdventCalendarReward extends ServiceMessageContent
   {
      
      private static const CONTENT_TOP_OFFSET:int = 20;
      
      private static const CONTENT_LEFT_OFFSET:int = 15;
      
      private static const TF_WITH_NO_DESC_Y:int = 233;
      
      private static const BUTTONS_GROUP_PADDING_BOTTOM:int = 56;
      
      private static const TF_BOUNDS_OFFSET:int = 4;
      
      private static const BUTTONS_GROUP_OFFSET_Y:int = 22;
      
      private static const SUB_BG_OFFSET_Y:int = 32;
       
      
      public var descTf:TextField = null;
      
      public var subBg:Sprite = null;
      
      public function SMAdventCalendarReward()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         contentTopOffset = CONTENT_TOP_OFFSET;
         contentLeftOffset = CONTENT_LEFT_OFFSET;
         buttonsAlign = TextFormatAlign.CENTER;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.descTf.selectable = false;
      }
      
      override protected function onDispose() : void
      {
         this.descTf = null;
         this.subBg = null;
         super.onDispose();
      }
      
      override protected function updateData() : void
      {
         if(!data)
         {
            return;
         }
         super.updateData();
         var _loc1_:SMAdventCalendarRewardVO = new SMAdventCalendarRewardVO(data.messageVO.linkageData);
         if(StringUtils.isNotEmpty(_loc1_.description))
         {
            this.descTf.text = _loc1_.description;
         }
         else
         {
            textField.y = TF_WITH_NO_DESC_Y;
         }
         if(!bgIcon.source)
         {
            bgIcon.source = RES_ICONS.MAPS_ICONS_ADVENT_CALENDAR_MESSENGER_SYS_NOTIFICATION_BG_290X240;
         }
         invalidateLayout();
      }
      
      override protected function updateLayout() : void
      {
         super.updateLayout();
         this.descTf.y = textField.y + textField.textHeight + TF_BOUNDS_OFFSET | 0;
         buttonsGroup.y = this.descTf.y + this.descTf.textHeight + TF_BOUNDS_OFFSET + BUTTONS_GROUP_OFFSET_Y | 0;
         this.subBg.y = buttonsGroup.y + buttonsGroup.height - this.subBg.height + SUB_BG_OFFSET_Y;
         background.height = this.subBg.y + this.subBg.height;
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      override protected function get buttonsAnchorVertical() : DisplayObject
      {
         return this.subBg;
      }
      
      override protected function get buttonsGroupPaddingTop() : int
      {
         return -BUTTONS_GROUP_PADDING_BOTTOM;
      }
   }
}
