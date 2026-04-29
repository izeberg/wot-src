package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.storage.categories.storage.StorageDevicesTabView;
   
   public class StorageRestoreDevicesContentMeta extends StorageDevicesTabView
   {
       
      
      public var restoreItem:Function;
      
      public function StorageRestoreDevicesContentMeta()
      {
         super();
      }
      
      public function restoreItemS(param1:Number, param2:Number) : void
      {
         App.utils.asserter.assertNotNull(this.restoreItem,"restoreItem" + Errors.CANT_NULL);
         this.restoreItem(param1,param2);
      }
   }
}
