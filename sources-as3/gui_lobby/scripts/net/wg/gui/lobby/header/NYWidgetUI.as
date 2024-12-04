package net.wg.gui.lobby.header
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class NYWidgetUI extends GFInjectComponent
   {
      
      private static const WIDTH:int = 560;
      
      private static const HEIGHT:int = 256;
       
      
      public function NYWidgetUI()
      {
         super();
         setManageSize(true);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         width = WIDTH;
         height = HEIGHT;
      }
   }
}
