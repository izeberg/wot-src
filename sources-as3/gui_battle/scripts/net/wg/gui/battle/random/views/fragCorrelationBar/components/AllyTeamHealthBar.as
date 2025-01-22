package net.wg.gui.battle.random.views.fragCorrelationBar.components
{
   import flash.text.TextField;
   import net.wg.data.constants.FragCorrelationBarStatus;
   import scaleform.gfx.TextFieldEx;
   
   public class AllyTeamHealthBar extends BaseTeamHealthBar
   {
      
      private static const HP_BAR_LEFT_PADDING:int = -9;
       
      
      public var diffHpTF:TextField = null;
      
      private var _diffIsVisible:Boolean = false;
      
      private var _diff:String = "";
      
      public function AllyTeamHealthBar()
      {
         super();
         TextFieldEx.setNoTranslate(this.diffHpTF,false);
      }
      
      override public function setViewSettings(param1:int) : void
      {
         super.setViewSettings(param1);
         this._diffIsVisible = FragCorrelationBarStatus.isShowHPDifferenceValues(param1);
         this.diffHpTF.visible = this._diffIsVisible;
         this.setDiffValues(this._diff);
      }
      
      override protected function updatePositions() : void
      {
         super.updatePositions();
         this.diffHpTF.x = hpBar.x - hpBar.width - this.diffHpTF.width + HP_BAR_LEFT_PADDING;
      }
      
      override protected function onDispose() : void
      {
         this.diffHpTF = null;
         super.onDispose();
      }
      
      public function setDiffValues(param1:String) : void
      {
         this._diff = param1;
         if(this._diffIsVisible)
         {
            this.diffHpTF.text = param1;
         }
      }
   }
}
