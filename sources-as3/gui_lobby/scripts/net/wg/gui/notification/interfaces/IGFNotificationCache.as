package net.wg.gui.notification.interfaces
{
   public interface IGFNotificationCache
   {
       
      
      function addCachedSize(param1:String, param2:Number) : void;
      
      function getCachedSize(param1:String) : Number;
   }
}
