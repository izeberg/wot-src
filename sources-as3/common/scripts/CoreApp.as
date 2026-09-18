package
{
   import net.wg.app.ICoreApplication;
   import net.wg.infrastructure.managers.ISharedLayoutManager;
   
   public class CoreApp
   {
      
      private static var ms_instance:ICoreApplication;
       
      
      public function CoreApp()
      {
         super();
      }
      
      public static function get instance() : ICoreApplication
      {
         return ms_instance;
      }
      
      public static function set instance(param1:ICoreApplication) : void
      {
         if(ms_instance == null)
         {
            ms_instance = param1;
         }
         else
         {
            DebugUtils.LOG_ERROR("CoreApplication already set to App: " + param1);
         }
      }
      
      public static function get sharedLayoutMgr() : ISharedLayoutManager
      {
         return instance.sharedLayoutMgr;
      }
   }
}
