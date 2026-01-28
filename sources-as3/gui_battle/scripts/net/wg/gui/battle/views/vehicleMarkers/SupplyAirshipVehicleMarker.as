package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.geom.Point;
   import net.wg.gui.battle.views.vehicleMarkers.VO.CrossOffset;
   import net.wg.gui.battle.views.vehicleMarkers.VO.VehicleMarkerPart;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class SupplyAirshipVehicleMarker extends SupplyVehicleMarker
   {
      
      private static const SUPPLY_ICON_NAME_LBL:String = "supplyStickyIcon";
      
      private static const AIRSHIP_NAME_STICKY_Y_OFFSET:int = 10;
      
      private static const AIRSHIP_ICON_Y_OFFSET:int = -44;
      
      private static const HIT_LABEL_Y_OFFSET:int = -8;
      
      private static const AIRSHIP_START_Y:int = -20;
      
      private static const SHADOW_STICKY_POSITION:Point = new Point(-94,-105);
      
      private static const SHADOW_POSITIONS:Array = [null,new Point(-94,-30),new Point(-94,-40),new Point(-94,-14)];
       
      
      public var supplyStickyIcon:MovieClip = null;
      
      public function SupplyAirshipVehicleMarker()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.supplyStickyIcon.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.supplyStickyIcon = null;
         super.onDispose();
      }
      
      override protected function getVehIconYOffset() : int
      {
         return AIRSHIP_ICON_Y_OFFSET;
      }
      
      override protected function prepareOffsets() : void
      {
         offsets = [0,0,0,0,0,0,0,0,0,18,54,0];
      }
      
      override protected function prepareCrossOffsets() : Array
      {
         return [null,null,new CrossOffset(hpField,-1),null,null,new CrossOffset(vehicleNameField,-4),null,null,new CrossOffset(vehicleNameField,3),new CrossOffset(statusContainer,16,vehicleDist,-4,hpField,18),new CrossOffset(vehicleDist,14,hpField,36,actionMarker,24,vehicleNameField,36),null];
      }
      
      override protected function getStartY() : int
      {
         return AIRSHIP_START_Y;
      }
      
      override protected function redrawShadow(param1:Boolean, param2:Boolean, param3:Boolean, param4:Boolean) : void
      {
         var _loc6_:Point = null;
         var _loc5_:int = !param3 && param4 ? int(1) : int(0);
         _loc5_ += !!param2 ? 1 : 0;
         if(_loc5_ == 1)
         {
            _loc5_ += !!param3 ? 2 : 0;
         }
         if(_loc5_ > 0)
         {
            _loc6_ = !!this.isStickyState ? SHADOW_STICKY_POSITION : SHADOW_POSITIONS[_loc5_];
            vmManager.drawGraphics(VMAtlasItemName.getShadowName(_loc5_),bgShadow.graphics,_loc6_);
            bgShadow.visible = true;
         }
         else
         {
            bgShadow.visible = false;
         }
      }
      
      override protected function layoutParts(param1:Vector.<Boolean>) : void
      {
         var _loc4_:VehicleMarkerPart = null;
         var _loc6_:int = 0;
         var _loc2_:int = this.getStartY();
         var _loc3_:int = markerParts.length;
         var _loc5_:VehicleMarkerPart = null;
         var _loc7_:Boolean = canUseCachedVisibility;
         var _loc8_:Boolean = false;
         var _loc9_:int = 0;
         while(_loc9_ < _loc3_)
         {
            _loc4_ = markerParts[_loc9_];
            _loc8_ = param1[_loc9_];
            if(_loc7_ && _loc8_ && _loc4_.cachedVisibility == _loc8_)
            {
               _loc2_ = _loc4_.y + _loc4_.height;
               _loc5_ = _loc4_;
            }
            else
            {
               _loc7_ = false;
               if(_loc8_)
               {
                  _loc6_ = _loc4_.offsetFromPart(_loc5_);
                  _loc4_.y = _loc2_ + _loc6_;
                  _loc5_ = _loc4_;
                  _loc2_ = _loc4_.y + _loc4_.height;
               }
            }
            _loc4_.cachedVisibility = _loc8_;
            _loc9_++;
         }
         healthBar.y = hpField.y + HP_FIELD_TO_HP_BAR_OFFSET;
         hitLabel.y = criticalHitLabel.y = healthBar.y + HIT_LABEL_Y_OFFSET;
         if(this.isStickyState)
         {
            vehicleNameField.y = this.supplyStickyIcon.y + AIRSHIP_NAME_STICKY_Y_OFFSET | 0;
         }
         canUseCachedVisibility = true;
      }
      
      override protected function updatePartsVisibility() : Vector.<Boolean>
      {
         this.supplyStickyIcon.visible = this.getIsPartVisible(SUPPLY_ICON_NAME_LBL);
         return super.updatePartsVisibility();
      }
      
      override protected function getIsPartVisible(param1:String, param2:Object = null) : Boolean
      {
         if(param1 == V_NAME_LBL || param1 == SUPPLY_ICON_NAME_LBL)
         {
            return this.isStickyState;
         }
         return super.getIsPartVisible(param1,param2);
      }
      
      private function get isStickyState() : Boolean
      {
         return isStickyAndOutOfScreen && StringUtils.isEmpty(lastActionState);
      }
   }
}
