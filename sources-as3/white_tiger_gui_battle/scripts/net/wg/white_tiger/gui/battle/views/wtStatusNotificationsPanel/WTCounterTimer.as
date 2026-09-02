package net.wg.white_tiger.gui.battle.views.wtStatusNotificationsPanel
{
   import net.wg.gui.battle.battleRoyale.views.components.BattleRoyaleCounterTimer;
   import net.wg.gui.battle.views.destroyTimers.components.secondaryTimerFx.ISecondaryTimerFX;
   
   public class WTCounterTimer extends BattleRoyaleCounterTimer
   {
      
      private static const PADDING:uint = 20;
      
      private static const CROPPED_SIZE_PADDING:uint = 25;
      
      private static const CROPPED_SIZE_WIDTH:uint = 100;
       
      
      public function WTCounterTimer()
      {
         super();
      }
      
      override public function setTimerFx(param1:ISecondaryTimerFX) : void
      {
      }
      
      override public function get actualWidth() : Number
      {
         if(container.textFieldLabel.visible)
         {
            return super.width + PADDING;
         }
         return CROPPED_SIZE_WIDTH + CROPPED_SIZE_PADDING;
      }
   }
}
