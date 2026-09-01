package net.wg.white_tiger.gui.battle.components
{
   import net.wg.data.constants.Values;
   
   public class WhiteTigerGeneratorProgressCircle extends WhiteTigerBaseProgressCircle
   {
      
      private static const FRAME_LABEL_ONLINE:String = "online";
      
      private static const FRAME_LABEL_CAPTURING:String = "capture";
      
      private static const FRAME_LABEL_OFFLINE:String = "offline";
      
      private static const FRAME_LABEL_LOCKED:String = "locked";
      
      private static const LAST_FRAME:int = 146;
      
      private static const COLOR_BLIND_SUFFIX:String = "_colorBlind";
       
      
      private var _isGeneratorLocked:Boolean = false;
      
      public function WhiteTigerGeneratorProgressCircle()
      {
         super();
         this.resetGenerator();
      }
      
      override public function updateProgress(param1:Number) : void
      {
         if(this._isGeneratorLocked)
         {
            return;
         }
         if(currentFrameLabel != FRAME_LABEL_CAPTURING)
         {
            gotoAndStop(FRAME_LABEL_CAPTURING);
         }
         var _loc2_:int = param1 / 100 * LAST_FRAME | 0;
         progressCircle.gotoAndStop(_loc2_);
      }
      
      override protected function getCorrectState(param1:String) : String
      {
         return FRAME_LABEL_CAPTURING;
      }
      
      public function resetGenerator() : void
      {
         if(this._isGeneratorLocked)
         {
            return;
         }
         gotoAndStop(FRAME_LABEL_ONLINE);
      }
      
      public function setGeneratorOffline() : void
      {
         gotoAndStop(FRAME_LABEL_OFFLINE + this.getColorSuffix(colorblindMode));
      }
      
      public function setGeneratorLocked(param1:Boolean) : void
      {
         this._isGeneratorLocked = param1;
         if(this._isGeneratorLocked)
         {
            gotoAndStop(FRAME_LABEL_LOCKED + this.getColorSuffix(colorblindMode));
         }
         else
         {
            gotoAndStop(FRAME_LABEL_ONLINE);
         }
      }
      
      public function setColorBlindMode(param1:Boolean) : void
      {
         colorblindMode = param1;
         this.updateColorSettings();
      }
      
      private function updateColorSettings() : void
      {
         if(currentLabel == FRAME_LABEL_ONLINE || currentLabel == FRAME_LABEL_CAPTURING)
         {
            return;
         }
         var _loc1_:String = !!colorblindMode ? currentLabel + this.getColorSuffix(colorblindMode) : currentLabel.replace(COLOR_BLIND_SUFFIX,Values.EMPTY_STR);
         gotoAndStop(_loc1_);
      }
      
      private function getColorSuffix(param1:Boolean) : String
      {
         return !!param1 ? (currentLabel.indexOf(COLOR_BLIND_SUFFIX) == -1 ? COLOR_BLIND_SUFFIX : Values.EMPTY_STR) : Values.EMPTY_STR;
      }
   }
}
