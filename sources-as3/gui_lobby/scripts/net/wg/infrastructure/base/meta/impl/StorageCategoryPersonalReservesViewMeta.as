package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.components.data.ButtonFiltersVO;
   import net.wg.gui.lobby.storage.categories.BaseCategoryView;
   import net.wg.gui.lobby.storage.categories.personalreserves.StorageCategoryPersonalReservesVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class StorageCategoryPersonalReservesViewMeta extends BaseCategoryView
   {
       
      
      public var navigateToStore:Function;
      
      public var activateReserve:Function;
      
      public var resetFilter:Function;
      
      public var onFiltersChange:Function;
      
      public var onInfoClicked:Function;
      
      private var _storageCategoryPersonalReservesVO:StorageCategoryPersonalReservesVO;
      
      private var _buttonFiltersVO:ButtonFiltersVO;
      
      public function StorageCategoryPersonalReservesViewMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._storageCategoryPersonalReservesVO)
         {
            this._storageCategoryPersonalReservesVO.dispose();
            this._storageCategoryPersonalReservesVO = null;
         }
         if(this._buttonFiltersVO)
         {
            this._buttonFiltersVO.dispose();
            this._buttonFiltersVO = null;
         }
         super.onDispose();
      }
      
      public function navigateToStoreS() : void
      {
         App.utils.asserter.assertNotNull(this.navigateToStore,"navigateToStore" + Errors.CANT_NULL);
         this.navigateToStore();
      }
      
      public function activateReserveS(param1:Number) : void
      {
         App.utils.asserter.assertNotNull(this.activateReserve,"activateReserve" + Errors.CANT_NULL);
         this.activateReserve(param1);
      }
      
      public function resetFilterS() : void
      {
         App.utils.asserter.assertNotNull(this.resetFilter,"resetFilter" + Errors.CANT_NULL);
         this.resetFilter();
      }
      
      public function onFiltersChangeS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.onFiltersChange,"onFiltersChange" + Errors.CANT_NULL);
         this.onFiltersChange(param1);
      }
      
      public function onInfoClickedS() : void
      {
         App.utils.asserter.assertNotNull(this.onInfoClicked,"onInfoClicked" + Errors.CANT_NULL);
         this.onInfoClicked();
      }
      
      public final function as_init(param1:Object) : void
      {
         var _loc2_:StorageCategoryPersonalReservesVO = this._storageCategoryPersonalReservesVO;
         this._storageCategoryPersonalReservesVO = new StorageCategoryPersonalReservesVO(param1);
         this.init(this._storageCategoryPersonalReservesVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_initFilter(param1:Object) : void
      {
         var _loc2_:ButtonFiltersVO = this._buttonFiltersVO;
         this._buttonFiltersVO = new ButtonFiltersVO(param1);
         this.initFilter(this._buttonFiltersVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function init(param1:StorageCategoryPersonalReservesVO) : void
      {
         var _loc2_:String = "as_init" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function initFilter(param1:ButtonFiltersVO) : void
      {
         var _loc2_:String = "as_initFilter" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
