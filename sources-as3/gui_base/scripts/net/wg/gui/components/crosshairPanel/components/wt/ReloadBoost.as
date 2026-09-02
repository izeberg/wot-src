package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class ReloadBoost extends SimpleDisposable
   {
      
      public static const MAX_PROGRESS:uint = 5;
      
      private static const OFFSET_X:uint = 10;
      
      private static const OFFSET_Y:uint = 12;
       
      
      public var reloadBoostOnIconMc:MovieClip = null;
      
      public var reloadBoostOnCharge:MovieClip = null;
      
      public var reloadBoostOffIconMc:MovieClip = null;
      
      public var reloadBoostOffCharge:MovieClip = null;
      
      public var reloadBoostFailIconMc:MovieClip = null;
      
      public var reloadBoostFailCharge:MovieClip = null;
      
      public function ReloadBoost()
      {
         super();
         this.initialize();
      }
      
      override protected function onDispose() : void
      {
         this.reloadBoostOnIconMc = null;
         this.reloadBoostOnCharge = null;
         this.reloadBoostOffIconMc = null;
         this.reloadBoostOffCharge = null;
         this.reloadBoostFailIconMc = null;
         this.reloadBoostFailCharge = null;
      }
      
      public function showProgress(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(param1 > MAX_PROGRESS)
         {
            param1 = MAX_PROGRESS;
         }
         this.playBarAnimation(this.reloadBoostOnCharge,param1,param3);
         this.playBarAnimation(this.reloadBoostFailCharge,param1,param3);
         if(param2)
         {
            this.reloadBoostOnIconMc.visible = this.reloadBoostOnCharge.visible = false;
            this.reloadBoostOffIconMc.visible = this.reloadBoostOffCharge.visible = false;
            this.reloadBoostFailIconMc.visible = this.reloadBoostFailCharge.visible = true;
            this.playIconAnimation(this.reloadBoostFailIconMc,param3);
            return;
         }
         if(param1 > 0)
         {
            this.reloadBoostOnIconMc.visible = this.reloadBoostOnCharge.visible = true;
            this.reloadBoostOffIconMc.visible = this.reloadBoostOffCharge.visible = false;
            this.reloadBoostFailIconMc.visible = this.reloadBoostFailCharge.visible = false;
            this.playIconAnimation(this.reloadBoostOnIconMc,param3);
         }
         else
         {
            this.reloadBoostOnIconMc.visible = this.reloadBoostOnCharge.visible = false;
            this.reloadBoostOffIconMc.visible = this.reloadBoostOffCharge.visible = true;
            this.reloadBoostFailIconMc.visible = this.reloadBoostFailCharge.visible = false;
            this.playIconAnimation(this.reloadBoostOffIconMc,param3);
         }
      }
      
      public function updatePosition(param1:int, param2:int) : void
      {
         x = param1 - (width >> 1) + OFFSET_X;
         y = param2 - (height >> 1) + OFFSET_Y;
      }
      
      protected function initialize() : void
      {
         this.reloadBoostOnIconMc.visible = this.reloadBoostOnCharge.visible = false;
         this.reloadBoostOffIconMc.visible = this.reloadBoostOffCharge.visible = true;
         this.reloadBoostFailIconMc.visible = this.reloadBoostFailCharge.visible = false;
      }
      
      private function playIconAnimation(param1:MovieClip, param2:Boolean) : void
      {
         if(param2)
         {
            param1.gotoAndPlay(1);
         }
         else
         {
            param1.gotoAndStop(param1.totalFrames);
         }
      }
      
      private function playBarAnimation(param1:MovieClip, param2:Object, param3:Boolean) : void
      {
         if(param3)
         {
            param1.gotoAndPlay(param2);
         }
         else
         {
            param1.gotoAndStop(param2);
         }
      }
   }
}
