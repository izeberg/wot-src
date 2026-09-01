package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.autoreloaderSurge.AutoreloaderSurgeActionLine;
   import net.wg.gui.battle.views.widgetsPanel.autoreloaderSurge.AutoreloaderSurgeSectors;
   import net.wg.infrastructure.base.meta.IAutoreloaderSurgeWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.AutoreloaderSurgeWidgetMeta;
   
   public class AutoreloaderSurgeWidget extends AutoreloaderSurgeWidgetMeta implements IAutoreloaderSurgeWidgetMeta
   {
      
      private static const ARCADE_X:int = -131;
      
      private static const ARCADE_Y:int = 72;
      
      private static const SNIPER_X:int = -130;
      
      private static const SNIPER_Y:int = 77;
      
      private static const HOTKEYS_OFFSET_X:int = -30;
      
      private static const HOTKEYS_OFFSET_Y:int = -33;
      
      private static const HOTKEYS_CONTAINER_NAME:String = "HotkeysContainer";
      
      private static const HOTKEYS_DIM_ALPHA:Number = 0.2;
      
      private static const TIMER_DEFAULT_ALPHA:Number = 0.6;
      
      private static const REDUCE_LINE_BOOST_FRAME:int = 31;
      
      private static const LABEL_BLINK:String = "blink";
      
      private static const LABEL_SHOW:String = "show";
      
      private static const LABEL_HIDE:String = "hide";
      
      private static const LABEL_ACTIVE:String = "active";
      
      private static const LABEL_PLAY:String = "play";
      
      private static const LABEL_IDLE:String = "idle";
       
      
      public var sectors:AutoreloaderSurgeSectors = null;
      
      public var actionLine:AutoreloaderSurgeActionLine = null;
      
      public var reduceLine:MovieClip = null;
      
      public var buttonGlow:MovieClip = null;
      
      public var timerBlink:MovieClip = null;
      
      public var timerGlow:MovieClip = null;
      
      private var _chargeCount:int = 0;
      
      private var _isAvailable:Boolean = false;
      
      private var _wasActive:Boolean = false;
      
      private var _isBoosted:Boolean = false;
      
      private var _hotkeysContainer:Sprite;
      
      public function AutoreloaderSurgeWidget()
      {
         super();
         this.blendMode = BlendMode.SCREEN;
         timer.alpha = TIMER_DEFAULT_ALPHA;
         this.actionLine.addFrameScript(AutoreloaderSurgeActionLine.GLOW_ANIMATION_FRAME,this.onActionLineComplete);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.getHotKeysTarget().alpha = !!this._isAvailable ? Number(1) : Number(HOTKEYS_DIM_ALPHA);
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            x = crosshairType == CROSSHAIR_VIEW_ID.ARCADE ? Number(ARCADE_X) : Number(SNIPER_X);
            y = crosshairType == CROSSHAIR_VIEW_ID.ARCADE ? Number(ARCADE_Y) : Number(SNIPER_Y);
         }
         if(this._hotkeysContainer)
         {
            this._hotkeysContainer.x = -this._hotkeysContainer.width;
         }
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         super.applyState(param1,param2);
         if(param1 == MECHANICS_WIDGET_CONST.ACTIVE)
         {
            timer.visible = false;
            this._wasActive = true;
            this.sectors.playActivation(this._chargeCount);
            this.actionLine.playFromSector(this._chargeCount);
         }
         else if(this._wasActive)
         {
            this._wasActive = false;
            this.sectors.playRecharge(this._chargeCount);
            this.actionLine.hide();
            this.timerGlow.gotoAndPlay(LABEL_HIDE);
         }
      }
      
      override protected function setStagesProgress(param1:Array) : void
      {
         this.sectors.setProgress(param1);
         var _loc2_:int = -1;
         var _loc3_:int = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            if(param1[_loc4_] > 0 && param1[_loc4_] < 1)
            {
               _loc2_ = _loc4_;
               break;
            }
            _loc4_++;
         }
         this.sectors.setChargingSector(_loc2_);
      }
      
      override protected function onDispose() : void
      {
         this.actionLine.addFrameScript(AutoreloaderSurgeActionLine.GLOW_ANIMATION_FRAME,null);
         this.clearReduceLineScript();
         this.sectors.dispose();
         this.sectors = null;
         this.actionLine.dispose();
         this.actionLine = null;
         this.buttonGlow = null;
         this.timerBlink = null;
         this.reduceLine = null;
         this.timerGlow = null;
         this._hotkeysContainer = null;
         super.onDispose();
      }
      
      override protected function setTimer(param1:Number) : void
      {
         super.setTimer(param1);
         var _loc2_:Boolean = param1 > 0 && state != MECHANICS_WIDGET_CONST.ACTIVE;
         timer.visible = _loc2_;
         if(!_loc2_ && this._isBoosted)
         {
            this._isBoosted = false;
            this.clearReduceLineScript();
            this.reduceLine.gotoAndStop(LABEL_IDLE);
            timer.alpha = TIMER_DEFAULT_ALPHA;
         }
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.PREPARING;
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         return Boolean(super.getHotKeyVisibility() && state != MECHANICS_WIDGET_CONST.ACTIVE);
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         if(!this._hotkeysContainer)
         {
            this._hotkeysContainer = new Sprite();
            this._hotkeysContainer.x = HOTKEYS_OFFSET_X;
            this._hotkeysContainer.y = HOTKEYS_OFFSET_Y;
            this._hotkeysContainer.name = HOTKEYS_CONTAINER_NAME;
            addChild(this._hotkeysContainer);
         }
         return this._hotkeysContainer;
      }
      
      public function as_setChargeCount(param1:Number) : void
      {
         this._chargeCount = int(param1);
      }
      
      public function as_setAvailable(param1:Boolean) : void
      {
         if(this._isAvailable == param1)
         {
            return;
         }
         this._isAvailable = param1;
         invalidateData();
         if(param1)
         {
            this.buttonGlow.gotoAndPlay(LABEL_BLINK);
            this.timerBlink.gotoAndPlay(LABEL_SHOW);
         }
         else
         {
            this.timerBlink.gotoAndPlay(LABEL_HIDE);
         }
      }
      
      public function as_setSectorCount(param1:int) : void
      {
         this.sectors.setup(param1);
         this.actionLine.sectorCount = param1;
      }
      
      public function as_setBoostedCharge(param1:Boolean) : void
      {
         if(param1 && !this._isBoosted)
         {
            timer.alpha = 1;
            this.reduceLine.addFrameScript(REDUCE_LINE_BOOST_FRAME,this.onReduceLineBoostReached);
            this.reduceLine.gotoAndPlay(LABEL_PLAY);
         }
         else if(!param1 && this._isBoosted)
         {
            this.clearReduceLineScript();
            this.reduceLine.gotoAndStop(LABEL_IDLE);
            timer.alpha = TIMER_DEFAULT_ALPHA;
         }
         this._isBoosted = param1;
      }
      
      private function onActionLineComplete() : void
      {
         if(state == MECHANICS_WIDGET_CONST.ACTIVE)
         {
            this.showTimerGlow();
         }
      }
      
      private function showTimerGlow() : void
      {
         this.timerGlow.gotoAndPlay(LABEL_ACTIVE);
      }
      
      private function onReduceLineBoostReached() : void
      {
         this.clearReduceLineScript();
         timer.alpha = 1;
      }
      
      private function clearReduceLineScript() : void
      {
         this.reduceLine.addFrameScript(REDUCE_LINE_BOOST_FRAME,null);
      }
   }
}
