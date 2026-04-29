package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import flash.display.Sprite;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.utils.IScheduler;
   import scaleform.clik.motion.Tween;
   
   public class HBEnemyAnimHelper extends SimpleDisposable
   {
      
      private static const STATE_DEFAULT:uint = 0;
      
      private static const STATE_ATTENTION:uint = 1;
      
      private static const VEHICLE_TYPE_X:int = 157;
      
      private static const VEHICLE_TYPE_Y:int = 3;
      
      private static const VEHICLE_TYPE_SIZE:uint = 24;
      
      private static const VEHICLE_TYPE_SCALE:Number = 1.2;
      
      private static const VEHICLE_TYPE_X_SCALED:int = VEHICLE_TYPE_X - (VEHICLE_TYPE_SIZE * VEHICLE_TYPE_SCALE - VEHICLE_TYPE_SIZE >> 1);
      
      private static const VEHICLE_TYPE_Y_SCALED:int = VEHICLE_TYPE_Y - (VEHICLE_TYPE_SIZE * VEHICLE_TYPE_SCALE - VEHICLE_TYPE_SIZE >> 1);
      
      private static const DURATION:uint = 1000;
      
      private static const DURATION_HALF:uint = DURATION >> 1;
      
      private static const REPEAT_COUNT:uint = 3;
       
      
      private var _state:int = 0;
      
      private var _vehicleType:Sprite = null;
      
      private var _glow:Sprite = null;
      
      private var _scheduler:IScheduler;
      
      private var _tweens:Vector.<Tween>;
      
      private var _repeatCount:int = 0;
      
      public function HBEnemyAnimHelper(param1:Sprite, param2:Sprite)
      {
         this._scheduler = App.utils.scheduler;
         this._tweens = new Vector.<Tween>(0);
         super();
         this._vehicleType = param1;
         this._glow = param2;
         this._glow.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.clearTween();
         this._tweens = null;
         this._scheduler.cancelTask(this.showAttentionAnim);
         this._scheduler = null;
         this._vehicleType = null;
         this._glow = null;
         super.onDispose();
      }
      
      public function showAttention() : void
      {
         if(this._state == STATE_ATTENTION)
         {
            return;
         }
         this._state = STATE_ATTENTION;
         this.clearTween();
         this._glow.alpha = 0;
         this._glow.visible = true;
         this._repeatCount = REPEAT_COUNT;
         this._scheduler.scheduleRepeatableTask(this.showAttentionAnim,DURATION,REPEAT_COUNT);
      }
      
      public function showDefault() : void
      {
         if(this._state == STATE_DEFAULT)
         {
            return;
         }
         this._state = STATE_DEFAULT;
         this.clearTween();
         this._scheduler.cancelTask(this.showAttentionAnim);
         this._glow.visible = false;
         this._vehicleType.x = VEHICLE_TYPE_X;
         this._vehicleType.y = VEHICLE_TYPE_Y;
         this._vehicleType.scaleX = this._vehicleType.scaleY = 1;
      }
      
      private function clearTween() : void
      {
         var _loc1_:Tween = null;
         if(this._tweens && this._tweens.length)
         {
            for each(_loc1_ in this._tweens)
            {
               _loc1_.dispose();
            }
            this._tweens.length = 0;
         }
      }
      
      private function showAttentionAnim() : void
      {
         var _loc1_:Object = {"delay":DURATION_HALF};
         if(this._repeatCount > 0)
         {
            --this._repeatCount;
            if(this._repeatCount == 0)
            {
               _loc1_.onComplete = this.showDefault;
            }
         }
         this._tweens.push(new Tween(DURATION_HALF,this._glow,{"alpha":1}));
         this._tweens.push(new Tween(DURATION_HALF,this._glow,{"alpha":0},_loc1_));
         this._tweens.push(new Tween(DURATION_HALF,this._vehicleType,{
            "x":VEHICLE_TYPE_X_SCALED,
            "y":VEHICLE_TYPE_Y_SCALED,
            "scaleX":VEHICLE_TYPE_SCALE,
            "scaleY":VEHICLE_TYPE_SCALE
         }));
         this._tweens.push(new Tween(DURATION_HALF,this._vehicleType,{
            "x":VEHICLE_TYPE_X,
            "y":VEHICLE_TYPE_Y,
            "scaleX":1,
            "scaleY":1
         },{"delay":DURATION_HALF}));
      }
   }
}
