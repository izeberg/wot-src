package net.wg.frontline.gui.battle.battleLoading.components
{
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   import net.wg.frontline.gui.battle.VO.daapi.FrontlineVehicleStatsVO;
   import net.wg.frontline.gui.battle.battleLoading.renderers.FrontlineBattleLoadingPlayerItemRenderer;
   import net.wg.frontline.gui.battle.views.data.FrontlineVehicleDataProvider;
   import scaleform.clik.controls.ScrollingList;
   import scaleform.clik.data.ListData;
   
   public class FrontlineBattleScrollingList extends ScrollingList
   {
       
      
      public function FrontlineBattleScrollingList()
      {
         super();
      }
      
      override protected function populateData(param1:Array) : void
      {
         var _loc5_:uint = 0;
         var _loc6_:ListData = null;
         var _loc7_:FrontlineBattleLoadingPlayerItemRenderer = null;
         var _loc8_:DAAPIVehicleInfoVO = null;
         var _loc9_:FrontlineVehicleDataProvider = null;
         var _loc10_:FrontlineVehicleStatsVO = null;
         var _loc2_:uint = param1.length;
         var _loc3_:uint = _renderers.length;
         var _loc4_:uint = 0;
         while(_loc4_ < _loc3_)
         {
            _loc5_ = _scrollPosition + _loc4_;
            _loc6_ = new ListData(_loc5_,itemToLabel(param1[_loc4_]),_selectedIndex == _loc5_);
            _loc7_ = getRendererAt(_loc4_) as FrontlineBattleLoadingPlayerItemRenderer;
            if(_loc7_)
            {
               _loc7_.enabled = _loc4_ < _loc2_;
               _loc7_.setListData(_loc6_);
               if(param1[_loc4_])
               {
                  _loc8_ = param1[_loc4_] as DAAPIVehicleInfoVO;
                  if(_loc8_)
                  {
                     _loc7_.setData(_loc8_);
                  }
                  _loc9_ = _dataProvider as FrontlineVehicleDataProvider;
                  if(_loc9_)
                  {
                     _loc10_ = _loc9_.requestEpicData(_loc8_.vehicleID);
                     if(_loc10_)
                     {
                        _loc7_.setEpicData(_loc10_);
                     }
                  }
               }
               _loc7_.validateNow();
            }
            _loc4_++;
         }
         App.tutorialMgr.dispatchEventForCustomComponent(this);
      }
   }
}
