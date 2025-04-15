package net.wg.gui.notification.caches
{
   import flash.utils.Dictionary;
   import net.wg.gui.notification.interfaces.IGFNotificationCache;
   
   public final class GFNotificationCache implements IGFNotificationCache
   {
      
      private static var instance:GFNotificationCache = null;
       
      
      private var _sizeCache:Dictionary;
      
      public function GFNotificationCache()
      {
         this._sizeCache = new Dictionary();
         super();
         instance = this;
      }
      
      public static function getInstance() : IGFNotificationCache
      {
         if(instance == null)
         {
            instance = new GFNotificationCache();
         }
         return instance;
      }
      
      public function addCachedSize(param1:String, param2:Number) : void
      {
         this._sizeCache[param1] = param2;
      }
      
      public function getCachedSize(param1:String) : Number
      {
         return this._sizeCache[param1];
      }
   }
}
