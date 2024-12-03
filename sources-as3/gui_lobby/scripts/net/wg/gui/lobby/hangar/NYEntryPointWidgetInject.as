package net.wg.gui.lobby.hangar
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   
   public class NYEntryPointWidgetInject extends GFInjectComponent
   {
      
      private static const WIDTH:int = 300;
      
      private static const HEIGHT:int = 210;
      
      private static const ENTRY_POINT_HIT_AREA_OFFSET_X:int = -40;
      
      private static const ENTRY_POINT_HIT_AREA_OFFSET_Y:int = 210;
       
      
      public function NYEntryPointWidgetInject()
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
      
      public function get offsetX() : int
      {
         return ENTRY_POINT_HIT_AREA_OFFSET_X;
      }
      
      public function get offsetY() : int
      {
         return ENTRY_POINT_HIT_AREA_OFFSET_Y;
      }
   }
}
