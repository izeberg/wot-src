package net.wg.historical_battles.gui.battle.views.enemiesPanel.VO
{
   import flash.events.Event;
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   
   public class HBEnemyInfoVO extends DAAPIVehicleInfoVO
   {
       
      
      public var hpMax:int = 0;
      
      public var hpCurrent:int = 0;
      
      public function HBEnemyInfoVO(param1:Object = null)
      {
         super(param1);
      }
      
      override public function update(param1:DAAPIVehicleInfoVO) : void
      {
         fromHash(param1);
         if(hasEventListener(Event.CHANGE))
         {
            dispatchEvent(new Event(Event.CHANGE));
         }
      }
   }
}
