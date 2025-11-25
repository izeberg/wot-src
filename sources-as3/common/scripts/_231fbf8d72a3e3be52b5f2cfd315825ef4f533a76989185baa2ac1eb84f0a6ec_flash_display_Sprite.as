package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _231fbf8d72a3e3be52b5f2cfd315825ef4f533a76989185baa2ac1eb84f0a6ec_flash_display_Sprite extends Sprite
   {
       
      
      public function _231fbf8d72a3e3be52b5f2cfd315825ef4f533a76989185baa2ac1eb84f0a6ec_flash_display_Sprite()
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
