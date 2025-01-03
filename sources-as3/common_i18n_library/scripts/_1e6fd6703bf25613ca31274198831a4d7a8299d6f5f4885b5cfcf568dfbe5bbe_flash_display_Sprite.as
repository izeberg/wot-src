package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1e6fd6703bf25613ca31274198831a4d7a8299d6f5f4885b5cfcf568dfbe5bbe_flash_display_Sprite extends Sprite
   {
       
      
      public function _1e6fd6703bf25613ca31274198831a4d7a8299d6f5f4885b5cfcf568dfbe5bbe_flash_display_Sprite()
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
