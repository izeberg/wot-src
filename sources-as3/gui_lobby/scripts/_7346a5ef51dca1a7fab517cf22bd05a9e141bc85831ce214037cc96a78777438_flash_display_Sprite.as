package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7346a5ef51dca1a7fab517cf22bd05a9e141bc85831ce214037cc96a78777438_flash_display_Sprite extends Sprite
   {
       
      
      public function _7346a5ef51dca1a7fab517cf22bd05a9e141bc85831ce214037cc96a78777438_flash_display_Sprite()
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
