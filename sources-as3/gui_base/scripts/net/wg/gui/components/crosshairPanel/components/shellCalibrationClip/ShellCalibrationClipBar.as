package net.wg.gui.components.crosshairPanel.components.shellCalibrationClip
{
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.clik.constants.InvalidationType;
   
   public class ShellCalibrationClipBar extends SimpleContainer
   {
       
      
      public var shell_1:ShellCalibrationProgressBar;
      
      public var shell_2:ShellCalibrationProgressBar;
      
      public var shell_3:ShellCalibrationProgressBar;
      
      public var shell_4:ShellCalibrationProgressBar;
      
      private var _shellsList:Vector.<ShellCalibrationProgressBar> = null;
      
      private var _isCritical:Boolean = false;
      
      private var _clipCapacity:uint = 0;
      
      private var _shellCount:uint = 0;
      
      private var _totalAmmo:uint = 0;
      
      private var _isReloading:Boolean = false;
      
      private var _reloadProgress:Number = 0;
      
      private var _calibrationState:ShellCalibrationState = null;
      
      private var _applyNow:Boolean = false;
      
      public function ShellCalibrationClipBar()
      {
         super();
         this._shellsList = new <ShellCalibrationProgressBar>[this.shell_1,this.shell_2,this.shell_3,this.shell_4];
         this._calibrationState = new ShellCalibrationState();
      }
      
      override protected function draw() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:ShellCalibrationProgressBar = null;
         var _loc3_:uint = 0;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            _loc1_ = this._shellsList.length;
            _loc3_ = 0;
            while(_loc3_ < _loc1_)
            {
               _loc2_ = this._shellsList[_loc3_];
               _loc2_.visible = _loc3_ < this._clipCapacity;
               if(_loc2_.visible)
               {
                  _loc2_.setState(_loc3_ < this._shellCount ? ShellProgressBar.READY_STATE : ShellProgressBar.EMPTY_STATE,this._applyNow);
                  _loc2_.reloadingPercent = _loc3_ < this._shellCount ? Number(1) : (_loc3_ < this._totalAmmo ? Number(this._reloadProgress) : Number(0));
                  _loc2_.isCritical = this._isCritical;
                  if(!this._calibrationState.isReady || _loc3_ >= this._shellCount)
                  {
                     _loc2_.setCalibrationState(ShellCalibrationProgressBar.CALIBRATION_STATE_DISABLED,this._applyNow);
                  }
                  else if(_loc3_ < this._shellCount - 1 || this._calibrationState.isCalibrating)
                  {
                     _loc2_.setCalibrationState(ShellCalibrationProgressBar.CALIBRATION_STATE_WAITING,this._applyNow);
                  }
                  else
                  {
                     _loc2_.setCalibrationState(!!this._calibrationState.isCalibrated ? ShellCalibrationProgressBar.CALIBRATION_STATE_COMPLETE : ShellCalibrationProgressBar.CALIBRATION_STATE_CANCEL,this._applyNow);
                  }
               }
               _loc3_++;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:ShellCalibrationProgressBar = null;
         this._calibrationState = null;
         for each(_loc1_ in this._shellsList)
         {
            _loc1_.dispose();
         }
         this._shellsList.length = 0;
         this._shellsList = null;
         this.shell_4 = this.shell_3 = this.shell_2 = this.shell_1 = null;
         super.onDispose();
      }
      
      public function get clipCapacity() : uint
      {
         return this._clipCapacity;
      }
      
      public function set clipCapacity(param1:uint) : void
      {
         this._clipCapacity = param1;
         invalidateData();
      }
      
      public function get shellCount() : uint
      {
         return this._shellCount;
      }
      
      public function set shellCount(param1:uint) : void
      {
         this._shellCount = param1;
         invalidateData();
      }
      
      public function get isCritical() : Boolean
      {
         return this._isCritical;
      }
      
      public function set isCritical(param1:Boolean) : void
      {
         this._isCritical = param1;
         invalidateData();
      }
      
      public function get totalAmmo() : uint
      {
         return this._totalAmmo;
      }
      
      public function set totalAmmo(param1:uint) : void
      {
         this._totalAmmo = param1;
         invalidateData();
      }
      
      public function get isReloading() : Boolean
      {
         return this._isReloading;
      }
      
      public function set isReloading(param1:Boolean) : void
      {
         this._isReloading = param1;
         invalidateData();
      }
      
      public function get reloadProgress() : Number
      {
         return this._reloadProgress;
      }
      
      public function set reloadProgress(param1:Number) : void
      {
         this._reloadProgress = param1;
         invalidateData();
      }
      
      public function get calibrationState() : uint
      {
         return this._calibrationState.mask;
      }
      
      public function set calibrationState(param1:uint) : void
      {
         this._calibrationState = new ShellCalibrationState(param1);
         invalidateData();
      }
      
      public function applyNow() : void
      {
         this._applyNow = true;
         validateNow();
         this._applyNow = false;
      }
   }
}
