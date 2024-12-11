package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0667875944c30a6d304d69c7795bfec93d4c9ceb458248e3836ac8dc729ff8b5_flash_display_Sprite extends Sprite
   {
       
      
      public function _0667875944c30a6d304d69c7795bfec93d4c9ceb458248e3836ac8dc729ff8b5_flash_display_Sprite()
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
