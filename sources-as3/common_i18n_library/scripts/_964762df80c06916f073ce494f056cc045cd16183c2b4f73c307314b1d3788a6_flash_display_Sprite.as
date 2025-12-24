package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _964762df80c06916f073ce494f056cc045cd16183c2b4f73c307314b1d3788a6_flash_display_Sprite extends Sprite
   {
       
      
      public function _964762df80c06916f073ce494f056cc045cd16183c2b4f73c307314b1d3788a6_flash_display_Sprite()
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
