package net.wg.gui.battle.views.tabContent
{
   import net.wg.infrastructure.base.meta.IPersonalReservesTabMeta;
   import net.wg.infrastructure.base.meta.impl.TabContentMeta;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class TabContent extends TabContentMeta implements IPersonalReservesTabMeta, IDisplayableComponent
   {
       
      
      public function TabContent()
      {
         super();
         setManageSize(true);
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
      }
   }
}
