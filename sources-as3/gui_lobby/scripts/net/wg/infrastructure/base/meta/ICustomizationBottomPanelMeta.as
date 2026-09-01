package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface ICustomizationBottomPanelMeta extends IEventDispatcher
   {
       
      
      function resetFilterS() : void;
      
      function showBuyWindowS() : void;
      
      function refreshFilterDataS() : void;
      
      function onSelectItemS(param1:int, param2:int, param3:int) : void;
      
      function onEditItemS(param1:int) : void;
      
      function showGroupFromTabS(param1:int) : void;
      
      function onSelectHotFilterS(param1:int, param2:Boolean) : void;
      
      function switchModeS(param1:int) : void;
      
      function onItemIsNewAnimationShownS(param1:int) : void;
      
      function showVideoS() : void;
      
      function showVehiclesSideBarS() : void;
      
      function as_showBill() : void;
      
      function as_hideBill() : void;
      
      function as_setBottomPanelInitData(param1:Object) : void;
      
      function as_setBottomPanelTabsData(param1:Object) : void;
      
      function as_setCarouselData(param1:Object) : void;
      
      function as_setCarouselInfoLabelData(param1:String, param2:String) : void;
      
      function as_setFilterData(param1:Object) : void;
      
      function as_setBottomPanelPriceState(param1:Object) : void;
      
      function as_setCarouselFiltersData(param1:Object) : void;
      
      function as_setProjectionDecalHintVisibility(param1:Boolean) : void;
      
      function as_showPopoverBtn(param1:String, param2:String, param3:String) : void;
      
      function as_getDataProvider() : Object;
      
      function as_setItemsPopoverBtnEnabled(param1:Boolean) : void;
      
      function as_setNotificationCounters(param1:Object) : void;
      
      function as_scrollToSlot(param1:int, param2:Boolean) : void;
      
      function as_playFilterBlink() : void;
      
      function as_updateEscHelpMessage(param1:Boolean) : void;
      
      function as_setFilterFallbackData(param1:Object) : void;
      
      function as_setStageSwitcherVisibility(param1:Boolean) : void;
      
      function as_setVehiclesSidebarBtnVisibility(param1:Boolean) : void;
   }
}
