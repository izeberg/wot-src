package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core
{
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.minimap.MinimapEntryController;
   import net.wg.gui.battle.views.minimap.components.entries.constants.PointsOfInterestMinimapEntryConst;
   import net.wg.gui.battle.views.minimap.components.entries.constants.ScenarioMinimapEntryConst;
   
   public class SimpleMinimapEntry extends BattleUIComponent
   {
       
      
      public var marker:MinimapEntry = null;
      
      public function SimpleMinimapEntry()
      {
         super();
         this.marker.visible = true;
         MinimapEntryController.instance.registerScalableEntry(this);
      }
      
      override protected function initialize() : void
      {
         this.marker.iconType = ScenarioMinimapEntryConst.SCENARIO_MARKER_ICON;
         this.marker.backIcon = PointsOfInterestMinimapEntryConst.POI_MARKER_BACK_ICON;
         super.initialize();
      }
      
      override protected function onDispose() : void
      {
         MinimapEntryController.instance.unregisterScalableEntry(this);
         this.marker.dispose();
         this.marker = null;
         super.onDispose();
      }
      
      public function setProgress(param1:int) : void
      {
      }
   }
}
