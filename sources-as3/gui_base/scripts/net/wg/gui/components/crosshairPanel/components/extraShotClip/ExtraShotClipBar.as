package net.wg.gui.components.crosshairPanel.components.extraShotClip
{
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.clik.constants.InvalidationType;
   
   public class ExtraShotClipBar extends SimpleContainer
   {
       
      
      public var cursor:ExtraShotClipCursor;
      
      public var shell_1:ExtraShotShellProgressBar;
      
      public var shell_2:ShellProgressBar;
      
      public var shell_3:ShellProgressBar;
      
      public var shell_4:ShellProgressBar;
      
      public var shell_5:ShellProgressBar;
      
      public var shell_6:ShellProgressBar;
      
      public var shell_7:ShellProgressBar;
      
      public var shell_8:ShellProgressBar;
      
      private var _shellsList:Vector.<ShellProgressBar> = null;
      
      private var _isCritical:Boolean = false;
      
      private var _clipCapacity:uint = 0;
      
      private var _shellCount:uint = 0;
      
      private var _totalAmmo:uint = 0;
      
      private var _isReloading:Boolean = false;
      
      private var _reloadProgress:Number = 0;
      
      private var _applyNow:Boolean = false;
      
      public function ExtraShotClipBar()
      {
         super();
         this._shellsList = new <ShellProgressBar>[this.shell_1,this.shell_2,this.shell_3,this.shell_4,this.shell_5,this.shell_6,this.shell_7,this.shell_8];
      }
      
      override protected function draw() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:ShellProgressBar = null;
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
               }
               _loc3_++;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:ShellProgressBar = null;
         for each(_loc1_ in this._shellsList)
         {
            _loc1_.dispose();
         }
         this._shellsList.length = 0;
         this._shellsList = null;
         this.shell_8 = this.shell_7 = this.shell_6 = this.shell_5 = this.shell_4 = this.shell_3 = this.shell_2 = this.shell_1 = null;
         this.cursor.dispose();
         this.cursor = null;
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
      
      public function applyNow() : void
      {
         this._applyNow = true;
         validateNow();
         this._applyNow = false;
      }
      
      public function showShot() : void
      {
         if(this.cursor.showShot())
         {
            this.shell_1.showShot();
         }
      }
      
      public function setCursorState(param1:String, param2:Boolean = false) : void
      {
         if(param1 == ExtraShotClipCursor.CRITICAL_STATE_LABEL)
         {
            this.cursor.criticalStateFrame = this.criticalStateFrame;
         }
         this.cursor.setState(param1,param2);
      }
      
      public function get criticalStateFrame() : int
      {
         return this.shell_1.criticalStateFrame;
      }
   }
}
