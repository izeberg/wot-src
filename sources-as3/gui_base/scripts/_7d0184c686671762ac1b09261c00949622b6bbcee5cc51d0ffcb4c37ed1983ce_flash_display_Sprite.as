package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7d0184c686671762ac1b09261c00949622b6bbcee5cc51d0ffcb4c37ed1983ce_flash_display_Sprite extends Sprite
   {
       
      
      public function _7d0184c686671762ac1b09261c00949622b6bbcee5cc51d0ffcb4c37ed1983ce_flash_display_Sprite()
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
