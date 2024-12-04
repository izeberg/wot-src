package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class EarnListRendererVO extends DAAPIDataClass
   {
       
      
      public var text:String = "";
      
      public var linkText:String = "";
      
      public var eventType:String = "";
      
      public var enable:Boolean = true;
      
      public function EarnListRendererVO(param1:Object)
      {
         super(param1);
      }
   }
}
