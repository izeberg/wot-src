package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IMissionsGroupedViewMeta extends IEventDispatcher
   {
       
      
      function expandS(param1:String, param2:Boolean) : void;
      
      function clickActionBtnS(param1:String) : void;
      
      function openTokenPopoverS(param1:int) : void;
      
      function useTokenClickS(param1:String) : void;
      
      function onClickButtonDetailsS() : void;
      
      function onGotoRtsQuestsClickS() : void;
   }
}
