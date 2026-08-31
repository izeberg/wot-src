package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.infrastructure.base.meta.ISightPointerWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.SightPointerWidgetMeta;
   
   public class SightPointerWidget extends SightPointerWidgetMeta implements ISightPointerWidgetMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.IDLE];
      
      private static const HIGHLIGHT_FRAME:String = "highlight";
      
      private static const HOT_KEY_START_POS_X:int = 0;
      
      private static const HOT_KEY_START_POS_Y:int = 0;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
       
      
      public var hotkeyTarget:MovieClip = null;
      
      public var reverseProgress:MovieClip = null;
      
      public var forwardProgress:MovieClip = null;
      
      public var indicator:MovieClip = null;
      
      public var cone:MovieClip = null;
      
      private var _isHighlightLocked:Boolean = false;
      
      private var _pendingState:String = "hide";
      
      private var _highlightScriptFrame:int = -1;
      
      public function SightPointerWidget()
      {
         super();
         this.blendMode = BlendMode.SCREEN;
         var _loc1_:Array = this.indicator.currentLabels;
         var _loc2_:int = _loc1_.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            if(FrameLabel(_loc1_[_loc3_]).name == HIGHLIGHT_FRAME)
            {
               this._highlightScriptFrame = _loc3_ + 1 < _loc2_ ? int(FrameLabel(_loc1_[_loc3_ + 1]).frame - 1) : int(this.indicator.totalFrames - 1);
               break;
            }
            _loc3_++;
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
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),true,HotkeySettings.DIRECTION_DOWN,Values.ZERO,HOT_KEY_GAP_Y);
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return this.hotkeyTarget;
      }
      
      override protected function onDispose() : void
      {
         if(this._highlightScriptFrame >= 0)
         {
            this.indicator.addFrameScript(this._highlightScriptFrame,null);
         }
         this.forwardProgress = null;
         this.reverseProgress = null;
         this.cone = null;
         this.indicator = null;
         this.hotkeyTarget = null;
         super.onDispose();
      }
      
      public function as_setProgress(param1:Number, param2:Number) : void
      {
         var _loc3_:int = param1 * WidgetsPanel.FORWARD_PROGRESSION_MAX_FRAME;
         var _loc4_:int = param1 * WidgetsPanel.REVERES_PROGRESSION_MAX_FRAME;
         this.reverseProgress.gotoAndStop(_loc4_);
         this.forwardProgress.gotoAndStop(_loc3_);
      }
      
      public function as_setTankIconState(param1:String) : void
      {
         this._pendingState = param1;
         if(this._isHighlightLocked)
         {
            return;
         }
         this.applyConeState(param1);
      }
      
      public function as_triggerHighlightLamp() : void
      {
         if(this._highlightScriptFrame < 0)
         {
            return;
         }
         this._isHighlightLocked = true;
         this.indicator.addFrameScript(this._highlightScriptFrame,this.onHighlightComplete);
         this.applyConeState(HIGHLIGHT_FRAME);
      }
      
      private function onHighlightComplete() : void
      {
         this.indicator.addFrameScript(this._highlightScriptFrame,null);
         this._isHighlightLocked = false;
         this.applyConeState(this._pendingState);
      }
      
      private function applyConeState(param1:String) : void
      {
         this.cone.gotoAndPlay(param1);
         this.indicator.gotoAndPlay(param1);
      }
   }
}
