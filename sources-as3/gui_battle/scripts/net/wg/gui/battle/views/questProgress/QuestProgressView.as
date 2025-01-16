package net.wg.gui.battle.views.questProgress
{
   import flash.display.DisplayObject;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.gui.battle.views.questProgress.interfaces.IQuestProgressView;
   import net.wg.gui.components.questProgress.events.QuestProgressComponentEvent;
   import net.wg.gui.components.questProgress.interfaces.components.IQPItemOrConditionIcon;
   import net.wg.gui.components.questProgress.interfaces.components.IQPItemRenderer;
   import net.wg.gui.components.questProgress.interfaces.data.IHeaderProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQPInitData;
   import net.wg.gui.components.questProgress.interfaces.data.IQPProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQuestProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQuestProgressItemData;
   
   public class QuestProgressView extends BattleDisplayable implements IQuestProgressView
   {
      
      private static const INVALID_LAYOUT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
       
      
      private var _questID:int = -1;
      
      private var _items:Vector.<IQPItemRenderer> = null;
      
      private var _secondItems:Vector.<IQPItemRenderer> = null;
      
      private var _orItems:Vector.<IQPItemOrConditionIcon> = null;
      
      private var _isInitCompleted:Boolean = false;
      
      private var _itemsMap:Dictionary = null;
      
      private var _lockedItemsId:Vector.<String> = null;
      
      public function QuestProgressView()
      {
         super();
         this._lockedItemsId = new Vector.<String>();
      }
      
      override protected function onBeforeDispose() : void
      {
         this.removeDynamicData();
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this._lockedItemsId.splice(0,this._lockedItemsId.length);
         this._lockedItemsId = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALID_LAYOUT))
         {
            this.doLayout();
         }
      }
      
      public function addConditionItem(param1:DisplayObject) : void
      {
         addChild(param1);
      }
      
      public function findItemById(param1:String) : IQPItemRenderer
      {
         return param1 in this._itemsMap ? this._itemsMap[param1] : null;
      }
      
      public function hideView(param1:Function, param2:int) : void
      {
      }
      
      public final function init(param1:IQuestProgressData) : void
      {
         if(this._questID != param1.questID)
         {
            this.reset();
            this._questID = param1.questID;
         }
         this.initData(param1);
         this._isInitCompleted = true;
      }
      
      public function playSnd(param1:String) : void
      {
      }
      
      public function removeConditionItem(param1:DisplayObject) : void
      {
         removeChild(param1);
      }
      
      public function showView(param1:Function, param2:int) : void
      {
      }
      
      public final function update(param1:String, param2:IQPProgressData) : void
      {
         this.updateData(param1,param2);
      }
      
      public function updateHeaderProgress(param1:Vector.<IHeaderProgressData>) : void
      {
         this.onUpdateHeaderProgress(param1);
      }
      
      public function updateSecondHeaderProgress(param1:Vector.<IHeaderProgressData>) : void
      {
         this.onUpdateSecondHeaderProgress(param1);
      }
      
      protected function updateData(param1:String, param2:IQPProgressData) : void
      {
         this.updateItemById(param1,param2);
      }
      
      protected function initData(param1:IQuestProgressData) : void
      {
         var _loc2_:IQPItemRenderer = null;
         var _loc3_:IQPItemOrConditionIcon = null;
         if(!this._items)
         {
            this.createItems(param1);
            for each(_loc2_ in this._items)
            {
               this.addConditionItem(DisplayObject(_loc2_));
            }
            for each(_loc2_ in this._secondItems)
            {
               this.addConditionItem(DisplayObject(_loc2_));
            }
            for each(_loc3_ in this._orItems)
            {
               this.addConditionItem(DisplayObject(_loc3_));
            }
         }
         else
         {
            this.updateItems(param1);
         }
         this.invalidateLayout();
      }
      
      protected function reset() : void
      {
         this.removeDynamicData();
         this._isInitCompleted = false;
      }
      
      protected function invalidateLayout() : void
      {
         invalidate(INVALID_LAYOUT);
      }
      
      protected function getViewType() : String
      {
         App.utils.asserter.assert(false,"getViewType" + Errors.ABSTRACT_INVOKE);
         return null;
      }
      
      protected function doLayout() : void
      {
      }
      
      protected function getRendererLinkage() : String
      {
         App.utils.asserter.assert(false,"getRendererLinkage" + Errors.ABSTRACT_INVOKE);
         return null;
      }
      
      protected function getRendererOrLinkage() : String
      {
         App.utils.asserter.assert(false,"getRendererOrLinkage" + Errors.ABSTRACT_INVOKE);
         return null;
      }
      
      protected function isHidden(param1:IQPInitData) : Boolean
      {
         return false;
      }
      
      protected function onUpdateHeaderProgress(param1:Vector.<IHeaderProgressData>) : void
      {
      }
      
      protected function onUpdateSecondHeaderProgress(param1:Vector.<IHeaderProgressData>) : void
      {
      }
      
      protected function hasLockedItems() : Boolean
      {
         return this._lockedItemsId.length > 0;
      }
      
      protected function manageOrBetweenItems() : void
      {
         var _loc1_:IQPItemOrConditionIcon = null;
         if(this._secondItems && this._secondItems.length)
         {
            _loc1_ = App.utils.classFactory.getComponent(this.getRendererOrLinkage(),IQPItemOrConditionIcon);
            _loc1_.setItems(this._items[this._items.length - 1],this._secondItems[0]);
            this._orItems.push(_loc1_);
         }
      }
      
      private function updateItemRenderer(param1:IQPItemRenderer, param2:IQPProgressData) : void
      {
         param1.update(param2);
         var _loc3_:Boolean = param2.isLocked;
         var _loc4_:int = this._lockedItemsId.indexOf(param1.id);
         if(_loc4_ >= 0)
         {
            if(!_loc3_)
            {
               this._lockedItemsId.splice(_loc4_,1);
               this.invalidateLayout();
            }
         }
         else if(_loc3_)
         {
            this._lockedItemsId.push(param1.id);
            this.invalidateLayout();
         }
      }
      
      private function removeDynamicData() : void
      {
         var _loc1_:IQPItemRenderer = null;
         var _loc2_:IQPItemOrConditionIcon = null;
         App.utils.data.cleanupDynamicObject(this._itemsMap);
         this._itemsMap = null;
         if(this._items)
         {
            for each(_loc1_ in this._items)
            {
               this.removeConditionItem(DisplayObject(_loc1_));
               _loc1_.removeEventListener(QuestProgressComponentEvent.LAYOUT_COMPLETED,this.onItemRendererLayoutCompletedHandler);
               _loc1_.dispose();
            }
            this._items.splice(0,this._items.length);
            this._items = null;
         }
         if(this._secondItems)
         {
            for each(_loc1_ in this._secondItems)
            {
               this.removeConditionItem(DisplayObject(_loc1_));
               _loc1_.removeEventListener(QuestProgressComponentEvent.LAYOUT_COMPLETED,this.onItemRendererLayoutCompletedHandler);
               _loc1_.dispose();
            }
            this._secondItems.splice(0,this._secondItems.length);
            this._secondItems = null;
         }
         if(this._orItems)
         {
            for each(_loc2_ in this._orItems)
            {
               this.removeConditionItem(DisplayObject(_loc2_));
            }
            this._orItems.splice(0,this._orItems.length);
            this._orItems = null;
         }
         this._lockedItemsId.splice(0,this._lockedItemsId.length);
      }
      
      private function updateItemById(param1:String, param2:IQPProgressData) : void
      {
         var _loc3_:IQPItemRenderer = this.findItemById(param1);
         if(_loc3_)
         {
            if(_loc3_.isHidden != param2.isHidden)
            {
               this.invalidateLayout();
            }
            this.updateItemRenderer(_loc3_,param2);
         }
      }
      
      private function createItems(param1:IQuestProgressData) : void
      {
         var _loc3_:IQPItemRenderer = null;
         var _loc4_:IQPItemRenderer = null;
         var _loc5_:IQPItemOrConditionIcon = null;
         this._itemsMap = new Dictionary();
         this._items = new Vector.<IQPItemRenderer>(0);
         this._orItems = new Vector.<IQPItemOrConditionIcon>();
         this._secondItems = new Vector.<IQPItemRenderer>(0);
         var _loc2_:Vector.<IQuestProgressItemData> = param1.getSecondData();
         this.initItems(param1.getData(),this._items);
         this.initItems(_loc2_,this._secondItems);
         if(!param1.isSecondHeaderHasProgress && _loc2_ && _loc2_.length)
         {
            _loc3_ = this._items[this._items.length - 1];
            _loc4_ = this._secondItems[0];
            if(_loc3_ && _loc3_.isInOrGroup && _loc4_.isInOrGroup && _loc3_.orderType == _loc4_.orderType)
            {
               _loc5_ = App.utils.classFactory.getComponent(this.getRendererOrLinkage(),IQPItemOrConditionIcon);
               _loc5_.setItems(_loc3_,_loc4_);
               this._orItems.push(_loc5_);
            }
         }
         this.manageOrBetweenItems();
      }
      
      private function initItems(param1:Vector.<IQuestProgressItemData>, param2:Vector.<IQPItemRenderer>) : void
      {
         var _loc5_:IQuestProgressItemData = null;
         var _loc3_:String = this.getViewType();
         var _loc4_:IQPItemRenderer = null;
         for each(_loc5_ in param1)
         {
            if(!this.isHidden(_loc5_.initData))
            {
               _loc4_ = this.initItem(_loc5_,_loc4_,_loc3_,param2);
            }
         }
      }
      
      private function initItem(param1:IQuestProgressItemData, param2:IQPItemRenderer, param3:String, param4:Vector.<IQPItemRenderer>) : IQPItemRenderer
      {
         var _loc6_:IQPItemOrConditionIcon = null;
         var _loc5_:IQPItemRenderer = App.utils.classFactory.getComponent(this.getRendererLinkage(),IQPItemRenderer);
         _loc5_.addEventListener(QuestProgressComponentEvent.LAYOUT_COMPLETED,this.onItemRendererLayoutCompletedHandler);
         _loc5_.viewType = param3;
         _loc5_.id = param1.id;
         _loc5_.init(param1.initData);
         _loc5_.initMetrics(param1.progressData.metricsValue,param1.progressData.state);
         this.updateItemRenderer(_loc5_,param1.progressData);
         _loc5_.validateNow();
         param4.push(_loc5_);
         this._itemsMap[param1.id] = _loc5_;
         if(param2 && param2.isInOrGroup && _loc5_.isInOrGroup && param2.orderType == _loc5_.orderType)
         {
            _loc6_ = App.utils.classFactory.getComponent(this.getRendererOrLinkage(),IQPItemOrConditionIcon);
            _loc6_.setItems(param2,_loc5_);
            this._orItems.push(_loc6_);
         }
         return _loc5_;
      }
      
      private function updateItems(param1:IQuestProgressData) : void
      {
         var _loc2_:IQPItemRenderer = null;
         var _loc4_:IQuestProgressItemData = null;
         var _loc3_:Vector.<IQuestProgressItemData> = param1.getData();
         for each(_loc4_ in _loc3_)
         {
            if(!this.isHidden(_loc4_.initData))
            {
               _loc2_ = this.findItemById(_loc4_.id);
               if(_loc2_)
               {
                  this.updateItemRenderer(_loc2_,_loc4_.progressData);
               }
            }
         }
      }
      
      public function get isQPVisibleBySettings() : Boolean
      {
         return true;
      }
      
      protected function get items() : Vector.<IQPItemRenderer>
      {
         return this._items;
      }
      
      protected function get secondItems() : Vector.<IQPItemRenderer>
      {
         return this._secondItems;
      }
      
      protected function get orItems() : Vector.<IQPItemOrConditionIcon>
      {
         return this._orItems;
      }
      
      protected function get isInitCompleted() : Boolean
      {
         return this._isInitCompleted;
      }
      
      private function onItemRendererLayoutCompletedHandler(param1:QuestProgressComponentEvent) : void
      {
         this.invalidateLayout();
      }
   }
}
