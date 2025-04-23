package net.wg.frontline.gui.battle.views.frontlineInGameRank.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FrontlineInGameRankVO extends DAAPIDataClass
   {
       
      
      public var rank:int = 0;
      
      public var isMaxRank:Boolean = false;
      
      public var previousProgress:Number = 0;
      
      public var newProgress:Number = 0;
      
      public var rankText:String = "";
      
      public function FrontlineInGameRankVO(param1:Object)
      {
         super(param1);
      }
   }
}
