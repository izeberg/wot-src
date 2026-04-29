package net.wg.gui.lobby.historicalBattles
{
   import flash.display.Sprite;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.gui.lobby.historicalBattles.constants.HB_HANGAR_COMPONENTS;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.IStageSizeManager;
   import net.wg.utils.StageBreakPoint;
   
   public class HBHangarComponentsContainer extends Sprite implements IDisposable
   {
      
      private static const DIVISION_PANEL:String = "divisionPanel";
      
      private static const ORDER_WIDGET:String = "orderWidget";
      
      private static const SHOP_WIDGET:String = "shopWidget";
      
      private static const PROGRESSION_WIDGET:String = "progressionWidget";
      
      private static const FRONT_PANEL:String = "frontPanel";
      
      private static const QUESTS_WIDGET:String = "questsWidget";
      
      private static const HANGAR_VIGNETTE:String = "hangarVignette";
       
      
      public var divisionPanel:GFInjectComponent = null;
      
      public var orderWidget:GFInjectComponent = null;
      
      public var shopWidget:GFInjectComponent = null;
      
      public var progressionWidget:GFInjectComponent = null;
      
      public var frontPanel:GFInjectComponent = null;
      
      public var questsWidget:GFInjectComponent = null;
      
      public var hangarVignette:GFInjectComponent = null;
      
      private var _stageSizeMgr:IStageSizeManager;
      
      private var _disposed:Boolean = false;
      
      public function HBHangarComponentsContainer()
      {
         this._stageSizeMgr = App.stageSizeMgr;
         super();
         this.hangarVignette = new GFInjectComponent();
         this.hangarVignette.name = HANGAR_VIGNETTE;
         this.hangarVignette.setManageSize(true);
         this.hangarVignette.y = 0;
         this.hangarVignette.x = 0;
         this.orderWidget = new GFInjectComponent();
         this.orderWidget.name = ORDER_WIDGET;
         this.orderWidget.setManageSize(true);
         this.orderWidget.x = 0;
         this.divisionPanel = new GFInjectComponent();
         this.divisionPanel.name = DIVISION_PANEL;
         this.divisionPanel.setManageSize(true);
         this.shopWidget = new GFInjectComponent();
         this.shopWidget.name = SHOP_WIDGET;
         this.shopWidget.setManageSize(true);
         this.frontPanel = new GFInjectComponent();
         this.frontPanel.name = FRONT_PANEL;
         this.frontPanel.setManageSize(true);
         this.frontPanel.y = 0;
         this.frontPanel.x = 0;
         this.progressionWidget = new GFInjectComponent();
         this.progressionWidget.name = PROGRESSION_WIDGET;
         this.progressionWidget.setManageSize(true);
         this.progressionWidget.y = 0;
         this.questsWidget = new GFInjectComponent();
         this.questsWidget.name = QUESTS_WIDGET;
         this.questsWidget.setManageSize(true);
         addChild(this.hangarVignette);
         addChild(this.divisionPanel);
         addChild(this.orderWidget);
         addChild(this.shopWidget);
         addChild(this.questsWidget);
         addChild(this.frontPanel);
         addChild(this.progressionWidget);
      }
      
      public final function dispose() : void
      {
         if(this._disposed)
         {
            return;
         }
         this.onDispose();
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         var _loc3_:StageBreakPoint = null;
         _loc3_ = this._stageSizeMgr.currentBreakPoint;
         this.hangarVignette.width = param1;
         this.hangarVignette.height = param2;
         this.orderWidget.width = HB_HANGAR_COMPONENTS.ORDER_WIDGET_SIZE[_loc3_.name].width;
         this.orderWidget.height = HB_HANGAR_COMPONENTS.ORDER_WIDGET_SIZE[_loc3_.name].height;
         this.orderWidget.y = param2 - this.orderWidget.height | 0;
         this.shopWidget.width = HB_HANGAR_COMPONENTS.SHOP_WIDGET_SIZE[_loc3_.name];
         this.shopWidget.height = HB_HANGAR_COMPONENTS.SHOP_WIDGET_SIZE[_loc3_.name];
         this.shopWidget.x = param1 - this.shopWidget.width | 0;
         this.shopWidget.y = param2 - this.shopWidget.height | 0;
         this.progressionWidget.width = HB_HANGAR_COMPONENTS.PROGRESSION_WIDGET_SIZE[_loc3_.name].width;
         this.progressionWidget.height = HB_HANGAR_COMPONENTS.PROGRESSION_WIDGET_SIZE[_loc3_.name].height;
         this.progressionWidget.x = param1 - this.progressionWidget.width >> 1;
         this.questsWidget.width = HB_HANGAR_COMPONENTS.QUESTS_WIDGET_SIZE[_loc3_.name].width;
         this.questsWidget.height = HB_HANGAR_COMPONENTS.QUESTS_WIDGET_SIZE[_loc3_.name].height;
         this.questsWidget.y = HB_HANGAR_COMPONENTS.QUESTS_WIDGET_SIZE[_loc3_.name].top;
         this.frontPanel.height = HB_HANGAR_COMPONENTS.FRONT_PANEL_HEIGHT[_loc3_.name];
         this.frontPanel.width = param1;
         this.divisionPanel.width = HB_HANGAR_COMPONENTS.DIVISION_PANEL_SIZE[_loc3_.name].width;
         this.divisionPanel.height = HB_HANGAR_COMPONENTS.DIVISION_PANEL_SIZE[_loc3_.name].height;
         this.divisionPanel.x = param1 - this.divisionPanel.width >> 1;
         this.divisionPanel.y = param2 - this.divisionPanel.height | 0;
      }
      
      protected function onDispose() : void
      {
         this.orderWidget = null;
         this.divisionPanel = null;
         this.shopWidget = null;
         this.progressionWidget = null;
         this.frontPanel = null;
         this.questsWidget = null;
         this.hangarVignette = null;
         this._stageSizeMgr = null;
      }
   }
}
