package net.wg.historical_battles.gui.battle.views.spgPanel.VO
{
   import flash.events.Event;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   
   public class HBSPGInfoVO extends DAAPIDataClass implements IUpdatable
   {
       
      
      public var vehicleType:String = "";
      
      public var vehicleName:String = "";
      
      public var hpMax:int = 0;
      
      public var hpCurrent:int = 0;
      
      public var vehicleID:Number = 0;
      
      public function HBSPGInfoVO(param1:Object = null)
      {
         super(param1);
      }
      
      public function update(param1:Object) : void
      {
         fromHash(param1);
         if(hasEventListener(Event.CHANGE))
         {
            dispatchEvent(new Event(Event.CHANGE));
         }
      }
   }
}
