package net.wg.gui.battle.components
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLE_NOTIFICATIONS_TIMER_TYPES;
   import net.wg.gui.battle.components.interfaces.IStatusNotification;
   import net.wg.gui.battle.components.interfaces.IStatusNotificationCallback;
   import net.wg.gui.battle.views.destroyTimers.ResupplyTimer;
   import net.wg.gui.battle.views.destroyTimers.SecondaryTimer;
   import net.wg.gui.battle.views.destroyTimers.StatusNotificationTimer;
   import net.wg.gui.battle.views.destroyTimers.data.NotificationTimerSettingVO;
   import net.wg.gui.battle.views.destroyTimers.data.StatusNotificationVO;
   import net.wg.gui.battle.views.destroyTimers.data.StatusNotificationsPanelInitVO;
   import net.wg.infrastructure.base.meta.IStatusNotificationsPanelMeta;
   import net.wg.infrastructure.base.meta.impl.StatusNotificationsPanelMeta;
   
   public class StatusNotificationsPanel extends StatusNotificationsPanelMeta implements IStatusNotificationsPanelMeta
   {
      
      protected static const INVALID_STATE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const NOTIFICATION_TIMERS_OFFSET_X:uint = 25;
      
      private static const MAX_TIMERS_COUNT_EXTRA_SMALL:uint = 2;
      
      private static const MAX_TIMERS_COUNT_SMALL:uint = 3;
      
      private static const MAX_TIMERS_COUNT_MEDIUM:uint = 4;
      
      private static const MAX_TIMERS_COUNT_BIG:uint = 5;
      
      private static const STAGE_SIZE_WIDTH_1730:uint = 1730;
      
      private static const STAGE_SIZE_WIDTH_1495:uint = 1495;
      
      private static const STAGE_SIZE_WIDTH_1220:uint = 1220;
      
      public static const ZONE_DAMAGE_EVENT_TYPE:String = "zoneDamageEvent";
       
      
      public var notificationsContainer:Sprite = null;
      
      private var _stageWidth:int = 0;
      
      private var _stageHeight:int = 0;
      
      private var _notificationTimers:Object = null;
      
      private var _data:Vector.<StatusNotificationVO> = null;
      
      private var _additionalTopOffset:int = 0;
      
      private var _callbacksByType:Dictionary;
      
      private var _additionalNotificationsOffset:int = 0;
      
      private var _tempTimersArr:Array;
      
      private var _tempNewNotifsArr:Array;
      
      private var _tempNewHash:Object;
      
      private var _tempCurrentHash:Object;
      
      private var _tempVisibleHash:Object;
      
      public function StatusNotificationsPanel()
      {
         this._callbacksByType = new Dictionary();
         this._tempTimersArr = [];
         this._tempNewNotifsArr = [];
         this._tempNewHash = {};
         this._tempCurrentHash = {};
         this._tempVisibleHash = {};
         super();
         this._additionalNotificationsOffset = this.getNotificationsOffset();
         this._notificationTimers = {};
         this._data = new Vector.<StatusNotificationVO>(0);
      }
      
      private static function fillStatusNotificationDataHash(param1:Object, param2:Vector.<StatusNotificationVO>) : void
      {
         var _loc3_:* = null;
         var _loc4_:StatusNotificationVO = null;
         for(_loc3_ in param1)
         {
            delete param1[_loc3_];
         }
         for each(_loc4_ in param2)
         {
            param1[_loc4_.typeID] = _loc4_;
         }
      }
      
      override public function isCompVisible() : Boolean
      {
         return alpha == 1;
      }
      
      override public function setCompVisible(param1:Boolean) : void
      {
         alpha = !!param1 ? Number(1) : Number(0);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALID_STATE))
         {
            x = this._stageWidth >> 1;
            y = (this._stageHeight >> 1) + this._additionalTopOffset | 0;
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseChildren = false;
         mouseEnabled = false;
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:BattleUIComponent = null;
         var _loc2_:Vector.<IStatusNotificationCallback> = null;
         var _loc3_:* = null;
         for each(_loc1_ in this._notificationTimers)
         {
            _loc1_.stop();
            _loc1_.dispose();
            this.notificationsContainer.removeChild(_loc1_);
         }
         this.notificationsContainer = null;
         this._notificationTimers = null;
         this._data = null;
         this._tempTimersArr.length = 0;
         this._tempTimersArr = null;
         this._tempNewNotifsArr.length = 0;
         this._tempNewNotifsArr = null;
         this._tempNewHash = null;
         this._tempCurrentHash = null;
         this._tempVisibleHash = null;
         _loc2_ = null;
         for(_loc3_ in this._callbacksByType)
         {
            _loc2_ = this._callbacksByType[_loc3_];
            if(_loc2_)
            {
               _loc2_.length = 0;
               this._callbacksByType[_loc3_] = null;
            }
         }
         this._callbacksByType = null;
         super.onDispose();
      }
      
      override protected function setData(param1:Vector.<StatusNotificationVO>) : void
      {
         if(!param1.length)
         {
            this.updateData(param1);
            App.utils.scheduler.cancelTask(this.updateData);
         }
         else
         {
            App.utils.scheduler.scheduleTask(this.updateData,20,param1);
         }
      }
      
      override protected function setInitData(param1:StatusNotificationsPanelInitVO) : void
      {
         var _loc3_:IStatusNotification = null;
         var _loc6_:NotificationTimerSettingVO = null;
         var _loc7_:IStatusNotificationCallback = null;
         var _loc8_:String = null;
         var _loc2_:Vector.<NotificationTimerSettingVO> = param1.settings;
         var _loc4_:Vector.<String> = null;
         var _loc5_:Vector.<IStatusNotificationCallback> = null;
         for each(_loc6_ in _loc2_)
         {
            _loc3_ = App.utils.classFactory.getComponent(_loc6_.linkage,IStatusNotification);
            _loc3_.setSettings(_loc6_);
            _loc3_.visible = false;
            this.notificationsContainer.addChild(DisplayObject(_loc3_));
            this._notificationTimers[_loc6_.typeId] = _loc3_;
            _loc7_ = _loc3_.getStatusCallback();
            if(_loc7_)
            {
               _loc4_ = _loc7_.getCallbackTypes();
               for each(_loc8_ in _loc4_)
               {
                  _loc5_ = this._callbacksByType[_loc8_] = this._callbacksByType[_loc8_] || new Vector.<IStatusNotificationCallback>(0);
                  _loc5_.push(_loc7_);
               }
            }
         }
         invalidateState();
      }
      
      public function as_setSpeed(param1:Number) : void
      {
         var _loc2_:IStatusNotification = null;
         for each(_loc2_ in this._notificationTimers)
         {
            _loc2_.setSpeed(param1);
         }
      }
      
      public function as_setVerticalOffset(param1:int) : void
      {
         if(this._additionalTopOffset != param1)
         {
            this._additionalTopOffset = param1;
            invalidate(INVALID_STATE);
         }
      }
      
      public function notifyZoneDamage() : void
      {
         this.invokeStatusCallbacks(ZONE_DAMAGE_EVENT_TYPE);
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         this._stageWidth = param1;
         this._stageHeight = param2;
         invalidate(INVALID_STATE);
         this.updtateNotificationsVisible();
      }
      
      protected function handleFirstTimer(param1:IStatusNotification) : Boolean
      {
         param1.cropSize();
         return true;
      }
      
      protected function getNotificationsOffset() : int
      {
         return Values.ZERO;
      }
      
      protected function getNotifications() : Object
      {
         return this._notificationTimers;
      }
      
      private function updateData(param1:Vector.<StatusNotificationVO>) : void
      {
         var _loc4_:StatusNotificationVO = null;
         var _loc5_:IStatusNotification = null;
         this._tempTimersArr.length = 0;
         this._tempNewNotifsArr.length = 0;
         fillStatusNotificationDataHash(this._tempNewHash,param1);
         fillStatusNotificationDataHash(this._tempCurrentHash,this._data);
         var _loc2_:uint = param1.length;
         this._data.length = _loc2_;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this._data[_loc3_] = param1[_loc3_];
            _loc3_++;
         }
         for each(_loc4_ in this._tempNewHash)
         {
            this._tempTimersArr.push(this._notificationTimers[_loc4_.typeID]);
            if(!Boolean(this._tempCurrentHash[_loc4_.typeID]))
            {
               this._tempNewNotifsArr.push(this.showNotification(_loc4_));
            }
            else
            {
               this.updateNotification(_loc4_);
            }
         }
         for each(_loc4_ in this._tempCurrentHash)
         {
            if(!Boolean(this._tempNewHash[_loc4_.typeID]))
            {
               this.hideNotification(_loc4_);
            }
         }
         if(this._tempTimersArr.length == 1)
         {
            _loc5_ = this._tempTimersArr[0];
            _loc5_.fullSize();
            if(this._tempNewNotifsArr.indexOf(_loc5_) == -1)
            {
               _loc5_.tweenToX(0);
            }
            else
            {
               _loc5_.x = 0;
            }
            return;
         }
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         for each(_loc5_ in this._tempTimersArr)
         {
            if(_loc5_.isShowing)
            {
               if(_loc9_ > 0)
               {
                  _loc6_ = _loc5_.cropSize();
                  if(_loc6_ && !_loc7_)
                  {
                     _loc8_ -= NOTIFICATION_TIMERS_OFFSET_X;
                  }
                  _loc7_ = _loc6_;
               }
               else if(!_loc5_ is SecondaryTimer && !_loc5_ is ResupplyTimer || _loc5_.typeId == BATTLE_NOTIFICATIONS_TIMER_TYPES.ORANGE_ZONE || _loc5_.typeId == BATTLE_NOTIFICATIONS_TIMER_TYPES.DAMAGING_ZONE || _loc5_ is StatusNotificationTimer)
               {
                  _loc5_.fullSize();
               }
               else
               {
                  _loc7_ = this.handleFirstTimer(_loc5_);
               }
               _loc9_++;
               if(this._tempNewNotifsArr.indexOf(_loc5_) == -1)
               {
                  if(_loc5_.x != _loc8_)
                  {
                     _loc5_.tweenToX(_loc8_);
                  }
               }
               else
               {
                  _loc5_.x = _loc8_;
               }
               _loc8_ += _loc5_.actualWidth + this._additionalNotificationsOffset;
            }
         }
         this.updtateNotificationsVisible();
      }
      
      private function updtateNotificationsVisible() : void
      {
         var _loc1_:IStatusNotification = null;
         var _loc4_:StatusNotificationVO = null;
         fillStatusNotificationDataHash(this._tempVisibleHash,this._data);
         var _loc2_:uint = 1;
         var _loc3_:uint = MAX_TIMERS_COUNT_BIG;
         if(this._stageWidth <= STAGE_SIZE_WIDTH_1730 && this._stageWidth >= STAGE_SIZE_WIDTH_1495)
         {
            _loc3_ = MAX_TIMERS_COUNT_MEDIUM;
         }
         else if(this._stageWidth <= STAGE_SIZE_WIDTH_1495 && this._stageWidth >= STAGE_SIZE_WIDTH_1220)
         {
            _loc3_ = MAX_TIMERS_COUNT_SMALL;
         }
         else if(this._stageWidth <= STAGE_SIZE_WIDTH_1220)
         {
            _loc3_ = MAX_TIMERS_COUNT_EXTRA_SMALL;
         }
         for each(_loc4_ in this._tempVisibleHash)
         {
            _loc1_ = this._notificationTimers[_loc4_.typeID];
            _loc1_.visible = !Boolean(_loc2_ > _loc3_);
            _loc2_++;
         }
      }
      
      private function showNotification(param1:StatusNotificationVO) : IStatusNotification
      {
         var _loc2_:IStatusNotification = this._notificationTimers[param1.typeID];
         App.utils.asserter.assertNotNull(_loc2_,Errors.CANT_NULL + " typeID: " + param1.typeID);
         _loc2_.isActive = true;
         this.updateNotification(param1);
         _loc2_.showTimer(true);
         _loc2_.visible = true;
         invalidate(INVALID_STATE);
         return _loc2_;
      }
      
      private function updateNotification(param1:StatusNotificationVO) : void
      {
         var _loc2_:IStatusNotification = this._notificationTimers[param1.typeID];
         _loc2_.updateData(param1);
      }
      
      private function hideNotification(param1:StatusNotificationVO) : void
      {
         var _loc2_:IStatusNotification = this._notificationTimers[param1.typeID];
         if(!_loc2_)
         {
            return;
         }
         _loc2_.resetTimer();
         _loc2_.isActive = false;
         _loc2_.hideTimer();
         invalidate(INVALID_STATE);
      }
      
      private function invokeStatusCallbacks(param1:String) : void
      {
         var _loc3_:IStatusNotificationCallback = null;
         var _loc2_:Vector.<IStatusNotificationCallback> = this._callbacksByType[param1];
         if(_loc2_)
         {
            for each(_loc3_ in _loc2_)
            {
               _loc3_.invoke(param1);
            }
         }
      }
   }
}
