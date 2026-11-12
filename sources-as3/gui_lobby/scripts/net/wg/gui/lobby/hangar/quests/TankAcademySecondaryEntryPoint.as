package net.wg.gui.lobby.hangar.quests
{
   public class TankAcademySecondaryEntryPoint extends HeaderSecondaryWidgetInject
   {
      
      private static const WIDTH:int = 80;
      
      private static const HEIGHT:int = 110;
      
      private static const MARGIN:int = 2;
       
      
      public function TankAcademySecondaryEntryPoint()
      {
         super();
         setManageSize(true);
         setSize(WIDTH + 2 * MARGIN,HEIGHT + 2 * MARGIN);
      }
   }
}
