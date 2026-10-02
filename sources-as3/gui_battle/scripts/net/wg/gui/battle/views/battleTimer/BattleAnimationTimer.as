package net.wg.gui.battle.views.battleTimer
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.base.meta.IBattleTimerMeta;
   import net.wg.infrastructure.base.meta.impl.BattleTimerMeta;
   import scaleform.gfx.TextFieldEx;
   
   public class BattleAnimationTimer extends BattleTimerMeta implements IBattleTimerMeta
   {
       
      
      public var minutesTF:TextField = null;
      
      public var secondsTF:TextField = null;
      
      public var background:MovieClip = null;
      
      public var delimiter:BattleAtlasSprite = null;
      
      public var shadow:BattleAtlasSprite = null;
      
      private var _isCritical:Boolean = false;
      
      private var _minutes:String = null;
      
      private var _seconds:String = null;
      
      public function BattleAnimationTimer()
      {
         super();
         this.delimiter.imageName = BATTLEATLAS.TIMER_DELIMITER;
         this.createBG();
         TextFieldEx.setNoTranslate(this.minutesTF,true);
         TextFieldEx.setNoTranslate(this.secondsTF,true);
      }
      
      protected function createBG() : void
      {
         this.shadow.imageName = BATTLEATLAS.TIMER_ANIM_BG;
      }
      
      public function as_setTotalTime(param1:String, param2:String) : void
      {
         if(this._minutes != param1)
         {
            this._minutes = param1;
            this.minutesTF.text = param1;
         }
         if(this._seconds != param2)
         {
            this._seconds = param2;
            this.secondsTF.text = param2;
         }
      }
      
      public function as_setColor(param1:Boolean) : void
      {
         if(this._isCritical != param1)
         {
            this.shadow.visible = !param1;
            if(param1)
            {
               this.background.play();
            }
            else
            {
               this.background.gotoAndStop(1);
            }
            this._isCritical = param1;
         }
      }
      
      public function as_showBattleTimer(param1:Boolean) : void
      {
         if(visible != param1)
         {
            visible = param1;
         }
      }
      
      override protected function onDispose() : void
      {
         this.delimiter = null;
         this.background = null;
         this.minutesTF = null;
         this.secondsTF = null;
         this.shadow = null;
         super.onDispose();
      }
   }
}
