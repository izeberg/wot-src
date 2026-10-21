package net.wg.portal.gui.battle.views.battleTimer
{
   import flash.display.MovieClip;
   import flash.filters.DropShadowFilter;
   import flash.text.TextField;
   import net.wg.data.constants.Time;
   import net.wg.infrastructure.base.meta.IBattleTimerMeta;
   import net.wg.infrastructure.base.meta.impl.BattleTimerMeta;
   import scaleform.gfx.TextFieldEx;
   
   public class PortalBattleAnimationTimer extends BattleTimerMeta implements IBattleTimerMeta
   {
       
      
      public var minutesTF:TextField = null;
      
      public var delimiterTF:TextField = null;
      
      public var secondsTF:TextField = null;
      
      public var background:MovieClip = null;
      
      private var _isCritical:Boolean = false;
      
      private var _minutes:String = null;
      
      private var _seconds:String = null;
      
      private var _dropShadowFilter:DropShadowFilter;
      
      public function PortalBattleAnimationTimer()
      {
         this._dropShadowFilter = new DropShadowFilter(0,0,5770752,1,4,4);
         super();
         this.delimiterTF.text = Time.DELIMITER;
         TextFieldEx.setNoTranslate(this.minutesTF,true);
         TextFieldEx.setNoTranslate(this.secondsTF,true);
         this.as_setColor(true);
      }
      
      override protected function onDispose() : void
      {
         this.delimiterTF = null;
         this.background = null;
         this.minutesTF = null;
         this.secondsTF = null;
         this._dropShadowFilter = null;
         super.onDispose();
      }
      
      public function as_setColor(param1:Boolean) : void
      {
         if(this._isCritical != param1)
         {
            if(param1)
            {
               this.background.play();
               this.minutesTF.filters = [this._dropShadowFilter];
               this.delimiterTF.filters = [this._dropShadowFilter];
               this.secondsTF.filters = [this._dropShadowFilter];
            }
            else
            {
               this.background.gotoAndStop(1);
               this.minutesTF.filters = [];
               this.delimiterTF.filters = [];
               this.secondsTF.filters = [];
            }
            this._isCritical = param1;
         }
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
      
      public function as_showBattleTimer(param1:Boolean) : void
      {
         if(visible != param1)
         {
            visible = param1;
         }
      }
   }
}
