package net.wg.gui.battle.interfaces
{
   import net.wg.gui.battle.views.gameMessagesPanel.data.BaseGameMessageVO;
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   
   public interface IGameMessageVO extends IDAAPIDataClass
   {
       
      
      function get duration() : int;
      
      function get messageType() : String;
      
      function set messageType(param1:String) : void;
      
      function get priority() : int;
      
      function set priority(param1:int) : void;
      
      function get length() : Number;
      
      function set length(param1:Number) : void;
      
      function get msgData() : BaseGameMessageVO;
      
      function set msgData(param1:BaseGameMessageVO) : void;
   }
}
