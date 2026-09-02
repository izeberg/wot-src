package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.constants.WT_ABILITY_STATES;
   
   public class EquipmentButtonBackground extends MovieClip
   {
      
      private static const BACKGROUND_IDLE_STATE:String = "idle";
      
      private static const BACKGROUND_BLUE_STATE:String = "blue";
      
      private static const BACKGROUND_DISABLED_STATE:String = "disabled";
       
      
      private var _wtState:String = null;
      
      public function EquipmentButtonBackground()
      {
         super();
      }
      
      public function updateWtState(param1:String) : void
      {
         if(this._wtState != param1)
         {
            this._wtState = param1;
            if(this._wtState == WT_ABILITY_STATES.PREPARING)
            {
               gotoAndPlay(BACKGROUND_BLUE_STATE);
            }
            else if(this._wtState == WT_ABILITY_STATES.DISABLED)
            {
               gotoAndPlay(BACKGROUND_DISABLED_STATE);
            }
            else
            {
               gotoAndStop(BACKGROUND_IDLE_STATE);
            }
         }
      }
   }
}
