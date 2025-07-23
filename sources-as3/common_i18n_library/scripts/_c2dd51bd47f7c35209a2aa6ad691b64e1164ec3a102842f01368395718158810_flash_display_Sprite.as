package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c2dd51bd47f7c35209a2aa6ad691b64e1164ec3a102842f01368395718158810_flash_display_Sprite extends Sprite
   {
       
      
      public function _c2dd51bd47f7c35209a2aa6ad691b64e1164ec3a102842f01368395718158810_flash_display_Sprite()
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
