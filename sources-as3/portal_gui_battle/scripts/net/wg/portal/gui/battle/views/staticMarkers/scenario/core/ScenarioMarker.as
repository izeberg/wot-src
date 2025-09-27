package net.wg.portal.gui.battle.views.staticMarkers.scenario.core
{
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class ScenarioMarker extends BattleUIComponent
   {
      
      private static const DIVIDE_100:Number = 0.01;
       
      
      public var marker:ScenarioMarkerProgressCircle = null;
      
      public function ScenarioMarker()
      {
         super();
         this.marker.visible = true;
      }
      
      override protected function onDispose() : void
      {
         this.marker.dispose();
         this.marker = null;
         super.onDispose();
      }
      
      public function hideStatTrackMarker(param1:Boolean = false) : void
      {
      }
      
      public function setProgress(param1:Number) : void
      {
         this.marker.updateProgress(param1 * DIVIDE_100);
      }
      
      public function showStatTrackMarker(param1:String, param2:String, param3:Number = 1, param4:Boolean = false) : void
      {
      }
   }
}
