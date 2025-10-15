package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface INotifyCenterDialogMeta extends IEventDispatcher
   {
       
      
      function doActionS(param1:String, param2:Boolean) : void;
   }
}
