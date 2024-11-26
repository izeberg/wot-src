package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b2e7a1dad83462fd455b7d910c6ab17c2d69aae439eeeab36843e02828658afd_flash_display_Sprite extends Sprite
   {
       
      
      public function _b2e7a1dad83462fd455b7d910c6ab17c2d69aae439eeeab36843e02828658afd_flash_display_Sprite()
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
