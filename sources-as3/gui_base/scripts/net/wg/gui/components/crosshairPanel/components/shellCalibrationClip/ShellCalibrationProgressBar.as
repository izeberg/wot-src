package net.wg.gui.components.crosshairPanel.components.shellCalibrationClip
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   
   public class ShellCalibrationProgressBar extends ShellProgressBar
   {
      
      public static const CALIBRATION_STATE_DISABLED:String = "disabled";
      
      public static const CALIBRATION_STATE_WAITING:String = "awaitingCalibration";
      
      public static const CALIBRATION_STATE_CANCEL:String = "cancelCalibration";
      
      public static const CALIBRATION_STATE_COMPLETE:String = "calibrated";
       
      
      public var calibrationIndicator:MovieClip;
      
      private var _calibrationState:String = "disabled";
      
      public function ShellCalibrationProgressBar()
      {
         super();
         this.calibrationIndicator.gotoAndStop(CALIBRATION_STATE_DISABLED + STATE_INSTANTLY_POSTFIX);
      }
      
      override protected function onDispose() : void
      {
         this.calibrationIndicator = null;
         super.onDispose();
      }
      
      public function setCalibrationState(param1:String, param2:Boolean = false) : void
      {
         if(this._calibrationState == param1)
         {
            return;
         }
         param2 = param2 || (param1 == CALIBRATION_STATE_WAITING && this._calibrationState != CALIBRATION_STATE_DISABLED || param1 == CALIBRATION_STATE_CANCEL && this._calibrationState != CALIBRATION_STATE_WAITING || param1 == CALIBRATION_STATE_COMPLETE && this._calibrationState != CALIBRATION_STATE_WAITING || param1 == CALIBRATION_STATE_DISABLED && this._calibrationState != CALIBRATION_STATE_COMPLETE);
         this._calibrationState = param1;
         if(param2)
         {
            this.calibrationIndicator.gotoAndStop(param1 + STATE_INSTANTLY_POSTFIX);
         }
         else
         {
            this.calibrationIndicator.gotoAndPlay(param1);
         }
      }
   }
}
