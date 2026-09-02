package net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers
{
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStatusMarker;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.WTVehicleMarkersConstants;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class WTVehicleStatusMarker extends VehicleStatusMarker
   {
       
      
      private var _atlasIconAlias:String = "";
      
      private var _atlasSrcMode:Boolean;
      
      public function WTVehicleStatusMarker()
      {
         super();
      }
      
      override public function isAtlasSrcMode() : Boolean
      {
         return this._atlasSrcMode;
      }
      
      override public function setStatusID(param1:int) : void
      {
         super.setStatusID(param1);
         this._atlasIconAlias = WTVehicleMarkersConstants.getStatusMarkerIconNameByStatusId(param1);
         this._atlasSrcMode = !StringUtils.isEmpty(this._atlasIconAlias);
      }
      
      override public function get altasIconAlias() : String
      {
         return this._atlasIconAlias;
      }
   }
}
