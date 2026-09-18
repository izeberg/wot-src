package net.wg.app.iml.base
{
   import flash.external.ExternalInterface;
   import net.wg.app.ICoreApplication;
   import net.wg.infrastructure.events.LibraryLoaderEvent;
   import net.wg.infrastructure.interfaces.IRootAppMainContent;
   import net.wg.infrastructure.managers.ILibrariesLoader;
   import net.wg.infrastructure.managers.ISharedLayoutManager;
   import net.wg.infrastructure.managers.impl.LibrariesLoader;
   import net.wg.infrastructure.managers.impl.SharedLayoutManager;
   
   public class RootApp extends BaseRootApp implements ICoreApplication
   {
       
      
      private var _loader:ILibrariesLoader = null;
      
      private var _registerCallback:String = null;
      
      private var _sharedLayoutMgr:ISharedLayoutManager;
      
      public function RootApp(param1:IRootAppMainContent, param2:Vector.<String>, param3:String = null)
      {
         this._sharedLayoutMgr = new SharedLayoutManager();
         super(param1);
         this.configAppInstance();
         if(param3 != null && param3.length > 0)
         {
            this._registerCallback = param3;
         }
         if(param2 != null && param2.length > 0)
         {
            this._loader = new LibrariesLoader();
            this._loader.addEventListener(LibraryLoaderEvent.LOADED_COMPLETED,this.onLoaderLoadedCompletedHandler);
            this._loader.load(param2);
         }
      }
      
      protected function configAppInstance() : void
      {
         CoreApp.instance = this;
      }
      
      override protected function onDispose() : void
      {
         if(this._loader != null)
         {
            this._loader.removeEventListener(LibraryLoaderEvent.LOADED_COMPLETED,this.onLoaderLoadedCompletedHandler);
            this._loader.dispose();
            this._loader = null;
         }
         if(this._sharedLayoutMgr != null)
         {
            this._sharedLayoutMgr.dispose();
            this._sharedLayoutMgr = null;
         }
         super.onDispose();
      }
      
      protected function onLibsLoadingComplete() : void
      {
      }
      
      protected function callRegisterCallback() : void
      {
         if(this._registerCallback != null)
         {
            ExternalInterface.call(this._registerCallback);
         }
      }
      
      public function get sharedLayoutMgr() : ISharedLayoutManager
      {
         return this._sharedLayoutMgr;
      }
      
      private function onLoaderLoadedCompletedHandler(param1:LibraryLoaderEvent) : void
      {
         this._loader.removeEventListener(LibraryLoaderEvent.LOADED_COMPLETED,this.onLoaderLoadedCompletedHandler);
         this.onLibsLoadingComplete();
      }
   }
}
