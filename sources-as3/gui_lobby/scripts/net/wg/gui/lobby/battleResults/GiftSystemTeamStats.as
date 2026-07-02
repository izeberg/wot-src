package net.wg.gui.lobby.battleResults
{
   import flash.events.Event;
   import net.wg.gui.lobby.battleResults.components.TeamStatsList;
   import net.wg.gui.lobby.battleResults.components.giftSystem.GiftSystemBanner;
   import net.wg.gui.lobby.battleResults.components.giftSystem.IGiftTeamMemberItemRenderer;
   import net.wg.gui.lobby.battleResults.controller.DefaultTeamStatsController;
   import net.wg.gui.lobby.battleResults.controller.giftSystem.GiftDefaultTeamStatsController;
   import net.wg.gui.lobby.battleResults.controller.giftSystem.GiftScrollBarTeamStatsController;
   import net.wg.gui.lobby.battleResults.data.GiftSystemVO;
   
   public class GiftSystemTeamStats extends TeamStats
   {
       
      
      public var giftBanner:GiftSystemBanner = null;
      
      private var _data:GiftSystemVO = null;
      
      public function GiftSystemTeamStats()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         team1List.addEventListener(Event.RESIZE,this.onTeamListChangedHandler);
         team2List.addEventListener(Event.RESIZE,this.onTeamListChangedHandler);
      }
      
      override protected function onDispose() : void
      {
         team1List.removeEventListener(Event.RESIZE,this.onTeamListChangedHandler);
         team2List.removeEventListener(Event.RESIZE,this.onTeamListChangedHandler);
         this.giftBanner.dispose();
         this.giftBanner = null;
         this._data = null;
         super.onDispose();
      }
      
      override protected function createDefaultController() : DefaultTeamStatsController
      {
         return !!_enableScrollbars ? new GiftScrollBarTeamStatsController(this) : new GiftDefaultTeamStatsController(this);
      }
      
      public function updateGiftSystemData(param1:GiftSystemVO) : void
      {
         this._data = param1;
         this.giftBanner.updateData(param1);
         this.updateTeamListGiftData(team1List);
         this.updateTeamListGiftData(team2List);
      }
      
      private function updateTeamListGiftData(param1:TeamStatsList) : void
      {
         var _loc2_:IGiftTeamMemberItemRenderer = null;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         if(this._data)
         {
            _loc4_ = param1.renderersCount;
            _loc3_ = 0;
            while(_loc3_ < _loc4_)
            {
               _loc2_ = param1.getRendererAt(_loc3_) as IGiftTeamMemberItemRenderer;
               if(_loc2_)
               {
                  _loc2_.setGiftSystemData(this._data);
               }
               _loc3_++;
            }
         }
      }
      
      private function onTeamListChangedHandler(param1:Event) : void
      {
         var _loc2_:TeamStatsList = param1.target as TeamStatsList;
         if(_loc2_)
         {
            this.updateTeamListGiftData(_loc2_);
         }
      }
   }
}
