package net.wg.gui.lobby.personalMissions.components
{
   import flash.display.Sprite;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.PERSONAL_MISSIONS_ALIASES;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.advanced.ViewStackEx;
   import net.wg.gui.events.ViewStackEvent;
   import net.wg.gui.lobby.components.SideBar;
   import net.wg.infrastructure.base.meta.IPersonalMissionOperationsMeta;
   import net.wg.infrastructure.base.meta.impl.PersonalMissionOperationsMeta;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.IndexEvent;
   
   public class PersonalMissionOperations extends PersonalMissionOperationsMeta implements IPersonalMissionOperationsMeta
   {
      
      private static const INV_SELECTED_IDX:String = "invSelectedIdx";
      
      private static const MENU_OFFSET_X:int = 32;
      
      private static const MENU_OFFSET_SMALL_X:int = 16;
      
      private static const MENU_OFFSET_Y:int = -102;
      
      private static const MENU_OFFSET_SMALL_Y:int = -75;
      
      private static const MENU_BG_OFFSET_Y:int = 90;
      
      private static const MENU_BG_OFFSET_SMALL_Y:int = 63;
      
      private static const DP_SOURCE:Array = [{
         "id":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM3_OPERATIONS,
         "viewId":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM3_OPERATIONS,
         "linkage":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM3_OPERATIONS_LINKAGE,
         "tooltip":TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_ANNOUNCE,
         "isWulfTooltip":true
      },{
         "id":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM_OLD_OPERATIONS,
         "viewId":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM_OLD_OPERATIONS,
         "linkage":PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PM_OLD_OPERATIONS_LINKAGE,
         "tooltip":TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_OLD_OPERATIONS,
         "isWulfTooltip":true
      }];
       
      
      public var menu:SideBar;
      
      public var menuBg:Sprite;
      
      public var content:ViewStackEx;
      
      private var _currentAlias:String;
      
      private var _selectedIdx:int;
      
      public function PersonalMissionOperations()
      {
         super();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         setSize(param1,param2);
         this.menu.height = height;
         this.content.setSize(width,height);
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.menu.enableOversize = true;
         this.updateMenu();
         this.menu.dataProvider = new DataProvider(DP_SOURCE);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.content.addEventListener(ViewStackEvent.NEED_UPDATE,this.onContentNeedUpdateHandler,false,0,true);
         this.menu.addEventListener(IndexEvent.INDEX_CHANGE,this.onMenuIndexChangeHandler,false,0,true);
      }
      
      override protected function onDispose() : void
      {
         this.menuBg = null;
         this.menu.removeEventListener(IndexEvent.INDEX_CHANGE,this.onMenuIndexChangeHandler,false);
         this.menu.dispose();
         this.menu = null;
         this.content.removeEventListener(ViewStackEvent.NEED_UPDATE,this.onContentNeedUpdateHandler,false);
         this.content.dispose();
         this.content = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(InvalidationType.SIZE)
         {
            this.updateMenu();
         }
         if(isInvalid(INV_SELECTED_IDX))
         {
            this.menu.selectedIndex = this._selectedIdx;
         }
      }
      
      override protected function onEscapeKeyDown() : void
      {
         closeViewS();
      }
      
      public function as_setSelectedTab(param1:int) : void
      {
         if(param1 != this._selectedIdx)
         {
            this._selectedIdx = param1;
            invalidate(INV_SELECTED_IDX);
         }
      }
      
      private function updateMenu() : void
      {
         var _loc1_:Boolean = App.appWidth < StageSizeBoundaries.WIDTH_1600 || App.appHeight < StageSizeBoundaries.HEIGHT_900;
         this.menu.itemRendererName = !!_loc1_ ? Linkages.SIDE_BAR_SMALL_RENDERER : Linkages.SIDE_BAR_NORMAL_RENDERER;
         this.menu.x = !!_loc1_ ? Number(MENU_OFFSET_SMALL_X) : Number(MENU_OFFSET_X);
         this.menu.y = (height >> 1) + (!!_loc1_ ? MENU_OFFSET_SMALL_Y : MENU_OFFSET_Y);
         this.menuBg.y = this.menu.y - (this.menuBg.height >> 1) + (!!_loc1_ ? MENU_BG_OFFSET_SMALL_Y : MENU_BG_OFFSET_Y);
      }
      
      override public function get isModal() : Boolean
      {
         return true;
      }
      
      private function onContentNeedUpdateHandler(param1:ViewStackEvent) : void
      {
         var _loc2_:String = param1.viewId;
         if(!isFlashComponentRegisteredS(_loc2_))
         {
            registerFlashComponentS(IDAAPIModule(param1.view),_loc2_);
         }
      }
      
      private function onMenuIndexChangeHandler(param1:IndexEvent) : void
      {
         if(param1.index != -1)
         {
            this._selectedIdx = param1.index;
            onTabSelectedS(this._selectedIdx);
            if(isFlashComponentRegisteredS(this._currentAlias))
            {
               unregisterFlashComponentS(this._currentAlias);
            }
            this._currentAlias = param1.data.viewId;
         }
      }
   }
}
