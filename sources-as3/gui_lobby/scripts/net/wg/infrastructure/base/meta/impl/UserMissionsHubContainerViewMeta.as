package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.AbstractView;
   
   public class UserMissionsHubContainerViewMeta extends AbstractView
   {
       
      
      public var resetFilters:Function;
      
      public var onClose:Function;
      
      public function UserMissionsHubContainerViewMeta()
      {
         super();
      }
      
      public function resetFiltersS() : void
      {
         App.utils.asserter.assertNotNull(this.resetFilters,"resetFilters" + Errors.CANT_NULL);
         this.resetFilters();
      }
      
      public function onCloseS() : void
      {
         App.utils.asserter.assertNotNull(this.onClose,"onClose" + Errors.CANT_NULL);
         this.onClose();
      }
   }
}
