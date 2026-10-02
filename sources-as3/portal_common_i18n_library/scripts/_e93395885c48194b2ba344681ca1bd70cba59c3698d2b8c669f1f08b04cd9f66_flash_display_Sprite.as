package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e93395885c48194b2ba344681ca1bd70cba59c3698d2b8c669f1f08b04cd9f66_flash_display_Sprite extends Sprite
   {
       
      
      public function _e93395885c48194b2ba344681ca1bd70cba59c3698d2b8c669f1f08b04cd9f66_flash_display_Sprite()
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
