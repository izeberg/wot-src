package net.wg.gui.battle.views.staticMarkers
{
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.text.TextField;
   import flash.utils.Timer;
   import flash.utils.getTimer;
   import net.wg.gui.battle.views.vehicleMarkers.VehicleMarkersManager;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.gfx.TextFieldEx;
   
   public class ArtilleryTargetMarker extends MovieClip implements IDisposable
   {
      
      private static const MAX_UPDATE_TIME_MS:int = 100;
      
      private static const FRAME_ALLY:String = "ally";
      
      private static const FRAME_ENEMY:String = "enemy";
      
      private static const FRAME_ENEMY_BLIND:String = "enemyBlind";
       
      
      public var tf:TextField = null;
      
      public var marker:MovieClip = null;
      
      private var _endTime:int = 0;
      
      private var _timer:Timer = null;
      
      private var _disposed:Boolean = false;
      
      public function ArtilleryTargetMarker()
      {
         super();
         TextFieldEx.setNoTranslate(this.tf,true);
         this.marker.visible = true;
         this._timer = new Timer(MAX_UPDATE_TIME_MS);
         this._timer.addEventListener(TimerEvent.TIMER,this.onTimerEventHandler);
      }
      
      public final function dispose() : void
      {
         this._timer.removeEventListener(TimerEvent.TIMER,this.onTimerEventHandler);
         this._timer.stop();
         this._timer = null;
         this.marker = null;
         this.tf = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function updateData(param1:Boolean, param2:int, param3:Boolean = false) : void
      {
         var _loc5_:int = 0;
         var _loc4_:String = FRAME_ALLY;
         if(!param1)
         {
            _loc4_ = !!VehicleMarkersManager.getInstance().isColorBlind ? FRAME_ENEMY_BLIND : FRAME_ENEMY;
         }
         gotoAndStop(_loc4_);
         this.tf.text = (param2 / 1000).toFixed(1);
         if(!param3)
         {
            this._endTime = getTimer() + param2;
            _loc5_ = 1 + int(param2 / MAX_UPDATE_TIME_MS);
            this._timer.stop();
            this._timer.delay = param2 / _loc5_;
            this._timer.repeatCount = _loc5_;
            this._timer.start();
         }
      }
      
      public function updateTextInReplay(param1:int) : void
      {
         this.tf.text = (param1 / 1000).toFixed(1);
      }
      
      private function onTimerEventHandler(param1:TimerEvent) : void
      {
         this.tf.text = ((this._endTime - getTimer()) / 1000).toFixed(1);
      }
   }
}
