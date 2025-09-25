package net.wg.gui.lobby.userMissions
{
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.geom.Rectangle;
   import flash.ui.Keyboard;
   import net.wg.data.constants.generated.QUESTS_ALIASES;
   import net.wg.data.constants.generated.USERMISSSIONS_ALIASES;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.controls.events.ScrollEvent;
   import net.wg.gui.events.FiltersEvent;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.gui.lobby.userMissions.components.MissionsFilter;
   import net.wg.gui.lobby.userMissions.components.MissionsGroupedView;
   import net.wg.gui.lobby.userMissions.components.UserMissionsHubContentInject;
   import net.wg.infrastructure.base.meta.IUserMissionsHubContainerViewMeta;
   import net.wg.infrastructure.base.meta.impl.UserMissionsHubContainerViewMeta;
   import net.wg.infrastructure.interfaces.IInnerView;
   
   public class UserMissionsHubContainerView extends UserMissionsHubContainerViewMeta implements IUserMissionsHubContainerViewMeta, IInnerView
   {
       
      
      public var filter:MissionsFilter;
      
      public var tabCommonMissions:MissionsGroupedView;
      
      public var gfContentInject:UserMissionsHubContentInject;
      
      public var background:UILoaderAlt;
      
      public function UserMissionsHubContainerView()
      {
         super();
      }
      
      public function as_setBackground(param1:String) : void
      {
         this.background.source = param1;
         this.background.visible = param1.length > 0;
      }
      
      public function as_updateCommonMissionsTabVisibility(param1:Boolean) : void
      {
         this.filter.visible = this.tabCommonMissions.visible = param1;
      }
      
      public function as_updateCommonMissionsTabPosition(param1:Number, param2:Number) : void
      {
         this.tabCommonMissions.x = 0;
         this.tabCommonMissions.y = this.gfContentInject.y + param1;
         this.filter.x = this.tabCommonMissions.list.x + 1;
         this.filter.y = this.gfContentInject.y + param1 + 8;
         this.tabCommonMissions.width = this.gfContentInject.width;
         this.tabCommonMissions.height = param2;
      }
      
      public function as_blinkFilterCounter() : void
      {
         this.filter.blink();
      }
      
      public function as_showFilterCounter(param1:String, param2:Boolean) : void
      {
         this.filter.showFilterCounter(param1,param2);
      }
      
      public function updateStageWithPadding(param1:Number, param2:Number, param3:Rectangle) : void
      {
         setViewSize(param1,param2);
         this.graphics.clear();
         this.graphics.beginFill(2303272);
         this.graphics.drawRect(0,0,param1,param2);
         this.graphics.endFill();
         this.gfContentInject.setSize(param1,param2 - param3.y - param3.height);
         this.gfContentInject.y = param3.y;
         this.updateBackgroundSize();
      }
      
      public function isFullScreenModeSupported() : Boolean
      {
         return true;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.filter.addEventListener(FiltersEvent.RESET_ALL_FILTERS,this.filterResetAllFiltersHandler);
         this.tabCommonMissions.addEventListener(ScrollEvent.UPDATE_SIZE,this.updateListSizeHandler);
         this.background.addEventListener(UILoaderEvent.COMPLETE,this.backgroundLoadedHandler);
         App.gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.escapeKeyHandler,true);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this.tabCommonMissions.visible = false;
         registerFlashComponentS(this.gfContentInject,USERMISSSIONS_ALIASES.USER_MISSIONS_HUB_CONTENT_INJECT);
         registerFlashComponentS(this.tabCommonMissions,QUESTS_ALIASES.MISSIONS_CATEGORIES_VIEW_PY_ALIAS);
      }
      
      override protected function onDispose() : void
      {
         App.popoverMgr.hide();
         App.gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.escapeKeyHandler);
         this.filter.removeEventListener(FiltersEvent.RESET_ALL_FILTERS,this.filterResetAllFiltersHandler);
         this.filter.dispose();
         this.filter = null;
         this.tabCommonMissions.removeEventListener(ScrollEvent.UPDATE_SIZE,this.updateListSizeHandler);
         this.tabCommonMissions = null;
         this.background.removeEventListener(UILoaderEvent.COMPLETE,this.backgroundLoadedHandler);
         this.background = null;
         this.gfContentInject = null;
         super.onDispose();
      }
      
      private function updateBackgroundSize() : void
      {
         if(this.background.source.length > 0)
         {
            this.background.scaleX = this.background.scaleY = Math.max(_originalWidth / this.background.content.width,_originalHeight / this.background.content.height);
            this.background.x = -(this.background.width - _originalWidth >> 1);
            this.background.y = -(this.background.height - _originalHeight >> 1);
         }
      }
      
      private function filterResetAllFiltersHandler(param1:Event) : void
      {
         resetFiltersS();
      }
      
      private function updateListSizeHandler(param1:ScrollEvent) : void
      {
         this.filter.x = this.tabCommonMissions.list.x + 1;
      }
      
      private function backgroundLoadedHandler(param1:UILoaderEvent) : void
      {
         this.updateBackgroundSize();
      }
      
      private function escapeKeyHandler(param1:Event) : void
      {
         onCloseS();
      }
   }
}
