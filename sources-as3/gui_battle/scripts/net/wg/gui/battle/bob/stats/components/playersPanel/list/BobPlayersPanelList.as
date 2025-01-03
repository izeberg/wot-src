package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import flash.display.Sprite;
   import flash.geom.ColorTransform;
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   import net.wg.data.constants.generated.PLAYERS_PANEL_STATE;
   import net.wg.gui.battle.bob.data.BobDAAPIVehicleInfoVO;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.list.PlayersPanelList;
   
   public class BobPlayersPanelList extends PlayersPanelList
   {
      
      private static const BOB_PLAYERS_LIST_HIGHLIGHT_SCHEME_PREFIX:String = "blogger_";
       
      
      public var teamHighlight:Sprite;
      
      public var teamSkill:BobPlayersListTeamSkill;
      
      public var header:BobPlayersListHeader;
      
      public function BobPlayersPanelList()
      {
         super();
         this.header.mouseChildren = this.header.mouseEnabled = false;
         this.teamHighlight.mouseChildren = this.teamHighlight.mouseEnabled = false;
      }
      
      override public function getItemHolderClass() : Class
      {
         return BobPlayersPanelListItemHolder;
      }
      
      override public function setVehicleData(param1:Vector.<DAAPIVehicleInfoVO>) : void
      {
         var _loc2_:DAAPIVehicleInfoVO = null;
         var _loc3_:BobDAAPIVehicleInfoVO = null;
         super.setVehicleData(param1);
         for each(_loc2_ in param1)
         {
            _loc3_ = _loc2_ as BobDAAPIVehicleInfoVO;
            if(_loc3_ && _loc3_.bloggerID > 0)
            {
               this.setBloggerId(_loc3_.bloggerID);
               break;
            }
         }
      }
      
      override protected function initializeState() : void
      {
         var _loc1_:Boolean = false;
         super.initializeState();
         this.header.setIsRightAligned(isRightAligned);
         _loc1_ = state == PLAYERS_PANEL_STATE.HIDDEN;
         this.teamHighlight.visible = !_loc1_;
         this.header.visible = !_loc1_;
      }
      
      override protected function onDispose() : void
      {
         this.teamHighlight = null;
         this.teamSkill.dispose();
         this.teamSkill = null;
         this.header.dispose();
         this.header = null;
         super.onDispose();
      }
      
      private function setBloggerId(param1:int) : void
      {
         var _loc2_:ColorTransform = App.colorSchemeMgr.getTransform(BOB_PLAYERS_LIST_HIGHLIGHT_SCHEME_PREFIX + param1);
         this.teamHighlight.transform.colorTransform = _loc2_;
         this.header.setBloggerId(param1);
      }
   }
}
