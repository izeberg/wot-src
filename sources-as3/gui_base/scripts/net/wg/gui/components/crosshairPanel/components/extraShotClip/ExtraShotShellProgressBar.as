package net.wg.gui.components.crosshairPanel.components.extraShotClip
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   
   public class ExtraShotShellProgressBar extends ShellProgressBar
   {
       
      
      public var shotMC:MovieClip;
      
      public function ExtraShotShellProgressBar()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.shotMC = null;
         super.onDispose();
      }
      
      public function showShot() : void
      {
         this.shotMC.play();
      }
      
      public function get criticalStateFrame() : uint
      {
         return activeMC.currentFrame - 1;
      }
   }
}
