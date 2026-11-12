package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _29f048e9329b6bbc955baf9ff097851b5bb85652c9c570d33661ceedca01c74e_flash_display_Sprite extends Sprite
   {
       
      
      public function _29f048e9329b6bbc955baf9ff097851b5bb85652c9c570d33661ceedca01c74e_flash_display_Sprite()
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
