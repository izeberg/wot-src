package net.wg.gui.notification.custom
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
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
