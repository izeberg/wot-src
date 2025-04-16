package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.battleTankCarousel.BattleCarouselEnvironment;
   
   public class BattleTankCarouselMeta extends BattleCarouselEnvironment
   {
       
      
      public var setFilter:Function;
      
      public function BattleTankCarouselMeta()
      {
         super();
      }
      
      public function setFilterS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.setFilter,"setFilter" + Errors.CANT_NULL);
         this.setFilter(param1);
      }
   }
}
