package net.wg.gui.battle.cosmic
{
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.gui.battle.battleloading.BaseBattleLoading;
   import net.wg.gui.battle.views.cosmicHud.CosmicHud;
   import net.wg.gui.battle.views.debugPanel.DebugPanel;
   import net.wg.infrastructure.base.meta.IBattlePageMeta;
   import net.wg.infrastructure.base.meta.impl.BattlePageMeta;
   import net.wg.infrastructure.interfaces.IDAAPIModule;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class CosmicBattlePage extends BattlePageMeta implements IBattlePageMeta
   {
       
      
      public var cosmicHud:CosmicHud = null;
      
      public var debugPanel:DebugPanel = null;
      
      public var battleLoading:BaseBattleLoading = null;
      
      private var _componentsStorage:Object;
      
      public function CosmicBattlePage()
      {
         this._componentsStorage = {};
         super();
      }
      
      override protected function configUI() : void
      {
         this.updateStage(App.appWidth,App.appHeight);
         super.configUI();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         this.battleLoading.updateStage(param1,param2);
         this.cosmicHud.updateStage(param1,param2);
      }
      
      override protected function onPopulate() : void
      {
         this.registerComponent(this.battleLoading,BATTLE_VIEW_ALIASES.BATTLE_LOADING);
         this.registerComponent(this.cosmicHud,BATTLE_VIEW_ALIASES.COSMIC_HUD);
         this.registerComponent(this.debugPanel,BATTLE_VIEW_ALIASES.DEBUG_PANEL);
         super.onPopulate();
      }
      
      override protected function onDispose() : void
      {
         this.cosmicHud = null;
         this.debugPanel = null;
         App.utils.data.cleanupDynamicObject(this._componentsStorage);
         this._componentsStorage = null;
         super.onDispose();
      }
      
      override protected function setComponentsVisibility(param1:Vector.<String>, param2:Vector.<String>) : void
      {
         var _loc3_:String = null;
         for each(_loc3_ in param1)
         {
            this.showComponent(_loc3_,true);
         }
         for each(_loc3_ in param2)
         {
            this.showComponent(_loc3_,false);
         }
      }
      
      public function as_getComponentsVisibility() : Array
      {
         var _loc2_:* = null;
         var _loc3_:IDisplayableComponent = null;
         var _loc1_:Array = [];
         for(_loc2_ in this._componentsStorage)
         {
            _loc3_ = this._componentsStorage[_loc2_];
            if(_loc3_.isCompVisible())
            {
               _loc1_.push(_loc2_);
            }
         }
         return _loc1_;
      }
      
      public function as_isComponentVisible(param1:String) : Boolean
      {
         var _loc2_:IDisplayableComponent = null;
         _loc2_ = this._componentsStorage[param1];
         App.utils.asserter.assertNotNull(_loc2_,"can\'t find component " + param1 + " in Battle Page");
         return _loc2_.isCompVisible();
      }
      
      protected function registerComponent(param1:IDAAPIModule, param2:String) : void
      {
         this._componentsStorage[param2] = param1;
         registerFlashComponentS(param1,param2);
      }
      
      override public function unregisterComponent(param1:String) : void
      {
         delete this._componentsStorage[param1];
         super.unregisterComponent(param1);
      }
      
      private function showComponent(param1:String, param2:Boolean) : void
      {
         var _loc3_:IDisplayableComponent = null;
         _loc3_ = this._componentsStorage[param1];
         App.utils.asserter.assertNotNull(_loc3_,param1 + " " + Errors.CANT_NULL);
         _loc3_.setCompVisible(param2);
      }
      
      public function as_checkDAAPI() : void
      {
      }
      
      public function as_setPostmortemTipsVisible(param1:Boolean) : void
      {
      }
      
      public function as_toggleCtrlPressFlag(param1:Boolean) : void
      {
         App.toolTipMgr.hide();
      }
      
      public function as_createRoleDescription() : void
      {
      }
      
      public function as_setArtyShotIndicatorFlag(param1:Boolean) : void
      {
      }
      
      public function as_togglePiercingPanel() : void
      {
      }
   }
}
