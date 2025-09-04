package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.infrastructure.base.meta.IRocketAcceleratorIndicatorMeta;
   import net.wg.infrastructure.base.meta.impl.RocketAcceleratorIndicatorMeta;
   
   public class RechargeableNitroWidget extends RocketAcceleratorIndicatorMeta implements IRocketAcceleratorIndicatorMeta
   {
      
      private static const INSTANT_TRANSITION_STATES:Array = [MECHANICS_WIDGET_CONST.IDLE];
      
      private static const MAX_FRAMES_COUNT:uint = 100;
      
      private static const FRAME_OVERHEAT:uint = 30;
      
      private static const STATE_ON:String = "on";
      
      private static const STATE_OFF:String = "off";
      
      private static const HOT_KEY_START_POS_X:int = 0;
      
      private static const HOT_KEY_START_POS_Y:int = 0;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
       
      
      public var emptyProgress:MovieClip = null;
      
      public var activeProgress:MovieClip = null;
      
      public var progressRight:MovieClip = null;
      
      public var progressLeft:MovieClip = null;
      
      public var overheatGlow:MovieClip = null;
      
      public var inactiveTimer:Timer = null;
      
      public var hotkeyTarget:MovieClip = null;
      
      private var _overheat:Boolean = true;
      
      public function RechargeableNitroWidget()
      {
         super();
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.PRIME;
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
      
      override protected function configUI() : void
      {
         super.configUI();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function setTimer(param1:Number) : void
      {
         super.setTimer(param1);
         this.inactiveTimer.setLabel(param1);
      }
      
      override protected function onDispose() : void
      {
         this.inactiveTimer.dispose();
         this.inactiveTimer = null;
         this.emptyProgress = null;
         this.activeProgress = null;
         this.progressRight = null;
         this.progressLeft = null;
         this.overheatGlow = null;
         this.hotkeyTarget = null;
         super.onDispose();
      }
      
      public function as_setProgress(param1:Number) : void
      {
         var _loc2_:Number = param1 * MAX_FRAMES_COUNT;
         if(this._overheat != _loc2_ <= FRAME_OVERHEAT)
         {
            this._overheat = _loc2_ <= FRAME_OVERHEAT;
            this.emptyProgress.gotoAndPlay(!!this._overheat ? STATE_OFF : STATE_ON);
            this.activeProgress.visible = !this._overheat;
            this.overheatGlow.visible = this._overheat;
         }
         this.progressRight.gotoAndStop(_loc2_);
         this.progressLeft.gotoAndStop(_loc2_);
      }
      
      public function as_updateLayout(param1:Number, param2:Number) : void
      {
      }
      
      public function as_setCount(param1:int) : void
      {
      }
   }
}
