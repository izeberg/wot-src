package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.widgetsPanel.vo.DeviceStateInfo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class Device extends MovieClip implements IDisposable
   {
      
      private static const START_FRAME:int = 1;
       
      
      public var icon:MovieClip = null;
      
      private var _isDisposable:Boolean = false;
      
      private var _deviceInfo:DeviceStateInfo = null;
      
      public function Device()
      {
         super();
      }
      
      public final function dispose() : void
      {
         stop();
         this.icon = null;
         this._deviceInfo = null;
         this._isDisposable = true;
      }
      
      public function getState() : String
      {
         return this._deviceInfo.deviceState;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposable;
      }
      
      public function setData(param1:DeviceStateInfo) : void
      {
         if(this._deviceInfo == null || !this._deviceInfo.isEquals(param1))
         {
            this._deviceInfo = param1;
            this.icon.gotoAndStop(param1.deviceName);
            gotoAndPlay(START_FRAME);
         }
      }
   }
}
