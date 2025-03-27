package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineUpgradePanelVO;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineBattleUpgradePanelMeta extends BattleDisplayable
   {
       
      
      public var onSelectItem:Function;
      
      private var _frontlineUpgradePanelVO:FrontlineUpgradePanelVO;
      
      public function FrontlineBattleUpgradePanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._frontlineUpgradePanelVO)
         {
            this._frontlineUpgradePanelVO.dispose();
            this._frontlineUpgradePanelVO = null;
         }
         super.onDispose();
      }
      
      public function onSelectItemS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.onSelectItem,"onSelectItem" + Errors.CANT_NULL);
         this.onSelectItem(param1);
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:FrontlineUpgradePanelVO = this._frontlineUpgradePanelVO;
         this._frontlineUpgradePanelVO = new FrontlineUpgradePanelVO(param1);
         this.setData(this._frontlineUpgradePanelVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:FrontlineUpgradePanelVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
