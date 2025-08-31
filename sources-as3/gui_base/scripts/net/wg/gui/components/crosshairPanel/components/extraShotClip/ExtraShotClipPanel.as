package net.wg.gui.components.crosshairPanel.components.extraShotClip
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class ExtraShotClipPanel extends SimpleContainer
   {
      
      private static const CLIP_STATE_CRITICAL:String = "critical";
      
      private static const CURRENT_SHELL_INVALID:String = "currentShellInvalid";
      
      private static const CURSOR_STATE_INVALID:String = "cursorStateInvalid";
      
      private static const GUN_RELOAD_INVALID:String = "gunReloadInvalid";
      
      private static const EXTRA_SHELL_ANGLE_GAP:int = 10;
      
      private static const BASE_SHELL_ANGLE_GAP:int = 5;
      
      private static const ROTATION_ANIMATION_DELAY:Number = 0.4;
      
      private static const ROTATION_ANIMATION_DURATION:Number = 0.6;
      
      private static const GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD:Number = 0.8;
       
      
      public var cursor:ExtraShotClipCursor;
      
      public var clipBar:ExtraShotClipBar;
      
      private var _currentShellIdx:uint = 0;
      
      private var _reloadProgress:Number = 0;
      
      private var _isReloading:Boolean = false;
      
      private var _isCritical:Boolean = false;
      
      private var _applyNow:Boolean = false;
      
      public function ExtraShotClipPanel()
      {
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:int = 0;
         var _loc3_:String = null;
         super.draw();
         if(this._reloadProgress > GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD && isInvalid(GUN_RELOAD_INVALID))
         {
            GTweener.removeTweens(this.clipBar);
            this._currentShellIdx = this.targetShellIndex;
            if(this._isReloading)
            {
               _loc1_ = (this._reloadProgress - GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD) / (1 - GUN_RELOAD_PROGRESS_ROTATION_START_THRESHOLD);
               _loc2_ = this._currentShellIdx == 1 ? int(-EXTRA_SHELL_ANGLE_GAP) : int(-BASE_SHELL_ANGLE_GAP);
               this.clipBar.rotation = this.targetRotationAngle + Cubic.easeOut(_loc1_,NaN,NaN,NaN) * _loc2_;
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
         if(isInvalid(CURSOR_STATE_INVALID))
         {
            _loc3_ = ExtraShotClipCursor.NORMAL_STATE_LABEL;
            if(this.clipBar.isReloading && this.clipBar.shellCount > 0)
            {
               if(this._isCritical)
               {
                  _loc3_ = ExtraShotClipCursor.CRITICAL_STATE_LABEL;
                  this.cursor.criticalStateFrame = this.clipBar.criticalStateFrame;
               }
               else
               {
                  _loc3_ = ExtraShotClipCursor.ACTIVE_STATE_LABEL;
               }
            }
            this.clipBar.setCursorState(_loc3_,this._applyNow);
            this.cursor.setState(_loc3_,this._applyNow);
         }
      }
      
      override protected function onDispose() : void
      {
         GTweener.removeTweens(this.clipBar);
         this.clipBar.dispose();
         this.clipBar = null;
         this.cursor.dispose();
         this.cursor = null;
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
         invalidate(CURRENT_SHELL_INVALID,CURSOR_STATE_INVALID);
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
      
      public function setReloading(param1:String, param2:Number, param3:Boolean) : void
      {
         var _loc4_:Boolean = false;
         var _loc6_:Boolean = false;
         _loc4_ = param1 == CrosshairConsts.GUN_RELOADING;
         var _loc5_:Number = !!_loc4_ ? Number(param2) : Number(1);
         if(this._isReloading != _loc4_ || _loc4_ && this._reloadProgress != _loc5_)
         {
            this._reloadProgress = _loc5_;
            this._isReloading = _loc4_;
            invalidate(GUN_RELOAD_INVALID);
         }
         _loc6_ = param1 == CrosshairConsts.CLIP_RELOADING;
         var _loc7_:Number = !!_loc6_ ? Number(param2) : Number(0);
         if(this._isCritical != param3 || this.clipBar.isReloading != _loc6_ || this.clipBar.reloadProgress != _loc7_)
         {
            this.clipBar.reloadProgress = _loc7_;
            this.clipBar.isReloading = _loc6_;
            this._isCritical = param3;
            invalidate(CURSOR_STATE_INVALID);
         }
      }
      
      public function applyNow() : void
      {
         GTweener.removeTweens(this.clipBar);
         this._currentShellIdx = this.targetShellIndex;
         this.clipBar.rotation = this.targetRotationAngle;
         this._applyNow = true;
         validateNow();
         this._applyNow = false;
         this.clipBar.applyNow();
      }
      
      public function showShot() : void
      {
         this.clipBar.showShot();
         this.cursor.showShot();
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
         return this._currentShellIdx > 0 ? int(EXTRA_SHELL_ANGLE_GAP + BASE_SHELL_ANGLE_GAP * (this._currentShellIdx - 1)) : int(0);
      }
   }
}
