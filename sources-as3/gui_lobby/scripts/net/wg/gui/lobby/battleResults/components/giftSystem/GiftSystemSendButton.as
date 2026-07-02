package net.wg.gui.lobby.battleResults.components.giftSystem
{
   import net.wg.gui.components.controls.SoundButton;
   
   public class GiftSystemSendButton extends SoundButton
   {
      
      private static const LOADING_STATE_LABEL:String = "loading";
       
      
      public function GiftSystemSendButton()
      {
         super();
         _stateMap[LOADING_STATE_LABEL] = [LOADING_STATE_LABEL];
      }
      
      public function get loading() : Boolean
      {
         return _state == LOADING_STATE_LABEL;
      }
      
      public function set loading(param1:Boolean) : void
      {
         enabled = !param1;
         if(param1)
         {
            super.setState(LOADING_STATE_LABEL);
         }
      }
   }
}
