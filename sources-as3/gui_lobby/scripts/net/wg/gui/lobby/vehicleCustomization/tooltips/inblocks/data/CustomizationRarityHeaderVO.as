package net.wg.gui.lobby.vehicleCustomization.tooltips.inblocks.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class CustomizationRarityHeaderVO extends DAAPIDataClass
   {
       
      
      public var rarity:String = "";
      
      public var width:Number = -1;
      
      public var height:Number = -1;
      
      public var imagePath:String = "";
      
      public var align:String = "center";
      
      public var rarityIcon:String = "";
      
      public var rarityBackground:String = "";
      
      public var title:String = "";
      
      public var subTitle:String = "";
      
      public var videoSource:String = "";
      
      public var imgOffset:int = -1;
      
      public function CustomizationRarityHeaderVO(param1:Object)
      {
         super(param1);
      }
   }
}
