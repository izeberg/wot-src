package net.wg.gui.components.crosshairPanel.components
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.utils.clearTimeout;
   import flash.utils.setTimeout;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CROSSHAIR_CONSTANTS;
   import net.wg.gui.components.crosshairPanel.CrosshairPanelEvent;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class ShotDamageInd extends SimpleDisposable
   {
      
      private static const ANIM_SPEED:int = 20;
      
      private static const TIMEOUT_APPLY_VALUE:int = 2000;
      
      private static const STATUS_HIGH:int = 8;
      
      private static const STATUS_NORMAL:int = 2;
      
      private static const STATUS_DISABLED:int = 1;
      
      private static const CURSOR_ANIM_START:int = 2;
      
      private static const HIGH_STATUS_VALUE:int = 140;
       
      
      public var dmgProgress:MovieClip = null;
      
      public var dmgStatus:MovieClip = null;
      
      private var _timeoutId:uint = 0;
      
      private var _cursor:MovieClip = null;
      
      private var _currentValue:int = 0;
      
      private var _animValue:int = 0;
      
      private var _dmgStatusId:int = 1;
      
      public function ShotDamageInd()
      {
         super();
         this._cursor = this.dmgProgress.cursor;
         this.updateStatus();
      }
      
      override protected function onDispose() : void
      {
         this.dmgProgress.removeEventListener(Event.ENTER_FRAME,this.onDmgProgressEnterFrameHandler);
         this.clearTimeoutId();
         this._cursor = null;
         this.dmgStatus = null;
         this.dmgProgress = null;
         super.onDispose();
      }
      
      public function setValue(param1:int) : void
      {
         param1 *= 2;
         if(this._currentValue == param1)
         {
            return;
         }
         this._currentValue = param1;
         this.clearTimeoutId();
         if(this._currentValue == Values.ZERO)
         {
            this._timeoutId = setTimeout(this.updateDmgProgress,TIMEOUT_APPLY_VALUE);
         }
         else
         {
            this.updateDmgProgress();
         }
      }
      
      private function updateStatus() : void
      {
         var _loc1_:int = 0;
         if(this._animValue > 1)
         {
            _loc1_ = this._animValue >= HIGH_STATUS_VALUE ? int(STATUS_HIGH) : int(STATUS_NORMAL);
            if(this._dmgStatusId != _loc1_)
            {
               this._dmgStatusId = _loc1_;
               this.dmgStatus.gotoAndPlay(this._dmgStatusId);
               if(visible && _loc1_ == STATUS_HIGH)
               {
                  dispatchEvent(new CrosshairPanelEvent(CrosshairPanelEvent.SOUND,CROSSHAIR_CONSTANTS.SOUND_INDICATOR_MAX_DAMAGE));
               }
            }
         }
         else
         {
            this._dmgStatusId = STATUS_DISABLED;
            this.dmgStatus.gotoAndStop(this._dmgStatusId);
         }
      }
      
      private function updateDmgProgress() : void
      {
         this.dmgProgress.addEventListener(Event.ENTER_FRAME,this.onDmgProgressEnterFrameHandler);
         if(this._animValue < this._currentValue)
         {
            this._animValue = this.dmgProgress.currentFrame + 1;
            this.dmgProgress.gotoAndStop(this._animValue);
         }
         else if(this._animValue > this._currentValue)
         {
            this._animValue = this.dmgProgress.currentFrame - 1;
            this.dmgProgress.gotoAndStop(this._animValue);
         }
      }
      
      private function clearTimeoutId() : void
      {
         clearTimeout(this._timeoutId);
         this._timeoutId = 0;
      }
      
      private function onDmgProgressEnterFrameHandler(param1:Event) : void
      {
         if(this._currentValue < this._animValue)
         {
            this._animValue -= ANIM_SPEED;
            if(this._animValue <= this._currentValue)
            {
               if(this._animValue > 1)
               {
                  this._cursor.gotoAndPlay(CURSOR_ANIM_START);
               }
               this._animValue = this._currentValue;
               this.dmgProgress.removeEventListener(Event.ENTER_FRAME,this.onDmgProgressEnterFrameHandler);
            }
         }
         else
         {
            this._animValue += ANIM_SPEED;
            if(this._animValue >= this._currentValue)
            {
               this._animValue = this._currentValue;
               this._cursor.gotoAndPlay(CURSOR_ANIM_START);
               this.dmgProgress.removeEventListener(Event.ENTER_FRAME,this.onDmgProgressEnterFrameHandler);
            }
         }
         this.dmgProgress.gotoAndStop(this._animValue);
         this.updateStatus();
      }
   }
}
