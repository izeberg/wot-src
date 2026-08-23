package net.wg.white_tiger.gui.battle.views.minimap
{
   import flash.display.Sprite;
   import net.wg.gui.battle.views.minimap.containers.MinimapEntriesContainer;
   
   public class WhiteTigerDeploymentMapEntriesContainer extends MinimapEntriesContainer
   {
       
      
      public var deploymentPoints:Sprite = null;
      
      public function WhiteTigerDeploymentMapEntriesContainer()
      {
         super();
         this.deploymentPoints.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.deploymentPoints = null;
         super.onDispose();
      }
      
      public function set isDeploymentMode(param1:Boolean) : void
      {
         this.deploymentPoints.visible = param1;
      }
   }
}
