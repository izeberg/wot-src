package net.wg.gui.lobby.storage.categories.storage
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ICON_TEXT_FRAMES;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.BlackButton;
   import net.wg.gui.events.FiltersEvent;
   import net.wg.gui.lobby.storage.data.StorageModulesFilterVO;
   import net.wg.gui.lobby.storage.data.StorageRestoreDevicesButtonVO;
   import net.wg.infrastructure.base.meta.IStorageDevicesTabViewMeta;
   import net.wg.infrastructure.base.meta.impl.StorageDevicesTabViewMeta;
   import net.wg.infrastructure.managers.IStageSizeManager;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import net.wg.utils.IStageSizeDependComponent;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class StorageDevicesTabView extends StorageDevicesTabViewMeta implements IStorageDevicesTabViewMeta, IStageSizeDependComponent
   {
      
      protected static const STATE_NORMAL_BALANCE_Y:int = 45;
      
      private static const STATE_SMALL_BALANCE_Y:int = 2;
      
      private static const RECOVERY_BUTTON_OFFSET:int = 20;
      
      private static const COUNTER_CONTAINER_ID:String = "storageDevicesTabView";
      
      private static const OFFSET_COUNTER_X:int = Values.ZERO;
      
      private static const OFFSET_COUNTER_Y:int = -3;
       
      
      public var balance:BalanceBlock;
      
      public var restoreButton:BlackButton;
      
      public var line:MovieClip;
      
      private var _isSmall:Boolean = false;
      
      private var _tooltipMgr:ITooltipMgr;
      
      private var _stageSizeMgr:IStageSizeManager;
      
      private var _counterManager:ICounterManager;
      
      private var _currentFiltersBlock:StorageModulesAndVehicleFilterBlock;
      
      private var _restoreButtonData:StorageRestoreDevicesButtonVO = null;
      
      public function StorageDevicesTabView()
      {
         this._tooltipMgr = App.toolTipMgr;
         this._stageSizeMgr = App.stageSizeMgr;
         this._counterManager = App.utils.counterManager;
         super();
         this._currentFiltersBlock = filtersBlock as StorageModulesAndVehicleFilterBlock;
         App.utils.asserter.assertNotNull(this._currentFiltersBlock,"_currentFiltersBlock " + Errors.CANT_NULL);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.balance.icon = ICON_TEXT_FRAMES.EQUIP_COIN_BIG;
         this.balance.addEventListener(MouseEvent.MOUSE_OVER,this.onBalanceValueRollOverHandler);
         this.balance.addEventListener(MouseEvent.ROLL_OUT,this.onBalanceValueRollOutHandler);
         if(this.restoreButton)
         {
            this.restoreButton.visible = false;
            this.restoreButton.label = STORAGE.DEVICES_BUTTONLABEL_GOTORESTORE;
            this.restoreButton.addEventListener(ButtonEvent.CLICK,this.onRestoreButtonClickHandler);
         }
         noItemsView.addEventListener(Event.CLOSE,this.onNoItemViewCloseHandler);
         this._currentFiltersBlock.addEventListener(FiltersEvent.MODULES_FILTER_CHANGED,this.onModulesIndexChangeHandler);
         this._stageSizeMgr.register(this);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.line.x = carousel.x;
            this.line.width = carousel.width;
            this.updateBalanceLayout();
            if(this.restoreButton)
            {
               this._counterManager.removeCounter(this.restoreButton,COUNTER_CONTAINER_ID);
               if(this.restoreButton.visible)
               {
                  this.restoreButton.x = carousel.x + carousel.width - this.restoreButton.width;
                  this._currentFiltersBlock.width = this._currentFiltersBlock.width - this.restoreButton.width - RECOVERY_BUTTON_OFFSET;
                  if(this._restoreButtonData && this._restoreButtonData.counterValue > Values.ZERO)
                  {
                     this._counterManager.setCounter(this.restoreButton,this._restoreButtonData.counterValue.toString(),COUNTER_CONTAINER_ID,new CounterProps(OFFSET_COUNTER_X,OFFSET_COUNTER_Y));
                  }
               }
            }
         }
      }
      
      override protected function initNoItemsView() : void
      {
         noItemsView.setTexts(STORAGE.STORAGE_NOITEMS_TITLE,STORAGE.STORAGE_NOITEMS_NAVIGATIONBUTTON);
      }
      
      override protected function doPartlyVisibility(param1:Boolean, param2:Boolean) : void
      {
         super.doPartlyVisibility(param1,param2);
         if(param2)
         {
            noItemsView.visible = false;
            filtersBlock.visible = true;
         }
         this.line.visible = filtersBlock.visible;
      }
      
      override protected function onDispose() : void
      {
         noItemsView.removeEventListener(Event.CLOSE,this.onNoItemViewCloseHandler);
         this.balance.removeEventListener(MouseEvent.ROLL_OVER,this.onBalanceValueRollOverHandler);
         this.balance.removeEventListener(MouseEvent.ROLL_OUT,this.onBalanceValueRollOutHandler);
         this.balance.dispose();
         this.balance = null;
         this._counterManager.disposeCountersForContainer(COUNTER_CONTAINER_ID);
         this._counterManager = null;
         if(this.restoreButton)
         {
            this.restoreButton.removeEventListener(ButtonEvent.CLICK,this.onRestoreButtonClickHandler);
            this.restoreButton.dispose();
            this.restoreButton = null;
         }
         this.line = null;
         this._restoreButtonData = null;
         this._currentFiltersBlock.removeEventListener(FiltersEvent.MODULES_FILTER_CHANGED,this.onModulesIndexChangeHandler);
         this._currentFiltersBlock = null;
         this._stageSizeMgr.unregister(this);
         this._stageSizeMgr = null;
         this._tooltipMgr = null;
         super.onDispose();
      }
      
      protected function updateBalanceLayout() : void
      {
         this.balance.x = carousel.x + carousel.width;
         this.balance.y = !!this._isSmall ? Number(STATE_SMALL_BALANCE_Y) : Number(STATE_NORMAL_BALANCE_Y);
      }
      
      private function onRestoreButtonClickHandler(param1:ButtonEvent) : void
      {
         onRestoreButtonClickS();
      }
      
      override protected function initModulesFilter(param1:StorageModulesFilterVO) : void
      {
         this._currentFiltersBlock.initModulesFilter(param1);
      }
      
      override protected function setRestoreButtonData(param1:StorageRestoreDevicesButtonVO) : void
      {
         if(this.restoreButton)
         {
            this._restoreButtonData = param1;
            this.restoreButton.visible = param1.isVisible;
            this._currentFiltersBlock.hasResetVehicleFilterButton = !this.restoreButton.visible;
            invalidateSize();
         }
      }
      
      public function as_setBalanceValue(param1:String) : void
      {
         this.balance.amount = param1;
      }
      
      public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         var _loc3_:Boolean = param1 < StageSizeBoundaries.WIDTH_1366;
         if(_loc3_ != this._isSmall)
         {
            this._isSmall = _loc3_;
            invalidateSize();
         }
      }
      
      private function onModulesIndexChangeHandler(param1:FiltersEvent) : void
      {
         onFiltersChangeS(param1.filtersValue);
      }
      
      private function onNoItemViewCloseHandler(param1:Event) : void
      {
         navigateToStoreS();
      }
      
      private function onBalanceValueRollOverHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.showSpecial(TOOLTIPS_CONSTANTS.EQUIP_COIN_INFO,null);
      }
      
      private function onBalanceValueRollOutHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.hide();
      }
   }
}
