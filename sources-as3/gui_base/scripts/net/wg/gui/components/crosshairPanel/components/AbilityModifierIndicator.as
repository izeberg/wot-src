package net.wg.gui.components.crosshairPanel.components
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class AbilityModifierIndicator extends SimpleContainer
   {
      
      private static const MODIFIER_VALUE_TEMPLATE:String = "+value%";
      
      private static const MODIFIER_VALUE_TWEEN_TIME:uint = 500;
      
      private static const GLOW_TWEEN_TIME:uint = 300;
      
      private static const GLOW_TWEEN_DELAY:uint = 1300;
      
      private static const THIS_TWEEN_TIME:uint = 300;
      
      public static const Y_OFFSET:int = -14;
       
      
      public var modifierValueMc:MovieClip = null;
      
      public var glowMc:MovieClip = null;
      
      public var bgMc:MovieClip = null;
      
      private var _modifierValueTf:TextField = null;
      
      private var _modifierValue:int = 0;
      
      private var _modifierValueCounterTween:Tween = null;
      
      private var _glowTween:Tween = null;
      
      private var _thisTween:Tween = null;
      
      public function AbilityModifierIndicator()
      {
         super();
         this._modifierValueTf = this.modifierValueMc.tf;
         this.hideThis();
      }
      
      override protected function onDispose() : void
      {
         this.clearModifierValueCounterTween();
         this.clearGlowTween();
         this.clearThisTween();
         this._modifierValueTf = null;
         this.modifierValueMc = null;
         this.glowMc = null;
         this.bgMc = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this._modifierValueTf.text = MODIFIER_VALUE_TEMPLATE.replace("value",this.modifierValue);
         }
      }
      
      private function clearModifierValueCounterTween() : void
      {
         if(this._modifierValueCounterTween)
         {
            this._modifierValueCounterTween.dispose();
            this._modifierValueCounterTween = null;
         }
      }
      
      private function clearGlowTween() : void
      {
         if(this._glowTween)
         {
            this._glowTween.dispose();
            this._glowTween = null;
         }
      }
      
      private function clearThisTween() : void
      {
         if(this._thisTween)
         {
            this._thisTween.dispose();
            this._thisTween = null;
         }
      }
      
      private function showGlow(param1:Boolean = false) : void
      {
         this.clearGlowTween();
         if(param1)
         {
            this.glowMc.alpha = Values.DEFAULT_ALPHA;
            this.hideGlow(false);
         }
         else
         {
            this._glowTween = new Tween(GLOW_TWEEN_TIME,this.glowMc,{"alpha":Values.DEFAULT_ALPHA},{
               "ease":Cubic.easeOut,
               "onComplete":this.hideGlow
            });
         }
      }
      
      private function hideGlow(param1:Boolean = true) : void
      {
         this.clearGlowTween();
         if(param1)
         {
            this._glowTween = new Tween(GLOW_TWEEN_TIME,this.glowMc,{"alpha":Values.ZERO},{
               "ease":Cubic.easeOut,
               "delay":GLOW_TWEEN_DELAY
            });
         }
         else
         {
            this.glowMc.alpha = Values.ZERO;
         }
      }
      
      private function hideThis() : void
      {
         this.clearThisTween();
         this.alpha = Values.ZERO;
         this.modifierValue = Values.ZERO;
      }
      
      public function show(param1:int, param2:Boolean = false) : void
      {
         this.clearThisTween();
         if(this.alpha < Values.DEFAULT_ALPHA)
         {
            if(param2)
            {
               this.alpha = Values.DEFAULT_ALPHA;
            }
            else
            {
               this._thisTween = new Tween(THIS_TWEEN_TIME,this,{"alpha":Values.DEFAULT_ALPHA},{"ease":Cubic.easeOut});
            }
         }
         this.clearModifierValueCounterTween();
         if(param2)
         {
            this.modifierValue = param1;
         }
         else
         {
            this._modifierValueCounterTween = new Tween(MODIFIER_VALUE_TWEEN_TIME,this,{"modifierValue":param1});
         }
         validateNow();
         this.showGlow(param2);
      }
      
      public function hide(param1:Boolean = false) : void
      {
         this.clearThisTween();
         if(param1)
         {
            this.hideThis();
         }
         else
         {
            this._thisTween = new Tween(THIS_TWEEN_TIME,this,{"alpha":Values.ZERO},{
               "ease":Cubic.easeOut,
               "onComplete":this.hideThis
            });
         }
      }
      
      public function get modifierValue() : int
      {
         return this._modifierValue;
      }
      
      public function set modifierValue(param1:int) : void
      {
         if(this._modifierValue == param1)
         {
            return;
         }
         this._modifierValue = param1;
         invalidateData();
      }
   }
}
