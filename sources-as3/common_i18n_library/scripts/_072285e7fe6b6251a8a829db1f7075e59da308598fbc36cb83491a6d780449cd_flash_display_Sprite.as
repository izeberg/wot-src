package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _072285e7fe6b6251a8a829db1f7075e59da308598fbc36cb83491a6d780449cd_flash_display_Sprite extends Sprite
   {
       
      
      public function _072285e7fe6b6251a8a829db1f7075e59da308598fbc36cb83491a6d780449cd_flash_display_Sprite()
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
