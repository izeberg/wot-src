package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.BattleCarouselEnvironment;
   
   public class BattleTankCarouselMeta extends BattleCarouselEnvironment
   {
       
      
      public var setFilter:Function;
      
      public var resetPlaylistAndFilters:Function;
      
      public function BattleTankCarouselMeta()
      {
         super();
      }
      
      public function setFilterS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.setFilter,"setFilter" + Errors.CANT_NULL);
         this.setFilter(param1);
      }
      
      public function resetPlaylistAndFiltersS() : void
      {
         App.utils.asserter.assertNotNull(this.resetPlaylistAndFilters,"resetPlaylistAndFilters" + Errors.CANT_NULL);
         this.resetPlaylistAndFilters();
      }
   }
}
