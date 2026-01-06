package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ICustomizationFiltersPopoverMeta extends IEventDispatcher
   {
       
      
      function changeGroupS(param1:int) : void;
      
      function changeDisplayMethodS(param1:int) : void;
      
      function setDefaultFilterS() : void;
      
      function setShowOnlyHistoricS(param1:Boolean) : void;
      
      function setShowOnlyAcquiredS(param1:Boolean) : void;
      
      function setHideOnAnotherVehS(param1:Boolean) : void;
      
      function setShowOnlyProgressionDecalsS(param1:Boolean) : void;
      
      function setShowOnlyEditableStylesS(param1:Boolean) : void;
      
      function setShowOnlyProgressionStylesS(param1:Boolean) : void;
      
      function onFilterChangeS(param1:int, param2:int, param3:Boolean) : void;
      
      function onFormChangeS(param1:int, param2:Boolean) : void;
      
      function as_setData(param1:Object) : void;
      
      function as_enableDefBtn(param1:Boolean) : void;
      
      function as_updateCounter(param1:int, param2:int, param3:int) : void;
   }
}
