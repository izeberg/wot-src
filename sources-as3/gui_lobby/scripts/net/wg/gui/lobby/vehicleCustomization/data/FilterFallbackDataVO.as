package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FilterFallbackDataVO extends DAAPIDataClass
   {
       
      
      public var message:String = "";
      
      public var hasVideo:Boolean = false;
      
      public var actionButtonVisible:Boolean = false;
      
      public var nySpecial:Boolean = false;
      
      public var grinchEnable:Boolean = false;
      
      public function FilterFallbackDataVO(param1:Object)
      {
         super(param1);
      }
   }
}
