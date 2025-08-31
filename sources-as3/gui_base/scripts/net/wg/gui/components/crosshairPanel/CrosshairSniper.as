package net.wg.gui.components.crosshairPanel
{
   import flash.text.TextField;
   import net.wg.utils.StageSizeBoundaries;
   
   public class CrosshairSniper extends CrosshairWithCassette
   {
      
      private static const CASSETE_POSITION_DIAGONAL:int = -2;
      
      private static const CASSETE_POSITION_HORIZONTAL:int = 8;
      
      private static const CASSETE_POSITION_RADIAL:int = -2;
      
      private static const CASSETE_POSITION_DASHED:int = -2;
      
      private static const RELOAD_TIME_BLINK_Y_DIAGONAL:int = 7;
      
      private static const RELOAD_TIME_BLINK_Y_HORIZONTAL:int = 39;
      
      private static const RELOAD_TIME_BLINK_Y_RADIAL:int = 11;
      
      private static const RELOAD_TIME_BLINK_Y_DASHED:int = 39;
      
      private static const RELOAD_TIME_BLINK_Y_SIEGE:int = 25;
      
      private static const RELOAD_TIME_BLINK_Y_PILLBOX:int = 25;
      
      private static const SIEGE_NET_SCALE_SMALL:Number = 0.72;
      
      private static const SIEGE_NET_SCALE_NORMAL:Number = 1;
      
      private static const ZOOM_OVERHEAT_POSITION_X:int = 240;
      
      private static const ZOOM_OVERHEAT_POSITION_Y:int = 20;
       
      
      public var zoomTF:TextField = null;
      
      private var _zoomIndicatorAlphaValue:Number = 1;
      
      private var _zoomStr:String = "";
      
      public function CrosshairSniper()
      {
         super();
      }
      
      override public function setComponentsAlpha(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : void
      {
         this._zoomIndicatorAlphaValue = param7;
         super.setComponentsAlpha(param1,param2,param3,param4,param5,param6,param7);
         this.zoomTF.alpha = this._zoomIndicatorAlphaValue;
      }
      
      override public function set overheatIndicatorVisible(param1:Boolean) : void
      {
         if(param1)
         {
            this.zoomTF.x = ZOOM_OVERHEAT_POSITION_X;
            this.zoomTF.y = ZOOM_OVERHEAT_POSITION_Y;
         }
         super.overheatIndicatorVisible = param1;
      }
      
      override public function setNetType(param1:Number) : void
      {
         super.setNetType(param1);
         this.zoomTF.text = this._zoomStr;
         this.zoomTF.alpha = this._zoomIndicatorAlphaValue;
      }
      
      override public function setZoom(param1:String) : void
      {
         if(this._zoomStr == param1)
         {
            return;
         }
         this._zoomStr = param1;
         this.zoomTF.text = this._zoomStr;
      }
      
      override protected function onDispose() : void
      {
         this.zoomTF = null;
         super.onDispose();
      }
      
      override protected function getCassettePositions() : Array
      {
         return [CASSETE_POSITION_DIAGONAL,CASSETE_POSITION_HORIZONTAL,CASSETE_POSITION_RADIAL,CASSETE_POSITION_DASHED];
      }
      
      override protected function getReloadTimeBlinkYPos() : Array
      {
         return [RELOAD_TIME_BLINK_Y_DIAGONAL,RELOAD_TIME_BLINK_Y_HORIZONTAL,RELOAD_TIME_BLINK_Y_RADIAL,RELOAD_TIME_BLINK_Y_DASHED,RELOAD_TIME_BLINK_Y_SIEGE,RELOAD_TIME_BLINK_Y_PILLBOX];
      }
      
      override protected function getSiegeNetScale(param1:Number, param2:Number) : Number
      {
         if(param1 < StageSizeBoundaries.WIDTH_1920)
         {
            return SIEGE_NET_SCALE_SMALL;
         }
         return SIEGE_NET_SCALE_NORMAL;
      }
   }
}
