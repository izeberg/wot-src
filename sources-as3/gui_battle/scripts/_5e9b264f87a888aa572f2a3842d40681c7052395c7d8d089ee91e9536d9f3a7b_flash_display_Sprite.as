package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5e9b264f87a888aa572f2a3842d40681c7052395c7d8d089ee91e9536d9f3a7b_flash_display_Sprite extends Sprite
   {
       
      
      public function _5e9b264f87a888aa572f2a3842d40681c7052395c7d8d089ee91e9536d9f3a7b_flash_display_Sprite()
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
