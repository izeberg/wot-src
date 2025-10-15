package net.wg.portal.gui.battle.portalHudWidgetView
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class PortalHudWidgetView extends GFInjectComponent implements IDisplayableComponent
   {
       
      
      public function PortalHudWidgetView()
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
         visible = param1;
      }
   }
}
