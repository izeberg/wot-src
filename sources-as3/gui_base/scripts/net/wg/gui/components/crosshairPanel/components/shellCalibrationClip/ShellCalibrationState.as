package net.wg.gui.components.crosshairPanel.components.shellCalibrationClip
{
   public class ShellCalibrationState
   {
      
      private static const READY_FLAG:uint = 1;
      
      private static const PENETRATION_BONUS_FLAG:uint = 1 << 1;
      
      private static const NON_PENETRATION_BONUS_FLAG:uint = 1 << 2;
      
      private static const WAITING_RESULT:uint = 1 << 3;
       
      
      private var _mask:uint;
      
      public function ShellCalibrationState(param1:uint = 0)
      {
         super();
         this._mask = param1;
      }
      
      public function get mask() : uint
      {
         return this._mask;
      }
      
      public function get isReady() : Boolean
      {
         return (this._mask & READY_FLAG) > 0;
      }
      
      public function get isCalibrated() : Boolean
      {
         return ((PENETRATION_BONUS_FLAG | NON_PENETRATION_BONUS_FLAG) & this._mask) > 0;
      }
      
      public function get isCalibrating() : Boolean
      {
         return (this._mask & WAITING_RESULT) > 0;
      }
   }
}
