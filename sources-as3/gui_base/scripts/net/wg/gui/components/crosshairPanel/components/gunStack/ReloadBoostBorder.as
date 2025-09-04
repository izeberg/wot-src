package net.wg.gui.components.crosshairPanel.components.gunStack
{
   import flash.display.MovieClip;
   
   public class ReloadBoostBorder extends MovieClip
   {
      
      private static const STATE_SHOWN:String = "shown";
      
      private static const STATE_SHOW:String = "show";
      
      private static const STATE_HIDE:String = "hide";
      
      private static const STATE_EMPTY:String = "empty";
      
      private static const STATE_BLINK:String = "blink";
       
      
      public function ReloadBoostBorder()
      {
         super();
      }
      
      public function updateState(param1:Boolean, param2:Boolean = false) : void
      {
         if(param1)
         {
            if(param2)
            {
               gotoAndStop(STATE_SHOWN);
            }
            else
            {
               gotoAndPlay(STATE_SHOW);
            }
         }
         else if(param2)
         {
            gotoAndPlay(STATE_EMPTY);
         }
         else
         {
            gotoAndPlay(STATE_HIDE);
         }
      }
      
      public function blink() : void
      {
         gotoAndPlay(STATE_BLINK);
      }
   }
}
