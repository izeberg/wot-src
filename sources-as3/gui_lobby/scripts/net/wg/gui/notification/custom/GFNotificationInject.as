package net.wg.gui.notification.custom
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class GFNotificationInject extends GFInjectComponent
   {
       
      
      public function GFNotificationInject()
      {
         super();
         setManageSize(true);
      }
      
      public function setViewSize(param1:Number, param2:Number) : void
      {
         setSize(param1,param2);
      }
   }
}
