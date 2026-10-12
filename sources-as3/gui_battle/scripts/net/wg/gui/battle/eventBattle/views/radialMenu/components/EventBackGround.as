package net.wg.gui.battle.eventBattle.views.radialMenu.components
{
   import net.wg.gui.battle.views.radialMenu.components.BackGround;
   
   public class EventBackGround extends BackGround
   {
      
      private static const HOLE_HALF_SIZE:int = 225;
       
      
      public function EventBackGround()
      {
         super();
      }
      
      override protected function get holeHalfSize() : int
      {
         return HOLE_HALF_SIZE;
      }
   }
}
