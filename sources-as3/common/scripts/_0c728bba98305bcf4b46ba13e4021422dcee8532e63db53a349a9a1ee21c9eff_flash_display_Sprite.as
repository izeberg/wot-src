package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0c728bba98305bcf4b46ba13e4021422dcee8532e63db53a349a9a1ee21c9eff_flash_display_Sprite extends Sprite
   {
       
      
      public function _0c728bba98305bcf4b46ba13e4021422dcee8532e63db53a349a9a1ee21c9eff_flash_display_Sprite()
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
