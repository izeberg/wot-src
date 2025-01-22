package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.AbstractScreen;
   
   public class PersonalMissionOperationsMeta extends AbstractScreen
   {
       
      
      public var closeView:Function;
      
      public var onTabSelected:Function;
      
      public function PersonalMissionOperationsMeta()
      {
         super();
      }
      
      public function closeViewS() : void
      {
         App.utils.asserter.assertNotNull(this.closeView,"closeView" + Errors.CANT_NULL);
         this.closeView();
      }
      
      public function onTabSelectedS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.onTabSelected,"onTabSelected" + Errors.CANT_NULL);
         this.onTabSelected(param1);
      }
   }
}
