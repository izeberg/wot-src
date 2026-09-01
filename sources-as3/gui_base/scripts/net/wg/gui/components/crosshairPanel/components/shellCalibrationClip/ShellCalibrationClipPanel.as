package net.wg.gui.components.crosshairPanel.components.shellCalibrationClip
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class ShellCalibrationClipPanel extends SimpleContainer
   {
      
      private static const CLIP_STATE_CRITICAL:String = "critical";
      
      private static const CURRENT_SHELL_INVALID:String = "currentShellInvalid";
      
      private static const GUN_RELOAD_INVALID:String = "gunReloadInvalid";
      
      private static const SHELL_ANGLE_GAP:int = 5;
      
      private static const ROTATION_ANIMATION_DELAY:Number = 0.4;
      
      private static const ROTATION_ANIMATION_DURATION:Number = 0.6;
      
      private static const GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD:Number = 0.8;
       
      
      public var clipBar:ShellCalibrationClipBar;
      
      private var _currentShellIdx:uint = 0;
      
      private var _reloadProgress:Number = 0;
      
      private var _isReloading:Boolean = false;
      
      public function ShellCalibrationClipPanel()
      {
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Number = NaN;
         super.draw();
         if(this._reloadProgress > GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD && isInvalid(GUN_RELOAD_INVALID))
         {
            GTweener.removeTweens(this.clipBar);
            this._currentShellIdx = this.targetShellIndex;
            if(this._isReloading)
            {
               _loc1_ = (this._reloadProgress - GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD) / (1 - GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD);
               this.clipBar.rotation = this.targetRotationAngle + Cubic.easeOut(_loc1_,NaN,NaN,NaN) * -SHELL_ANGLE_GAP;
            }
            else
            {
               this.clipBar.rotation = this.targetRotationAngle;
            }
         }
         if(isInvalid(CURRENT_SHELL_INVALID) && this._currentShellIdx != this.targetShellIndex)
         {
            GTweener.removeTweens(this.clipBar);
            this._currentShellIdx = this.targetShellIndex;
            GTweener.to(this.clipBar,ROTATION_ANIMATION_DURATION,{"rotation":this.targetRotationAngle},{
               "ease":Cubic.easeOut,
               "delay":ROTATION_ANIMATION_DELAY
            });
         }
      }
      
      override protected function onDispose() : void
      {
         GTweener.removeTweens(this.clipBar);
         this.clipBar.dispose();
         this.clipBar = null;
         super.onDispose();
      }
      
      public function set clipCapacity(param1:uint) : void
      {
         if(this.clipBar.clipCapacity == param1)
         {
            return;
         }
         this.clipBar.clipCapacity = param1;
         this._currentShellIdx = param1 - 1;
         GTweener.removeTweens(this.clipBar);
         this.clipBar.rotation = this.targetRotationAngle;
      }
      
      public function set shellCount(param1:uint) : void
      {
         if(this.clipBar.shellCount == param1)
         {
            return;
         }
         this.clipBar.shellCount = param1;
         invalidate(CURRENT_SHELL_INVALID);
      }
      
      public function set totalAmmo(param1:uint) : void
      {
         if(this.clipBar.totalAmmo == param1)
         {
            return;
         }
         this.clipBar.totalAmmo = param1;
         invalidate(CURRENT_SHELL_INVALID);
      }
      
      public function set clipState(param1:String) : void
      {
         var _loc2_:Boolean = param1 == CLIP_STATE_CRITICAL;
         if(this.clipBar.isCritical == _loc2_)
         {
            return;
         }
         this.clipBar.isCritical = _loc2_;
      }
      
      public function set calibrationState(param1:uint) : void
      {
         if(this.clipBar.calibrationState == param1)
         {
            return;
         }
         this.clipBar.calibrationState = param1;
      }
      
      public function setReloading(param1:String, param2:Number) : void
      {
         var _loc3_:Boolean = false;
         var _loc5_:Boolean = false;
         _loc3_ = param1 == CrosshairConsts.GUN_RELOADING;
         var _loc4_:Number = !!_loc3_ ? Number(param2) : Number(1);
         if(this._isReloading != _loc3_ || _loc3_ && this._reloadProgress != _loc4_)
         {
            this._reloadProgress = _loc4_;
            this._isReloading = _loc3_;
            invalidate(GUN_RELOAD_INVALID);
         }
         _loc5_ = param1 == CrosshairConsts.CLIP_RELOADING;
         var _loc6_:Number = !!_loc5_ ? Number(param2) : Number(0);
         if(this.clipBar.isReloading != _loc5_ || this.clipBar.reloadProgress != _loc6_)
         {
            this.clipBar.reloadProgress = _loc6_;
            this.clipBar.isReloading = _loc5_;
         }
      }
      
      public function applyNow() : void
      {
         GTweener.removeTweens(this.clipBar);
         this._currentShellIdx = this.targetShellIndex;
         this.clipBar.rotation = this.targetRotationAngle;
         validateNow();
         this.clipBar.applyNow();
      }
      
      private function get targetShellIndex() : uint
      {
         if(this._isReloading)
         {
            return this.clipBar.shellCount;
         }
         if(this.clipBar.shellCount > 0)
         {
            return this.clipBar.shellCount - 1;
         }
         return Math.max(0,Math.min(this.clipBar.clipCapacity,this.clipBar.totalAmmo) - 1);
      }
      
      private function get targetRotationAngle() : int
      {
         return this._currentShellIdx * SHELL_ANGLE_GAP;
      }
   }
}
