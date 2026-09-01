package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import net.wg.data.constants.generated.SHELL_CALIBRATION_WIDGET_CONSTS;
   
   public class ShellCalibrationWidget extends BaseVehicleMechanicsWidget
   {
      
      private static const BONUS_OFF_STATE_POSTFIX:String = "Off";
       
      
      public function ShellCalibrationWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function getInitialState() : String
      {
         return SHELL_CALIBRATION_WIDGET_CONSTS.NO_BONUS;
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return [];
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         if(param1 == SHELL_CALIBRATION_WIDGET_CONSTS.NO_BONUS)
         {
            param1 = this.state + BONUS_OFF_STATE_POSTFIX;
         }
         super.applyState(param1,param2);
      }
   }
}
