package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a2f21f034644e245057cb6b78ca171d7701dec88ffbf3e1cdcbf50d0998f42cf_flash_display_Sprite extends Sprite
   {
       
      
      public function _a2f21f034644e245057cb6b78ca171d7701dec88ffbf3e1cdcbf50d0998f42cf_flash_display_Sprite()
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
