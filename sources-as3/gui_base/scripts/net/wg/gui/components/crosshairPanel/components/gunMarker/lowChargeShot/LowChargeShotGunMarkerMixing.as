package net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import flash.display.BlendMode;
   import flash.display.Shape;
   import flash.events.Event;
   import flash.utils.clearInterval;
   import flash.utils.setInterval;
   import net.wg.data.constants.generated.LOW_CHARGE_SHOT_CONSTS;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarkerMixing;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class LowChargeShotGunMarkerMixing extends SimpleContainer implements IGunMarkerMixing
   {
      
      private static const DEFAULT_ROTATION_ANGLE:int = -90;
      
      private static const CIRCLE_RADIUS:int = 512;
      
      private static const REDRAW_INTERVAL:int = 100;
       
      
      private var _markerDrawer:MarkerDrawer = null;
      
      private var _curPercents:Number = -1;
      
      private var _zoomFactor:Number = 1.0;
      
      private var _gunState:Number = 0;
      
      private var _redrawEmptyInterval:Number = 0;
      
      public function LowChargeShotGunMarkerMixing()
      {
         super();
         var _loc1_:Shape = new Shape();
         addChild(_loc1_);
         var _loc2_:Shape = new Shape();
         _loc2_.blendMode = BlendMode.SCREEN;
         addChild(_loc2_);
         this._markerDrawer = new MarkerDrawer(_loc1_,_loc2_);
         this._markerDrawer.addEventListener(Event.RENDER,this.onMarkerDrawerRenderHandler);
         rotation = DEFAULT_ROTATION_ANGLE;
         this.setReloadingAsPercent(100);
      }
      
      override protected function onDispose() : void
      {
         this.clearTimer();
         GTweener.removeTweens(this);
         this._markerDrawer.removeEventListener(Event.RENDER,this.onMarkerDrawerRenderHandler);
         this._markerDrawer.dispose();
         this._markerDrawer = null;
         super.onDispose();
      }
      
      public function redrawProgress() : void
      {
         this._markerDrawer.curPercents = this._curPercents;
         this._markerDrawer.counterScale = parent.scaleX;
         this._markerDrawer.draw();
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         this._markerDrawer.setIsColorBlind(param1);
      }
      
      public function setLowChargeShotGunStageCaps(param1:Number, param2:Number) : void
      {
         this._markerDrawer.setLowChargeShotGunStageCaps(param1,param2);
         this.redrawProgress();
      }
      
      public function setReloadingAsPercent(param1:Number, param2:Boolean = false) : void
      {
      }
      
      public function setReloadingProgress(param1:Number, param2:Number) : void
      {
         if(this._gunState != param2)
         {
            this._gunState = param2;
            this._markerDrawer.gunState = this._gunState;
            this.clearTimer();
            if(this._gunState == LOW_CHARGE_SHOT_CONSTS.EMPTY)
            {
               this.startTimer();
            }
         }
         this._curPercents = param1;
         this.redrawProgress();
      }
      
      public function setReloadingState(param1:String) : void
      {
      }
      
      public function setThickness(param1:String) : void
      {
      }
      
      private function startTimer() : void
      {
         this._redrawEmptyInterval = setInterval(this.updateRedrawEmptyTimer,REDRAW_INTERVAL);
      }
      
      private function updateRedrawEmptyTimer() : void
      {
         if(this._markerDrawer.counterScale != parent.scaleX || this._markerDrawer.zoomFactor != this._zoomFactor)
         {
            this._markerDrawer.counterScale = parent.scaleX;
            this._markerDrawer.zoomFactor = this._zoomFactor;
            this._markerDrawer.drawEmpty();
         }
      }
      
      private function clearTimer() : void
      {
         clearInterval(this._redrawEmptyInterval);
         this._redrawEmptyInterval = 0;
      }
      
      override public function get width() : Number
      {
         return CIRCLE_RADIUS;
      }
      
      override public function get height() : Number
      {
         return CIRCLE_RADIUS;
      }
      
      public function set zoomFactor(param1:Number) : void
      {
         if(param1 == this._zoomFactor)
         {
            return;
         }
         this._zoomFactor = param1;
         if(this._gunState != LOW_CHARGE_SHOT_CONSTS.EMPTY)
         {
            this._markerDrawer.zoomFactor = this._zoomFactor;
            this.redrawProgress();
         }
      }
      
      private function onMarkerDrawerRenderHandler(param1:Event) : void
      {
         this._markerDrawer.invalidate();
         this.redrawProgress();
      }
   }
}
