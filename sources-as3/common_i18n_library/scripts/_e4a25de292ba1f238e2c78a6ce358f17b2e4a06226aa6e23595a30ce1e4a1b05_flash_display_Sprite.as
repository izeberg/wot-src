package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e4a25de292ba1f238e2c78a6ce358f17b2e4a06226aa6e23595a30ce1e4a1b05_flash_display_Sprite extends Sprite
   {
       
      
      public function _e4a25de292ba1f238e2c78a6ce358f17b2e4a06226aa6e23595a30ce1e4a1b05_flash_display_Sprite()
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
