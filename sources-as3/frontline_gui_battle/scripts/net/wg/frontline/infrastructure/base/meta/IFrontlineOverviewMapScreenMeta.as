package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineOverviewMapScreenMeta extends IEventDispatcher
   {
       
      
      function as_setKeyBindings(param1:Object) : void;
      
      function as_updateLaneButtonNames(param1:String, param2:String, param3:String) : void;
   }
}
