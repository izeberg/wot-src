package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import net.wg.data.ListDAAPIDataProvider;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.VO.HBEnemyInfoVO;
   import net.wg.historical_battles.infrastructure.base.meta.IHBEnemiesPanelMeta;
   import net.wg.historical_battles.infrastructure.base.meta.impl.HBEnemiesPanelMeta;
   
   public class HBEnemiesPanel extends HBEnemiesPanelMeta implements IHBEnemiesPanelMeta
   {
       
      
      public var enemiesList:HBEnemiesList = null;
      
      private var _dataProvider:ListDAAPIDataProvider = null;
      
      public function HBEnemiesPanel()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.enemiesList.dispose();
         this.enemiesList = null;
         if(this._dataProvider)
         {
            this._dataProvider.cleanUp();
            this._dataProvider = null;
         }
         super.onDispose();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this._dataProvider = new ListDAAPIDataProvider(HBEnemyInfoVO);
         this.enemiesList.dataProvider = this._dataProvider;
      }
      
      public function as_getEnemyInfoDP() : Object
      {
         return this._dataProvider;
      }
      
      public function as_setChatCommand(param1:int, param2:String, param3:uint) : void
      {
         var _loc4_:HBEnemyRenderer = this.enemiesList.getEnemyRender(param1);
         if(_loc4_)
         {
            _loc4_.setChatCommand(param2,param3);
         }
      }
      
      public function as_setChatCommandsVisibility(param1:Boolean) : void
      {
         this.enemiesList.isChatCommVisible = param1;
      }
      
      public function as_setEnemyHp(param1:int, param2:int, param3:int) : void
      {
         var _loc4_:HBEnemyRenderer = this.enemiesList.getEnemyRender(param1);
         if(_loc4_)
         {
            _loc4_.setHp(param2,param3);
         }
      }
      
      public function set maxHeight(param1:int) : void
      {
         this.enemiesList.maxHeight = param1;
      }
      
      public function get minYPosition() : uint
      {
         return y + HBEnemiesList.MIN_HEIGHT;
      }
   }
}
