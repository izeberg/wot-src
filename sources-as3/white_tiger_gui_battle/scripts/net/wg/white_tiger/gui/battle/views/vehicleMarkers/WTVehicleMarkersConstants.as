package net.wg.white_tiger.gui.battle.views.vehicleMarkers
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.Values;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_MARKER_STATES;
   
   public class WTVehicleMarkersConstants
   {
      
      public static const ATLAS_SRC_ICONS_STATUS_MARKERS:Dictionary = new Dictionary();
      
      {
         ATLAS_SRC_ICONS_STATUS_MARKERS[WHITE_TIGER_BATTLE_MARKER_STATES.WT_INVISIBLE_STATE] = "wt_invisible";
      }
      
      public function WTVehicleMarkersConstants()
      {
         super();
      }
      
      public static function getStatusMarkerIconNameByStatusId(param1:int) : String
      {
         if(param1 in ATLAS_SRC_ICONS_STATUS_MARKERS)
         {
            return ATLAS_SRC_ICONS_STATUS_MARKERS[param1];
         }
         return Values.EMPTY_STR;
      }
   }
}
