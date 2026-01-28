package net.wg.gui.battle.views.vehicleMarkers
{
   import org.idmedia.as3commons.util.StringUtils;
   
   public class SupplyVehicleMarker extends VehicleMarker implements IMarkerManagerHandler, IVehicleMarkerInvokable
   {
      
      private static const VEH_ICON_Y_OFFSET:int = -7;
      
      private static const SUPPLY_VIS_SETTINGS:Object = {
         "Icon":false,
         "Level":false,
         "PlayerName":false
      };
       
      
      private var _supplyType:String = null;
      
      public function SupplyVehicleMarker()
      {
         super();
      }
      
      public function setSupplyType(param1:String) : void
      {
         if(this._supplyType != param1)
         {
            this._supplyType = param1;
            invalidateData();
         }
      }
      
      override public function updateHealth(param1:int, param2:int, param3:String) : void
      {
         super.updateHealth(param1,param2,param3);
         this.updateRepairState(param1);
      }
      
      protected function getVehIconYOffset() : int
      {
         return VEH_ICON_Y_OFFSET;
      }
      
      override protected function initialDrawParts() : void
      {
      }
      
      override protected function setupVehicleIcon() : void
      {
      }
      
      override protected function getIsPartVisible(param1:String, param2:Object = null) : Boolean
      {
         if(param1 in SUPPLY_VIS_SETTINGS)
         {
            return SUPPLY_VIS_SETTINGS[param1];
         }
         if(vehicleDestroyed && model.currHealth > 0 && entityType == VehicleMarkersConstants.ENTITY_TYPE_ALLY && (param1 == HEALTH_BAR || param1 == HEALTH_LBL))
         {
            return super.getIsPartVisible(param1,vmManager.markerSettings[entityType]);
         }
         return super.getIsPartVisible(param1);
      }
      
      override protected function setVehicleType() : void
      {
         if(vehicleDestroyedAlready || StringUtils.isEmpty(this._supplyType))
         {
            return;
         }
         var _loc1_:String = VMAtlasItemName.getVehicleTypeIconName(markerColor,this._supplyType,false);
         vmManager.drawWithCenterAlign(_loc1_,marker.vehicleTypeIcon.graphics,true,false,0,this.getVehIconYOffset());
      }
      
      private function updateRepairState(param1:int) : void
      {
         updateMarkerSettings();
      }
   }
}
