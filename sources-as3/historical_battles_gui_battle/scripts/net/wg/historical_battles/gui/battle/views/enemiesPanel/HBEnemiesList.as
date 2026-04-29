package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import flash.display.Sprite;
   import flash.events.Event;
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.VO.HBEnemyInfoVO;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.events.ListDataProviderEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class HBEnemiesList extends BattleUIComponent
   {
      
      public static const LIST_ITEM_HEIGHT:int = 33;
      
      public static const MIN_ITEMS:uint = 10;
      
      public static const MIN_HEIGHT:uint = LIST_ITEM_HEIGHT * MIN_ITEMS;
      
      private static const LINKAGE:String = "HBEnemyRendererUI";
      
      private static const INV_RENDERERS_COUNT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
       
      
      public var hiddenEnemiesCounter:HBEnemiesCounter = null;
      
      protected var container:Sprite;
      
      private var _renderersCount:uint = 0;
      
      private var _dataProvider:ListDAAPIDataProvider = null;
      
      private var _renderers:Vector.<HBEnemyRenderer>;
      
      private var _enemiesMap:Object;
      
      private var _isChatCommVisible:Boolean = false;
      
      private var _maxHeight:uint = 330.0;
      
      private var _maxRenderers:uint = 10;
      
      private var _enemiesCount:uint = 0;
      
      private var _colorMgr:IColorSchemeManager = null;
      
      public function HBEnemiesList()
      {
         this.container = new Sprite();
         this._renderers = new Vector.<HBEnemyRenderer>();
         this._enemiesMap = {};
         super();
         this._colorMgr = App.colorSchemeMgr;
         this._colorMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         addChild(this.container);
         this.hiddenEnemiesCounter.visible = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.onColorSchemasUpdatedHandler(null);
      }
      
      override protected function onDispose() : void
      {
         this._colorMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
         this._colorMgr = null;
         this.hiddenEnemiesCounter.dispose();
         this.hiddenEnemiesCounter = null;
         this.disposeRenderers();
         removeChild(this.container);
         this.container = null;
         if(this._dataProvider)
         {
            this._dataProvider.removeEventListener(Event.CHANGE,this.onDataProviderChangeHandler);
            this._dataProvider.removeEventListener(ListDataProviderEvent.UPDATE_ITEM,this.onDataProviderUpdateItemHandler);
            this._dataProvider = null;
         }
         App.utils.data.cleanupDynamicObject(this._enemiesMap);
         this._enemiesMap = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         if(this._dataProvider)
         {
            if(isInvalid(INV_RENDERERS_COUNT))
            {
               this.validateRenderersCount();
               this.validateLayout();
               invalidateData();
            }
            if(isInvalid(InvalidationType.DATA))
            {
               this.validateData();
            }
         }
      }
      
      public function getEnemyRender(param1:int) : HBEnemyRenderer
      {
         if(this._enemiesMap.hasOwnProperty(param1.toString()))
         {
            return this._enemiesMap[param1];
         }
         return null;
      }
      
      private function disposeRenderers() : void
      {
         var _loc1_:HBEnemyRenderer = null;
         var _loc2_:int = this._renderers.length - 1;
         while(_loc2_ >= 0)
         {
            _loc1_ = this._renderers[_loc2_];
            this.container.removeChild(_loc1_);
            _loc1_.dispose();
            _loc2_--;
         }
         this._renderers.splice(0,this._renderers.length);
         this._renderers = null;
      }
      
      private function validateLayout() : void
      {
         var _loc2_:HBEnemyRenderer = null;
         var _loc1_:uint = this._renderers.length;
         var _loc3_:uint = 0;
         while(_loc3_ < _loc1_)
         {
            _loc2_ = this._renderers[_loc3_];
            _loc2_.y = _loc3_ * LIST_ITEM_HEIGHT;
            _loc3_++;
         }
         if(_loc2_)
         {
            this.hiddenEnemiesCounter.y = _loc2_.y;
         }
      }
      
      private function validateData() : void
      {
         var _loc2_:HBEnemyRenderer = null;
         var _loc4_:HBEnemyInfoVO = null;
         App.utils.data.cleanupDynamicObject(this._enemiesMap);
         var _loc1_:Array = this._dataProvider.requestItemRange(0,this._dataProvider.length);
         var _loc3_:uint = this._renderers.length;
         var _loc5_:int = 0;
         while(_loc5_ < _loc3_)
         {
            _loc4_ = _loc1_[_loc5_];
            _loc2_ = this._renderers[_loc5_];
            this._enemiesMap[_loc4_.vehicleID] = _loc2_;
            _loc2_.data = _loc4_;
            _loc2_.isChatCommVisibilityEnabled = this._isChatCommVisible;
            _loc5_++;
         }
      }
      
      private function validateRenderersCount() : void
      {
         var _loc2_:HBEnemyRenderer = null;
         var _loc1_:int = this._renderers.length;
         var _loc3_:uint = this._renderersCount;
         while(_loc1_ < _loc3_)
         {
            _loc2_ = App.utils.classFactory.getComponent(LINKAGE,HBEnemyRenderer);
            this.container.addChild(_loc2_);
            this._renderers.push(_loc2_);
            _loc1_++;
         }
         _loc1_ = this._renderers.length - 1;
         while(_loc1_ >= _loc3_)
         {
            _loc2_ = this._renderers[_loc1_];
            _loc2_.dispose();
            this.container.removeChild(_loc2_);
            this._renderers.splice(_loc1_,1);
            _loc1_--;
         }
         var _loc4_:int = this._enemiesCount - this._renderersCount;
         this.hiddenEnemiesCounter.visible = _loc4_ > 0;
         if(_loc4_ > 0)
         {
            this.hiddenEnemiesCounter.count = _loc4_;
         }
      }
      
      public function set maxHeight(param1:int) : void
      {
         if(this._maxHeight != param1 && param1 > MIN_HEIGHT)
         {
            this._maxHeight = param1;
            this._maxRenderers = this._maxHeight / LIST_ITEM_HEIGHT | 0;
            if(this._dataProvider)
            {
               this.renderersCount = Math.min(this._maxRenderers,this._enemiesCount);
            }
         }
      }
      
      public function set isChatCommVisible(param1:Boolean) : void
      {
         var _loc2_:HBEnemyRenderer = null;
         if(this._isChatCommVisible == param1)
         {
            return;
         }
         this._isChatCommVisible = param1;
         for each(_loc2_ in this._renderers)
         {
            _loc2_.isChatCommVisibilityEnabled = this._isChatCommVisible;
         }
      }
      
      public function set dataProvider(param1:ListDAAPIDataProvider) : void
      {
         if(this._dataProvider == param1)
         {
            return;
         }
         if(this._dataProvider)
         {
            this._dataProvider.removeEventListener(Event.CHANGE,this.onDataProviderChangeHandler);
            this._dataProvider.removeEventListener(ListDataProviderEvent.UPDATE_ITEM,this.onDataProviderUpdateItemHandler);
         }
         this._dataProvider = param1;
         this._dataProvider.addEventListener(Event.CHANGE,this.onDataProviderChangeHandler);
         this._dataProvider.addEventListener(ListDataProviderEvent.UPDATE_ITEM,this.onDataProviderUpdateItemHandler);
         this._enemiesCount = this._dataProvider.length;
         this.renderersCount = this._enemiesCount;
      }
      
      protected function set renderersCount(param1:uint) : void
      {
         if(this._renderersCount == param1)
         {
            return;
         }
         this._renderersCount = this._maxRenderers > param1 ? uint(param1) : uint(this._maxRenderers);
         invalidate(INV_RENDERERS_COUNT);
      }
      
      private function onDataProviderChangeHandler(param1:Event) : void
      {
         this._enemiesCount = this._dataProvider.length;
         this.renderersCount = this._enemiesCount;
      }
      
      private function onDataProviderUpdateItemHandler(param1:ListDataProviderEvent) : void
      {
         var _loc2_:HBEnemyInfoVO = HBEnemyInfoVO(param1.data);
         var _loc3_:HBEnemyRenderer = this._renderers[param1.index];
         delete this._enemiesMap[_loc3_.vehicleID];
         this._enemiesMap[_loc2_.vehicleID] = _loc3_;
         _loc3_.data = param1.data;
      }
      
      private function onColorSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this.hiddenEnemiesCounter.isBlindEnabled = this._colorMgr.getIsColorBlindS();
      }
   }
}
