package net.wg.gui.lobby.userMissions.interfaces
{
   import net.wg.infrastructure.interfaces.IDAAPIDataClass;
   
   public interface IConditionVO extends IDAAPIDataClass
   {
       
      
      function get useWideTextField() : Boolean;
      
      function set useWideTextField(param1:Boolean) : void;
   }
}
