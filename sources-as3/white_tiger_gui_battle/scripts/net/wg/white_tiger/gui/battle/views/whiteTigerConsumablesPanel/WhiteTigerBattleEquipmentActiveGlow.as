package net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel
{
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.containers.AnimatedTextContainer;
   
   public class WhiteTigerBattleEquipmentActiveGlow extends BattleUIComponent
   {
      
      private static const SHOW_GLOW_BLUE_STATE:String = "blue";
      
      private static const SHOW_GLOW_HIDE_STATE:String = "hide";
      
      private static const SHOW_GLOW_IDLE_STATE:String = "idle";
       
      
      public var tfContainer:AnimatedTextContainer = null;
      
      public function WhiteTigerBattleEquipmentActiveGlow()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.tfContainer.text = CONTROLS.KEYBOARD_KEY_ESCAPE;
         mouseEnabled = false;
         mouseChildren = false;
      }
      
      public function glowBlue() : void
      {
         if(currentLabel != SHOW_GLOW_BLUE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_BLUE_STATE);
         }
      }
      
      public function hideGlow() : void
      {
         if(currentFrameLabel != SHOW_GLOW_IDLE_STATE)
         {
            gotoAndPlay(SHOW_GLOW_HIDE_STATE);
         }
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.tfContainer.dispose();
         this.tfContainer = null;
         super.onDispose();
      }
   }
}
