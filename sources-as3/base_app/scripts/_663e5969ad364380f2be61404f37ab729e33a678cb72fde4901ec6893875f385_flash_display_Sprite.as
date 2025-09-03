package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _663e5969ad364380f2be61404f37ab729e33a678cb72fde4901ec6893875f385_flash_display_Sprite extends Sprite
   {
       
      
      public function _663e5969ad364380f2be61404f37ab729e33a678cb72fde4901ec6893875f385_flash_display_Sprite()
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
