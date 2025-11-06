package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _30a4ece60b5c3e94438831d2381d0cd8127430ccdfe0260cbeb60874ee05ec6a_flash_display_Sprite extends Sprite
   {
       
      
      public function _30a4ece60b5c3e94438831d2381d0cd8127430ccdfe0260cbeb60874ee05ec6a_flash_display_Sprite()
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
