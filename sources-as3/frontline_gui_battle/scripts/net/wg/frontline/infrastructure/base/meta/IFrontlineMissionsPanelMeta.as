package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineMissionsPanelMeta extends IEventDispatcher
   {
       
      
      function as_setPrimaryMission(param1:Object) : void;
      
      function as_setNearestHQ(param1:int) : void;
      
      function as_setMissionDescriptionValue(param1:String) : void;
   }
}
