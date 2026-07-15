package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _35db3f6fb9631e81fc9144d26c1a76ef9f2cb45c31d8308e0f6d3392b451e389_flash_display_Sprite extends Sprite
   {
       
      
      public function _35db3f6fb9631e81fc9144d26c1a76ef9f2cb45c31d8308e0f6d3392b451e389_flash_display_Sprite()
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
