package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.widgetsPanel.BaseVehicleMechanicsWidget;
   import net.wg.gui.battle.views.widgetsPanel.vo.DeviceStateInfo;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class PillboxSiegeWidgetMeta extends BaseVehicleMechanicsWidget
   {
       
      
      private var _vectorDeviceStateInfo:Vector.<DeviceStateInfo>;
      
      public function PillboxSiegeWidgetMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:DeviceStateInfo = null;
         if(this._vectorDeviceStateInfo)
         {
            for each(_loc1_ in this._vectorDeviceStateInfo)
            {
               _loc1_.dispose();
            }
            this._vectorDeviceStateInfo.splice(0,this._vectorDeviceStateInfo.length);
            this._vectorDeviceStateInfo = null;
         }
         super.onDispose();
      }
      
      public final function as_setDeviceStates(param1:Array) : void
      {
         var _loc5_:DeviceStateInfo = null;
         var _loc2_:Vector.<DeviceStateInfo> = this._vectorDeviceStateInfo;
         this._vectorDeviceStateInfo = new Vector.<DeviceStateInfo>(0);
         var _loc3_:uint = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            this._vectorDeviceStateInfo[_loc4_] = new DeviceStateInfo(param1[_loc4_]);
            _loc4_++;
         }
         this.setDeviceStates(this._vectorDeviceStateInfo);
         if(_loc2_)
         {
            for each(_loc5_ in _loc2_)
            {
               _loc5_.dispose();
            }
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      protected function setDeviceStates(param1:Vector.<DeviceStateInfo>) : void
      {
         var _loc2_:String = "as_setDeviceStates" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
