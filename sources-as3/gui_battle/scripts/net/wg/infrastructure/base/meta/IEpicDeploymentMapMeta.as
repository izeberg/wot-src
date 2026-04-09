package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IEpicDeploymentMapMeta extends IEventDispatcher
   {
       
      
      function as_setMapDimensions(param1:int, param2:int) : void;
      
      function as_setDirection(param1:String, param2:String, param3:String) : void;
   }
}
