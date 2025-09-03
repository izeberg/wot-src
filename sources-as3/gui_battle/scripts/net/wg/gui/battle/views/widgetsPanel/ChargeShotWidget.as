package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.decorativeCrosshair.shared.TextWrapper;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.infrastructure.base.meta.IChargeShotWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.ChargeShotWidgetMeta;
   
   public class ChargeShotWidget extends ChargeShotWidgetMeta implements IChargeShotWidgetMeta
   {
      
      private static const STACK_MAX_FRAME:uint = 50;
      
      private static const MAX_STACK:uint = 3;
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.IDLE];
      
      private static const OVERHEAT_LOW_THRESHOLD:Number = 0.5;
      
      private static const OVERHEAT_MED_THRESHOLD:Number = 0.8;
      
      private static const LABEL_LOW:String = "low";
      
      private static const LABEL_MED:String = "med";
      
      private static const LABEL_TOP:String = "top";
      
      private static const HOT_KEY_START_POS_X:int = -3;
      
      private static const HOT_KEY_START_POS_Y:int = 12;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
       
      
      public var damageTf:TextWrapper = null;
      
      public var progressMc:MovieClip = null;
      
      public var overheatAlert:MovieClip = null;
      
      public var hotkeyTarget:MovieClip = null;
      
      public var redTimer:Timer;
      
      private var _isOverheat:Boolean = false;
      
      private var _isShootBlock:Boolean = false;
      
      private var _overheatState:String = "";
      
      public function ChargeShotWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         this.overheatAlert = null;
         this.progressMc = null;
         this.damageTf.dispose();
         this.damageTf = null;
         this.redTimer.dispose();
         this.redTimer = null;
         this.hotkeyTarget = null;
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
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      private function setOverheat(param1:Boolean, param2:Number = 0) : void
      {
         var _loc3_:String = null;
         if(this._isShootBlock)
         {
            this.overheatAlert.visible = false;
            return;
         }
         this._isOverheat = param1;
         this.overheatAlert.visible = this._isOverheat;
         timer.visible = true;
         if(param1)
         {
            if(param2 < OVERHEAT_LOW_THRESHOLD)
            {
               _loc3_ = LABEL_LOW;
            }
            else if(param2 < OVERHEAT_MED_THRESHOLD)
            {
               _loc3_ = LABEL_MED;
            }
            else
            {
               _loc3_ = LABEL_TOP;
            }
            if(this._overheatState != _loc3_)
            {
               this._overheatState = _loc3_;
               this.overheatAlert.gotoAndPlay(_loc3_);
            }
         }
         else
         {
            this._overheatState = Values.EMPTY_STR;
         }
      }
      
      private function setShootBlock(param1:Boolean) : void
      {
         if(this._isShootBlock != param1)
         {
            this._isShootBlock = param1;
            this.setOverheat(this._isOverheat);
         }
      }
      
      override protected function setTimer(param1:Number) : void
      {
         this.redTimer.setLabel(param1);
         super.setTimer(param1);
      }
      
      public function as_setUpdateProgress(param1:uint, param2:Number) : void
      {
         var _loc3_:uint = param1 * STACK_MAX_FRAME + STACK_MAX_FRAME * param2;
         this.progressMc.gotoAndStop(_loc3_);
         this.setOverheat(param1 === MAX_STACK,param2);
      }
      
      public function as_setShootBlock(param1:Boolean) : void
      {
         this.setShootBlock(param1);
      }
      
      public function as_showShootBlockAnimation() : void
      {
         if(this._isShootBlock && currentFrame == totalFrames)
         {
            gotoAndPlay(MECHANICS_WIDGET_CONST.DISABLE);
         }
      }
      
      public function as_setDamage(param1:uint) : void
      {
         this.damageTf.setText(param1.toString());
      }
   }
}
