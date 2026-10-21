package net.wg.portal.gui.battle.views.battleHints
{
   import net.wg.gui.battle.eventBattle.views.battleHints.data.HintInfoVO;
   import net.wg.infrastructure.base.meta.IBattleHintMeta;
   import net.wg.infrastructure.base.meta.impl.BattleHintMeta;
   import net.wg.utils.StageBreakPointList;
   
   public class PortalBattleHint extends BattleHintMeta implements IBattleHintMeta
   {
      
      private static const HINT_SCALE_SMALL:Number = 0.7;
      
      private static const HINT_SCALE_MEDIUM:Number = 0.85;
      
      private static const HINT_SCALE_EXTRA_LARGE:Number = 1;
       
      
      public var hintContainer:InfoContainer = null;
      
      public function PortalBattleHint()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.hintContainer.dispose();
         this.hintContainer = null;
         super.onDispose();
      }
      
      override protected function showHint(param1:HintInfoVO) : void
      {
         this.hintContainer.showHint(param1);
         this.updateStage(App.appWidth,App.appHeight);
      }
      
      public function as_hideHint() : void
      {
         this.hintContainer.hideHint();
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         if(App.stageSizeMgr.currentBreakPoint == StageBreakPointList.EXTRA_SMALL || App.stageSizeMgr.currentBreakPoint == StageBreakPointList.SMALL)
         {
            this.hintContainer.scaleX = this.hintContainer.scaleY = HINT_SCALE_SMALL;
         }
         else if(App.stageSizeMgr.currentBreakPoint == StageBreakPointList.MEDIUM || App.stageSizeMgr.currentBreakPoint == StageBreakPointList.LARGE)
         {
            this.hintContainer.scaleX = this.hintContainer.scaleY = HINT_SCALE_MEDIUM;
         }
         else
         {
            this.hintContainer.scaleX = this.hintContainer.scaleY = HINT_SCALE_EXTRA_LARGE;
         }
         this.hintContainer.x = param1 >> 1;
      }
   }
}
