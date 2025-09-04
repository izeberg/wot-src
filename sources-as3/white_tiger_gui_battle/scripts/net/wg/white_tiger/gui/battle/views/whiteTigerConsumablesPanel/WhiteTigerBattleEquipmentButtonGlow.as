package net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel
{
   import net.wg.gui.battle.views.consumablesPanel.BattleEquipmentButtonGlow;
   
   public class WhiteTigerBattleEquipmentButtonGlow extends BattleEquipmentButtonGlow
   {
      
      private static const SHOW_GLOW_BLUE_STATE:String = "blue";
      
      private static const SHOW_GLOW_HIDE_STATE:String = "hide";
      
      private static const SHOW_GLOW_IDLE_STATE:String = "idle";
      
      private static const SHOW_GLOW_TIMEOUT_STATE:String = "timeout";
      
      private static const SHOW_GLOW_HIDETEXT_STATE:String = "hideText";
      
      private static const SHOW_GLOW_HIDEBACK_STATE:String = "hideBack";
      
      private static const SHOW_GLOW_ORANGE_STATE:String = "orange";
      
      private static const WHITE_TIGER_NORMAL_TEXT_COLOR:uint = 16777215;
       
      
      public function WhiteTigerBattleEquipmentButtonGlow()
      {
         super();
      }
      
      public function glowBlue() : void
      {
         if(currentLabel != SHOW_GLOW_BLUE_STATE && currentLabel != SHOW_GLOW_TIMEOUT_STATE)
         {
            gotoAndPlay(SHOW_GLOW_BLUE_STATE);
            textField.textColor = this.normalTextColor;
         }
      }
      
      public function hideText() : void
      {
         if(currentLabel == SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_HIDETEXT_STATE);
            textField.textColor = this.normalTextColor;
         }
      }
      
      override public function hideGlow(param1:Boolean = true) : void
      {
         if(currentLabel == SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_HIDE_STATE);
            textField.textColor = this.normalTextColor;
         }
         else if(currentLabel == SHOW_GLOW_HIDETEXT_STATE)
         {
            gotoAndPlay(SHOW_GLOW_HIDEBACK_STATE);
            textField.textColor = this.normalTextColor;
         }
         else if(currentLabel == SHOW_GLOW_TIMEOUT_STATE || currentLabel == SHOW_GLOW_ORANGE_STATE)
         {
            gotoAndStop(SHOW_GLOW_IDLE_STATE);
            textField.textColor = this.normalTextColor;
         }
      }
      
      public function hideOnTimeout() : void
      {
         if(currentLabel == SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_TIMEOUT_STATE);
            textField.textColor = this.normalTextColor;
         }
      }
      
      override protected function get normalTextColor() : uint
      {
         return WHITE_TIGER_NORMAL_TEXT_COLOR;
      }
   }
}
