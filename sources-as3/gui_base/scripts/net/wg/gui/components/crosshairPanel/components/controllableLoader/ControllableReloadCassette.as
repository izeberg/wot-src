package net.wg.gui.components.crosshairPanel.components.controllableLoader
{
   import flash.display.BlendMode;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.infrastructure.base.SimpleContainer;
   import scaleform.gfx.TextFieldEx;
   
   public class ControllableReloadCassette extends SimpleContainer
   {
      
      private static const CLIP_CAPACITY_VALIDATION:String = "clipCapacityInvalid";
      
      private static const CLIP_INFO_VALIDATION:String = "clipInfoInvalid";
      
      private static const FRACTIONAL_FORMAT_CMD:String = "WG.getFractionalFormat";
      
      private static const TIMER_NORMAL_TEXT_COLOR:uint = 16777215;
      
      private static const TIMER_CRITICAL_TEXT_COLOR:uint = 16740352;
       
      
      public var timerTF:TextField = null;
      
      public var shell_1:ControllableReloadShellProgressBar = null;
      
      public var shell_2:ControllableReloadShellProgressBar = null;
      
      public var shell_3:ControllableReloadShellProgressBar = null;
      
      public var shell_4:ControllableReloadShellProgressBar = null;
      
      public var shell_5:ControllableReloadShellProgressBar = null;
      
      public var shell_6:ControllableReloadShellProgressBar = null;
      
      public var shell_7:ControllableReloadShellProgressBar = null;
      
      public var shell_8:ControllableReloadShellProgressBar = null;
      
      public var shell_9:ControllableReloadShellProgressBar = null;
      
      public var shell_10:ControllableReloadShellProgressBar = null;
      
      public var shell_11:ControllableReloadShellProgressBar = null;
      
      public var shell_12:ControllableReloadShellProgressBar = null;
      
      private var _shells:Vector.<ControllableReloadShellProgressBar> = null;
      
      private var _clipCapacity:int = -1;
      
      private var _clipState:String = "";
      
      private var _quantityInClip:int = -1;
      
      private var _isReloading:Boolean = false;
      
      private var _applyNow:Boolean = false;
      
      public function ControllableReloadCassette()
      {
         super();
         this._shells = new <ControllableReloadShellProgressBar>[this.shell_1,this.shell_2,this.shell_3,this.shell_4,this.shell_5,this.shell_6,this.shell_7,this.shell_8,this.shell_9,this.shell_10,this.shell_11,this.shell_12];
         TextFieldEx.setNoTranslate(this.timerTF,true);
         this.timerTF.blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:ControllableReloadShellProgressBar = null;
         for each(_loc1_ in this._shells)
         {
            _loc1_.dispose();
         }
         this._shells.length = 0;
         this._shells = null;
         this.shell_1 = this.shell_2 = this.shell_3 = this.shell_4 = this.shell_5 = this.shell_6 = this.shell_7 = this.shell_8 = this.shell_9 = this.shell_10 = this.shell_11 = this.shell_12 = null;
         this.timerTF = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._clipCapacity > 0 && isInvalid(CLIP_CAPACITY_VALIDATION))
         {
            this.updateTotalAmmoState();
         }
         if(isInvalid(CLIP_INFO_VALIDATION))
         {
            this.updateCurrentAmmoStates(this._quantityInClip);
         }
      }
      
      public function applyNow() : void
      {
         this._applyNow = true;
         validateNow();
         this._applyNow = false;
      }
      
      public function setClipsParam(param1:int) : void
      {
         if(this._clipCapacity != param1)
         {
            this._clipCapacity = param1;
            invalidate(CLIP_CAPACITY_VALIDATION);
         }
      }
      
      public function updateInfo(param1:int, param2:String) : void
      {
         if(this._quantityInClip != param1 || this._clipState != param2)
         {
            this._quantityInClip = param1;
            this._clipState = param2;
            invalidate(CLIP_INFO_VALIDATION);
         }
      }
      
      private function updateCurrentAmmoStates(param1:int) : void
      {
         var _loc2_:Boolean = this._clipState == CrosshairConsts.CRITICAL;
         var _loc3_:ControllableReloadShellProgressBar = null;
         var _loc4_:int = 0;
         while(_loc4_ < this._clipCapacity)
         {
            _loc3_ = this._shells[_loc4_];
            _loc3_.setState(_loc4_ < param1 && !this._isReloading ? ShellProgressBar.READY_STATE : ShellProgressBar.EMPTY_STATE,this._applyNow);
            _loc3_.setReloading(_loc4_ < param1 ? Number(1) : Number(0),this._applyNow);
            _loc3_.isCritical = _loc2_;
            _loc4_++;
         }
      }
      
      private function updateTotalAmmoState() : void
      {
         var _loc1_:int = this._shells.length;
         var _loc2_:int = 0;
         while(_loc2_ < _loc1_)
         {
            this._shells[_loc2_].visible = _loc2_ < this._clipCapacity;
            _loc2_++;
         }
      }
      
      public function set reloadingPercent(param1:Number) : void
      {
         if(this._quantityInClip > -1)
         {
            this._shells[this._quantityInClip].setReloading(param1 > 0 && this._quantityInClip < this._clipCapacity ? Number(1 - param1) : Number(0));
         }
      }
      
      public function set isReloading(param1:Boolean) : void
      {
         if(this._isReloading != param1)
         {
            this._isReloading = param1;
            invalidate(CLIP_INFO_VALIDATION);
         }
      }
      
      public function setTimer(param1:Boolean, param2:Number, param3:Boolean) : void
      {
         var _loc4_:String = null;
         this.timerTF.visible = param1;
         if(param1)
         {
            _loc4_ = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param2]);
            this.timerTF.textColor = !!param3 ? uint(TIMER_CRITICAL_TEXT_COLOR) : uint(TIMER_NORMAL_TEXT_COLOR);
            this.timerTF.text = _loc4_.slice(0,_loc4_.length - 1);
         }
      }
   }
}
