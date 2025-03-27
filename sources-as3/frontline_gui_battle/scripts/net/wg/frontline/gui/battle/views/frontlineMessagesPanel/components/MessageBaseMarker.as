package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.components
{
   import flash.display.MovieClip;
   import net.wg.frontline.gui.battle.components.FrontlineProgressCircle;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class MessageBaseMarker extends BattleUIComponent
   {
       
      
      public var baseId:MovieClip = null;
      
      public var captureCircle:FrontlineProgressCircle = null;
      
      public function MessageBaseMarker()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.captureCircle.dispose();
         this.captureCircle = null;
         this.baseId = null;
         super.onDispose();
      }
   }
}
