package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _fec2e2ab1bcb8055a883c37c9775acf396d876de19f3fd875a9895d2cc592dcc_flash_display_Sprite extends Sprite
   {
       
      
      public function _fec2e2ab1bcb8055a883c37c9775acf396d876de19f3fd875a9895d2cc592dcc_flash_display_Sprite()
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
