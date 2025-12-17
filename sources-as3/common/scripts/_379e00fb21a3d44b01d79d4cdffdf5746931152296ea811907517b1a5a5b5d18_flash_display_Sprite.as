package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _379e00fb21a3d44b01d79d4cdffdf5746931152296ea811907517b1a5a5b5d18_flash_display_Sprite extends Sprite
   {
       
      
      public function _379e00fb21a3d44b01d79d4cdffdf5746931152296ea811907517b1a5a5b5d18_flash_display_Sprite()
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
