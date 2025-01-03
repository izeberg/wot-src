package net.wg.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IBobPlayersPanelMeta extends IEventDispatcher
   {
       
      
      function onVoiceChatControlClickS() : void;
      
      function as_setLeftTeamSkill(param1:String, param2:String, param3:String) : void;
      
      function as_setRightTeamSkill(param1:String, param2:String, param3:String) : void;
      
      function as_setBattleStarted(param1:Boolean) : void;
      
      function as_setVoiceChatData(param1:Object) : void;
      
      function as_setVoiceChatControlVisible(param1:Boolean) : void;
      
      function as_setVoiceChatControlSelected(param1:Boolean) : void;
   }
}
