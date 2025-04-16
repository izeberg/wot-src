package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.frontlineMissionsPanel.data.FrontlineMissionVO;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineMissionsPanelMeta extends BattleDisplayable
   {
       
      
      private var _frontlineMissionVO:FrontlineMissionVO;
      
      public function FrontlineMissionsPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlineMissionVO)
         {
            this._frontlineMissionVO.dispose();
            this._frontlineMissionVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setPrimaryMission(param1:Object) : void
      {
         var _loc2_:FrontlineMissionVO = this._frontlineMissionVO;
         this._frontlineMissionVO = new FrontlineMissionVO(param1);
         this.setPrimaryMission(this._frontlineMissionVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setPrimaryMission(param1:FrontlineMissionVO) : void
      {
         var _loc2_:String = "as_setPrimaryMission" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
