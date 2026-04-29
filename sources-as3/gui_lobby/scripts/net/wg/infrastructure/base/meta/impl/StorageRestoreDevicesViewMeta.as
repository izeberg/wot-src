package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.storage.data.StorageRestoreDevicesVO;
   import net.wg.infrastructure.base.AbstractScreen;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class StorageRestoreDevicesViewMeta extends AbstractScreen
   {
       
      
      public var onBackClick:Function;
      
      private var _storageRestoreDevicesVO:StorageRestoreDevicesVO;
      
      public function StorageRestoreDevicesViewMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._storageRestoreDevicesVO)
         {
            this._storageRestoreDevicesVO.dispose();
            this._storageRestoreDevicesVO = null;
         }
         super.onDispose();
      }
      
      public function onBackClickS() : void
      {
         App.utils.asserter.assertNotNull(this.onBackClick,"onBackClick" + Errors.CANT_NULL);
         this.onBackClick();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:StorageRestoreDevicesVO = this._storageRestoreDevicesVO;
         this._storageRestoreDevicesVO = new StorageRestoreDevicesVO(param1);
         this.setData(this._storageRestoreDevicesVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:StorageRestoreDevicesVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
