package net.wg.gui.components.crosshairPanel.components.coolantAbility
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class CoolantAbilityIndicator extends SimpleContainer
   {
      
      public static const ACTIVATED:String = "abilityActivated";
      
      public static const DEACTIVATED:String = "abilityDeactivated";
      
      private static const FRACTIONAL_FORMAT_CMD:String = "getFractionalFormat";
      
      private static const PENALTY_TWEEN_TIME:uint = 400;
      
      private static const PENALTY_VALUE_TWEEN_TIME:uint = 500;
      
      private static const BG_TWEEN_TIME:uint = 400;
      
      private static const BG_TWEEN_DELAY:uint = 500;
      
      private static const DIFF_TEXT_TWEEN_TIME:uint = 600;
      
      private static const DIFF_TEXT_TWEEN_DELAY:uint = 400;
      
      private static const ABILITY_MOD_TWEEN_TIME:uint = 400;
      
      private static const PENALTY_HIDDEN_OFFSET:int = 10;
       
      
      public var abilityModMc:MovieClip = null;
      
      public var penaltyMc:MovieClip = null;
      
      private var _penaltyTf:TextField = null;
      
      private var _penaltyActiveTf:TextField = null;
      
      private var _diffTf:TextField = null;
      
      private var _activeBg:MovieClip = null;
      
      private var _penalty:Number = 0;
      
      private var _penaltyTweenValue:Number = 0;
      
      private var _baseReloadingTime:Number = 0;
      
      private var _diffTextInitialY:Number = 0;
      
      private var _activePenaltyTimeoutTween:Tween = null;
      
      private var _penaltyValueTween:Tween = null;
      
      private var _penaltyMcTween:Tween = null;
      
      private var _diffTextTween:Tween = null;
      
      private var _activeBgTween:Tween = null;
      
      private var _abilityModTween:Tween = null;
      
      private var _hidden:Boolean = true;
      
      public function CoolantAbilityIndicator()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.penaltyMc.x = PENALTY_HIDDEN_OFFSET;
         this._penaltyTf = this.penaltyMc.penaltyTf;
         this._diffTf = this.penaltyMc.diffTf;
         this._diffTextInitialY = this._diffTf.y;
         this._activeBg = this.penaltyMc.activeBg;
         this._penaltyActiveTf = this._activeBg.penaltyActiveTf;
         this.penaltyMc.alpha = this.abilityModMc.alpha = this._activeBg.alpha = Values.ZERO;
      }
      
      override protected function onDispose() : void
      {
         this.clearAbilityModTween();
         this.clearActivePenaltyTimeoutTween();
         this.clearPenaltyValueTween();
         this.clearPenaltyMcTween();
         this.clearActiveBgTween();
         this.clearDiffTextTween();
         this._penaltyTf = null;
         this._penaltyActiveTf = null;
         this._diffTf = null;
         this._activeBg = null;
         this.abilityModMc = null;
         this.penaltyMc = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this._penaltyTf.text = this.formatValue(this._penaltyTweenValue);
            this._penaltyActiveTf.text = this._penaltyTf.text;
         }
      }
      
      public function updateReloadingPenalty(param1:Number) : void
      {
         var diff:Number = NaN;
         var value:Number = param1;
         if(this._penalty == value)
         {
            return;
         }
         if(this._penalty == Values.ZERO)
         {
            dispatchEvent(new Event(ACTIVATED));
            this._baseReloadingTime = value;
            this.abilityModMc.alpha = Values.ZERO;
            this._penaltyTf.text = this.formatValue(value);
            this.showPenalty();
         }
         else if(value == Values.ZERO)
         {
            dispatchEvent(new Event(DEACTIVATED));
            this.hidePenalty();
            if(this._penalty > this._baseReloadingTime)
            {
               this.showAbilityMod();
            }
            this._baseReloadingTime = Values.ZERO;
         }
         else
         {
            diff = value - this._penalty;
            if(diff > Values.ZERO)
            {
               this.clearActivePenaltyTimeoutTween();
               this._activePenaltyTimeoutTween = new Tween(DIFF_TEXT_TWEEN_TIME + DIFF_TEXT_TWEEN_DELAY,this,{},{"onComplete":function():void
               {
                  activatePenalty(value);
               }});
               this._diffTf.text = Values.PLUS + this.formatValue(diff);
               this.showDiffText();
            }
         }
         this._penalty = value;
      }
      
      public function showAbilityMod() : void
      {
         if(this._hidden)
         {
            this._hidden = false;
            this.clearAbilityModTween();
            this._abilityModTween = new Tween(ABILITY_MOD_TWEEN_TIME,this.abilityModMc,{"alpha":Values.DEFAULT_ALPHA},{"ease":Cubic.easeOut});
         }
      }
      
      public function hideAbilityMod() : void
      {
         if(!this._hidden)
         {
            this._hidden = true;
            this.clearAbilityModTween();
            this._abilityModTween = new Tween(ABILITY_MOD_TWEEN_TIME,this.abilityModMc,{"alpha":Values.ZERO},{"ease":Cubic.easeOut});
         }
      }
      
      private function formatValue(param1:Number) : String
      {
         return ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param1]);
      }
      
      private function activatePenalty(param1:Number) : void
      {
         this.clearPenaltyValueTween();
         this._penaltyValueTween = new Tween(PENALTY_VALUE_TWEEN_TIME,this,{"penaltyTweenValue":param1},{"onComplete":this.hideActiveBg});
         this.showActiveBg();
      }
      
      private function showActiveBg() : void
      {
         this.clearActiveBgTween();
         this._activeBgTween = new Tween(BG_TWEEN_TIME,this._activeBg,{"alpha":Values.DEFAULT_ALPHA},{"ease":Cubic.easeOut});
      }
      
      private function hideActiveBg() : void
      {
         this.clearActiveBgTween();
         this._activeBgTween = new Tween(BG_TWEEN_TIME,this._activeBg,{"alpha":Values.ZERO},{
            "ease":Cubic.easeOut,
            "delay":BG_TWEEN_DELAY
         });
      }
      
      private function showPenalty() : void
      {
         this.clearPenaltyMcTween();
         this._penaltyMcTween = new Tween(PENALTY_TWEEN_TIME,this.penaltyMc,{
            "x":Values.ZERO,
            "alpha":Values.DEFAULT_ALPHA
         },{"ease":Cubic.easeOut});
      }
      
      private function hidePenalty() : void
      {
         this.clearPenaltyMcTween();
         this._penaltyMcTween = new Tween(PENALTY_TWEEN_TIME,this.penaltyMc,{
            "x":PENALTY_HIDDEN_OFFSET,
            "alpha":Values.ZERO
         },{"ease":Cubic.easeOut});
      }
      
      private function showDiffText() : void
      {
         this.clearDiffTextTween();
         this._diffTf.y = this._diffTextInitialY;
         this._diffTf.alpha = Values.ZERO;
         this._diffTextTween = new Tween(DIFF_TEXT_TWEEN_TIME,this._diffTf,{"alpha":Values.DEFAULT_ALPHA},{
            "ease":Cubic.easeOut,
            "onComplete":this.moveDiffTextUp
         });
      }
      
      private function moveDiffTextUp() : void
      {
         this.clearDiffTextTween();
         this._diffTextTween = new Tween(DIFF_TEXT_TWEEN_TIME,this._diffTf,{
            "y":Values.ZERO,
            "alpha":Values.ZERO
         },{
            "ease":Cubic.easeOut,
            "delay":DIFF_TEXT_TWEEN_DELAY
         });
      }
      
      private function clearActivePenaltyTimeoutTween() : void
      {
         if(this._activePenaltyTimeoutTween)
         {
            this._activePenaltyTimeoutTween.dispose();
            this._activePenaltyTimeoutTween = null;
         }
      }
      
      private function clearActiveBgTween() : void
      {
         if(this._activeBgTween)
         {
            this._activeBgTween.dispose();
            this._activeBgTween = null;
         }
      }
      
      private function clearAbilityModTween() : void
      {
         if(this._abilityModTween)
         {
            this._abilityModTween.dispose();
            this._abilityModTween = null;
         }
      }
      
      private function clearPenaltyMcTween() : void
      {
         if(this._penaltyMcTween)
         {
            this._penaltyMcTween.dispose();
            this._penaltyMcTween = null;
         }
      }
      
      private function clearDiffTextTween() : void
      {
         if(this._diffTextTween)
         {
            this._diffTextTween.dispose();
            this._diffTextTween = null;
         }
      }
      
      private function clearPenaltyValueTween() : void
      {
         if(this._penaltyValueTween)
         {
            this._penaltyValueTween.dispose();
            this._penaltyValueTween = null;
         }
      }
      
      public function get penaltyTweenValue() : Number
      {
         return this._penaltyTweenValue;
      }
      
      public function set penaltyTweenValue(param1:Number) : void
      {
         if(this._penaltyTweenValue == param1)
         {
            return;
         }
         this._penaltyTweenValue = param1;
         invalidateData();
      }
   }
}
