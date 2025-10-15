package net.wg.portal.gui.battle.portalPostmortemPanel
{
   import net.wg.gui.battle.views.destroyTimers.components.TimerContainer;
   
   public class PostmortemTimerContainer extends TimerContainer
   {
       
      
      public function PostmortemTimerContainer()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         progressBar.stop();
         super.onDispose();
      }
   }
}
