package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _baea0351ac023a641f1cc887a8f022171361286eaf5c68976168b593c21c3ca7_flash_display_Sprite extends Sprite
   {
       
      
      public function _baea0351ac023a641f1cc887a8f022171361286eaf5c68976168b593c21c3ca7_flash_display_Sprite()
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
