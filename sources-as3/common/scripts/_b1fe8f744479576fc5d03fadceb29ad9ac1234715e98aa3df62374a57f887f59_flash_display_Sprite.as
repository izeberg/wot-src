package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b1fe8f744479576fc5d03fadceb29ad9ac1234715e98aa3df62374a57f887f59_flash_display_Sprite extends Sprite
   {
       
      
      public function _b1fe8f744479576fc5d03fadceb29ad9ac1234715e98aa3df62374a57f887f59_flash_display_Sprite()
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
