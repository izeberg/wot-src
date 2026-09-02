package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel
{
   import net.wg.gui.battle.views.consumablesPanel.BattleEquipmentButtonGlow;
   
   public class BattleEquipmentButtonGlow extends net.wg.gui.battle.views.consumablesPanel.BattleEquipmentButtonGlow
   {
      
      private static const SHOW_GLOW_BLUE_STATE:String = "blue";
      
      private static const SHOW_GLOW_HIDE_STATE:String = "hide";
      
      private static const SHOW_GLOW_IDLE_STATE:String = "idle";
      
      private static const EVENT_NORMAL_TEXT_COLOR:uint = 16777215;
       
      
      public function BattleEquipmentButtonGlow()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         bindKeyField.textColor = this.normalTextColor;
      }
      
      override public function hideGlow(param1:Boolean = true) : void
      {
         if(currentLabel == SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_HIDE_STATE);
         }
         else
         {
            gotoAndStop(SHOW_GLOW_IDLE_STATE);
         }
      }
      
      public function glowBlue() : void
      {
         if(currentLabel != SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_BLUE_STATE);
         }
      }
      
      override protected function get normalTextColor() : uint
      {
         return EVENT_NORMAL_TEXT_COLOR;
      }
   }
}
