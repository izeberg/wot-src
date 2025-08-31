package net.wg.white_tiger.gui.battle.components
{
   import flash.display.MovieClip;
   
   public class WhiteTigerGeneratorHoverIndicator extends MovieClip
   {
      
      private static const ONLINE_LABEL:String = "online";
      
      private static const LOCKED_LABEL:String = "locked";
      
      private static const COLOR_BLIND_SUFFIX:String = "_colorBlind";
       
      
      private var _isColorBlind:Boolean = false;
      
      public function WhiteTigerGeneratorHoverIndicator()
      {
         super();
      }
      
      public function setGeneratorLockedHover(param1:Boolean) : void
      {
         if(!param1)
         {
            gotoAndStop(ONLINE_LABEL);
            return;
         }
         gotoAndStop(!!this._isColorBlind ? LOCKED_LABEL + COLOR_BLIND_SUFFIX : LOCKED_LABEL);
      }
      
      public function setColorBlindMode(param1:Boolean) : void
      {
         this._isColorBlind = param1;
         if(currentLabel != ONLINE_LABEL)
         {
            gotoAndStop(!!param1 ? LOCKED_LABEL + COLOR_BLIND_SUFFIX : LOCKED_LABEL);
         }
      }
   }
}
