package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1ac5269c896ee7ccedd1ed989263eb676ff5c429662a0dc18b3b0d0cf2912e69_flash_display_Sprite extends Sprite
   {
       
      
      public function _1ac5269c896ee7ccedd1ed989263eb676ff5c429662a0dc18b3b0d0cf2912e69_flash_display_Sprite()
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
