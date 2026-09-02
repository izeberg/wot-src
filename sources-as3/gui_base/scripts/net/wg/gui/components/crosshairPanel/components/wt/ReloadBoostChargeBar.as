package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class ReloadBoostChargeBar extends SimpleDisposable
   {
       
      
      public var mc:MovieClip = null;
      
      public function ReloadBoostChargeBar()
      {
         super();
      }
      
      override public function gotoAndPlay(param1:Object, param2:String = null) : void
      {
         super.gotoAndStop(param1,param2);
         this.mc.gotoAndPlay(1);
      }
      
      override public function gotoAndStop(param1:Object, param2:String = null) : void
      {
         super.gotoAndStop(param1,param2);
         this.mc.gotoAndStop(this.mc.totalFrames);
      }
      
      override protected function onDispose() : void
      {
         this.mc = null;
      }
   }
}
