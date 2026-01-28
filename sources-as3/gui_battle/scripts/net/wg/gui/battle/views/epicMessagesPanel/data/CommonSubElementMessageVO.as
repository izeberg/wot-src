package net.wg.gui.battle.views.epicMessagesPanel.data
{
   import net.wg.gui.battle.views.gameMessagesPanel.data.BaseGameMessageVO;
   
   public class CommonSubElementMessageVO extends BaseGameMessageVO
   {
       
      
      public var iconFrame:int = -1;
      
      public var subTitle:String = "";
      
      public function CommonSubElementMessageVO(param1:Object)
      {
         super(param1);
      }
   }
}
