package net.wg.frontline.gui.battle.views.frontlineDeploymentMap.components
{
   import flash.display.Sprite;
   import net.wg.gui.battle.views.minimap.containers.MinimapEntriesContainer;
   
   public class FrontlineDeploymentMapEntriesContainer extends MinimapEntriesContainer
   {
       
      
      public var zones:Sprite = null;
      
      public var landingZone:Sprite = null;
      
      public var hqs:Sprite = null;
      
      public function FrontlineDeploymentMapEntriesContainer()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.zones = null;
         this.hqs = null;
         this.landingZone = null;
         super.onDispose();
      }
   }
}
