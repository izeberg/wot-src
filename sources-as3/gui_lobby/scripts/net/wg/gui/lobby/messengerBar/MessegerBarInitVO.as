package net.wg.gui.lobby.messengerBar
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.lobby.messengerBar.carousel.data.TooltipDataVO;
   
   public class MessegerBarInitVO extends DAAPIDataClass
   {
      
      private static const CONTACTS_TOOLTIP_DATA_FIELD_NAME:String = "contactsTooltipData";
      
      private static const CHANNELS_TOOLTIP_DATA_FIELD_NAME:String = "channelsTooltipData";
       
      
      public var channelsHtmlIcon:String = "";
      
      public var channelsLocked:Boolean = false;
      
      public var contactsHtmlIcon:String = "";
      
      public var contactsLocked:Boolean = false;
      
      public var contactsTooltip:String = "";
      
      public var vehicleCompareHtmlIcon:String = "";
      
      public var vehicleCompareTooltip:String = "";
      
      public var referralHtmlIcon:String = "";
      
      public var referralTooltip:String = "";
      
      public var sessionStatsHtmlIcon:String = "";
      
      public var referralCounter:int = 0;
      
      public var isReferralEnabled:Boolean = false;
      
      public var isReferralScoresLimitIndication:Boolean = false;
      
      private var _contactsTooltipData:Object = null;
      
      private var _contactsTooltipDataVO:TooltipDataVO = null;
      
      private var _channelsTooltipData:Object = null;
      
      private var _channelsTooltipDataVO:TooltipDataVO = null;
      
      public function MessegerBarInitVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == CONTACTS_TOOLTIP_DATA_FIELD_NAME && param2)
         {
            this._contactsTooltipDataVO = new TooltipDataVO(param2);
         }
         else if(param1 == CHANNELS_TOOLTIP_DATA_FIELD_NAME && param2)
         {
            this._channelsTooltipDataVO = new TooltipDataVO(param2);
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         super.onDispose();
         if(this._contactsTooltipDataVO)
         {
            this._contactsTooltipDataVO.dispose();
            this._contactsTooltipDataVO = null;
         }
         if(this._channelsTooltipDataVO)
         {
            this._channelsTooltipDataVO.dispose();
            this._channelsTooltipDataVO = null;
         }
      }
      
      public function get contactsTooltipDataVO() : TooltipDataVO
      {
         return this._contactsTooltipDataVO;
      }
      
      public function get contactsTooltipData() : Object
      {
         return this._contactsTooltipData;
      }
      
      public function set contactsTooltipData(param1:Object) : void
      {
         this._contactsTooltipData = param1;
      }
      
      public function get channelsTooltipDataVO() : TooltipDataVO
      {
         return this._channelsTooltipDataVO;
      }
      
      public function get channelsTooltipData() : Object
      {
         return this._channelsTooltipData;
      }
      
      public function set channelsTooltipData(param1:Object) : void
      {
         this._channelsTooltipData = param1;
      }
   }
}
