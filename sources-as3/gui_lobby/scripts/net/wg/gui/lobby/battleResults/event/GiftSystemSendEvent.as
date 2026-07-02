package net.wg.gui.lobby.battleResults.event
{
   import flash.events.Event;
   
   public class GiftSystemSendEvent extends Event
   {
      
      public static const SEND_GIFT_REQUEST:String = "sendGiftRequest";
       
      
      public var playerId:int = -1;
      
      public var stampName:String = "";
      
      public function GiftSystemSendEvent(param1:int, param2:String)
      {
         super(SEND_GIFT_REQUEST,true,true);
         this.playerId = param1;
         this.stampName = param2;
      }
      
      override public function clone() : Event
      {
         return new GiftSystemSendEvent(this.playerId,this.stampName);
      }
   }
}
