package net.wg.white_tiger.gui.battle.views.minimap.entries
{
   import flash.display.MovieClip;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerGeneratorProgressCircle;
   import net.wg.white_tiger.gui.battle.views.staticMarkers.WhiteTigerScaleAnimation;
   
   public class WhiteTigerGeneratorMinimapEntry extends WhiteTigerIndexedMinimapEntry
   {
      
      private static const HIGHLIGHT_SCALE:Number = 0.65;
       
      
      public var progressCircle:WhiteTigerGeneratorProgressCircle = null;
      
      public var highlightAnimation:MovieClip = null;
      
      public function WhiteTigerGeneratorMinimapEntry()
      {
         super();
         if(this.highlightAnimation is WhiteTigerScaleAnimation)
         {
            (this.highlightAnimation as WhiteTigerScaleAnimation).setScale(HIGHLIGHT_SCALE);
         }
      }
      
      public function setAlpha(param1:Number) : void
      {
         alpha = param1;
      }
      
      public function setEntityIndex(param1:int) : void
      {
         switch(param1)
         {
            case 1:
               textField.text = "A";
               break;
            case 2:
               textField.text = "B";
               break;
            case 3:
               textField.text = "C";
         }
      }
      
      public function setGeneratorProgress(param1:Number) : void
      {
         this.progressCircle.updateProgress(param1);
      }
      
      public function resetGeneratorMarker() : void
      {
         this.progressCircle.resetGenerator();
      }
      
      public function lockGeneratorMarker(param1:Boolean) : void
      {
         this.progressCircle.setGeneratorLocked(param1);
      }
      
      public function playAnimation() : void
      {
         if(this.highlightAnimation is WhiteTigerScaleAnimation)
         {
            (this.highlightAnimation as WhiteTigerScaleAnimation).playAnimation();
         }
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         this.progressCircle.setColorBlindMode(param1);
      }
   }
}
