package net.wg.infrastructure.managers.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.meta.impl.VoiceChatManagerMeta;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.infrastructure.managers.IVoiceChatManager;
   
   public class VoiceChatManagerBase extends VoiceChatManagerMeta implements IVoiceChatManager
   {
       
      
      public function VoiceChatManagerBase()
      {
         super();
      }
      
      public function as_onPlayerSpeak(param1:Number, param2:Boolean, param3:Boolean) : void
      {
         throw new AbstractException("VoiceChatManagerBase.as_onPlayerSpeak" + Errors.ABSTRACT_INVOKE);
      }
   }
}
