package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1a1ca49c94c60d5a94be9c506fbf0da58a358a65c30604db84386e07c095d051_flash_display_Sprite extends Sprite
   {
       
      
      public function _1a1ca49c94c60d5a94be9c506fbf0da58a358a65c30604db84386e07c095d051_flash_display_Sprite()
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
