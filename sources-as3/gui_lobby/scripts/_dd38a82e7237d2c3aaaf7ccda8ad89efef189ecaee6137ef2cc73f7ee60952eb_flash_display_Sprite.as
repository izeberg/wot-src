package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dd38a82e7237d2c3aaaf7ccda8ad89efef189ecaee6137ef2cc73f7ee60952eb_flash_display_Sprite extends Sprite
   {
       
      
      public function _dd38a82e7237d2c3aaaf7ccda8ad89efef189ecaee6137ef2cc73f7ee60952eb_flash_display_Sprite()
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
