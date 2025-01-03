package net.wg.gui.battle.random.views.fragCorrelationBar.components
{
   import flash.display.Graphics;
   import flash.display.Sprite;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class ScoreHealthBarElement extends BattleUIComponent
   {
      
      private static const SETTINGS:Object = {};
      
      private static const BG_INDEX:int = 0;
      
      private static const PROGRESS_INDEX:int = 1;
      
      private static const INDICATOR_INDEX:int = 2;
      
      private static const RED:String = "red";
      
      private static const GREEN:String = "green";
      
      private static const PURPLE:String = "purple";
      
      {
         SETTINGS[RED] = [BATTLEATLAS.FB_RED_BG,BATTLEATLAS.FB_PROGRESS_RED,BATTLEATLAS.FB_INDICATOR_RED];
         SETTINGS[PURPLE] = [BATTLEATLAS.FB_PURPLE_BG,BATTLEATLAS.FB_PROGRESS_PURPLE,BATTLEATLAS.FB_INDICATOR_PURPLE];
         SETTINGS[GREEN] = [BATTLEATLAS.FB_GREEN_BG,BATTLEATLAS.FB_PROGRESS_GREEN,BATTLEATLAS.FB_INDICATOR_GREEN];
      }
      
      private var _currentState:String = "";
      
      private var _progress:Number = 0;
      
      private var _bitMapDataBar:Sprite = null;
      
      private var _bitMapDataBarBG:Sprite = null;
      
      private var _progressIndicator:Sprite = null;
      
      private var _barWidth:int = 0;
      
      private var _curSettings:Array;
      
      public function ScoreHealthBarElement()
      {
         super();
         this._bitMapDataBar = new Sprite();
         this._bitMapDataBarBG = new Sprite();
         this._progressIndicator = new Sprite();
         addChild(this._bitMapDataBarBG);
         addChild(this._bitMapDataBar);
         addChild(this._progressIndicator);
      }
      
      override protected function onDispose() : void
      {
         this._bitMapDataBar = null;
         this._bitMapDataBarBG = null;
         this._progressIndicator = null;
         super.onDispose();
      }
      
      public function setColor(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:String = GREEN;
         if(param1)
         {
            _loc3_ = !!param2 ? PURPLE : RED;
         }
         if(_loc3_ == this._currentState)
         {
            return;
         }
         this._currentState = _loc3_;
         this._curSettings = SETTINGS[_loc3_];
         App.atlasMgr.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,this._curSettings[INDICATOR_INDEX],this._progressIndicator.graphics);
         this.updateWidth(this._barWidth);
         this.updateProgress();
      }
      
      public function setProgress(param1:Number) : void
      {
         this._progress = param1;
         this.updateProgress();
      }
      
      public function updateWidth(param1:int) : void
      {
         this._barWidth = param1;
         if(this._curSettings)
         {
            this.drawImage(this._bitMapDataBarBG.graphics,this._curSettings[BG_INDEX],param1,10);
            this.updateProgress();
         }
      }
      
      private function updateProgress() : void
      {
         var _loc1_:int = 0;
         if(this._curSettings)
         {
            _loc1_ = int(this._barWidth * this._progress);
            this.drawImage(this._bitMapDataBar.graphics,this._curSettings[PROGRESS_INDEX],_loc1_,10);
            this._progressIndicator.x = _loc1_ - (this._progressIndicator.width >> 1);
            this._progressIndicator.y = -5;
         }
      }
      
      private function drawImage(param1:Graphics, param2:String, param3:int, param4:int) : void
      {
         App.atlasMgr.drawAtlasItemPart(ATLAS_CONSTANTS.BATTLE_ATLAS,param2,param1,param3,param4);
      }
   }
}
