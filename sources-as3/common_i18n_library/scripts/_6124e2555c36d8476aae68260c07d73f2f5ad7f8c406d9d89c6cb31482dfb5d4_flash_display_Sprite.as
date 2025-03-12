package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6124e2555c36d8476aae68260c07d73f2f5ad7f8c406d9d89c6cb31482dfb5d4_flash_display_Sprite extends Sprite
   {
       
      
      public function _6124e2555c36d8476aae68260c07d73f2f5ad7f8c406d9d89c6cb31482dfb5d4_flash_display_Sprite()
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
