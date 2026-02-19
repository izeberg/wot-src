package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _61501b7939f500b33a9dd2ad0f0065cd26730e32b0f28b095c66b1ce3b157bec_flash_display_Sprite extends Sprite
   {
       
      
      public function _61501b7939f500b33a9dd2ad0f0065cd26730e32b0f28b095c66b1ce3b157bec_flash_display_Sprite()
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
