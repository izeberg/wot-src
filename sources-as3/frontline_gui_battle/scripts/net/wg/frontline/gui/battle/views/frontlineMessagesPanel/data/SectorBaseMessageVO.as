package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data
{
   import net.wg.gui.battle.views.gameMessagesPanel.data.BaseGameMessageVO;
   
   public class SectorBaseMessageVO extends BaseGameMessageVO
   {
       
      
      public var baseID:int = -1;
      
      public var timerText:String = "";
      
      public var descriptionText:String = "";
      
      public function SectorBaseMessageVO(param1:Object)
      {
         super(param1);
      }
   }
}
