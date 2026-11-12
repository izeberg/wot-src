package net.wg.gui.components.carousels
{
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.VehicleTypes;
   import net.wg.gui.components.carousels.controls.RolesContainer;
   import net.wg.gui.components.carousels.data.FilterRoleItemData;
   import net.wg.gui.components.carousels.events.FiltersTileListEvent;
   import net.wg.gui.components.controls.SimpleTileList;
   import net.wg.gui.components.controls.VO.SimpleRendererVO;
   import net.wg.gui.components.controls.events.RendererEvent;
   import scaleform.clik.constants.DirectionMode;
   
   public class FilterPopoverContent extends VehiclesFilterPopoverContent
   {
       
      
      public var rolesContainer:RolesContainer = null;
      
      public var lblDifficulty:TextField = null;
      
      public var listDifficulties:SimpleTileList = null;
      
      private var _rolesData:FilterRoleItemData = null;
      
      private var _selectedVehType:String = null;
      
      private var _setListState:Boolean = false;
      
      public function FilterPopoverContent()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.listDifficulties.itemRenderer = App.utils.classFactory.getClass(Linkages.TOGGLE_RENDERER_UI);
         this.listDifficulties.tileWidth = TOGGLE_TILE_WIDTH;
         this.listDifficulties.tileHeight = TOGGLE_TILE_HEIGHT;
         this.listDifficulties.directionMode = DirectionMode.HORIZONTAL;
         this.listDifficulties.addEventListener(RendererEvent.ITEM_CLICK,this.onDifficultyItemClickHandler);
         this.listDifficulties.addEventListener(Event.RESIZE,this.onDifficultyListResizeHandler);
         this.rolesContainer.addEventListener(Event.RESIZE,this.onRolesContainerResizeHandler);
         this.rolesContainer.addEventListener(Event.COMPLETE,this.onRolesContainerCompleteHandler);
      }
      
      override protected function onDispose() : void
      {
         this.listDifficulties.removeEventListener(RendererEvent.ITEM_CLICK,this.onDifficultyItemClickHandler);
         this.listDifficulties.removeEventListener(Event.RESIZE,this.onDifficultyListResizeHandler);
         this.listDifficulties.dispose();
         this.listDifficulties = null;
         this.lblDifficulty = null;
         this.rolesContainer.removeEventListener(Event.RESIZE,this.onRolesContainerResizeHandler);
         this.rolesContainer.removeEventListener(Event.COMPLETE,this.onRolesContainerCompleteHandler);
         this.rolesContainer.dispose();
         this.rolesContainer = null;
         if(this._rolesData != null)
         {
            this._rolesData.dispose();
            this._rolesData = null;
         }
         super.onDispose();
      }
      
      override protected function updateSize() : void
      {
         var _loc1_:int = 0;
         _loc1_ = listVehicleType.y + listVehicleType.height + LIST_OFFSET;
         if(this.rolesContainer.visible)
         {
            this.rolesContainer.y = _loc1_;
            _loc1_ += this.rolesContainer.height;
         }
         setSize(width,getNewHeight(_loc1_));
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      override protected function layoutDifficultySection(param1:int) : int
      {
         if(initData.difficultiesSectionVisible)
         {
            this.lblDifficulty.y = param1;
            this.listDifficulties.y = this.lblDifficulty.y + this.lblDifficulty.height + LABEL_OFFSET | 0;
            return this.listDifficulties.y + this.listDifficulties.height + LIST_OFFSET;
         }
         return param1;
      }
      
      override protected function updateState() : void
      {
         super.updateState();
         if(stateData.difficultiesSelected != null)
         {
            listSetState(this.listDifficulties,stateData.difficultiesSelected);
         }
         var _loc1_:Boolean = stateData.rolesSectionVisible;
         this.rolesContainer.setAnimVisibility(_loc1_);
         this._setListState = _loc1_;
         if(_loc1_)
         {
            this.updateRolesContainerData(false);
         }
         else
         {
            this.rolesContainer.clearList();
         }
         invalidateSize();
      }
      
      override protected function updateData() : void
      {
         super.updateData();
         var _loc1_:Boolean = initData.difficultiesSectionVisible && initData.difficulties != null;
         this.lblDifficulty.visible = this.listDifficulties.visible = _loc1_;
         if(_loc1_)
         {
            this.lblDifficulty.htmlText = initData.difficultiesLabel;
            this.listDifficulties.dataProvider = initData.difficulties;
         }
         else
         {
            this.listDifficulties.dataProvider = null;
         }
         var _loc2_:Boolean = initData.rolesSectionVisible;
         this.rolesContainer.visible = _loc2_;
         if(_loc2_)
         {
            this.updateRolesContainerData(true);
         }
         invalidateSize();
      }
      
      private function updateRolesContainerData(param1:Boolean) : void
      {
         var _loc2_:String = !!param1 ? initData.rolesLabel : stateData.rolesLabel;
         var _loc3_:int = this.getSelectedVehTypeIdx(param1);
         this._selectedVehType = VehicleTypes.CAROUSEL_FILTER_ORDER[_loc3_];
         if(this._rolesData)
         {
            this._rolesData.dispose();
         }
         this._rolesData = new FilterRoleItemData(initData.rolesSectionId,_loc2_,initData.roles.getDataProvider(this._selectedVehType),_loc3_);
         this.rolesContainer.setData(this._rolesData);
      }
      
      private function getSelectedVehTypeIdx(param1:Boolean) : int
      {
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         var _loc4_:SimpleRendererVO = null;
         if(param1)
         {
            _loc3_ = initData.vehicleTypes.length;
            _loc2_ = 0;
            while(_loc2_ < _loc3_)
            {
               _loc4_ = initData.vehicleTypes[_loc2_];
               if(_loc4_.selected)
               {
                  return _loc2_;
               }
               _loc2_++;
            }
         }
         else
         {
            _loc3_ = stateData.vehicleTypesSelected.length;
            _loc2_ = 0;
            while(_loc2_ < _loc3_)
            {
               if(stateData.vehicleTypesSelected[_loc2_])
               {
                  return _loc2_;
               }
               _loc2_++;
            }
         }
         return -1;
      }
      
      private function onDifficultyListResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
      
      private function onDifficultyItemClickHandler(param1:RendererEvent) : void
      {
         dispatchEvent(new FiltersTileListEvent(FiltersTileListEvent.ITEM_CLICK,initData.difficultiesSectionId,param1.index));
      }
      
      private function onRolesContainerCompleteHandler(param1:Event) : void
      {
         if(this._setListState)
         {
            this._setListState = false;
            listSetState(this.rolesContainer.listRoles,stateData.rolesStates.getStates(this._selectedVehType));
         }
      }
      
      private function onRolesContainerResizeHandler(param1:Event) : void
      {
         invalidateSize();
         validateNow();
      }
   }
}
