package net.wg.gui.lobby.epicBattles.components
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.SoundManagerStates;
   import net.wg.data.constants.SoundTypes;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.utils.StageSizeBoundaries;
   
   public class EpicBattlesWidgetBaseButton extends SimpleDisposable
   {
      
      public static const CLICK:String = "epicBattlesWidgetBaseButtonClick";
      
      protected static const OUT:String = "out";
      
      protected static const OVER:String = "over";
       
      
      public function EpicBattlesWidgetBaseButton()
      {
         super();
         this.init();
      }
      
      protected function init() : void
      {
         App.utils.asserter.assert(false,"EpicBattlesWidgetBaseButton:init" + Errors.ABSTRACT_INVOKE);
      }
      
      protected function dispatchClickEvent() : void
      {
         dispatchEvent(new Event(EpicBattlesWidgetBaseButton.CLICK));
      }
      
      protected function onRollOverHandler(param1:MouseEvent) : void
      {
         this.updateOverState(true);
         App.soundMgr.playControlsSnd(SoundManagerStates.SND_OVER,SoundTypes.NORMAL_BTN,null);
         App.toolTipMgr.showSpecial(TOOLTIPS_CONSTANTS.EPIC_BATTLE_WIDGET_INFO,null);
      }
      
      protected function onRollOutHandler(param1:MouseEvent) : void
      {
         this.updateOverState(false);
         App.toolTipMgr.hide();
      }
      
      protected function updateOverState(param1:Boolean, param2:Boolean = false) : void
      {
         if(param2)
         {
            gotoAndStop(!!param1 ? OUT : OVER);
         }
         else
         {
            gotoAndPlay(!!param1 ? OVER : OUT);
         }
      }
      
      public function updateSize() : void
      {
         App.utils.asserter.assert(false,"EpicBattlesWidgetBaseButton:updateSize" + Errors.ABSTRACT_INVOKE);
      }
      
      public function get isSmallHeight() : Boolean
      {
         return App.appHeight <= StageSizeBoundaries.HEIGHT_900;
      }
      
      public function get isSmallWidth() : Boolean
      {
         return App.appWidth <= StageSizeBoundaries.WIDTH_1280;
      }
   }
}
