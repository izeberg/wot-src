package net.wg.gui.components.crosshairPanel.components
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.utils.clearTimeout;
   import flash.utils.setTimeout;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class ShotFlyTimeInd extends SimpleContainer
   {
      
      private static const INV_VALUE:String = "invValue";
      
      private static const TIMEOUT_APPLY_VALUE:int = 2000;
      
      private static const ZERO_VALUE:String = "- -";
      
      private static const SECONDS:String = "с";
      
      private static const FRAME_DISABLED:int = 96;
      
      private static const FRAME_ENABLED:int = 1;
      
      private static const FRAME_ANIMATE_DISABLED:int = 2;
       
      
      public var content:MovieClip = null;
      
      private var _currentValue:Number = 0;
      
      private var _valueTF:TextField = null;
      
      private var _timeoutId:uint = 0;
      
      public function ShotFlyTimeInd()
      {
         super();
         this._valueTF = this.content.valueTF;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INV_VALUE))
         {
            this.applyNewValue();
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearTimeoutId();
         this._valueTF = null;
         this.content = null;
         super.onDispose();
      }
      
      public function setValue(param1:Number) : void
      {
         if(this._currentValue == param1)
         {
            return;
         }
         this._currentValue = param1;
         this.applyFilter();
         if(this._timeoutId == 0)
         {
            this.invalidateValue();
         }
      }
      
      private function applyNewValue() : void
      {
         if(this._currentValue == 0)
         {
            gotoAndStop(FRAME_DISABLED);
            this._valueTF.text = ZERO_VALUE;
         }
         else
         {
            gotoAndStop(FRAME_ENABLED);
            this._valueTF.text = this._currentValue.toFixed(1) + SECONDS;
         }
      }
      
      private function invalidateValue() : void
      {
         this.clearTimeoutId();
         invalidate(INV_VALUE);
      }
      
      private function applyFilter() : void
      {
         if(this._currentValue == 0)
         {
            this.clearTimeoutId();
            gotoAndPlay(FRAME_ANIMATE_DISABLED);
            this._timeoutId = setTimeout(this.invalidateValue,TIMEOUT_APPLY_VALUE);
         }
         else
         {
            this.clearTimeoutId();
         }
      }
      
      private function clearTimeoutId() : void
      {
         clearTimeout(this._timeoutId);
         this._timeoutId = 0;
      }
   }
}
