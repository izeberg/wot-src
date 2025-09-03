package net.wg.white_tiger.gui.battle.views.staticMarkers
{
   import net.wg.white_tiger.gui.battle.components.WhiteTigerGeneratorHoverIndicator;
   import net.wg.white_tiger.gui.battle.components.WhiteTigerGeneratorProgressCircle;
   
   public class WhiteTigerGeneratorContent extends WhiteTigerIndexedContent
   {
       
      
      public var progressCircle:WhiteTigerGeneratorProgressCircle = null;
      
      public var hoverIndicator:WhiteTigerGeneratorHoverIndicator = null;
      
      public function WhiteTigerGeneratorContent()
      {
         super();
         this.progressCircle.visible = false;
         this.hoverIndicator.visible = false;
      }
      
      public function setHoverVisibility(param1:Boolean) : void
      {
         this.hoverIndicator.visible = param1;
      }
      
      public function setIndex(param1:int) : void
      {
         var _loc2_:String = null;
         if(indexField != null)
         {
            _loc2_ = "";
            switch(param1)
            {
               case 1:
                  _loc2_ = "A";
                  break;
               case 2:
                  _loc2_ = "B";
                  break;
               case 3:
                  _loc2_ = "C";
            }
            indexField.text = _loc2_;
         }
      }
      
      public function updateGeneratorTimer(param1:Number) : void
      {
         if(icon.visible)
         {
            icon.visible = false;
            this.progressCircle.visible = true;
         }
         if(this.progressCircle.visible)
         {
            this.progressCircle.updateProgress(param1);
         }
      }
      
      public function resetGeneratorTimer() : void
      {
         icon.visible = true;
         this.progressCircle.visible = false;
      }
      
      public function lockGenerator(param1:Boolean) : void
      {
         icon.visible = false;
         this.progressCircle.visible = true;
         this.progressCircle.setGeneratorLocked(param1);
         this.hoverIndicator.setGeneratorLockedHover(param1);
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         this.progressCircle.setColorBlindMode(param1);
         this.hoverIndicator.setColorBlindMode(param1);
      }
      
      override protected function onDispose() : void
      {
         this.progressCircle.dispose();
         this.progressCircle = null;
         this.hoverIndicator = null;
         super.onDispose();
      }
   }
}
