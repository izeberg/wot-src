package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerBossTeleportViewMeta extends IEventDispatcher
   {
       
      
      function onTeleportPointClickS(param1:String) : void;
      
      function onCancelS() : void;
   }
}
