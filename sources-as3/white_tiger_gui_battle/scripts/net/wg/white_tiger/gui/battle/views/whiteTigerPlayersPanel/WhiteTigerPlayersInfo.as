package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class WhiteTigerPlayersInfo extends BattleUIComponent
   {
       
      
      public var titleTF:TextField = null;
      
      public var pointsTF:TextField = null;
      
      public var pointsImage:MovieClip = null;
      
      public function WhiteTigerPlayersInfo()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
      }
      
      public function setCountPoints(param1:uint) : void
      {
         this.pointsTF.text = param1.toString();
         this.pointsImage.visible = this.pointsTF.visible = param1 > 0;
      }
      
      override protected function onDispose() : void
      {
         this.titleTF = null;
         this.pointsTF = null;
         this.pointsImage = null;
         super.onDispose();
      }
   }
}
