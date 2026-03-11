package net.wg.story_mode.battle.views.consumablesPanel
{
   import net.wg.gui.battle.views.consumablesPanel.BattleShellButton;
   import net.wg.gui.battle.views.consumablesPanel.ConsumablesPanel;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleShellButton;
   
   public class StoryModeConsumablesPanel extends ConsumablesPanel
   {
      
      private static const STORY_MODE_SHELL_BUTTON:String = "StoryModeShellButtonUI";
       
      
      public function StoryModeConsumablesPanel()
      {
         super();
      }
      
      override protected function createShellButton() : IBattleShellButton
      {
         return App.utils.classFactory.getComponent(STORY_MODE_SHELL_BUTTON,BattleShellButton);
      }
   }
}
