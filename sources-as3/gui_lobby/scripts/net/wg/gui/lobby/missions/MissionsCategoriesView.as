package net.wg.gui.lobby.missions
{
   import net.wg.gui.lobby.missions.event.MissionViewEvent;
   
   public class MissionsCategoriesView extends MissionsGroupedView
   {
       
      
      public function MissionsCategoriesView()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MissionViewEvent.GOTO_NY_QUESTS,this.onGotoNyQuestsHandler);
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(MissionViewEvent.GOTO_NY_QUESTS,this.onGotoNyQuestsHandler);
      }
      
      private function onGotoNyQuestsHandler(param1:MissionViewEvent) : void
      {
         onNyQuestsClick();
      }
   }
}
