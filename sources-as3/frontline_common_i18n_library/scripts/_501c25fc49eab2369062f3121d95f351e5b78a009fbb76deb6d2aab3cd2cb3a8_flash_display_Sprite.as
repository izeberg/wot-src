package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _501c25fc49eab2369062f3121d95f351e5b78a009fbb76deb6d2aab3cd2cb3a8_flash_display_Sprite extends Sprite
   {
       
      
      public function _501c25fc49eab2369062f3121d95f351e5b78a009fbb76deb6d2aab3cd2cb3a8_flash_display_Sprite()
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
