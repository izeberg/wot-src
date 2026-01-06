package net.wg.gui.battle.views.epicMessagesPanel.components
{
   import net.wg.gui.battle.views.epicMessagesPanel.data.CommonSubElementMessageVO;
   
   public class SupplyUnlockMessage extends CommonSubElementMessage
   {
       
      
      public function SupplyUnlockMessage()
      {
         super();
      }
      
      override public function getID() : int
      {
         var _loc1_:CommonSubElementMessageVO = null;
         if(messageData)
         {
            _loc1_ = messageData.msgData as CommonSubElementMessageVO;
            return _loc1_.iconFrame;
         }
         return -1;
      }
   }
}
