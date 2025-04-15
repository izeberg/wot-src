package net.wg.frontline.gui.battle.views.frontlineMessagesPanel.data
{
   import net.wg.gui.battle.views.gameMessagesPanel.data.BaseGameMessageVO;
   
   public class HeadquarterAttackedMessageVO extends BaseGameMessageVO
   {
       
      
      public var hqID:int = -1;
      
      public var destroyedProgress:Number = 0;
      
      public function HeadquarterAttackedMessageVO(param1:Object)
      {
         super(param1);
      }
   }
}
