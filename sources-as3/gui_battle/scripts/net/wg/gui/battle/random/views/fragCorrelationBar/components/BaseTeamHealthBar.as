package net.wg.gui.battle.random.views.fragCorrelationBar.components
{
   import flash.text.TextField;
   import net.wg.data.constants.FragCorrelationBarStatus;
   import net.wg.gui.battle.components.BattleUIComponent;
   import scaleform.gfx.TextFieldEx;
   
   public class BaseTeamHealthBar extends BattleUIComponent
   {
      
      private static const HP_BAR_Y:int = 8;
      
      private static const HP_BAR_OFFSET_NO_TF_FROM_CENTER:int = 66;
      
      private static const HP_BAR_OFFSET_FROM_CENTER:int = 109;
      
      private static const MIN_RESOLUTION:int = 1128;
      
      private static const REGULAR_BAR_SIZE:int = 234;
      
      private static const MIN_RESOLUTION_BAR_SIZE:int = 174;
       
      
      public var healthTF:TextField = null;
      
      protected var hpBar:ScoreHealthBarElement = null;
      
      private var _showHPValues:Boolean = false;
      
      private var _showHPBar:Boolean = false;
      
      private var _healthValue:String = "";
      
      private var _currentPercentage:Number = 0;
      
      private var _isEnemyBar:Boolean = true;
      
      private var _barWidth:int = -1;
      
      public function BaseTeamHealthBar()
      {
         super();
         this.configureHPBar();
         TextFieldEx.setNoTranslate(this.healthTF,false);
      }
      
      override protected function onDispose() : void
      {
         this.healthTF = null;
         this.hpBar.dispose();
         this.hpBar = null;
         super.onDispose();
      }
      
      public function init(param1:Boolean, param2:Boolean) : void
      {
         this._isEnemyBar = param1;
         this.hpBar.setColor(param1,param2);
         if(!param1)
         {
            this.hpBar.scaleX = -1;
         }
         this.updatePositions();
      }
      
      public function setHealthValue(param1:String, param2:Number) : void
      {
         this._healthValue = param1;
         this._currentPercentage = param2;
         if(this._showHPBar)
         {
            this.hpBar.setProgress(param2);
         }
         if(this._showHPValues)
         {
            this.healthTF.text = param1;
         }
      }
      
      public function setViewSettings(param1:int) : void
      {
         this._showHPValues = FragCorrelationBarStatus.isShowTeamHPValues(param1);
         this._showHPBar = FragCorrelationBarStatus.isShowTeamHPBar(param1);
         this.hpBar.visible = this._showHPBar;
         this.healthTF.visible = this._showHPValues;
         this.setHealthValue(this._healthValue,this._currentPercentage);
         this.updatePositions();
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         if(param1 < MIN_RESOLUTION)
         {
            this._barWidth = MIN_RESOLUTION_BAR_SIZE;
         }
         else
         {
            this._barWidth = REGULAR_BAR_SIZE;
         }
         this.hpBar.updateWidth(this._barWidth);
         this.updatePositions();
      }
      
      protected function updatePositions() : void
      {
         if(this._showHPValues)
         {
            this.hpBar.x = !!this._isEnemyBar ? Number(HP_BAR_OFFSET_FROM_CENTER) : Number(-HP_BAR_OFFSET_FROM_CENTER);
         }
         else
         {
            this.hpBar.x = !!this._isEnemyBar ? Number(HP_BAR_OFFSET_NO_TF_FROM_CENTER) : Number(-HP_BAR_OFFSET_NO_TF_FROM_CENTER);
         }
      }
      
      private function configureHPBar() : void
      {
         this.hpBar = new ScoreHealthBarElement();
         addChildAt(this.hpBar,getChildIndex(this.healthTF));
         this.hpBar.y = HP_BAR_Y;
      }
   }
}
