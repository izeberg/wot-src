package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.constants.WT_ABILITY_STATES;
   
   public class PassiveAbilityActive extends MovieClip
   {
      
      private static const IDLE_STATE:String = "idle";
      
      private static const NOT_ACTIVE_STATE:String = "notActive";
      
      private static const ACTIVE_STATE:String = "active";
       
      
      private var _wtState:String = null;
      
      public function PassiveAbilityActive()
      {
         super();
      }
      
      public function updateWtState(param1:String) : void
      {
         if(this._wtState == param1)
         {
            return;
         }
         this._wtState = param1;
         if(this._wtState == WT_ABILITY_STATES.ACTIVE)
         {
            gotoAndPlay(ACTIVE_STATE);
         }
         else if(this._wtState == WT_ABILITY_STATES.DEFAULT)
         {
            gotoAndPlay(NOT_ACTIVE_STATE);
         }
         else
         {
            gotoAndStop(IDLE_STATE);
         }
      }
   }
}
