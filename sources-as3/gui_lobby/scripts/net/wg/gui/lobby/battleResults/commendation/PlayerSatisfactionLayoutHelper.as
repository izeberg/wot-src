package net.wg.gui.lobby.battleResults.commendation
{
   import flash.geom.Point;
   import net.wg.gui.lobby.battleResults.CommonStats;
   
   public class PlayerSatisfactionLayoutHelper
   {
      
      private static const COMPONENT_COORDINATES:Point = new Point(510,240);
      
      private static const COMPONENT_HEIGHT_OFFSET:int = 57;
      
      private static const NO_EFFICIENCY_LBL_OFFSET:int = 36;
      
      private static const EFFICIENCY_LIST_SMALL_SCALE:Number = 1.32206;
      
      private static const EFFICIENCY_LIST_NORMAL_SCALE:Number = 1.5648;
       
      
      public function PlayerSatisfactionLayoutHelper()
      {
         super();
      }
      
      public static function updateLayout(param1:CommonStats, param2:Boolean) : Point
      {
         if(param2)
         {
            param1.efficiencyHeader.y += COMPONENT_HEIGHT_OFFSET;
            param1.efficiencyTitle.y += COMPONENT_HEIGHT_OFFSET;
            param1.noEfficiencyLbl.y += NO_EFFICIENCY_LBL_OFFSET;
            param1.efficiencyList.y += COMPONENT_HEIGHT_OFFSET;
            param1.efficiencyList.scaleY = EFFICIENCY_LIST_SMALL_SCALE;
            return COMPONENT_COORDINATES;
         }
         param1.efficiencyHeader.y -= COMPONENT_HEIGHT_OFFSET;
         param1.efficiencyTitle.y -= COMPONENT_HEIGHT_OFFSET;
         param1.noEfficiencyLbl.y -= NO_EFFICIENCY_LBL_OFFSET;
         param1.efficiencyList.scaleY = EFFICIENCY_LIST_NORMAL_SCALE;
         param1.efficiencyList.y -= COMPONENT_HEIGHT_OFFSET;
         return null;
      }
   }
}
