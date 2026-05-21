package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IMissionsGroupedViewMeta extends IEventDispatcher
   {
       
      
      function expandS(param1:String, param2:Boolean) : void;
      
      function clickActionBtnS(param1:String) : void;
      
      function onClickButtonDetailsS() : void;
      
      function onClickInfoBtnS(param1:String) : void;
      
      function onClickOpenShopBtnS(param1:String) : void;
      
      function onClickOpenEventBtnS(param1:String) : void;
   }
}
