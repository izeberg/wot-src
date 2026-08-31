package net.wg.white_tiger.gui.battle.views.whiteTigerPlayersPanel.comps
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldType;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.BattleUIComponent;
   import scaleform.gfx.TextFieldEx;
   
   public class WhiteTigerBotListInfo extends BattleUIComponent
   {
      
      private static const FRAME_LABEL_ALLY:String = "ally";
      
      private static const FRAME_LABEL_ENEMY:String = "enemy";
       
      
      public var titleTF:TextField = null;
      
      public var infoIcon:WhiteTigerBotListInfoIcon = null;
      
      public var deadTimerTF:TextField = null;
      
      public var deadTimerBg:MovieClip = null;
      
      public function WhiteTigerBotListInfo()
      {
         super();
         TextFieldEx.setNoTranslate(this.titleTF,true);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.deadTimerTF.visible = false;
         this.deadTimerBg.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.titleTF = null;
         this.deadTimerTF = null;
         this.deadTimerBg = null;
         super.onDispose();
      }
      
      public function setData(param1:int) : void
      {
         this.deadTimerTF.mouseEnabled = this.titleTF.mouseEnabled = this.deadTimerTF.selectable = this.deadTimerTF.tabEnabled = this.titleTF.selectable = false;
         this.titleTF.type = TextFieldType.DYNAMIC;
         this.updateIconStatus();
         var _loc2_:String = "";
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
         this.titleTF.text = App.utils.locale.makeString(WHITE_TIGER_BATTLE.PLAYERSPANEL_CAMPLABEL,{"index":_loc2_});
      }
      
      public function updateTeam(param1:Boolean) : void
      {
         gotoAndStop(!!param1 ? FRAME_LABEL_ALLY : FRAME_LABEL_ENEMY);
      }
      
      public function updateIconStatus() : void
      {
         this.infoIcon.resetIconTimer();
      }
      
      public function updateGeneratorCaptureTimer(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         this.infoIcon.updateCaptureTimer(param1,param2,param3,param4);
      }
      
      public function setIsDestroyed() : void
      {
         this.infoIcon.setIsDestroyed();
      }
      
      public function resetGeneratorCaptureTimer() : void
      {
         this.infoIcon.resetIconTimer();
      }
      
      public function lockGenerator(param1:Boolean) : void
      {
         this.infoIcon.lockGenerator(param1);
      }
      
      public function setColorBlindMode(param1:Boolean) : void
      {
         this.infoIcon.setColorBlindMode(param1);
      }
      
      public function updateGeneratorDownTime(param1:String) : void
      {
         this.showDeadTimer(param1 != Values.EMPTY_STR);
         if(this.deadTimerTF.visible)
         {
            this.deadTimerTF.text = param1;
         }
      }
      
      public function showDeadTimer(param1:Boolean) : void
      {
         this.deadTimerTF.visible = param1;
         this.deadTimerBg.visible = param1;
      }
   }
}
