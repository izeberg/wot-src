package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.DisplayObjectContainer;
   import flash.geom.Point;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.gui.battle.views.widgetsPanel.common.HotkeySettings;
   import net.wg.gui.battle.views.widgetsPanel.stanceDance.StanceDanceProgress;
   import net.wg.infrastructure.base.meta.IStanceDanceTurboWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.StanceDanceTurboWidgetMeta;
   
   public class StanceDanceTurboWidget extends StanceDanceTurboWidgetMeta implements IStanceDanceTurboWidgetMeta
   {
      
      private static const ARCADE_SCALE_FACTOR:Number = 0.76;
      
      private static const ARCADE_POSITION_X:int = 0;
      
      private static const ARCADE_POSITION_Y:int = 30;
      
      private static const ARCADE_ENERGY_X:int = 63;
      
      private static const ARCADE_ENERGY_Y:int = -90;
      
      private static const ARCADE_BUTTONS_X:int = 0;
      
      private static const ARCADE_BUTTONS_Y:int = 112;
      
      private static const ARCADE_WIDGET_X:int = -54;
      
      private static const ARCADE_WIDGET_Y:int = 4;
      
      private static const SNIPER_SCALE_FACTOR:Number = 1;
      
      private static const SNIPER_POSITION_X:int = 0;
      
      private static const SNIPER_POSITION_Y:int = 0;
      
      private static const SNIPER_ENERGY_X:int = 80;
      
      private static const SNIPER_ENERGY_Y:int = -145;
      
      private static const SNIPER_WIDGET_X:int = -65;
      
      private static const SNIPER_WIDGET_Y:int = -30;
      
      private static const SNIPER_BUTTONS_X:int = 15;
      
      private static const SNIPER_BUTTONS_Y:int = 61;
      
      private static const HOT_KEY_START_POS_X:int = 0;
      
      private static const HOT_KEY_START_POS_Y:int = 0;
      
      private static const HOT_KEY_GAP_Y:uint = 0;
       
      
      public var energyProgress:StanceDanceProgress = null;
      
      public var widget:StanceDanceSpeedWidget = null;
      
      private var _targetLabel:String = "";
      
      private var _hotKeyVisible:Boolean = true;
      
      public function StanceDanceTurboWidget()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            _loc1_ = crosshairType == CROSSHAIR_VIEW_ID.ARCADE;
            x = !!_loc1_ ? Number(ARCADE_POSITION_X) : Number(SNIPER_POSITION_X);
            y = !!_loc1_ ? Number(ARCADE_POSITION_Y) : Number(SNIPER_POSITION_Y);
            _loc2_ = !!_loc1_ ? Number(ARCADE_SCALE_FACTOR) : Number(SNIPER_SCALE_FACTOR);
            _loc3_ = !!_loc1_ ? Number(ARCADE_ENERGY_X) : Number(SNIPER_ENERGY_X);
            _loc4_ = !!_loc1_ ? Number(ARCADE_ENERGY_Y) : Number(SNIPER_ENERGY_Y);
            _loc5_ = !!_loc1_ ? Number(ARCADE_WIDGET_X) : Number(SNIPER_WIDGET_X);
            _loc6_ = !!_loc1_ ? Number(ARCADE_WIDGET_Y) : Number(SNIPER_WIDGET_Y);
            this.energyProgress.scaleX = this.energyProgress.scaleY = _loc2_;
            this.energyProgress.x = _loc3_;
            this.energyProgress.y = _loc4_;
            this.widget.x = _loc5_;
            this.widget.y = _loc6_;
            this.updateButtonsPositions();
            updateButtonsState(true);
         }
      }
      
      override protected function getHotkeySettings() : HotkeySettings
      {
         return new HotkeySettings(new Point(HOT_KEY_START_POS_X,HOT_KEY_START_POS_Y),true,HotkeySettings.DIRECTION_DOWN,Values.ZERO,HOT_KEY_GAP_Y);
      }
      
      override protected function getHotKeysTarget() : DisplayObjectContainer
      {
         return hotKeysContainer.container;
      }
      
      override protected function setTimer(param1:Number) : void
      {
         super.setTimer(param1);
         hotKeysContainer.time = param1;
      }
      
      private function updateButtonsPositions() : void
      {
         var _loc1_:Boolean = crosshairType == CROSSHAIR_VIEW_ID.ARCADE;
         var _loc2_:Number = !!_loc1_ ? Number(ARCADE_BUTTONS_X) : Number(SNIPER_BUTTONS_X);
         var _loc3_:Number = !!_loc1_ ? Number(ARCADE_BUTTONS_Y) : Number(SNIPER_BUTTONS_Y);
         hotKeysContainer.x = _loc2_;
         hotKeysContainer.y = _loc3_;
      }
      
      public function as_keysVisible(param1:Boolean) : void
      {
         this._hotKeyVisible = param1;
         invalidateState();
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         return super.getHotKeyVisibility() && this._hotKeyVisible;
      }
      
      override public function as_setState(param1:String, param2:Boolean) : void
      {
         super.as_setState(param1,param2);
         if(this._targetLabel != targetLabel)
         {
            this._targetLabel = targetLabel;
            if(param2)
            {
               this.energyProgress.gotoAndStop(this._targetLabel);
               this.widget.gotoAndStop(this._targetLabel);
            }
            else
            {
               this.energyProgress.gotoAndPlay(this._targetLabel);
               this.widget.gotoAndPlay(this._targetLabel);
            }
            this.updateButtonsPositions();
            updateButtonsState(param2);
         }
      }
      
      public function as_setProgress(param1:Boolean, param2:Number) : void
      {
         this.energyProgress.setProgress(param2);
      }
      
      override protected function onDispose() : void
      {
         this.energyProgress.dispose();
         this.energyProgress = null;
         this.widget.dispose();
         this.widget = null;
         super.onDispose();
      }
      
      public function as_setSpeed(param1:Number, param2:Boolean) : void
      {
         this.widget.setSpeed(param1,param2);
      }
      
      public function as_setParams(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         this.widget.draw(param1,param2,param3,param4);
      }
      
      public function as_switchTimer(param1:Number) : void
      {
         this.widget.setTransitionTimer(param1);
      }
   }
}
