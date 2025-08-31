package net.wg.gui.battle.views.decorativeCrosshair
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.gui.battle.views.decorativeCrosshair.overheat.OverheatCounter;
   import net.wg.gui.battle.views.decorativeCrosshair.overheat.OverheatDecoration;
   import net.wg.gui.battle.views.decorativeCrosshair.overheat.OverheatIcon;
   import net.wg.gui.battle.views.decorativeCrosshair.overheat.OverheatProgress;
   import net.wg.gui.battle.views.decorativeCrosshair.overheat.OverheatStatus;
   import net.wg.infrastructure.base.meta.IOverheatDecorativeCrosshairMeta;
   import net.wg.infrastructure.base.meta.impl.OverheatDecorativeCrosshairMeta;
   
   public class OverheatDecorativeCrosshair extends OverheatDecorativeCrosshairMeta implements IOverheatDecorativeCrosshairMeta
   {
      
      public static const STATE_NULL:uint = 1 << 0;
      
      public static const STATE_NO_SHELL_IN_CHAMBER:uint = 1 << 1;
      
      public static const STATE_DT_GAIN:uint = 1 << 2;
      
      public static const STATE_DT_LOOSE:uint = 1 << 3;
      
      public static const STATE_STACK_GAIN:uint = 1 << 4;
      
      public static const STATE_STACK_LOOSE:uint = 1 << 5;
      
      public static const STATE_CHARGE_MIN:uint = 1 << 6;
      
      public static const STATE_CHARGE_MAX:uint = 1 << 7;
      
      private static const SCALE_ARCADE:Number = 0.86;
      
      private static const SCALE_SNIPER:Number = 1;
      
      private static const SCALE_ARCADE_DECORATION:Number = 0.88;
      
      private static const SCALE_SNIPER_DECORATION:Number = 1;
      
      private static const HEAT_FRAMES:Number = 100;
      
      private static const HEAT_ICON_ARCADE_X:int = 250;
      
      private static const HEAT_ICON_ARCADE_Y:int = -122;
      
      private static const COUNTER_ARCADE_X:int = 154;
      
      private static const COUNTER_ARCADE_Y:int = -11;
      
      private static const HEAT_PROGRESS_ARCADE_X:int = 237;
      
      private static const HEAT_PROGRESS_ARCADE_Y:int = -106;
      
      private static const MAIN_PROGRESS_ARCADE_X:int = 47;
      
      private static const MAIN_PROGRESS_ARCADE_Y:int = -126;
      
      private static const DECORATION_SMALL_ARCADE_X:int = 205;
      
      private static const DECORATION_SMALL_ARCADE_Y:int = 120;
      
      private static const DECORATION_BIG_ARCADE_X:int = -355;
      
      private static const DECORATION_BIG_ARCADE_Y:int = -185;
      
      private static const STATUS_ARCADE_X:int = 210;
      
      private static const STATUS_ARCADE_Y:int = 82;
      
      private static const HEAT_ICON_SNIPER_X:int = 355;
      
      private static const HEAT_ICON_SNIPER_Y:int = -134;
      
      private static const COUNTER_SNIPER_X:int = 240;
      
      private static const COUNTER_SNIPER_Y:int = -10;
      
      private static const HEAT_PROGRESS_SNIPER_X:int = 338;
      
      private static const HEAT_PROGRESS_SNIPER_Y:int = -118;
      
      private static const MAIN_PROGRESS_SNIPER_X:int = 117;
      
      private static const MAIN_PROGRESS_SNIPER_Y:int = -141;
      
      private static const DECORATION_SMALL_SNIPER_X:int = 303;
      
      private static const DECORATION_SMALL_SNIPER_Y:int = 150;
      
      private static const DECORATION_BIG_SNIPER_X:int = -410;
      
      private static const DECORATION_BIG_SNIPER_Y:int = -164;
      
      private static const STATUS_SNIPER_X:int = 315;
      
      private static const STATUS_SNIPER_Y:int = 106;
       
      
      public var heatIcon:OverheatIcon = null;
      
      public var counter:OverheatCounter = null;
      
      public var overheatDecoration:OverheatDecoration = null;
      
      public var heatProgress:MovieClip = null;
      
      public var decorationSmall:Sprite = null;
      
      public var mainProgress:OverheatProgress = null;
      
      public var status:OverheatStatus = null;
      
      private var _state:uint;
      
      public function OverheatDecorativeCrosshair()
      {
         this._state = STATE_NULL;
         super();
         this.mainProgress.setDependency(this.counter);
      }
      
      public function as_setStacksProgres(param1:Number, param2:int) : void
      {
         this.mainProgress.setProgress(param1,param2);
      }
      
      public function as_setInitData(param1:int, param2:int, param3:Number, param4:Number, param5:Boolean) : void
      {
         this.status.setSpeed(param1);
         this.mainProgress.setInitData(param2,param3,param4,param5);
      }
      
      public function as_setHeatProgres(param1:Number) : void
      {
         this.heatProgress.gotoAndStop(param1 * HEAT_FRAMES);
         this.mainProgress.setHeatProgress(param1);
      }
      
      public function as_setDamageData(param1:int, param2:int) : void
      {
         this.mainProgress.setDamageData(param1,param2);
         this.counter.setDamageData(param1);
      }
      
      public function as_updateState(param1:int) : void
      {
         if(param1 == STATE_NULL || param1 == this._state)
         {
            return;
         }
         this.heatIcon.setState(this._state,param1);
         if(param1 == STATE_CHARGE_MIN)
         {
            this.mainProgress.setHeatProgress(0);
         }
         this.overheatDecoration.setState(this._state,param1);
         this.status.setState(param1);
         this.mainProgress.setState(param1);
         this.decorationSmall.visible = !(param1 == OverheatDecorativeCrosshair.STATE_DT_GAIN || param1 == OverheatDecorativeCrosshair.STATE_STACK_GAIN || param1 == OverheatDecorativeCrosshair.STATE_CHARGE_MAX);
         this._state = param1;
      }
      
      override public function updateScale(param1:int) : void
      {
         var _loc2_:Boolean = param1 == CROSSHAIR_VIEW_ID.ARCADE;
         var _loc3_:Number = !!_loc2_ ? Number(SCALE_ARCADE) : Number(SCALE_SNIPER);
         var _loc4_:Number = !!_loc2_ ? Number(SCALE_ARCADE_DECORATION) : Number(SCALE_SNIPER_DECORATION);
         this.mainProgress.scaleX = this.mainProgress.scaleY = _loc3_;
         this.heatProgress.scaleX = this.heatProgress.scaleY = _loc3_;
         this.decorationSmall.scaleX = this.decorationSmall.scaleY = _loc3_;
         this.overheatDecoration.scaleX = this.overheatDecoration.scaleY = _loc4_;
         if(_loc2_)
         {
            this.heatIcon.x = HEAT_ICON_ARCADE_X;
            this.heatIcon.y = HEAT_ICON_ARCADE_Y;
            this.counter.x = COUNTER_ARCADE_X;
            this.counter.y = COUNTER_ARCADE_Y;
            this.heatProgress.x = HEAT_PROGRESS_ARCADE_X;
            this.heatProgress.y = HEAT_PROGRESS_ARCADE_Y;
            this.mainProgress.x = MAIN_PROGRESS_ARCADE_X;
            this.mainProgress.y = MAIN_PROGRESS_ARCADE_Y;
            this.status.x = STATUS_ARCADE_X;
            this.status.y = STATUS_ARCADE_Y;
            this.decorationSmall.x = DECORATION_SMALL_ARCADE_X;
            this.decorationSmall.y = DECORATION_SMALL_ARCADE_Y;
            this.overheatDecoration.x = DECORATION_BIG_ARCADE_X;
            this.overheatDecoration.y = DECORATION_BIG_ARCADE_Y;
            this.overheatDecoration.setMode(false);
         }
         else
         {
            this.heatIcon.x = HEAT_ICON_SNIPER_X;
            this.heatIcon.y = HEAT_ICON_SNIPER_Y;
            this.counter.x = COUNTER_SNIPER_X;
            this.counter.y = COUNTER_SNIPER_Y;
            this.heatProgress.x = HEAT_PROGRESS_SNIPER_X;
            this.heatProgress.y = HEAT_PROGRESS_SNIPER_Y;
            this.mainProgress.x = MAIN_PROGRESS_SNIPER_X;
            this.mainProgress.y = MAIN_PROGRESS_SNIPER_Y;
            this.status.x = STATUS_SNIPER_X;
            this.status.y = STATUS_SNIPER_Y;
            this.decorationSmall.x = DECORATION_SMALL_SNIPER_X;
            this.decorationSmall.y = DECORATION_SMALL_SNIPER_Y;
            this.overheatDecoration.x = DECORATION_BIG_SNIPER_X;
            this.overheatDecoration.y = DECORATION_BIG_SNIPER_Y;
            this.overheatDecoration.setMode(true);
         }
      }
      
      override protected function onDispose() : void
      {
         this.mainProgress.dispose();
         this.mainProgress = null;
         this.heatIcon.dispose();
         this.heatIcon = null;
         this.counter.dispose();
         this.counter = null;
         this.overheatDecoration.dispose();
         this.overheatDecoration = null;
         this.decorationSmall = null;
         this.status = null;
         super.onDispose();
      }
   }
}
