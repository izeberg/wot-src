package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class PrebattleCarouselViewMeta extends GFInjectComponent
   {
       
      
      public var setFilter:Function;
      
      public var onViewIsHidden:Function;
      
      public function PrebattleCarouselViewMeta()
      {
         super();
      }
      
      public function setFilterS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.setFilter,"setFilter" + Errors.CANT_NULL);
         this.setFilter(param1);
      }
      
      public function onViewIsHiddenS() : void
      {
         App.utils.asserter.assertNotNull(this.onViewIsHidden,"onViewIsHidden" + Errors.CANT_NULL);
         this.onViewIsHidden();
      }
   }
}
