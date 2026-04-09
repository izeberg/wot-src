package net.wg.gui.lobby.storage.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class StorageRestoreDevicesButtonVO extends DAAPIDataClass
   {
       
      
      public var isVisible:Boolean = false;
      
      public var counterValue:int = -1;
      
      public function StorageRestoreDevicesButtonVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
