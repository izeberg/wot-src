package net.wg.data.VO.daapi
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class DAAPITriggeredPriorityCommandVO extends DAAPIDataClass
   {
       
      
      public var vehicleID:Number = -1;
      
      public var chatCommand:String = "";
      
      public var chatCommandDurationMS:uint = 0;
      
      public var chatCommandFlags:uint = 0;
      
      public function DAAPITriggeredPriorityCommandVO(param1:Object = null)
      {
         super(param1);
      }
      
      override public function toString() : String
      {
         return "[DAAPITriggeredCommandVO] > id: " + this.vehicleID + ", chatCommandName:" + this.chatCommand + ", " + "chatCommandDurationMS:" + this.chatCommandDurationMS + ", chatCommandFlags:" + this.chatCommandFlags + "]";
      }
   }
}
