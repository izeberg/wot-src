package net.wg.frontline.gui.battle.battleLoading
{
   import net.wg.frontline.gui.battle.VO.daapi.FrontlinePlayerStatsVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehiclesStatsVO;
   import net.wg.frontline.gui.battle.battleLoading.events.FrontlineBattleLoadingEvent;
   import net.wg.frontline.infrastructure.helpers.statisticsDataController.interfaces.IFrontlineBattleStatisticDataController;
   import net.wg.gui.battle.battleloading.BattleLoading;
   
   public class FrontlineBattleLoading extends BattleLoading implements IFrontlineBattleStatisticDataController
   {
      
      private static const FORM_VISIBLE_AREA_HEIGHT:int = 750;
       
      
      private var _epicForm:FrontlineBattleLoadingForm = null;
      
      public function FrontlineBattleLoading()
      {
         super();
      }
      
      override public function hasAmmunitionPanel(param1:Boolean) : void
      {
         if(param1)
         {
            form.updateTipVisibility(false);
         }
      }
      
      override public function setCompVisible(param1:Boolean) : void
      {
         super.setCompVisible(param1);
         dispatchEvent(new FrontlineBattleLoadingEvent(FrontlineBattleLoadingEvent.VISIBILITY_CHANGED));
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         form.y = param2 - FORM_VISIBLE_AREA_HEIGHT >> 1;
      }
      
      override protected function onDispose() : void
      {
         if(this._epicForm)
         {
            this._epicForm = null;
         }
         super.onDispose();
      }
      
      override protected function onPopulate() : void
      {
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._epicForm = form as FrontlineBattleLoadingForm;
      }
      
      override protected function updateFormY() : void
      {
      }
      
      public function setEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         if(this._epicForm)
         {
            this._epicForm.setEpicVehiclesStats(param1);
         }
      }
      
      public function updateEpicPlayerStats(param1:FrontlinePlayerStatsVO) : void
      {
      }
      
      public function updateEpicVehiclesStats(param1:FrontlineVehiclesStatsVO) : void
      {
         if(this._epicForm)
         {
            this._epicForm.setEpicVehiclesStats(param1);
         }
      }
   }
}
