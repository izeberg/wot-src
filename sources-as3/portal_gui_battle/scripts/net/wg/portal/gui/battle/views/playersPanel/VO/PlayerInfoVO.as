package net.wg.portal.gui.battle.views.playersPanel.VO
{
   import flash.events.Event;
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   
   public class PlayerInfoVO extends DAAPIVehicleInfoVO
   {
      
      private static const VEHICLE_LEVEL:String = "vehicleLevel";
       
      
      public var igrType:int = 0;
      
      public var hpMax:int = 0;
      
      public var hpCurrent:int = 0;
      
      public var secondsToRespawn:int = 0;
      
      public var vehicleLvlRoman:String = "";
      
      public function PlayerInfoVO(param1:Object = null)
      {
         super(param1);
      }
      
      override public function update(param1:DAAPIVehicleInfoVO) : void
      {
         super.update(param1);
         if(hasEventListener(Event.CHANGE))
         {
            dispatchEvent(new Event(Event.CHANGE));
         }
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == VEHICLE_LEVEL)
         {
            this.vehicleLvlRoman = param2.toString();
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
   }
}
