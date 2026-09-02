package net.wg.gui.battle.views.damagePanel.components.modules
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.text.TextField;
   import flash.utils.getTimer;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Time;
   import net.wg.data.constants.generated.BATTLE_DEVICES_REPAIR_MODES;
   import net.wg.data.constants.generated.BATTLE_ITEM_STATES;
   import net.wg.gui.battle.events.RepairAnimEvent;
   import net.wg.gui.battle.views.damagePanel.components.DamagePanelItemFrameStates;
   import net.wg.gui.utils.FrameHelper;
   
   public class ModuleRepairAnim extends DamagePanelItemFrameStates
   {
      
      private static const REPAIR_ANIM_COUNT_FRAMES:int = 42;
      
      private static const FIRST_FRAME_REPAIR_ANIM:int = 1;
      
      private static const DEFAULT_PLAYBACK_SPEED:int = 1;
      
      private static const IS_REPAIRING_INVALID_MASK:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const PERCENTS_100:int = 100;
      
      private static const PAUSED_ANIM_SPEED:Number = 0.0001;
      
      private static const MS_PER_TENTH:Number = Time.MILLISECOND_IN_SECOND / 10;
      
      private static const LBL_END_POSTFIX:String = "_end";
      
      private static const LBL_REPAIRED_END:String = BATTLE_ITEM_STATES.REPAIRED + LBL_END_POSTFIX;
      
      private static const LBL_REPAIRED_FULL_END:String = BATTLE_ITEM_STATES.REPAIRED_FULL + LBL_END_POSTFIX;
      
      private static const LBL_REPAIRED_FULL_HIDE:String = BATTLE_ITEM_STATES.REPAIRED_FULL + "_hide";
      
      private static const DECIMAL_SEPARATOR:String = ".";
       
      
      public var repairTimeTF:TextField;
      
      public var highlightRepairTimeTF:TextField;
      
      public var warningMc:Sprite;
      
      private var _showRepairTimer:Boolean = false;
      
      private var _startTime:int;
      
      private var _animDuration:int;
      
      private var _playbackSpeed:Number = 1;
      
      private var _repairPercents:int = 0;
      
      private var _isRepairing:Boolean = false;
      
      private var _needsHighlightText:Boolean = false;
      
      private var _needsShowWarning:Boolean = false;
      
      private var _frameHelper:FrameHelper = null;
      
      private var _needsApplyLocalPercents:Boolean = false;
      
      private var _lastDisplayedTenths:int = -1;
      
      private var _progressListenerAdded:Boolean = false;
      
      public function ModuleRepairAnim()
      {
         super();
         stop();
         this.repairTimeTF.visible = false;
         this.highlightRepairTimeTF.visible = false;
         this._frameHelper = new FrameHelper(this);
         this._frameHelper.addScriptToFrame(this._frameHelper.getFrameByLabel(LBL_REPAIRED_END),this.repairAnimEndHandler);
         this._frameHelper.addScriptToFrame(this._frameHelper.getFrameByLabel(LBL_REPAIRED_FULL_END),this.repairFullAnimEndHandler);
         this._frameHelper.addScriptToFrame(this._frameHelper.getFrameByLabel(LBL_REPAIRED_FULL_HIDE),this.repairFullAnimHideHandler);
      }
      
      override protected function onDispose() : void
      {
         this.stopProgressUpdates();
         this.repairTimeTF = null;
         this.highlightRepairTimeTF = null;
         this.warningMc = null;
         this._frameHelper.dispose();
         this._frameHelper = null;
         super.onDispose();
      }
      
      override protected function applyState() : void
      {
         stop();
         if(state == BATTLE_ITEM_STATES.CRITICAL || state == BATTLE_ITEM_STATES.DESTROYED)
         {
            gotoAndStop(state);
         }
         else
         {
            gotoAndPlay(state);
         }
      }
      
      override protected function calcVisibility() : Boolean
      {
         return state != BATTLE_ITEM_STATES.DESTROYED && state != BATTLE_ITEM_STATES.NORMAL && state != BATTLE_ITEM_STATES.CRITICAL;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(IS_REPAIRING_INVALID_MASK))
         {
            if(!this._isRepairing && (state == BATTLE_ITEM_STATES.REPAIRED || state == BATTLE_ITEM_STATES.REPAIRED_FULL))
            {
               this.updateElementsVisibility();
            }
            else
            {
               visible = this._isRepairing;
            }
         }
      }
      
      private function onProgressEnterFrameHandler(param1:Event) : void
      {
         var _loc2_:int = getTimer() - this._startTime;
         this._repairPercents = Math.min(PERCENTS_100 * _loc2_ / this._animDuration,PERCENTS_100);
         if(this._repairPercents >= PERCENTS_100)
         {
            this.setRepairing(false);
            return;
         }
         gotoAndStop(this.currentRepairFrame(this._repairPercents));
         var _loc3_:int = this._animDuration - _loc2_;
         var _loc4_:int = _loc3_ * this._playbackSpeed / MS_PER_TENTH | 0;
         if(_loc4_ != this._lastDisplayedTenths)
         {
            this._lastDisplayedTenths = _loc4_;
            this.updateElementsVisibility(_loc4_);
         }
      }
      
      private function startProgressUpdates() : void
      {
         if(!this._progressListenerAdded && App.stage)
         {
            App.stage.addEventListener(Event.ENTER_FRAME,this.onProgressEnterFrameHandler,false,0,true);
            this._progressListenerAdded = true;
         }
      }
      
      private function stopProgressUpdates() : void
      {
         if(this._progressListenerAdded && App.stage)
         {
            App.stage.removeEventListener(Event.ENTER_FRAME,this.onProgressEnterFrameHandler);
         }
         this._progressListenerAdded = false;
      }
      
      public function setPlaybackSpeed(param1:Number) : void
      {
         var _loc2_:int = 0;
         var _loc3_:Number = NaN;
         if(param1 < PAUSED_ANIM_SPEED)
         {
            param1 = PAUSED_ANIM_SPEED;
         }
         if(this._isRepairing)
         {
            _loc2_ = getTimer();
            _loc3_ = this._playbackSpeed / param1;
            this._startTime = _loc2_ - (_loc2_ - this._startTime) * _loc3_;
            this._animDuration *= _loc3_;
         }
         this._playbackSpeed = param1;
      }
      
      public function setRepairSeconds(param1:int, param2:int, param3:int = 0) : void
      {
         if(param2 <= 0)
         {
            this.setRepairing(false);
            return;
         }
         this.setRepairing(true);
         param2 /= this._playbackSpeed;
         var _loc4_:int = param1 * (param2 / (PERCENTS_100 - param1));
         var _loc5_:int = getTimer();
         this._startTime = _loc5_ - _loc4_;
         this._animDuration = _loc5_ + param2 - this._startTime;
         this._needsHighlightText = param3 == BATTLE_DEVICES_REPAIR_MODES.SLOWED;
         this._needsShowWarning = param3 == BATTLE_DEVICES_REPAIR_MODES.SUSPENDED;
         if(!this._needsApplyLocalPercents && this._needsShowWarning)
         {
            this._needsApplyLocalPercents = true;
         }
         else if(!this._needsShowWarning)
         {
            this._needsApplyLocalPercents = false;
         }
         if(!this._needsApplyLocalPercents)
         {
            this._repairPercents = param1;
         }
      }
      
      public function setRepairTimeVisible(param1:Boolean) : void
      {
         this._showRepairTimer = param1;
      }
      
      private function repairFullAnimEndHandler() : void
      {
         this.dispatchRepairAnimComplete();
      }
      
      private function repairAnimEndHandler() : void
      {
         this.dispatchRepairAnimComplete();
      }
      
      private function repairFullAnimHideHandler() : void
      {
         dispatchEvent(new RepairAnimEvent(RepairAnimEvent.ANIM_HIDE));
      }
      
      private function dispatchRepairAnimComplete() : void
      {
         this._repairPercents = 0;
         this._needsApplyLocalPercents = false;
         dispatchEvent(new RepairAnimEvent(RepairAnimEvent.ANIM_COMPLETE));
      }
      
      private function currentRepairFrame(param1:int) : int
      {
         return FIRST_FRAME_REPAIR_ANIM + param1 * REPAIR_ANIM_COUNT_FRAMES / PERCENTS_100 | 0;
      }
      
      private function setRepairing(param1:Boolean) : void
      {
         if(this._isRepairing == param1)
         {
            return;
         }
         this._isRepairing = param1;
         if(param1)
         {
            this.startProgressUpdates();
         }
         else
         {
            this.stopProgressUpdates();
            this._repairPercents = 0;
            this._lastDisplayedTenths = -1;
            this.repairTimeTF.visible = false;
            this.highlightRepairTimeTF.visible = false;
            this.warningMc.visible = false;
         }
         invalidate(IS_REPAIRING_INVALID_MASK);
      }
      
      private function updateElementsVisibility(param1:int = -1) : void
      {
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:String = null;
         var _loc2_:Boolean = this._showRepairTimer && this._isRepairing;
         var _loc3_:Boolean = _loc2_ && !this._needsShowWarning;
         this.highlightRepairTimeTF.visible = _loc3_ && this._needsHighlightText;
         this.repairTimeTF.visible = _loc3_ && !this._needsHighlightText;
         this.warningMc.visible = _loc2_ && this._needsShowWarning;
         if(_loc3_ && param1 >= 0)
         {
            _loc4_ = param1 / 10;
            _loc5_ = param1 % 10;
            _loc6_ = _loc4_ + DECIMAL_SEPARATOR + _loc5_;
            if(this._needsHighlightText)
            {
               this.highlightRepairTimeTF.text = _loc6_;
            }
            else
            {
               this.repairTimeTF.text = _loc6_;
            }
         }
      }
      
      override public function set state(param1:String) : void
      {
         setStateManually(param1);
         this.setRepairing(false);
      }
   }
}
