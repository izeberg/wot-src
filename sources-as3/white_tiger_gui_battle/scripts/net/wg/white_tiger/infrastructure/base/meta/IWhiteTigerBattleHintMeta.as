package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerBattleHintMeta extends IEventDispatcher
   {
       
      
      function onFadeOutFinishedS() : void;
      
      function as_showHint(param1:Object) : void;
      
      function as_hideHint() : void;
      
      function as_cancelFadeOut() : void;
   }
}
