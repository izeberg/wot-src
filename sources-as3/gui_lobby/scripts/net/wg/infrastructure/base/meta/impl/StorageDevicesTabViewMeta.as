package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.storage.categories.storage.ItemsWithVehicleFilterTabView;
   import net.wg.gui.lobby.storage.data.StorageModulesFilterVO;
   import net.wg.gui.lobby.storage.data.StorageRestoreDevicesButtonVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class StorageDevicesTabViewMeta extends ItemsWithVehicleFilterTabView
   {
       
      
      public var onRestoreButtonClick:Function;
      
      private var _storageModulesFilterVO:StorageModulesFilterVO;
      
      private var _storageRestoreDevicesButtonVO:StorageRestoreDevicesButtonVO;
      
      public function StorageDevicesTabViewMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._storageModulesFilterVO)
         {
            this._storageModulesFilterVO.dispose();
            this._storageModulesFilterVO = null;
         }
         if(this._storageRestoreDevicesButtonVO)
         {
            this._storageRestoreDevicesButtonVO.dispose();
            this._storageRestoreDevicesButtonVO = null;
         }
         super.onDispose();
      }
      
      public function onRestoreButtonClickS() : void
      {
         App.utils.asserter.assertNotNull(this.onRestoreButtonClick,"onRestoreButtonClick" + Errors.CANT_NULL);
         this.onRestoreButtonClick();
      }
      
      public final function as_initModulesFilter(param1:Object) : void
      {
         var _loc2_:StorageModulesFilterVO = this._storageModulesFilterVO;
         this._storageModulesFilterVO = new StorageModulesFilterVO(param1);
         this.initModulesFilter(this._storageModulesFilterVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_setRestoreButtonData(param1:Object) : void
      {
         var _loc2_:StorageRestoreDevicesButtonVO = this._storageRestoreDevicesButtonVO;
         this._storageRestoreDevicesButtonVO = new StorageRestoreDevicesButtonVO(param1);
         this.setRestoreButtonData(this._storageRestoreDevicesButtonVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function initModulesFilter(param1:StorageModulesFilterVO) : void
      {
         var _loc2_:String = "as_initModulesFilter" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setRestoreButtonData(param1:StorageRestoreDevicesButtonVO) : void
      {
         var _loc2_:String = "as_setRestoreButtonData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
