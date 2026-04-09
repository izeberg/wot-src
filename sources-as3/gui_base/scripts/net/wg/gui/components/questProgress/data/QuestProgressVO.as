package net.wg.gui.components.questProgress.data
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.QUEST_PROGRESS_BASE;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.components.questProgress.interfaces.data.IHeaderProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQPProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQuestProgressData;
   import net.wg.gui.components.questProgress.interfaces.data.IQuestProgressItemData;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class QuestProgressVO extends DAAPIDataClass implements IQuestProgressData
   {
      
      private static const BODY_PROGRESS_FIELD_NAME:String = "bodyProgress";
      
      private static const HEADER_PROGRESS_FIELD_NAME:String = "headerProgress";
       
      
      private var _questName:String = "";
      
      private var _questIndexStr:String = "";
      
      private var _questIcon:String = "";
      
      private var _questID:int = -1;
      
      private var _bodyItemsMap:Dictionary = null;
      
      private var _isQPActive:Boolean = false;
      
      private var _headerConditions:Vector.<IHeaderProgressData> = null;
      
      private var _secondHeaderConditions:Vector.<IHeaderProgressData> = null;
      
      private var _bodyProgressData:Vector.<IQuestProgressItemData> = null;
      
      private var _secondBodyProgressData:Vector.<IQuestProgressItemData> = null;
      
      private var _isHeaderHasProgress:Boolean = false;
      
      private var _isSecondHeaderHasProgress:Boolean = true;
      
      private var _isMainOnly:Boolean = true;
      
      public function QuestProgressVO(param1:Object = null)
      {
         super(param1);
         this._isQPActive = Boolean(this._bodyProgressData);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Array = null;
         var _loc4_:QuestProgressItemVO = null;
         var _loc5_:Object = null;
         var _loc6_:Array = null;
         if(param1 == BODY_PROGRESS_FIELD_NAME)
         {
            if(param2 != null)
            {
               _loc3_ = param2 as Array;
               App.utils.asserter.assertNotNull(_loc3_,BODY_PROGRESS_FIELD_NAME + Errors.INVALID_TYPE + Array);
               this._bodyProgressData = new Vector.<IQuestProgressItemData>();
               this._secondBodyProgressData = new Vector.<IQuestProgressItemData>();
               this._bodyItemsMap = new Dictionary();
               for each(_loc5_ in _loc3_)
               {
                  _loc4_ = new QuestProgressItemVO(_loc5_);
                  if(_loc4_.initData.groupID > QUEST_PROGRESS_BASE.DEFAULT_GROUP_ID)
                  {
                     this._secondBodyProgressData.push(_loc4_);
                  }
                  else
                  {
                     this._bodyProgressData.push(_loc4_);
                  }
                  this._bodyItemsMap[_loc4_.id] = _loc4_;
               }
            }
            return false;
         }
         if(param1 == HEADER_PROGRESS_FIELD_NAME)
         {
            _loc6_ = param2 as Array;
            App.utils.asserter.assertNotNull(_loc6_,HEADER_PROGRESS_FIELD_NAME + Errors.INVALID_TYPE + Array);
            this.fillHeaderItems(_loc6_);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         if(this._bodyProgressData)
         {
            for each(_loc1_ in this._bodyProgressData)
            {
               _loc1_.dispose();
            }
            this._bodyProgressData.splice(0,this._bodyProgressData.length);
            this._bodyProgressData = null;
         }
         if(this._secondBodyProgressData)
         {
            for each(_loc1_ in this._secondBodyProgressData)
            {
               _loc1_.dispose();
            }
            this._secondBodyProgressData.splice(0,this._secondBodyProgressData.length);
            this._secondBodyProgressData = null;
         }
         this.clearHeaderConditions();
         App.utils.data.cleanupDynamicObject(this._bodyItemsMap);
         this._bodyItemsMap = null;
         super.onDispose();
      }
      
      public function getData() : Vector.<IQuestProgressItemData>
      {
         return this._bodyProgressData;
      }
      
      public function getDataItem(param1:String) : IQuestProgressItemData
      {
         return param1 in this._bodyItemsMap ? this._bodyItemsMap[param1] : null;
      }
      
      public function getSecondData() : Vector.<IQuestProgressItemData>
      {
         return this._secondBodyProgressData;
      }
      
      public function parseProgressData(param1:String, param2:Object) : IQPProgressData
      {
         var _loc3_:IQuestProgressItemData = this.getDataItem(param1);
         App.utils.asserter.assertNotNull(_loc3_,"Item data for id" + param1 + Errors.WASNT_FOUND);
         return _loc3_.parseProgressData(param2);
      }
      
      public function updateHeaderProgressData(param1:Array) : void
      {
         this.clearHeaderConditions();
         this.fillHeaderItems(param1);
      }
      
      public function updateProgressData(param1:String, param2:IQPProgressData) : void
      {
         var _loc3_:IQuestProgressItemData = this.getDataItem(param1);
         App.utils.asserter.assertNotNull(_loc3_,"Item data for id" + param1 + Errors.WASNT_FOUND);
         _loc3_.updateProgressData(param2);
      }
      
      private function fillHeaderItems(param1:Array) : void
      {
         var _loc2_:HeaderProgressDataVO = null;
         var _loc3_:Object = null;
         this._headerConditions = new Vector.<IHeaderProgressData>();
         this._secondHeaderConditions = new Vector.<IHeaderProgressData>();
         for each(_loc3_ in param1)
         {
            _loc2_ = new HeaderProgressDataVO(_loc3_);
            this.addHeaderItem(_loc2_);
         }
         if(!this._headerConditions.length)
         {
            this._isHeaderHasProgress = false;
         }
         if(!this._secondHeaderConditions.length)
         {
            this._isSecondHeaderHasProgress = false;
         }
      }
      
      private function addHeaderItem(param1:HeaderProgressDataVO) : void
      {
         if(param1.groupID > QUEST_PROGRESS_BASE.DEFAULT_GROUP_ID)
         {
            this._secondHeaderConditions.push(param1);
            this._isSecondHeaderHasProgress = this._isSecondHeaderHasProgress && param1.progressType != QUEST_PROGRESS_BASE.HEADER_PROGRESS_TYPE_NONE;
         }
         else
         {
            this._headerConditions.push(param1);
            this._isHeaderHasProgress = this._isHeaderHasProgress || param1.progressType != QUEST_PROGRESS_BASE.HEADER_PROGRESS_TYPE_NONE;
         }
         this._isMainOnly = this._isMainOnly && param1.orderType == QUEST_PROGRESS_BASE.MAIN_ORDER_TYPE;
      }
      
      private function clearHeaderConditions() : void
      {
         var _loc1_:IDisposable = null;
         this._isHeaderHasProgress = true;
         this._isSecondHeaderHasProgress = true;
         this._isMainOnly = true;
         if(this._headerConditions)
         {
            for each(_loc1_ in this._headerConditions)
            {
               _loc1_.dispose();
            }
            this._headerConditions.splice(0,this._headerConditions.length);
            this._headerConditions = null;
         }
         if(this._secondHeaderConditions)
         {
            for each(_loc1_ in this._secondHeaderConditions)
            {
               _loc1_.dispose();
            }
            this._secondHeaderConditions.splice(0,this._secondHeaderConditions.length);
            this._secondHeaderConditions = null;
         }
      }
      
      public function get headerConditions() : Vector.<IHeaderProgressData>
      {
         return this._headerConditions;
      }
      
      public function get secondHeaderConditions() : Vector.<IHeaderProgressData>
      {
         return this._secondHeaderConditions;
      }
      
      public function get questName() : String
      {
         return this._questName;
      }
      
      public function set questName(param1:String) : void
      {
         this._questName = param1;
      }
      
      public function get questIndexStr() : String
      {
         return this._questIndexStr;
      }
      
      public function set questIndexStr(param1:String) : void
      {
         this._questIndexStr = param1;
      }
      
      public function get questIcon() : String
      {
         return this._questIcon;
      }
      
      public function set questIcon(param1:String) : void
      {
         this._questIcon = param1;
      }
      
      public function get isActiveData() : Boolean
      {
         return this._questIndexStr != Values.EMPTY_STR;
      }
      
      public function get isQPActive() : Boolean
      {
         return this._isQPActive;
      }
      
      public function get questID() : int
      {
         return this._questID;
      }
      
      public function set questID(param1:int) : void
      {
         this._questID = param1;
      }
      
      public function get isHeaderHasProgress() : Boolean
      {
         return this._isHeaderHasProgress;
      }
      
      public function get isSecondHeaderHasProgress() : Boolean
      {
         return this._isSecondHeaderHasProgress;
      }
      
      public function get isMainOnly() : Boolean
      {
         return this._isMainOnly;
      }
   }
}
