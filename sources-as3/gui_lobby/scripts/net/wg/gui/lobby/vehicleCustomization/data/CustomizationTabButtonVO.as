package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.gui.components.advanced.collapsingBar.data.CollapsingBarButtonVO;
   
   public class CustomizationTabButtonVO extends CollapsingBarButtonVO
   {
       
      
      public var icon:String = "";
      
      public var counter:int = -1;
      
      public var counterID:String = "";
      
      public var groupId:int = -1;
      
      public function CustomizationTabButtonVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
