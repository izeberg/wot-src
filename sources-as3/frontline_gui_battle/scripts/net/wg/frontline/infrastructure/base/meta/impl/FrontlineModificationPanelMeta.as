package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.modificationPanel.data.FrontlineModificationPanelVO;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineModificationPanelMeta extends BattleDisplayable
   {
       
      
      private var _frontlineModificationPanelVO:FrontlineModificationPanelVO;
      
      public function FrontlineModificationPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlineModificationPanelVO)
         {
            this._frontlineModificationPanelVO.dispose();
            this._frontlineModificationPanelVO = null;
         }
         super.onDispose();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:FrontlineModificationPanelVO = this._frontlineModificationPanelVO;
         this._frontlineModificationPanelVO = new FrontlineModificationPanelVO(param1);
         this.setData(this._frontlineModificationPanelVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:FrontlineModificationPanelVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
