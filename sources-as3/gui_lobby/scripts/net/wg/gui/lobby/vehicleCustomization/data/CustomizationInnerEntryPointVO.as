package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class CustomizationInnerEntryPointVO extends DAAPIDataClass
   {
       
      
      public var itemId:String = "";
      
      public var isSelected:Boolean = false;
      
      public var label:String = "";
      
      public var isVisible:Boolean = false;
      
      public var isSmall:Boolean = false;
      
      public var hasNovelty:Boolean = false;
      
      public function CustomizationInnerEntryPointVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
