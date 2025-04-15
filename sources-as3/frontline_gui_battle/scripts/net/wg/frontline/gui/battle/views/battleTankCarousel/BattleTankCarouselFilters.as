package net.wg.frontline.gui.battle.views.battleTankCarousel
{
   import net.wg.frontline.data.constants.generated.FRONTLINE_BATTLE_VIEW_ALIASES;
   import net.wg.gui.components.carousels.filters.TankCarouselFilters;
   
   public class BattleTankCarouselFilters extends TankCarouselFilters
   {
       
      
      public function BattleTankCarouselFilters()
      {
         super();
      }
      
      override protected function showPopup() : void
      {
         popoverMgr.show(this,FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_CAROUSEL_FILTER_POPOVER);
      }
   }
}
