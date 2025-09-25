package net.wg.gui.battle.views.widgetsPanel.vo
{
   import net.wg.data.constants.VehicleModules;
   import net.wg.data.constants.generated.BATTLE_ITEM_STATES;
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class DeviceStateInfo extends DAAPIDataClass
   {
      
      private static const PRIORITY:Vector.<String> = new <String>[VehicleModules.ENGINE + BATTLE_ITEM_STATES.CRITICAL,VehicleModules.CHASSIS + BATTLE_ITEM_STATES.DESTROYED,VehicleModules.ENGINE + BATTLE_ITEM_STATES.DESTROYED];
       
      
      public var deviceName:String = "";
      
      public var deviceState:String = "";
      
      public function DeviceStateInfo(param1:Object = null)
      {
         super(param1);
      }
      
      override public function isEquals(param1:DAAPIDataClass) : Boolean
      {
         var _loc2_:DeviceStateInfo = param1 as DeviceStateInfo;
         if(!_loc2_)
         {
            return false;
         }
         return this.deviceName == _loc2_.deviceName && this.deviceState == _loc2_.deviceState;
      }
      
      public function get priority() : int
      {
         return PRIORITY.indexOf(this.deviceName + this.deviceState);
      }
   }
}
