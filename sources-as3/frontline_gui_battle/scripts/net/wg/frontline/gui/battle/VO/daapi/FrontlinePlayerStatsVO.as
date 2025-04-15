package net.wg.frontline.gui.battle.VO.daapi
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FrontlinePlayerStatsVO extends DAAPIDataClass
   {
       
      
      public var isAttacker:Boolean = false;
      
      public var lane:int = -1;
      
      public var respawnLane:int = -1;
      
      public var rank:int = -1;
      
      public function FrontlinePlayerStatsVO(param1:Object)
      {
         super(param1);
      }
   }
}
