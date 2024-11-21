package net.wg.gui.lobby.header
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class NYWidgetUI extends GFInjectComponent
   {
      
      private static const WIDTH:int = 220;
      
      private static const HEIGHT:int = 220;
       
      
      public function NYWidgetUI()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
   }
}
