package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1bc9e1ea21195a28a0eedc4d059be81ada470b620620679030203bdaa8219ba1_flash_display_Sprite extends Sprite
   {
       
      
      public function _1bc9e1ea21195a28a0eedc4d059be81ada470b620620679030203bdaa8219ba1_flash_display_Sprite()
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
