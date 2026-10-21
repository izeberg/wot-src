package net.wg.portal.gui.battle.views.staticMarkers.scenario.core
{
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class SimpleMarker extends BattleUIComponent
   {
       
      
      public var marker:MarkerCircle = null;
      
      public function SimpleMarker()
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
      
      public function showStatTrackMarker(param1:String, param2:String, param3:Number = 1, param4:Boolean = false) : void
      {
      }
   }
}
