package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _acb80174f54a1291eabfa0c01c9ea959b10a669d2e57d92761e5c296b4f1784c_flash_display_Sprite extends Sprite
   {
       
      
      public function _acb80174f54a1291eabfa0c01c9ea959b10a669d2e57d92761e5c296b4f1784c_flash_display_Sprite()
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
