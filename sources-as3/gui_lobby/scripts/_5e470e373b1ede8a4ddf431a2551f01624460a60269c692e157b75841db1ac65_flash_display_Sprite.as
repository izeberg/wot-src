package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5e470e373b1ede8a4ddf431a2551f01624460a60269c692e157b75841db1ac65_flash_display_Sprite extends Sprite
   {
       
      
      public function _5e470e373b1ede8a4ddf431a2551f01624460a60269c692e157b75841db1ac65_flash_display_Sprite()
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
