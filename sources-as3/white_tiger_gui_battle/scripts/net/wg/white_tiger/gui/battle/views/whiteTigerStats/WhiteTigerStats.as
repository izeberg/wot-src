package net.wg.white_tiger.gui.battle.views.whiteTigerStats
{
   import net.wg.data.VO.daapi.DAAPIVehicleStatusVO;
   import net.wg.data.VO.daapi.DAAPIVehiclesStatsVO;
   import net.wg.gui.battle.StatsBase;
   import net.wg.gui.battle.interfaces.ITabbedFullStatsTableController;
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   import net.wg.white_tiger.gui.battle.VO.DAAPIHunterVehicleInfoVO;
   import net.wg.white_tiger.gui.battle.VO.DAAPIHunterVehiclesDataVO;
   
   public class WhiteTigerStats extends StatsBase
   {
       
      
      private var _tableCtrl:WhiteTigerFullStatsTableCtrl = null;
      
      public function WhiteTigerStats()
      {
         super();
         visible = false;
         this._tableCtrl = WhiteTigerFullStatsTableCtrl(tableCtrl);
      }
      
      override public function setCompVisible(param1:Boolean) : void
      {
         super.setCompVisible(param1);
         if(!param1)
         {
            App.toolTipMgr.hide();
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         header.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this._tableCtrl = null;
         super.onDispose();
      }
      
      override public function getTableCtrl() : ITabbedFullStatsTableController
      {
         return new WhiteTigerFullStatsTableCtrl(WhiteTigerFullStatsTable(statsTable),this);
      }
      
      override public function addVehiclesInfo(param1:IDAAPIDataClass) : void
      {
         var _loc2_:DAAPIHunterVehiclesDataVO = DAAPIHunterVehiclesDataVO(param1);
         this._tableCtrl.addVehiclesInfo(_loc2_.leftVehicleInfos,_loc2_.leftVehiclesIDs,false);
         this._tableCtrl.addVehiclesInfo(_loc2_.rightVehicleInfos,_loc2_.rightVehiclesIDs,true);
      }
      
      override public function setVehiclesData(param1:IDAAPIDataClass) : void
      {
         var _loc2_:DAAPIHunterVehiclesDataVO = DAAPIHunterVehiclesDataVO(param1);
         var _loc3_:DAAPIHunterVehicleInfoVO = null;
         var _loc4_:Array = [];
         for each(_loc3_ in _loc2_.leftVehicleInfos)
         {
            _loc4_.push(_loc3_);
         }
         this._tableCtrl.setVehiclesData(_loc4_,_loc2_.leftVehiclesIDs,false);
         _loc4_ = [];
         for each(_loc3_ in _loc2_.rightVehicleInfos)
         {
            _loc4_.push(_loc3_);
         }
         this._tableCtrl.setVehiclesData(_loc4_,_loc2_.rightVehiclesIDs,true);
      }
      
      override public function updateVehiclesData(param1:IDAAPIDataClass) : void
      {
         var _loc2_:DAAPIHunterVehiclesDataVO = DAAPIHunterVehiclesDataVO(param1);
         this._tableCtrl.updateVehiclesData(_loc2_.leftVehicleInfos,_loc2_.leftVehiclesIDs,false);
         this._tableCtrl.updateVehiclesData(_loc2_.rightVehicleInfos,_loc2_.rightVehiclesIDs,true);
      }
      
      override public function updateVehicleStatus(param1:IDAAPIDataClass) : void
      {
         var _loc2_:DAAPIVehicleStatusVO = DAAPIVehicleStatusVO(param1);
         this._tableCtrl.setVehicleStatus(false,_loc2_.vehicleID,_loc2_.status,_loc2_.leftVehiclesIDs);
         this._tableCtrl.setVehicleStatus(true,_loc2_.vehicleID,_loc2_.status,_loc2_.rightVehiclesIDs);
         if(_loc2_.dogTag)
         {
            this._tableCtrl.setDogTagToShow(_loc2_.vehicleID,_loc2_.dogTag);
         }
      }
      
      override public function updateVehiclesStat(param1:IDAAPIDataClass) : void
      {
         this.updateFrags(param1);
      }
      
      override protected function updateFrags(param1:IDAAPIDataClass) : void
      {
         var _loc2_:DAAPIVehiclesStatsVO = DAAPIVehiclesStatsVO(param1);
         this._tableCtrl.setVehiclesStats(_loc2_.leftFrags,_loc2_.rightFrags);
      }
   }
}
