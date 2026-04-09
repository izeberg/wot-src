package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IStorageDevicesTabViewMeta extends IEventDispatcher
   {
       
      
      function onRestoreButtonClickS() : void;
      
      function as_initModulesFilter(param1:Object) : void;
      
      function as_setRestoreButtonData(param1:Object) : void;
      
      function as_setBalanceValue(param1:String) : void;
   }
}
