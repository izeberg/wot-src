package net.wg.white_tiger.gui.battle.views.wtBattleLoading
{
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   import net.wg.white_tiger.infrastructure.base.meta.IWTBattleLoadingMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WTBattleLoadingMeta;
   
   public class WTBattleLoading extends WTBattleLoadingMeta implements IWTBattleLoadingMeta, IDisplayableComponent
   {
       
      
      private var _isCompVisible:Boolean = true;
      
      public function WTBattleLoading()
      {
         super();
         setManageSize(true);
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         if(this._isCompVisible != param1)
         {
            this._isCompVisible = param1;
            visible = this._isCompVisible;
         }
      }
   }
}
