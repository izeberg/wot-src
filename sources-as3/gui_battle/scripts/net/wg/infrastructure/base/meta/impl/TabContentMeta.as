package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class TabContentMeta extends GFInjectComponent
   {
       
      
      public var onTabChanged:Function;
      
      public function TabContentMeta()
      {
         super();
      }
      
      public function onTabChangedS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onTabChanged,"onTabChanged" + Errors.CANT_NULL);
         this.onTabChanged(param1);
      }
   }
}
