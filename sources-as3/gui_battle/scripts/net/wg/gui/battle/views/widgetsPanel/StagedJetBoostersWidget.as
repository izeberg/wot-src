package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.data.constants.generated.STAGED_JET_BOOSTERS_CONSTS;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.infrastructure.base.meta.IStagedJetBoostersWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.StagedJetBoostersWidgetMeta;
   
   public class StagedJetBoostersWidget extends StagedJetBoostersWidgetMeta implements IStagedJetBoostersWidgetMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [];
      
      private static const BALLOON_Y:int = -3;
      
      private static const BALLOON_H_FULL:int = 42;
      
      private static const HOT_KEY_START_POS_X:int = -3;
      
      private static const HOT_KEY_START_POS_Y:int = 12;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
      
      public static const DIRECTION:uint = 1 << 7;
      
      private static const ARROW_INACTIVE:String = "inactive";
      
      private static const ARROW_ACTIVE:String = "active";
      
      private static const STATE_COOLDOWN:String = "cooldown";
       
      
      public var countTF:TextField;
      
      public var balloonMask:MovieClip;
      
      public var hotkeyTarget:MovieClip = null;
      
      public var leftArrowActive:MovieClip = null;
      
      public var rightArrowActive:MovieClip = null;
      
      public var flame:MovieClip = null;
      
      public var _direction:String = "backward";
      
      public var _currentState:String = "cooldown";
      
      public function StagedJetBoostersWidget()
      {
         super();
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         if(this.state == MECHANICS_WIDGET_CONST.IDLE && param1 == MECHANICS_WIDGET_CONST.PREPARING)
         {
            return;
         }
         super.applyState(param1,param2);
         if(param1 == MECHANICS_WIDGET_CONST.ACTIVE || param1 == MECHANICS_WIDGET_CONST.PREPARING)
         {
            invalidate(DIRECTION);
         }
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         this.countTF = null;
         this.balloonMask = null;
         this.hotkeyTarget = null;
         this.leftArrowActive = null;
         this.rightArrowActive = null;
         this.flame = null;
         super.onDispose();
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),true,HotkeySettings.DIRECTION_DOWN,Values.ZERO,HOT_KEY_GAP_Y);
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return this.hotkeyTarget;
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         super.draw();
         if(isInvalid(DIRECTION))
         {
            _loc1_ = STATE_COOLDOWN;
            if(state == MECHANICS_WIDGET_CONST.ACTIVE)
            {
               _loc1_ = this._direction != STAGED_JET_BOOSTERS_CONSTS.BACKWARD ? STAGED_JET_BOOSTERS_CONSTS.FORWARD : STAGED_JET_BOOSTERS_CONSTS.BACKWARD;
               this.leftArrowActive.gotoAndStop(ARROW_INACTIVE);
               this.rightArrowActive.gotoAndStop(ARROW_INACTIVE);
               if(this._direction == STAGED_JET_BOOSTERS_CONSTS.LEFT)
               {
                  this.leftArrowActive.gotoAndPlay(ARROW_ACTIVE);
               }
               else if(this._direction == STAGED_JET_BOOSTERS_CONSTS.RIGHT)
               {
                  this.rightArrowActive.gotoAndPlay(ARROW_ACTIVE);
               }
            }
            if(_loc1_ && this._currentState != _loc1_)
            {
               this.flame.gotoAndPlay(this._currentState + "_" + _loc1_);
               this._currentState = _loc1_;
            }
         }
      }
      
      public function as_setCount(param1:int) : void
      {
         this.countTF.text = param1.toString();
      }
      
      public function as_setMovementInfo(param1:String) : void
      {
         if(this._direction != param1)
         {
            this._direction = param1;
            invalidate(DIRECTION);
         }
      }
      
      public function as_setProgress(param1:Number) : void
      {
         this.balloonMask.y = BALLOON_Y + BALLOON_H_FULL * (1 - param1) | 0;
      }
      
      public function as_updateLayout(param1:Number, param2:Number) : void
      {
      }
   }
}
