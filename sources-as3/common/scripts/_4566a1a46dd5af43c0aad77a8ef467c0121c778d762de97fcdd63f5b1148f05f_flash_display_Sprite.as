package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4566a1a46dd5af43c0aad77a8ef467c0121c778d762de97fcdd63f5b1148f05f_flash_display_Sprite extends Sprite
   {
       
      
      public function _4566a1a46dd5af43c0aad77a8ef467c0121c778d762de97fcdd63f5b1148f05f_flash_display_Sprite()
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
