package net.wg.gui.lobby.battleRoyale
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class ProxyCurrencyPanel extends GFInjectComponent
   {
      
      private static const PANEL_WIDTH:int = 349;
      
      private static const PANEL_HEIGHT:int = 92;
       
      
      public function ProxyCurrencyPanel()
      {
         super();
         width = PANEL_WIDTH;
         height = PANEL_HEIGHT;
      }
   }
}
