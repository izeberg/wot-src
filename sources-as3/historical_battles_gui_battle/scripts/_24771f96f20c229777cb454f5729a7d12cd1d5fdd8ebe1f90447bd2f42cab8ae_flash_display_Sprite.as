package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _24771f96f20c229777cb454f5729a7d12cd1d5fdd8ebe1f90447bd2f42cab8ae_flash_display_Sprite extends Sprite
   {
       
      
      public function _24771f96f20c229777cb454f5729a7d12cd1d5fdd8ebe1f90447bd2f42cab8ae_flash_display_Sprite()
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
