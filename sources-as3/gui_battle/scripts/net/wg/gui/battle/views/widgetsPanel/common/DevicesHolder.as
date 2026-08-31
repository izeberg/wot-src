package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.MECHANIC_WIDGET_DEVICES_CONST;
   import net.wg.gui.battle.views.widgetsPanel.vo.DeviceStateInfo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class DevicesHolder extends MovieClip implements IDisposable
   {
       
      
      private var _isDisposed:Boolean = false;
      
      private var _device:Device = null;
      
      private var _deviceStates:Vector.<DeviceStateInfo> = null;
      
      public function DevicesHolder()
      {
         super();
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.removeDevice();
         if(this._deviceStates)
         {
            this._deviceStates.splice(0,this._deviceStates.length);
            this._deviceStates = null;
         }
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function hasDeviceState(param1:DeviceStateInfo) : Boolean
      {
         var _loc2_:DeviceStateInfo = null;
         if(!this._deviceStates)
         {
            return false;
         }
         for each(_loc2_ in this._deviceStates)
         {
            if(param1.isEquals(_loc2_))
            {
               return true;
            }
         }
         return false;
      }
      
      public function setDevices(param1:Vector.<DeviceStateInfo>) : void
      {
         var _loc4_:DeviceStateInfo = null;
         this._deviceStates = param1;
         var _loc2_:DeviceStateInfo = null;
         var _loc3_:int = -1;
         for each(_loc4_ in param1)
         {
            if(MECHANIC_WIDGET_DEVICES_CONST.DEVICES.indexOf(_loc4_.deviceName) != -1)
            {
               if(_loc4_.priority > _loc3_)
               {
                  _loc2_ = _loc4_;
                  _loc3_ = _loc4_.priority;
               }
            }
         }
         if(_loc2_ == null)
         {
            this.removeDevice();
            return;
         }
         if(this._device == null || this._device.getState() != _loc2_.deviceState)
         {
            this.removeDevice();
            this.addDevice(_loc2_.deviceState);
         }
         if(this._device)
         {
            this._device.setData(_loc2_);
         }
      }
      
      private function removeDevice() : void
      {
         if(this._device)
         {
            this._device.stop();
            removeChild(this._device);
            this._device.dispose();
            this._device = null;
         }
      }
      
      private function addDevice(param1:String) : void
      {
         var _loc2_:String = Values.EMPTY_STR;
         if(param1 == MECHANIC_WIDGET_DEVICES_CONST.DEVICE_STATE_CRITICAL)
         {
            _loc2_ = MECHANIC_WIDGET_DEVICES_CONST.LINKAGE_DEVICE_CRITICAL;
         }
         else if(param1 == MECHANIC_WIDGET_DEVICES_CONST.DEVICE_STATE_DESTROYED)
         {
            _loc2_ = MECHANIC_WIDGET_DEVICES_CONST.LINKAGE_DEVICE_DESTROYED;
         }
         if(StringUtils.isEmpty(_loc2_))
         {
            return;
         }
         this._device = App.utils.classFactory.getComponent(_loc2_,Device);
         addChild(this._device);
      }
   }
}
