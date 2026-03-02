package net.wg.gui.battle.views.minimap.components.entries.interfaces
{
   import net.wg.infrastructure.interfaces.IDisplayObject;
   
   public interface IVehicleMinimapEntry extends IDisplayObject
   {
       
      
      function showVehicleName() : void;
      
      function hideVehicleName() : void;
      
      function highlight() : void;
      
      function unhighlight() : void;
      
      function get vehicleID() : Number;
      
      function updateSizeIndex(param1:int) : void;
      
      function setAlive() : void;
      
      function setDead(param1:Boolean) : void;
      
      function setAnimation(param1:String) : void;
      
      function setFlagBearer(param1:Boolean) : void;
      
      function setGUILabel(param1:String) : void;
      
      function setInAoI(param1:Boolean) : void;
      
      function setVehicleHealth(param1:int) : void;
      
      function setVehicleInfo(param1:Number, param2:String, param3:String, param4:String, param5:String) : void;
      
      function showVehicleHp(param1:Boolean) : void;
      
      function showExtendedInfo(param1:Boolean) : void;
      
      function get isVehicleLabelVisible() : Boolean;
      
      function get isHpCircleVisible() : Boolean;
   }
}
