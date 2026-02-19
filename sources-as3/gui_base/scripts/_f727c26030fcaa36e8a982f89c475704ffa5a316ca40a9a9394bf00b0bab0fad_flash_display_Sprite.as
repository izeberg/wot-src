package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f727c26030fcaa36e8a982f89c475704ffa5a316ca40a9a9394bf00b0bab0fad_flash_display_Sprite extends Sprite
   {
       
      
      public function _f727c26030fcaa36e8a982f89c475704ffa5a316ca40a9a9394bf00b0bab0fad_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
