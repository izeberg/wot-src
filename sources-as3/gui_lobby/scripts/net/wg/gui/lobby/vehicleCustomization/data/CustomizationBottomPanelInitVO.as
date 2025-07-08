package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.data.VO.TankCarouselFilterInitVO;
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class CustomizationBottomPanelInitVO extends DAAPIDataClass
   {
      
      private static const FILTERS_VO:String = "filtersVO";
       
      
      public var filtersVO:TankCarouselFilterInitVO = null;
      
      public function CustomizationBottomPanelInitVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == FILTERS_VO)
         {
            this.filtersVO = new TankCarouselFilterInitVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.filtersVO)
         {
            this.filtersVO.dispose();
            this.filtersVO = null;
         }
         super.onDispose();
      }
   }
}
