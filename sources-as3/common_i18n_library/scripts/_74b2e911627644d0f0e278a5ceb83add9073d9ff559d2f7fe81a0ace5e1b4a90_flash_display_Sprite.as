package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _74b2e911627644d0f0e278a5ceb83add9073d9ff559d2f7fe81a0ace5e1b4a90_flash_display_Sprite extends Sprite
   {
       
      
      public function _74b2e911627644d0f0e278a5ceb83add9073d9ff559d2f7fe81a0ace5e1b4a90_flash_display_Sprite()
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
