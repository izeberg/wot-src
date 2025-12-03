package net.wg.gui.battle.views.consumablesPanel
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.utils.IScheduler;
   import scaleform.clik.motion.Tween;
   
   public class BattleAbilityModifierIndicator extends BattleUIComponent
   {
      
      private static const SLOT_VALUE_OFFSET_WITHOUT_TYPE:int = -11;
      
      private static const SLOT_FRAME_LABEL:String = "slot_";
      
      private static const SLOT_FRAME_SMALL_RESOLUTION_POSTFIX:String = "_small";
      
      private static const MODIFIER_VALUE_TEMPLATE:String = "+value%";
      
      private static const INVALIDATE_DRAW_LAYOUT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const INVALIDATE_MODIFIER_VALUE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const HIDE_TWEEN_Y_OFFSET:int = 10;
      
      private static const THIS_TWEEN_TIME:uint = 300;
      
      private static const SLOTS_GLOW_TWEEN_TIME:uint = 300;
      
      private static const SLOTS_GLOW_TWEEN_DELAY:uint = 1300;
      
      private static const SLOTS_GLOW_TASK_DELAY:uint = SLOTS_GLOW_TWEEN_DELAY + SLOTS_GLOW_TWEEN_TIME;
      
      private static const MODIFIER_VALUE_TWEEN_TIME:uint = 500;
       
      
      public var slotsModifierType:MovieClip = null;
      
      public var slotsModifierValue:MovieClip = null;
      
      public var slotsFrame:MovieClip = null;
      
      public var slotsGlowContainer:MovieClip = null;
      
      public var hitMc:MovieClip = null;
      
      public var bg:MovieClip = null;
      
      private var _slotsGlows:Vector.<MovieClip>;
      
      private var _slotsModifierValueIcon:MovieClip = null;
      
      private var _slotsModifierValueTf:TextField = null;
      
      private var _modifierValue:int = 0;
      
      private var _shellPadding:int = 0;
      
      private var _shellSlots:int = 0;
      
      private var _isSmall:Boolean = false;
      
      private var _hasHover:Boolean = false;
      
      private var _isExtendedAnim:Boolean = false;
      
      private var _scheduler:IScheduler;
      
      private var _thisInitialY:int = 0;
      
      private var _slotsModifierTypeInitialY:int = 0;
      
      private var _thisTween:Tween = null;
      
      private var _slotsGlowTween:Tween = null;
      
      private var _slotsModifierTypeTween:Tween = null;
      
      private var _modifierValueTween:Tween = null;
      
      public function BattleAbilityModifierIndicator()
      {
         this._scheduler = App.utils.scheduler;
         super();
         this._thisInitialY = this.y;
         this._slotsModifierTypeInitialY = this.slotsModifierType.y;
         this.slotsModifierType.y = this._slotsModifierTypeInitialY + HIDE_TWEEN_Y_OFFSET;
         this.slotsModifierType.tf.autoSize = TextFieldAutoSize.LEFT;
         this._slotsModifierValueIcon = this.slotsModifierValue.icon;
         this._slotsModifierValueTf = this.slotsModifierValue.tf;
         this.slotsGlowContainer.alpha = this.slotsModifierType.alpha = Values.ZERO;
         this.hideThis();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.hitMc.addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         this.hitMc.addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
      }
      
      private function onMouseOverHandler(param1:MouseEvent) : void
      {
         this.hasHover = true;
      }
      
      private function onMouseOutHandler(param1:MouseEvent) : void
      {
         this.hasHover = false;
      }
      
      override protected function onDispose() : void
      {
         this.hitMc.removeEventListener(MouseEvent.MOUSE_OVER,this.onMouseOverHandler);
         this.hitMc.removeEventListener(MouseEvent.MOUSE_OUT,this.onMouseOutHandler);
         this.hitMc = null;
         this._scheduler.cancelTask(this.hideSlotsGlow);
         this._scheduler.cancelTask(this.hideSlotsModifierType);
         this._scheduler = null;
         this.clearThisTween();
         this.clearSlotsModifierTypeTween();
         this.clearSlotsGlowTween();
         this.clearModifierValueTween();
         if(this._slotsGlows)
         {
            this._slotsGlows.splice(0,this._slotsGlows.length);
            this._slotsGlows = null;
         }
         this._slotsModifierValueIcon = null;
         this._slotsModifierValueTf = null;
         this.slotsModifierType = null;
         this.slotsModifierValue = null;
         this.slotsFrame = null;
         this.slotsGlowContainer = null;
         this.bg = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALIDATE_DRAW_LAYOUT))
         {
            this.drawLayout();
         }
         if(isInvalid(INVALIDATE_MODIFIER_VALUE))
         {
            this.updateSlotsModifierValueText();
         }
      }
      
      private function drawLayout() : void
      {
         var _loc2_:int = 0;
         var _loc3_:MovieClip = null;
         var _loc1_:String = SLOT_FRAME_LABEL + this.shellSlots;
         this.slotsFrame.gotoAndStop(!!this.isSmall ? _loc1_ + SLOT_FRAME_SMALL_RESOLUTION_POSTFIX : _loc1_);
         this.bg.x = this.shellPadding * this.shellSlots - this.bg.width >> 1;
         this.slotsModifierType.x = this.shellPadding * this.shellSlots - this.slotsModifierType.width >> 1;
         this.slotsModifierValue.x = this.shellPadding * this.shellSlots - this.slotsModifierValue.width >> 1;
         this._slotsModifierValueIcon.visible = this.shellSlots > 1;
         if(!this._slotsModifierValueIcon.visible)
         {
            this.slotsModifierValue.x += SLOT_VALUE_OFFSET_WITHOUT_TYPE;
         }
         if(!this._slotsGlows)
         {
            this._slotsGlows = new Vector.<MovieClip>();
            _loc2_ = 0;
            while(_loc2_ < this.shellSlots)
            {
               _loc3_ = App.utils.classFactory.getComponent(Linkages.ABILITY_MODIFIER_SLOT_GLOW,MovieClip);
               this.slotsGlowContainer.addChild(_loc3_);
               this._slotsGlows.push(_loc3_);
               _loc2_++;
            }
         }
         _loc2_ = 0;
         while(_loc2_ < this.shellSlots)
         {
            this._slotsGlows[_loc2_].x = _loc2_ * this.shellPadding;
            _loc2_++;
         }
         this.hitMc.width = this.slotsGlowContainer.width;
      }
      
      private function clearThisTween() : void
      {
         if(this._thisTween)
         {
            this._thisTween.dispose();
            this._thisTween = null;
         }
      }
      
      private function clearSlotsGlowTween() : void
      {
         if(this._slotsGlowTween)
         {
            this._slotsGlowTween.dispose();
            this._slotsGlowTween = null;
         }
      }
      
      private function clearSlotsModifierTypeTween() : void
      {
         if(this._slotsModifierTypeTween)
         {
            this._slotsModifierTypeTween.dispose();
            this._slotsModifierTypeTween = null;
         }
      }
      
      private function clearModifierValueTween() : void
      {
         if(this._modifierValueTween)
         {
            this._modifierValueTween.dispose();
            this._modifierValueTween = null;
         }
      }
      
      private function showSlotsGlow() : void
      {
         this.clearSlotsGlowTween();
         if(this._isExtendedAnim)
         {
            this._slotsGlowTween = new Tween(SLOTS_GLOW_TWEEN_TIME,this.slotsGlowContainer,{"alpha":Values.DEFAULT_ALPHA},{
               "ease":Cubic.easeOut,
               "onComplete":this.hideSlotsGlow
            });
         }
         else
         {
            this.slotsGlowContainer.alpha = Values.DEFAULT_ALPHA;
            this.hideSlotsGlow();
         }
      }
      
      private function hideSlotsGlow(param1:Boolean = true) : void
      {
         this.clearSlotsGlowTween();
         if(this._isExtendedAnim)
         {
            this._slotsGlowTween = new Tween(SLOTS_GLOW_TWEEN_TIME,this.slotsGlowContainer,{"alpha":Values.ZERO},{
               "ease":Cubic.easeOut,
               "delay":(!!param1 ? SLOTS_GLOW_TWEEN_DELAY : Values.ZERO)
            });
         }
         else if(param1)
         {
            this._scheduler.scheduleTask(this.hideSlotsGlow,SLOTS_GLOW_TASK_DELAY,false);
         }
         else
         {
            this._scheduler.cancelTask(this.hideSlotsModifierType);
            this.slotsGlowContainer.alpha = Values.ZERO;
         }
         if(!this.hasHover)
         {
            this.hideSlotsModifierType(param1);
         }
      }
      
      private function hideThis() : void
      {
         this.clearThisTween();
         this.alpha = Values.ZERO;
         this.visible = false;
      }
      
      private function updateSlotsModifierValueText() : void
      {
         this._slotsModifierValueTf.text = MODIFIER_VALUE_TEMPLATE.replace("value",this.modifierValue);
      }
      
      public function show(param1:int, param2:Boolean = false) : void
      {
         if(!this.visible)
         {
            this.y = this._thisInitialY;
            this.visible = true;
            this.clearThisTween();
            if(param2 || !this._isExtendedAnim)
            {
               this.alpha = Values.DEFAULT_ALPHA;
            }
            else
            {
               this._thisTween = new Tween(THIS_TWEEN_TIME,this,{"alpha":Values.DEFAULT_ALPHA},{"ease":Cubic.easeOut});
            }
         }
         this.clearModifierValueTween();
         if(param2 || !this._isExtendedAnim)
         {
            this.modifierValue = param1;
         }
         else
         {
            this._modifierValueTween = new Tween(MODIFIER_VALUE_TWEEN_TIME,this,{"modifierValue":param1});
         }
         validateNow();
         this.showSlotsGlow();
         this.showSlotsModifierType();
      }
      
      public function hide(param1:Boolean = false) : void
      {
         this.clearThisTween();
         if(param1 || !this._isExtendedAnim)
         {
            this.hideThis();
         }
         else
         {
            this._thisTween = new Tween(THIS_TWEEN_TIME,this,{
               "alpha":Values.ZERO,
               "y":HIDE_TWEEN_Y_OFFSET
            },{
               "ease":Cubic.easeOut,
               "onComplete":this.hideThis
            });
         }
      }
      
      public function showSlotsModifierType() : void
      {
         this.clearSlotsModifierTypeTween();
         if(this._isExtendedAnim)
         {
            this._slotsModifierTypeTween = new Tween(SLOTS_GLOW_TWEEN_TIME,this.slotsModifierType,{
               "alpha":Values.DEFAULT_ALPHA,
               "y":this._slotsModifierTypeInitialY
            },{"ease":Cubic.easeOut});
         }
         else
         {
            this.slotsModifierType.alpha = Values.DEFAULT_ALPHA;
            this.slotsModifierType.y = this._slotsModifierTypeInitialY;
         }
      }
      
      public function hideSlotsModifierType(param1:Boolean = true) : void
      {
         this.clearSlotsModifierTypeTween();
         if(this._isExtendedAnim)
         {
            this._slotsModifierTypeTween = new Tween(SLOTS_GLOW_TWEEN_TIME,this.slotsModifierType,{
               "alpha":Values.ZERO,
               "y":this._slotsModifierTypeInitialY + HIDE_TWEEN_Y_OFFSET
            },{
               "ease":Cubic.easeOut,
               "delay":(!!param1 ? SLOTS_GLOW_TWEEN_DELAY : Values.ZERO)
            });
         }
         else if(param1)
         {
            this._scheduler.scheduleTask(this.hideSlotsModifierType,SLOTS_GLOW_TASK_DELAY,false);
         }
         else
         {
            this._scheduler.cancelTask(this.hideSlotsModifierType);
            this.slotsModifierType.alpha = Values.ZERO;
            this.slotsModifierType.y = this._slotsModifierTypeInitialY + HIDE_TWEEN_Y_OFFSET;
         }
      }
      
      public function updateAnimationsSettings(param1:Boolean) : void
      {
         this._isExtendedAnim = param1;
      }
      
      public function set hasHover(param1:Boolean) : void
      {
         if(this._hasHover == param1)
         {
            return;
         }
         this._hasHover = param1;
         if(this._hasHover)
         {
            this.showSlotsModifierType();
         }
         else
         {
            this.hideSlotsModifierType(false);
         }
      }
      
      public function get hasHover() : Boolean
      {
         return this._hasHover;
      }
      
      public function get shellPadding() : int
      {
         return this._shellPadding;
      }
      
      public function set shellPadding(param1:int) : void
      {
         if(this._shellPadding == param1)
         {
            return;
         }
         this._shellPadding = param1;
         invalidate(INVALIDATE_DRAW_LAYOUT);
      }
      
      public function get shellSlots() : int
      {
         return this._shellSlots;
      }
      
      public function set shellSlots(param1:int) : void
      {
         if(this._shellSlots == param1)
         {
            return;
         }
         this._shellSlots = param1;
         invalidate(INVALIDATE_DRAW_LAYOUT);
      }
      
      public function get isSmall() : Boolean
      {
         return this._isSmall;
      }
      
      public function set isSmall(param1:Boolean) : void
      {
         if(this._isSmall == param1)
         {
            return;
         }
         this._isSmall = param1;
         invalidate(INVALIDATE_DRAW_LAYOUT);
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
         invalidate(INVALIDATE_MODIFIER_VALUE);
      }
   }
}
