package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _86632457c90f7db664d9fcafcee08eab714bc350a643c12ab97ec671cbd37d99_flash_display_Sprite extends Sprite
   {
       
      
      public function _86632457c90f7db664d9fcafcee08eab714bc350a643c12ab97ec671cbd37d99_flash_display_Sprite()
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
