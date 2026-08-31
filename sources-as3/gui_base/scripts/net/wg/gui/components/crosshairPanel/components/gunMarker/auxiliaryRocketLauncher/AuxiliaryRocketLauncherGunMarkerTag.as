package net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher
{
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class AuxiliaryRocketLauncherGunMarkerTag extends SimpleContainer
   {
       
      
      public var tag:AuxiliaryRocketLauncherGunMarkerTagClip = null;
      
      public function AuxiliaryRocketLauncherGunMarkerTag()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.tag.dispose();
         this.tag = null;
         super.onDispose();
      }
      
      public function setVisible(param1:Boolean) : void
      {
         this.tag.visible = param1;
         this.tag.setVisible(param1);
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this.tag.setZoomFactor(param1);
      }
   }
}
