package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4c22ccb352a5153178a57bcfe58aad2f6d21af0b554702ee5f25111e6ae95883_flash_display_Sprite extends Sprite
   {
       
      
      public function _4c22ccb352a5153178a57bcfe58aad2f6d21af0b554702ee5f25111e6ae95883_flash_display_Sprite()
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
