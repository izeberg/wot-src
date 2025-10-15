package net.wg.gui.components.crosshairPanel.components
{
   import net.wg.data.constants.generated.CROSSHAIR_CONSTANTS;
   
   public class ShotDamageInd extends ShotIndBase
   {
      
      private static const INV_STATE:String = "invState";
       
      
      private var _currentValue:int = 0;
      
      private var _currentState:int = 0;
      
      public function ShotDamageInd()
      {
         super();
      }
      
      override protected function setNewValue(param1:Number) : void
      {
         this._currentValue = int(param1);
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
         valueTF.text = this._currentValue.toString();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INV_STATE))
         {
            gotoAndStop(this._currentState);
            this.applyNewValue();
         }
      }
      
      public function setState(param1:int) : void
      {
         this._currentState = Math.max(Math.min(param1,CROSSHAIR_CONSTANTS.SHOT_DAMAGE_IND_HIGH),CROSSHAIR_CONSTANTS.SHOT_DAMAGE_IND_LOW);
         invalidate(INV_STATE);
      }
   }
}
