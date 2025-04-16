package net.wg.frontline.gui.battle.views.battleTankCarousel
{
   import net.wg.frontline.gui.battle.views.battleTankCarousel.data.BattleVehicleCarouselVO;
   import net.wg.gui.components.carousels.CarouselEnvironment;
   
   public class BattleCarouselEnvironment extends CarouselEnvironment
   {
       
      
      public function BattleCarouselEnvironment()
      {
         super();
      }
      
      override protected function getRendererVo() : Class
      {
         return BattleVehicleCarouselVO;
      }
   }
}
