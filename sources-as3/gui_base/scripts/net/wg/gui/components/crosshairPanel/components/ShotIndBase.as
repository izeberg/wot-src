package net.wg.gui.components.crosshairPanel.components
{
   import flash.text.TextField;
   import flash.utils.clearTimeout;
   import flash.utils.setTimeout;
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class ShotIndBase extends SimpleContainer
   {
      
      private static const INV_VALUE:String = "invValue";
      
      private static const TIMEOUT_APPLY_VALUE:int = 2000;
       
      
      public var valueTF:TextField = null;
      
      private var _timeoutId:uint = 0;
      
      public function ShotIndBase()
      {
         super();
         this.applyFilter();
      }
      
      override protected function onDispose() : void
      {
         this.clearTimeoutId();
         this.valueTF = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INV_VALUE))
         {
            this.applyNewValue();
         }
      }
      
      public function setValue(param1:Number) : void
      {
         if(this.isSameValue(param1))
         {
            return;
         }
         this.setNewValue(param1);
         this.applyFilter();
         if(this._timeoutId == 0)
         {
            this.invalidateValue();
         }
      }
      
      protected function isGrayscaledValue() : Boolean
      {
         return true;
      }
      
      protected function isSameValue(param1:Number) : Boolean
      {
         return false;
      }
      
      protected function setNewValue(param1:Number) : void
      {
         throw new Error(Errors.ABSTRACT_INVOKE);
      }
      
      protected function applyNewValue() : void
      {
         throw new Error(Errors.ABSTRACT_INVOKE);
      }
      
      private function invalidateValue() : void
      {
         this.clearTimeoutId();
         invalidate(INV_VALUE);
      }
      
      private function applyFilter() : void
      {
         if(this.isGrayscaledValue())
         {
            this.clearTimeoutId();
            this._timeoutId = setTimeout(this.invalidateValue,TIMEOUT_APPLY_VALUE);
            filters = [CrosshairConsts.GRAYSCALE_FILTER];
         }
         else
         {
            this.clearTimeoutId();
            filters = [];
         }
      }
      
      private function clearTimeoutId() : void
      {
         clearTimeout(this._timeoutId);
         this._timeoutId = 0;
      }
   }
}
