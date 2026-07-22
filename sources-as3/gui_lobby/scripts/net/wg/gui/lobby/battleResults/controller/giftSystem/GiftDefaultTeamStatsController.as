package net.wg.gui.lobby.battleResults.controller.giftSystem
{
   import flash.events.IEventDispatcher;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.lobby.battleResults.components.TeamStatsList;
   import net.wg.gui.lobby.battleResults.controller.ColumnConstants;
   import net.wg.gui.lobby.battleResults.controller.DefaultTeamStatsController;
   import net.wg.gui.lobby.battleResults.data.CommonStatsVO;
   
   public class GiftDefaultTeamStatsController extends DefaultTeamStatsController
   {
       
      
      public function GiftDefaultTeamStatsController(param1:IEventDispatcher)
      {
         super(param1);
      }
      
      override protected function initColumnsData(param1:CommonStatsVO) : void
      {
         super.initColumnsData(param1);
         if(param1.isShowSquad)
         {
            columnWidth[ColumnConstants.SQUAD] = GiftColumnConstants.FIRST_COLUMN_WIDTH;
            columnWidth[ColumnConstants.PLAYER] = GiftColumnConstants.PLAYER_COLUMN_WIDTH;
         }
         else
         {
            columnWidth[ColumnConstants.PLAYER] = GiftColumnConstants.PLAYER_COLUMN_WIDTH + GiftColumnConstants.FIRST_COLUMN_WIDTH;
         }
         columnWidth[ColumnConstants.TANK] = GiftColumnConstants.TANK_COLUMN_WIDTH;
         columnWidth[ColumnConstants.DAMAGE] = GiftColumnConstants.DAMAGE_COLUMN_WIDTH;
         columnWidth[ColumnConstants.FRAG] = GiftColumnConstants.DEFAULT_FRAG_COLUMN_WIDTH;
         columnWidth[ColumnConstants.XP] = GiftColumnConstants.XP_COLUMN_WIDTH;
         columnWidth[ColumnConstants.MEDAL] = GiftColumnConstants.MEDAL_COLUMN_WIDTH;
         columnWidth[ColumnConstants.GIFT_SYSTEM] = GiftColumnConstants.GIFT_COLUMN_WIDTH;
      }
      
      override protected function getColumnIds(param1:CommonStatsVO) : Vector.<String>
      {
         var _loc2_:Vector.<String> = super.getColumnIds(param1);
         _loc2_.push(ColumnConstants.GIFT_SYSTEM);
         return _loc2_;
      }
      
      override protected function setupRenderers(param1:TeamStatsList, param2:TeamStatsList) : void
      {
         param1.itemRendererName = Linkages.GIFT_TEAM_LEFT_MEMBER_RENDERER;
         param2.itemRendererName = Linkages.GIFT_TEAM_RIGHT_MEMBER_RENDERER;
      }
   }
}
