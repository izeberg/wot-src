package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a26a7e5544f8364108bfd17e67d62e7c79d0db31f512f7f70a64d091692ebdac_flash_display_Sprite extends Sprite
   {
       
      
      public function _a26a7e5544f8364108bfd17e67d62e7c79d0db31f512f7f70a64d091692ebdac_flash_display_Sprite()
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
