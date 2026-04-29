package net.wg.historical_battles.gui.battle.views.respawn.components
{
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import flash.utils.Timer;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.components.preBattleTimer.TimerAnim;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_TIMER_RESP_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBTimerRespVO;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import net.wg.utils.ICommons;
   
   public class HBTimerResp extends BattleUIComponent implements IUpdatable
   {
      
      private static const TICK_DELAY:int = 1000;
      
      private static const GLOW_WIDTH:int = 800;
       
      
      public var timer:TimerAnim = null;
      
      public var titleTF:TextField = null;
      
      public var labelTF:TextField = null;
      
      public var glow:MovieClip = null;
      
      private var _data:HBTimerRespVO = null;
      
      private var _size:int = 0;
      
      private var _time:int = 0;
      
      private var _delayTimer:Timer = null;
      
      private var _titleTf:TextFormat = null;
      
      private var _labelTf:TextFormat = null;
      
      private var _commons:ICommons;
      
      public function HBTimerResp()
      {
         this._commons = App.utils.commons;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._titleTf = this.titleTF.getTextFormat();
         this._labelTf = this.labelTF.getTextFormat();
         this._delayTimer = new Timer(TICK_DELAY);
         this._delayTimer.addEventListener(TimerEvent.TIMER,this.onDelayTimerHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.validateData();
               invalidateSize();
            }
            if(this._size != HB_STAGE_SIZE.UNDEFINED && isInvalid(InvalidationType.SIZE))
            {
               this.validateLayout();
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this._delayTimer.removeEventListener(TimerEvent.TIMER,this.onDelayTimerHandler);
         this._delayTimer.stop();
         this._delayTimer = null;
         this.timer.dispose();
         this.timer = null;
         this.titleTF = null;
         this.labelTF = null;
         this.glow = null;
         this._data = null;
         this._titleTf = null;
         this._labelTf = null;
         this._commons = null;
         super.onDispose();
      }
      
      public function ownerVisibleChange(param1:Boolean) : void
      {
         if(this._delayTimer)
         {
            this._delayTimer.stop();
         }
         this.timer.ownerVisibleChange(param1);
      }
      
      public function update(param1:Object) : void
      {
         if(this._data != param1)
         {
            this._data = HBTimerRespVO(param1);
            invalidateData();
         }
      }
      
      public function updateSize(param1:int) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            invalidateSize();
         }
      }
      
      private function validateData() : void
      {
         this._delayTimer.stop();
         this.titleTF.text = this._data.title;
         this.labelTF.text = this._data.label;
         this._time = this._data.time;
         if(this._time >= 0)
         {
            this.timer.setTime(this._time,true);
            --this._time;
            this._delayTimer.start();
         }
      }
      
      private function validateLayout() : void
      {
         this._titleTf.size = HB_TIMER_RESP_PROPS.getTitleFontSize(this._size);
         this._labelTf.size = HB_TIMER_RESP_PROPS.getLabelFontSize(this._size);
         this.titleTF.setTextFormat(this._titleTf);
         this.labelTF.setTextFormat(this._labelTf);
         this._commons.updateTextFieldSize(this.titleTF);
         this._commons.updateTextFieldSize(this.labelTF);
         this.timer.scaleX = this.timer.scaleY = HB_TIMER_RESP_PROPS.getTimerScale(this._size);
         this.glow.scaleX = this.glow.scaleY = HB_TIMER_RESP_PROPS.getGlowScale(this._size);
         this.titleTF.x = this.width - this.titleTF.width >> 1;
         this.titleTF.y = HB_TIMER_RESP_PROPS.getTitleY(this._size);
         this.labelTF.x = this.width - this.labelTF.width >> 1;
         this.labelTF.y = HB_TIMER_RESP_PROPS.getLabelY(this._size);
         this.timer.x = this.width >> 1;
         this.glow.y = HB_TIMER_RESP_PROPS.getGlowY(this._size);
      }
      
      override public function get width() : Number
      {
         return GLOW_WIDTH * HB_TIMER_RESP_PROPS.getGlowScale(this._size);
      }
      
      private function onDelayTimerHandler(param1:TimerEvent) : void
      {
         if(this._time >= 0)
         {
            this.timer.setTime(this._time,false);
            --this._time;
         }
         else
         {
            this._delayTimer.stop();
         }
      }
   }
}
