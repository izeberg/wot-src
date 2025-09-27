package net.wg.gui.components.crosshairPanel.components
{
   public class ShotFlyTimeInd extends ShotIndBase
   {
       
      
      private var _currentValue:Number = 0;
      
      public function ShotFlyTimeInd()
      {
         super();
      }
      
      override protected function setNewValue(param1:Number) : void
      {
         this._currentValue = param1;
      }
      
      override protected function isGrayscaledValue() : Boolean
      {
         return this._currentValue == 0;
      }
      
      override protected function isSameValue(param1:Number) : Boolean
      {
         return this._currentValue == param1;
      }
      
      override protected function applyNewValue() : void
      {
         valueTF.text = this._currentValue.toFixed(1);
      }
   }
}
