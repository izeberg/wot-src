package net.wg.historical_battles.gui.battle.views.gameMessagesPanel.components
{
   import flash.display.Sprite;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.utils.StageBreakPoint;
   import net.wg.utils.StageBreakPointList;
   
   public class HBVictoryFlare extends BattleUIComponent
   {
      
      private static const FLARE_Y:int = 0;
      
      private static const FLARE_Y_SMALL:int = -38;
      
      private static const FLARE_Y_SMALL_EXTRA_LARGE:int = 40;
      
      private static const FLARE_SCALE:int = 1;
      
      private static const FLARE_SCALE_EXTRA_LARGE:int = 1.8;
       
      
      public var flare:Sprite;
      
      public function HBVictoryFlare()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.flare = null;
         super.onDispose();
      }
      
      public function updateLayout(param1:StageBreakPoint) : void
      {
         this.flare.y = this.getFlareY(param1);
         this.flare.scaleX = this.flare.scaleY = this.getFlareScale(param1);
      }
      
      private function getFlareY(param1:StageBreakPoint) : uint
      {
         if(param1.width < StageBreakPointList.SMALL.width)
         {
            return FLARE_Y_SMALL;
         }
         if(param1 == StageBreakPointList.EXTRA_LARGE)
         {
            return FLARE_Y_SMALL_EXTRA_LARGE;
         }
         return FLARE_Y;
      }
      
      private function getFlareScale(param1:StageBreakPoint) : uint
      {
         if(param1 == StageBreakPointList.EXTRA_LARGE)
         {
            return FLARE_SCALE_EXTRA_LARGE;
         }
         return FLARE_SCALE;
      }
   }
}
