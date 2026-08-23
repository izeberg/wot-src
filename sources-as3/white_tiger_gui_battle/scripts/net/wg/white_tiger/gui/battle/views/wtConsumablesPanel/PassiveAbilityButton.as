package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel
{
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components.PassiveAbilityActive;
   
   public class PassiveAbilityButton extends BaseConsumablesButton
   {
       
      
      public var active:PassiveAbilityActive = null;
      
      public function PassiveAbilityButton()
      {
         super();
         useHandCursor = buttonMode = false;
      }
      
      override protected function updateWtState() : void
      {
         this.active.updateWtState(wtState);
      }
      
      override protected function onDispose() : void
      {
         this.active = null;
         super.onDispose();
      }
   }
}
