package net.wg.historical_battles.infrastructure.base.meta.impl
{
   import net.wg.historical_battles.gui.battle.views.staticMarkers.controlPoint.HBLocationActionMarker;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleActionMarker;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleMarker;
   import net.wg.historical_battles.gui.battle.views.vehicleMarkers.HBVehicleMarkerBase;
   
   public class ClassManagerExtensionBattleMarkersMeta
   {
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_STATICMARKERS_CONTROLPOINT_HBLOCATIONACTIONMARKER:Class = HBLocationActionMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEACTIONMARKER:Class = HBVehicleActionMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEMARKER:Class = HBVehicleMarker;
      
      public static const NET_WG_HISTORICAL_BATTLES_GUI_BATTLE_VIEWS_VEHICLEMARKERS_HBVEHICLEMARKERBASE:Class = HBVehicleMarkerBase;
       
      
      public function ClassManagerExtensionBattleMarkersMeta()
      {
         super();
      }
   }
}
