package net.wg.gui.lobby.storage.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class StorageRestoreDevicesVO extends DAAPIDataClass
   {
       
      
      public var bgSource:String = "";
      
      public var titleLabel:String = "";
      
      public var backBtn:String = "";
      
      public var backBtnLabel:String = "";
      
      public function StorageRestoreDevicesVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
